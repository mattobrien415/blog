Title:  Deep Learning for Sport Wagering Part 1 of 3
Date: 2017-09-15
Tags: deep learning, sport, wagering
Summary: Characteristics of the dataset

#### Part 1: Characteristics of the dataset
[Part 2 Modeling](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-2-of-3.html)  
[Part 3: Prediction and Evaluation](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-3-of-3.html)  

Not long ago, I was reading Nate Silver's blog, where there was some discussion about basketball. In particular, my hometown's team, the Golden State Warriors. At the time of the writing, the Warriors were surging towards the status of present-day dynasty, and the blog post was examining ways that the team performed that were revolutionary in the sport.

One particular line in [the blog post](https://fivethirtyeight.com/features/how-the-golden-state-warriors-are-breaking-the-nba/) stuck out for me: "It’s as if at some point in the past few years, the Warriors solved contemporary basketball..."

Solved? A bit heavy on the hyperbole, but maybe not too far off.

This got me thinking about other sports, and their capacity to be understood via data science, analytics, and deep learning. In particular, I became interested in the somewhat marginal and obscure (by major American sport standards, anyway) sport of boxing. I began to think that boxing could lend itself to being 'solved' nicely, because it has many characteristics that lend it to straightforward analysis and modeling.

At it's heart, boxing has a simple structure.  Unlike many popular sports, it's not a team sport -- so there isn't a dynamic interplay between multiple individuals. It's also not new: the sport became standardized in the late 1600s, via the [Marquess of Queensberry Rules](https://en.wikipedia.org/wiki/Marquess_of_Queensberry_Rules). Thus, there is plenty of data available.  Fortunately for me, much of it is available online.

To make the project more impactful, I decided to set a very specific goal. I've found that often, personal projects such as these will get more attention on the evenings and weekends if there is the possibility of a good payoff at the end --  so I figured, why not try to build an algorithm that would allow me to win money in Vegas? Thus I set the goal of creating a tool for successful wagering on boxing.

After quite a long process of collecting, reshaping, and modeling a dataset, I came into posession a what I consider to be a very model. **The tl;dr is that the model returned a 22.5% return on investment.** This is really exciting and shows the power of deep learning in a tangible manner. 

So, if you make it through these (hopefully not painful to read) blog posts, then I invite you to go ahead and check on some upcoming fights. Ask me where to put your money, and I might be able to provide you with the 'nap.' In case you didn't know, the term 'nap' refers to a highly confident bet. That's been a fun side-effect from this project -- I learned a lot of cool new slang. 

There will be 3 parts to this blog post:

1) [Characteristics of the dataset](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-1-of-3.html)  
2) [Modeling](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-2-of-3.html)
3) [Prediction and Evaluation](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-3-of-3.html)  

Part 1 is fairly dry and reflect the laborous truth that the majority of data science work is often dominated by collection and transforming data.  

Part 2 is short and has some interesting forays into feature engineering vis-à-vis graph databases.  

Part 3 is the most exciting, since we finally get to talk money!  

### Characteristics of the data 

The project was built on a very substantial dataset. The were two major sources of data. First, I aquired metadata on 373,415 individual boxers. Second, I had a collection of over 3.5 million fights (3,529,624 to be exact). Both were imported into MySQL tables. Interestingly, the dataset spanned the entire history of the sport. It was really fun to dig into. There were fighters from every corner of the globe, competing from the very beginning of the sport to the present day. There were boxers in every weight class from minimumweight upward, possessing all skill levels. They came in all ages, and exhibited all levels of success. Casually perusing revealed some quite obscure fighters: a boxer from Accra, Ghana, who fought only once back in 19066 (unfortunately losing by knockout). There was data on all the modern day multimillionaire champions. There were was, for example, [Wladamir Klitchko](https://en.wikipedia.org/wiki/Wladimir_Klitschko), nicknamed 'Dr Steelhammer.' The dataset definitely possessed depth. 

Looking specifically at the breadth of features for the metadata on each fighter, I had:



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


At this point it was time to being sifting through the features. Although elements like a boxer's weight are extremely important in real life boxing, this particular feature was not applicable because weight usually changes across a boxer's career. For example, Manny Pacquiao's first fight was at 98 pounds, but his [most recent fight](https://www.youtube.com/watch?v=OdvxQDVP4WI) was at 146 pounds. So a single value pulled from the metadata table would only reflect the most recent weight, not the weight at each fight.

It was simple to keep stance (orthodox or southpaw) as a categorical variable.

The dataset was balanced: 55% Wins, 45% Losses.

More useful was the second source of data, which was the specific data for each boxing match:  


##### fight data  

  
boxer_id  
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

With that being settled, the first important decision I made with respect to transformation of the data was to do a self-join within the fight table in MySQL. Thus each record in the dataset represented one fight. There would be a Boxer 1 and a Boxer 2 . The target for each row would be Win, Lose, or Draw, with respect to Boxer 1. There would also be the granular outcome information: the type of W, L or D. After all, there are many ways for a boxing match to end: points, knockout, disqualification, waved off via accidental headbut, quitting on the stool, etc, etc.

Quick note on a detail of the sport itself: Notice that although boxing is an individual sport, each fighter also has a whole team behind them. During competition, there is a coach in the corner, and there is also the [cutman](https://en.wikipedia.org/wiki/Cutman). The cutman handles the first aid between rounds. These two team members are called the 'secondaries' -- so in boxing, we'll refer to the 2 actual fighters 'primaries'. I quickly renamed Boxer 1 and Boxer 2 to P1 and P2.

Looking at these data, all seemed promising. But after some more reflection, I started to be concerned with what this rectangular representation was missing.  

In truth, these fights are all sequences of events that happen for a boxer -- they start with fight #1, then continue forward until the end of their careers. This made me interested in engineering 4 temporal variables, which I proceed to do in Pandas. Now, each row had these features:  


P1_ageAtFight  
P2_ageAtFight  
P1_rounds_fought  
P2_rounds_fought  

These variables are rather self-explanatory given their names.  

Another engineered feature was basically 'career length', or how many days it had been since the boxer's debut. These became:  

P1_days_since_ff  
P2_days_since_ff  

where 'ff' is just short for 'first fight'.

Some boxers were missing a birthdate, so I imputed these birthdates by assuming that each boxer's debut was on their 20th birthday. This was a simple subtraction from of 20 years from the date of the first fight.

But beyond the sequential, temporal perspective, there was still something more to be done. I realized this dataset could also be realized as a graph, with nodes for the boxers and the fights. I could set nodes for the boxers' professional W, L, D records at the time of each fight. So I exported my dataset out of SQL and into Neo4J.

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

Envisioned as a graph, it is insightful to see the interconnectedness of the sport as a whole.  I generated some pretty looking art which I enjoyed on an asthetic level as as well as analytic:  

![Neo4J graph 4](https://github.com/mobbSF/blog/blob/master/images/Neo_004.png?raw=true)  

![Neo4J graph 5](https://github.com/mobbSF/blog/blob/master/images/Neo_005.png?raw=true)  

Time to Move along. Now that now that the Neo4J database was built, the first metric I focused on creating using Cypher was a 'quality of opposition' (QOO) score.

QOO is necessary to suss out boxers with inflated records. Interestingly enough, boxing is the only sport (that I am aware of, at least) where a boxer actually gets to choose their opponent. There are no tournaments...no leagues...just arrangements between two boxers and the businesspeople around them, to hold an event. So what is stopping a boxer from inflating their record with [lousy opposition](http://boxrec.com/en/boxer/4741)? Not much. And this happens often in practice.  

It all really comes down to the quality of a boxer's opponents. If a boxer (say P1) has been beating up on [tomato cans](https://en.wikipedia.org/wiki/Tomato_can_(sports_idiom)), then we need to acknowledge this. 
Because if during that same time, another boxer (say P2) was battling top-quality opposition, then you'd be wise to put your money on P2. Because both P1 and P2 could have records of 20 Wins, 0 losses. In short, W L D records can be misleading.  

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

There are still many other ways to extract value from the Neo4J implementation. For example, implementing an [elo rating](https://en.wikipedia.org/wiki/Elo_rating_system) (as borrowed from chess) could result in a valuable datum for the state of each boxer during each match. But this was a good enough start and took me pretty far.

Now that the data were all cleaned up ready to go, it was time to (finally!) get to the fun part...building some deep learning models.