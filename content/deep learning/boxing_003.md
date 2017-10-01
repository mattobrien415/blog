Title:  Deep Learning for Sport Wagering Part 3 of 3
Date: 2017-10-09
Tags: deep learning, sport, wagering
Summary: Predicting

#### Part 3: Predicting
[Part 1 here:](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-1-of-3.html)  
[Part 2 here:](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-2-of-3.html)

I considered two major betting strategies during this final phase of the project. They are as follows:  

1) If   
model probability > some decision threshold, and  
model probability > sportsbook probability  
then place bet  

2) If model probability > some decision threshold
then place bet

The first strategy is a more conservative approach in one sense. With this perspective, we care if we feel like we have an edge on the casino or sportsbook. 

Allow me a quick foray into the structure of gambling. Sportsbook odds are set, not by information, but by popular sentiment. If some Boxer A is favored by the public, then the sportsbook will consider Boxer A to be more likely to win. Thus, my model is attempting to answer the question, "When does prediction based on historic data result in a confidence higher than the confidence represented by public perception?".

This first strategy also has a built in safeguard. If the sportsbook places some Boxer A at a 10% chance of winning, and the model predicts an 11% chance of winning, then a bet will not placed (assuming the decision threshold is greater than 10%, which, it is).

Moving on, the second strategy isn't concerned with the sportsbook's behavior at all; merely concerned with the strength of it's (the model's) own predictions. 

Let's examine both strategies, and see how they played out.   

#### Strategy 1  

To be implemented, the first strategy required a data acquisition step first. Historic sportsbook odds needed to be collected. This is for the purpose of compairing the probability of a win assigned by a sportsbook to the probability of a win assigned by the model.  

In boxing, the bookmaker's odds come structured into a form which is referred to as the [moneyline](https://en.wikipedia.org/wiki/Odds#Moneyline_odds). The moneyline is a little confusing at first. Generally, one fighter who considered favored to win is assigned a negative number. The other fighter is considered the underdog, and is assigned a positive number. 

The best way to remember how to read the moneyline is to always start with the image of a one-hundred dollar bill in your mind.  

- A negative number shows how much money you need to bet to win a profit of $100.  
- A positive number shows how much profit a winning wager of $100 would yield.

So if the moneyline has Boxer A at -130, we know that Boxer A is expected to win. Further, you know you'd have to place a $130 bet on this fighter to win $100.  
For Boxer B, the moneyline might have them set at +110. This mean Boxer B is the underdog, and if you placed a $100 bet on this fighter, you'd win $110.  

The actual numeric values (-130 and +110, on this example above), can be converted to what are referred to as [implied probabilities](https://www.sbo.net/strategy/implied-probability/) (more about these in a second).

Implied probability =   ( - ( 'negative' moneyline value ) ) / ( - ( 'negative' moneyline value ) ) + 100  
and  
Implied probability =   100 / ( 'positive' moneyline value + 100 )  

Thus, -130 is converted to %56.5, and +110 is converted to %50.  

But what is an implied probability anyway?

Implied probability is our usual notion of probability which has actually been modified by what is called either [vigorish, or juice](https://en.wikipedia.org/wiki/Vigorish). Both of these terms refer to a built-in modification, by the bookmaker, of the true odds. The modification shifts the moneyline is such a way that the sportsbooks can never ultimately lose money. Usually, the vig amounts to 20 points. It's basically the casino's cut. Fortunately, it's easy to remove the vigorish using this simple formula:  

Take one of your implied probability. Divide it by the sum of both of your implied probabilities.  
  
For example:  

Actual probability = Implied probability A / (Implied probability A + Implied probability B)  

With the math settled, I began searching for a set of historic moneylines for records which I could use in my test set. Using a variety of sources (including laborious searching of the Wayback Machine), I collected a set of 690 moneylines. 




