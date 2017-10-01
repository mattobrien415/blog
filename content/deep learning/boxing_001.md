Title:  Deep Learning for Sport Wagering Part 1 of 3
Date: 2017-09-15
Tags: deep learning, sport, wagering
Summary: Characteristics of the dataset

#### Part 1: Characteristics of the dataset
[Part 2 here:](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-2-of-3.html)  
[Part 3 here:](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-3-of-3.html)  

Not long ago, I was reading Nate Silver's blog, where there was some discussion about basketball. In particular, my hometown's team, the Golden State Warriors. At the time of the writing, the Warriors were surging towards the status of present-day dynasty, and the blog post was examining ways that the team performed that were revolutionary in the sport.

One particular line in [the blog post](https://fivethirtyeight.com/features/how-the-golden-state-warriors-are-breaking-the-nba/) stuck out for me: "It’s as if at some point in the past few years, the Warriors solved contemporary basketball..."

Solved? A bit heavy on the hyperbole, but maybe not too far off.

This got me thinking about other sports, and their capacity to be understood via data science, analytics, and deep learning. In particular, I became interested in the somewhat marginal and obscure (by major American sport standards, anyway) sport of boxing. I began to think that boxing could lend itself to being 'solved' nicely, because it has many characteristics that lend it to straightforward analysis and modeling.

At it's heart, boxing has a simple structure.  Unlike many popular sports, it's not a team sport -- so there isn't a dynamic interplay between multiple individuals. It's also not new: the sport became standardized in the late 1600s, via the [Marquess of Queensberry Rules](https://en.wikipedia.org/wiki/Marquess_of_Queensberry_Rules). Thus, there is plenty of data available.  Fortunately for me, much of it is available online.

To make the project more impactful, I decided to set a very specific goal. I've found that often, personal projects such as these will hold up better if there is the possibility of a good payoff at the end --  so I figured, why not try to build an algorithm that would allow me to win money in Vegas? Thus I set the goal of creating a tool for successful wagering on boxing.

After quite a few long nights and weekends of collecting, reshaping, and modeling the data, I came into posession a pretty good model. The tl;dr is that the model guarantees a result of up to an (fill this in soon) <insert> return on investment. 

So, if you make it through these (hopefully not painful to read) blog posts, then go ahead and check on some upcoming fights. Ask me where to put your money, and I might be able to provide you with the 'nap.' In case you didn't know, the word 'nap' refers to a highly confident bet. That's been a fun side-effect from this project -- I learned a lot of cool new slang terms! 

There will be 3 parts to this blog post:

1) Characteristics of the data  
2) Building models  
3) Prediction and Evaluation  

### Characteristics of the data 

The project was built on a very substantial dataset. The were two major sources of data. First, I aquired metadata on 373,415 individual boxers. Second, I had a collection of over 3.5 million fights (3,529,624 to be exact). These I imported into two MySQL tables. The dataset spanned the entire history of the sport. It was really fun to dig into. There were fighters from every corner of the globe, competing from the very beginning of the sport to the present day. There were boxers in every weight class from minimumweight upward, possessing all skill levels, at all ages, and exhibiting all levels of success. Perusing revealed some quite obscure fighters: a boxer from Accra, Ghana, who fought only once (unfortunately losing by knockout), back in 1966. Then, there was data on all the modern day multimillionaire heavyweight champions. There were was, for example, [Wladamir Klitchko](https://en.wikipedia.org/wiki/Wladimir_Klitschko), nicknamed 'Dr Steelhammer.' 

The dataset definitely possessed depth. The breadth in features for the first source of data, was as such:



##### boxer data  


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

More useful was the second source of data, the specific data for each boxing match:  


##### fight data  

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

With that being settled, the first important decision I made with respect to transformation of the data was to do a self-join within the fight table in MySQL. Thus, as shown above, each record in the dataset represented one fight. There would be a boxer1 and a boxer2. The target for each row would be Win, Lose, or Draw, with respect to boxer1. There would also be the granular outcome information: the type of W, L or D. After all, there are many ways for a boxing match to end: points, knockout, disqualification, waved off via accidental headbut, quitting on the stool, etc, etc.

(Quick note on a detail of the sport itself: Notice that although boxing is an individual sport, each fighter also has a whole team behind them. During competition, there is a coach, obviously, and there is the [cutman](https://en.wikipedia.org/wiki/Cutman) as well. The cutman handles the first aid between rounds. These two team members are called the 'secondaries' -- so in boxing, we'll call the 2 boxers 'primaries'. I quickly renamed boxer1 and boxer2 to P1 and P2.)

Looking at these data, all seemed promising. But after some more reflection, I started to be concerned with what this rectangular representation was missing.
Really, these fights are all sequences of events that happen for a boxer -- they start with fight #1, then continue forward until the end of their careers. This made me interested in engineering some temporal variables, which I proceed to do in Pandas. Now, each row had these features:  


P1_ageAtFight  
P2_ageAtFight  
P1_rounds_fought  
P2_rounds_fought  

These 4 variables are rather self-explanatory given their names.  

Another engineered feature was basically 'career length', or how many days it had been since the boxer's debut. These became:  

P1_days_since_ff  
P2_days_since_ff  

where 'ff' is short for 'first fight'.

Some boxers were missing a birthdate, so I imputed these birthdates by assuming that each boxer's debut was on their 20th birthday. This was a simple subtraction from of 20 years from the date of the first fight.

But beyond the sequential, temporal perspective, there was still something more to be done. I realized this dataset could also be realized as a graph, with nodes for the boxers and the fights, and nodes for their professional W, L, D records at the time of the fight. So I exported my dataset out of SQL and into Neo4J.

Once this was done (and it took quite some time, given I had never used Neo4J before), I had a new way of conceptualizing these competitions. The schema is, in ASCI art:

(A boxer, call them 'P1')--[had a record (W, L, D) on some date] -->(and there was a Fight at some location, with some outcome).

Now, going the other direction,  

(and there was a Fight at some location, with some outcome)<--[the opponent had a record, (W, L, D) on that same date]---(The opponent, call them 'P2')

This actually is more clear when you look at the actual Neo4J graph itself:

![Neo4J graph](https://github.com/mobbSF/blog/blob/master/images/Neo_000.png?raw=true)

Here you see the blue boxer nodes, their records at a given time (red node), the fight node (green), and the complementary information for their opponents. Note that this particular boxer had a few rematches which are visible when two edges touch the same blue P2 (P2 being the opponent), node.

Actually, it's interesting to see how the graph can be expanded. Take a look a Muhammad Ali's and his career:

![Neo4J graph 1](https://github.com/mobbSF/blog/blob/master/images/Neo_001.png?raw=true)

and here's [Ali's fight with Archie Moore](https://www.youtube.com/watch?v=-FZBzGhxERg), and Archie Moore's career: 

![Neo4J graph 2](https://github.com/mobbSF/blog/blob/master/images/Neo_002.png?raw=true)

...and here's [Archie Moore's fight with Jimmy Slade](https://www.youtube.com/watch?v=MUT71-jyY2s),

![Neo4J graph 3](https://github.com/mobbSF/blog/blob/master/images/Neo_003.png?raw=true)

and so forth.

Envisioned as a graph, it is insigtful to see the interconnectedness of the sport as a whole. 

Now that the Neo4J database was built, the first metric I focused on creating using Cypher was a 'quality of opposition' (QOO) score.

QOO is necessary to suss out boxers with inflated records. Interestingly enough, boxing is the only sport (that I can think of, anyway) where a boxer actually gets to choose their opponent. There are no tournaments...no leagues...just arrangements between two boxers and the businesspeople around them, to hold an event. So what is stopping a boxer from inflating their record with [lousy opposition](http://boxrec.com/en/boxer/4741)? Not much.

It all really comes down to the quality of a boxer's opponents. If a boxer (say P1) has just been beating up on [tomato cans](https://en.wikipedia.org/wiki/Tomato_can_(sports_idiom)), then we need to acknowledge this. 
Because if P2 was battling top-quality opposition, then you'd be wise to put your money on P2. Because they both could have records of 20 Wins, 0 losses.

(In reality, most successful fighters start competing relatively frequently, against somewhat weak opposition. Later, they increase the quality of opposition as they decrease the frequency of competition. So the above scenario is an exaggeration, in most cases).

To show how the metric works, let's first start with this made up, simplified visual scenario:

![QOO 1](https://github.com/mobbSF/blog/blob/master/images/QOO_001.png?raw=true)

As you can see, P1 has fought 3 opponents (they live in 'Layer 1'), and each of those opponents had fought 3 opponents themselves (they live in 'Layer 2').

Now consider Layer 2. For each group of 3 fights, sum up these fighters' records as : count(Wins) / count(fights).

![QOO 2](https://github.com/mobbSF/blog/blob/master/images/QOO_002.png?raw=true)

Now, recursively running back up the graph, let's see how the boxer in Layer 1 performed against this group. This will be count(Wins) / count(opponents) from above, but now multiplied by the previously calculated value. Voila; we have the QOO metric.

![QOO 3](https://github.com/mobbSF/blog/blob/master/images/QOO_003.png?raw=true)

After setting a QOO score for all fights on the nodes in Neo4J, it was easy to put together another quick and dirty metric: QOOP, which for lack of better nomenclature, is 'Quality of opposition prime'. Here, I just took the mean of all a boxer's opponents' QOOs and wrote it to the record node.

Indicator columns with 0 or 1 were included, in case the QOO metrics couldn't be built. This could happen if, say, a fight was a boxer's debut.

As a work in progress, I'm still playing with different ways to extract value from the Neo4J implementation. But this was a good start and took me pretty far.

Now that the data were all cleaned up ready to go, it was time to (finally!!) get to the fun part...building some deep learning models.