Title:  Deep Learning for Sport Wagering
Date: 2017-09-15
Tags: deep learning, sport, wagering
Summary: Part 1 Characteristics of the dataset


Not long ago, I was reading Nate Silver's blog, where there was some discussion about basketball. In particular, my hometown's team, the Golden State Warriors. At the time of the writing, the Warriors were surging towards the status of present-day dynasty, and the blog post was examining ways that the team performed that were revolutionary in the sport.

One particular line in the blog post stuck out for me: "It’s as if at some point in the past few years, the Warriors solved contemporary basketball..."

Solved! A bit heavy on the hyperbole, but maybe not too far off.

This got me thinking about other sports, and their capacity to be understood via data science and analytics. In particular, I became interested in the somewhat marginal and obscure (by major American sport standards, anyway) sport of boxing. I began to think that boxing could lend itself to being 'solved' nicely, because it has many characteristics that lend it to straightforward analysis and modeling.

At it's heart, boxing has a simple structure.  Unlike many popular sports, it's not a team sport -- so there isn't a dynamic interplay between multiple individuals. It's also not new: the sport became standardized in the late 1600s. Thus, there is plenty of data available.  Fortunately for me, much of it is available online.

To make the project more impactful, I decided to set a very specific goal. I've found that often, personal projects such as these will hold up better if there is the possibility of a good payoff at the end --  so I figured, why not try to build an algorithm that would allow me to win money in Vegas? Yes, I'm talking about wagering on boxing.

After quite a few long nights and weekends of collecting, reshaping, and modeling the data, I came into posession a pretty good model. The tl;dr is that the model guarantees a result of up to a <insert> return on investment. 

So, if you make it through these (hopefully not painful to read) blog posts, then go ahead and check on some upcoming fights. Ask me where to put your money, and I might be able to provide you with the 'nap.' The word 'nap' refers to a highly confident bet. That's been a fun side-effect from this project -- I learned a lot of cool new slang terms! 

There will be 3 parts to this blog post:

1) Characteristics of the data  
2) Building models  
3) Prediction and Evaluation  




1) Data 

The project was built on a very substantial dataset. I had metadata on 373,415 individual boxers, alongside a collection of over 3.5 million fights (3,529,624 to be exact). These I imported into two MySQL tables. The dataset spanned the entire history of the sport. It was really fun to dig into. There were fighters from every corner of the globe, competing from the mid-1800s to the present day. There were boxers in every weight class from minimumweight upward, possessing all skill levels, at all ages, and exhibiting all levels of success. Perusing revealed some quite obscure fighters: a boxer from Accra, Ghana, who fought only once (unfortunately losing by knockout), back in 1966. Then, there was data on all the modern day multimillionaire heavyweight champions. There were was, for example, Wladamir Klitchko, nicknamed 'Dr Steelhammer.' 

The dataset definitely possessed depth. The breadth in features was as such:

Boxer's metadata
name 
sex 
birth_date 
division 
stance 
height 
reach 
country 
residence 
birth_place 
world_rank 
total_wins 
ko_wins 
total_losses 
ko_losses 
draws 
rounds 
ko_percent 


Although elements like a boxer's weight are extremely important in real life boxing, some particular features like that and others were not applicable.
For example, Manny Pacquiao's first fight was at 98 pounds, but his most recent fight was at 146. So a single value pulled from the metadata would only reflect the most recent weight, not the weight at each fight.

It was simple to keep stance (orthodox or southpaw) as a categorical variable.

The dataset was balanced: 55% Wins, 45% Losses.

More useful was the specific data for each boxing match:
boxer1_id 
boxer2_id 
date 
location 
rounds_planned 
rounds_happened 
boxer1_mass 
boxer2_mass 
boxer2_wins 
boxer2_loses 
boxer2_draws 
boxer2_last6_wins 
boxer2_last6_loses 
boxer2_last6_draws 
outcome 
outcome_type 
rating 
time 
referee 
judge1 
judge2 
judge3 
judge1_score 
judge2_score 
judge3_score 
titles 
comments 


As with the metadata for the boxer, I discarded some features of the fights. Much of it was nice but not functionally applicable, such as the names of the referee and judges, and comments, etc.

With that being settled, the first important decision I made with respect to transformation of the data was to do a self-join within the fight table in MySQL. Thus, as shown above, each record in the dataset represented one fight. There would be a boxer1 and a boxer2. The target for each row would be Win, Lose, or Draw, with respect to boxer1. There would also be the granular outcome information: the type of W, L or D. After all, there are many ways for a boxing match to end: points, knockout, quitting on the stool, etc etc.

(Quick note on a detail of the sport itself: Notice that although boxing is an individual sport, each fighter also has a whole team behind them. During competition, there is a coach, obviously, and there is the cutman as well. The cutman handles the first aid between rounds. These guys are the secondaries -- so in boxing, we'll call the 2 boxers primaries. I quickly renamed boxer1 and boxer2 to P1 and P2.)

Looking at these data, all seemed promising. But after some more reflection, I started to be concerned with what this rectangular representation was missing.
Really, these fights are all sequences of events that happen for a boxer -- they start with fight #1, then continue forward until the end of their careers. This made me interested in engineering some temporal variables, which I proceed to do in Pandas. Now, each row had these features:

P1_ageAtFight
P2_ageAtFight
P1_rounds_fought
P2_rounds_fought

Another feature as basically 'career length', or how many days it had been since the boxer's debut. These became:  
P1_days_since_ff
P2_days_since_ff

where 'ff' is just 'first fight'.

Some boxers were missing a birthdate, so I imputed these birthdates by assuming that each boxer's debut was on their 20th birthday. This was a simple subtraction from of 20 years from the date of the first fight.

But beyond the sequential, temporal perspective, there was still something more to be done. I realized this dataset could also be realized as a graph, with nodes for the boxers and the fights, and nodes for their professional W, L, D records at the time of the fight. So I imported if out of SQL and into Neo4J.

Once this was done (and it took quite some time, given I had never used Neo4J before), I had a new way of conceptualizing these competitions. The schema is, in ASCI art:

(A boxer, call them 'P1')--[had a record (W, L, D) on some date] -->(and there was a Fight at some location, with some outcome).

Now, going the other direction,
(and there was a Fight at some location, with some outcome)<--[the opponent had a record, (W, L, D) on that same date]---(The opponent, call them 'P2')

This actually is more clear when you look at the actual Neo4J graph itself:

<Neo_000.jpg>

Here you see the boxer node, their record at a given time (node), the fight node, and the complementary information for their opponents. Note that this particular boxer had a few rematches which are visible when two edges touch the same P2 node.

Actually, it's interesting to see how the graph can be expanded:

<Neo_001.jpg>

again, 

<Neo_002.jpg>

and again,

<Neo_003.jpg>

and so forth.

Envisioned as a graph, it was amazing to see the interconnectedness of the sport as a whole. 

The first metric I focussed on creating using Cypher was a 'quality of opposition' (QOO) score.

QOO is necessary to suss out boxers with inflated records. Interestingly enough, boxing is the only sport (that I can think of, anyway) where a boxer actually gets to choose their opponent. There are no tournaments...no leagues...just arrangements between two boxers and the businesspeople around them, to hold an event. So what is stopping a boxer from inflating their record with lousy opposition? http://boxrec.com/en/boxer/4741 Absolutely nothing.

It all really comes down to the quality of those 20 fight for each boxer. If P1 was just beating up on 20 tomato cans, then we need to consider P1 in this light. Since if P2 was battling top-quality opposition that whole time, then you'd be wise to put your money on P2.

(In reality, most successful fighters start competing relatively frequently, against somewhat weak opposition. Later, they increase the quality of opposition as they decrease the frequency of competition. So the above scenario is an exaggeration, in most cases).

To show how the metric works, let's first start with this made up, simplified visual scenario:

<QOO_001.jpg>

As you can see, P1 has fought 3 opponents (they live in 'Layer 1'), and each of those opponents had fought 3 opponents themselves (they live in 'Layer 2').

Now consider Layer 2. For each group of 3 fights, sum up these fighters' records as : count(Wins) / count(fights).

<QOO_002.jpg>

Now, recursively running back up the graph, let's see how the boxer in Layer 1 performed against this group. This will be count(Wins) / count(opponents) from above, but now multiplied by the previously calculated value. Voila; we have the QOO metric.

<QOO_003.jpg>

After setting a QOO score for all fights on the nodes in Neo4J, it was easy to put together another quick and dirty metric: QOOP, which for lack of better nomenclature, is 'Quality of opposition prime'. Here, I just took the mean of all a boxers' opponents' QOOs and wrote it to the node.

Indicator columns with 0 or 1 were included, in case the QOO metrics couldn't be built. This could happen, say, if a fight was a boxer's debut.

 As a work in progress, I'm still playing with different ways to extract value from the Neo4J implementation. But this was a good start and took me pretty far.

Now that the data were all cleaned up ready to go, it was time to (finally!!) get to the fun part...building some deep learning models.



# Dillinger

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

Dillinger is a cloud-enabled, mobile-ready, offline-storage, AngularJS powered HTML5 Markdown editor.

  - Type some Markdown on the left
  - See HTML in the right
  - Magic

# New Features!

  - Import a HTML file and watch it magically convert to Markdown
  - Drag and drop images (requires your Dropbox account be linked)


You can also:
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop markdown and HTML files into Dillinger
  - Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](http://breakdance.io) - HTML to Markdown converter
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md] [PlDb] |
| Github | [plugins/github/README.md] [PlGh] |
| Google Drive | [plugins/googledrive/README.md] [PlGd] |
| OneDrive | [plugins/onedrive/README.md] [PlOd] |
| Medium | [plugins/medium/README.md] [PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md] [PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version}
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
