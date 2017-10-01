Title:  Deep Learning for Sport Wagering Part 3 of 3
Date: 2017-10-09
Tags: deep learning, sport, wagering
Summary: Predicting

#### Part 3: Predicting
[Part 1: Characteristics of the dataset](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-1-of-3.html)  
[Part 2: Modeling](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-2-of-3.html)

I considered two major betting strategies during this final phase of the project. They are as follows:  

1) If  
$\text{model probability} > \text{some decision threshold}$, and  
$\text{model probability} > \text{sportsbook probability}$  
then place bet  

2) If  
$\text{model probability} > \text{some decision threshold}$  
then place bet

The first strategy is a more conservative approach in one sense. With this perspective, we include a parameter that indicates if we feel like we have an edge on the casino or sportsbook. 

Allow me a quick foray into the structure of gambling. Sportsbook odds are set, not by information, but by popular sentiment as it is revealed by [action](https://www.docsports.com/gambling-terms.html). If some Boxer A gets a large amount of action, then the sportsbook will consider Boxer A to be more likely to win, and consequently, payout on this outcome is reduced. Thus, my model is attempting to answer the question, "When does prediction based on historic data result in a confidence higher than the confidence of the sportsbook -- which is a function of popular sentiment?". In this sense, at it's most stripped down, the model is trying make a totally impartial, data driven decision, and looks for opportunities when public perception is not aligned with historically based signal.  

This first strategy also has a built in safeguard. If the sportsbook places some Boxer A at a 10% chance of winning, and the model predicts an 11% chance of winning, then without the safeguard, the bet would be place. This is something we don't want. Instead we want to see action whenever the algorithm is confident above some threshold.

Moving on, the second strategy isn't concerned with the sportsbook's behavior at all; merely concerned with the strength of it's (the model's) own predictions. This strategy might be more successful if it allows more bets to be made, and hopefully more money to be made, quicker. This assumes the model is accurate enough to exhibit this success.

Let's examine both strategies, and see how they played out. We will start with strategy 1, because is it the more comprehensive one.  

#### Strategy 1  

To be implemented, the first strategy required a data acquisition step first. Historic sportsbook odds needed to be collected. This is for the purpose of compairing the probability of a win assigned by the model with the probability of a win assigned by a sportsbook.  

In boxing, the bookmaker's odds come structured into a form which is referred to as the [moneyline](https://en.wikipedia.org/wiki/Odds#Moneyline_odds). The moneyline is a little confusing at first. Generally, one fighter who considered favored to win is assigned a negative number. The other fighter is considered the underdog, and is assigned a positive number. 

The best way to remember how to read the moneyline is to always start with the image of a one-hundred dollar bill in your mind.  

- A negative number (assocated with the favored fighter) shows how much money you need to bet to win a profit of $100.  
- A positive number (associated with the underdog) shows how much profit a winning wager of $100 would yield.

So if the moneyline has Boxer A at -130, we know that Boxer A is expected to win. Further, you know you'd have to place a \$130 bet on this fighter to win \$100.  
For Boxer B, the moneyline might have them set at +110. This mean Boxer B is the underdog, and if you placed a \$100 bet on this fighter, you'd win \$110.  

Since Keras is returning the probability of a boxer winning, we now need to convert the moneyline into regular probabilities so we can compare apples to apples.  

To do this, first the actual numeric values (-130 and +110, on this example above), must be converted to what are referred to as [implied probabilities](https://www.sbo.net/strategy/implied-probability/) (more about implied probabilities in a second). The formula is as follows:  

$\text{Implied probability for 'negative' moneyline} = \frac{ - ( \text{'negative' moneyline value})}{- ( \text{'negative' moneyline value} ) + 100}$  
and  

$\text{Implied probability for 'positive' moneyline} = \frac{100}{\text{'positive' moneyline value} + 100}$

Thus, -130 is converted to 0.56, and +110 is converted to 0.50.  

But what is an implied probability anyway?

Implied probability is our usual notion of probability which has actually been modified by what is called either [vigorish, or juice](https://en.wikipedia.org/wiki/Vigorish). Both of these terms refer to a built-in modification, by the bookmaker, of the true odds. The modification shifts the moneyline is such a way that the sportsbooks can never ultimately lose money. Usually, the vig amounts to 20 points. It's basically the casino's cut. Fortunately, it's easy to remove the vigorish using this simple formula:  

Take one of your implied probability. Divide it by the sum of both of your implied probabilities.  
  
Thus:  

$\text{Actual probability } = \frac{\text{Implied probability A}}{\text{Implied probability A} + \text{Implied probability B}}$

With the math settled, I began searching for a set of historic moneylines for records which I could use in my test set. Using a variety of sources (including laborious searching of the Wayback Machine, and locating an actual broker for assistance), I collected a set of 728 moneylines. After munging, the final size was 679.  

We now bring our attention back to decision thresholds. What would be the optimal value where our $\text{model probability} > \text{some decision threshold}$?  To determine this, it was merely a matter of looping through thresholds from $\[ 0, 1 \]$ by 0.1 and collecting results.  

The outputs collects as a function of varying decision threshold were as follows:   

1. Number of wagers that satisified the criteria and thus were placed  
2. Number of wagers placed which won  
3. Number of wagers placed which lost  
4. A tabulation of the balance resulting from money won via successful wagers and money lost via unsuccessful wagers  
5. ROI (return on investment): simply $\frac{\text{balance}}{\text{total investment}}$  

The iterations assumed that each bet placed was a \$100 bet. Every loss will incur a deduction of \$100, whereas each winning bet will earn a deposit depending on the sportsbook odds. This means if the model can predict 'easy' matches, it can win a smaller amount of money, but if the matches are harder to predict, the model can earn more.  



Here is a plot showing the outcome for #1 on the list above:  

![wagers](https://github.com/mobbSF/blog/blob/master/images/wagers.png?raw=true)  

This gives us an intuition on where to place our decision threshold. We are interested in the point where the blue line and the green line are closest together, which means we will win the highest proportion of our placed bets. Simultaneously we would like this point to be as high as possible along the y axis, meaning the model chose to place a high net number of bets. 

The chart below shows the model will place the proportionately largest number of winning bets around an 0.85 to 0.95 decision threshold.  

<img src="https://github.com/mobbSF/blog/blob/master/images/chart_002.png" width="200">

![chart_002](https://github.com/mobbSF/blog/blob/master/images/chart_002.png?raw=true)  

It looks like roughly 0.90 is a reasonable place to set the threshold.  

Here is a plot showing the outcome for #5 (ROI) on the list above:  

![ROI](https://github.com/mobbSF/blog/blob/master/images/ROI.png?raw=true)  


This chart shows the ROI values at the region of interest:  

![chart_002](https://github.com/mobbSF/blog/blob/master/images/chart_002.png?raw=true)  

This shows we can get an ROI around 22.5\% if we set the decision threshold to roughly 0.90. We could push it up to 24.8\% if we choose 0.94 as the threshold, but notice the precipitous drop at 0.95 on the plot above. Better to be wary of possible noise and choose the median value.

The ROI plot above doesn't show the net cash balance. Perhaps the ROI is high, but the best placed has low payouts. The plot below clarifies:  

![cash](https://github.com/mobbSF/blog/blob/master/images/cash.png?raw=true)  



We are seeing that when we stick with 0.90 we earn \$292.00.  

Finally, let's see what the plot looks like when we view all these results simultaneously:  

![functions](https://github.com/mobbSF/blog/blob/master/images/functions.png?raw=true)  

Clearly, the model is a success as a result of this tuning step.  






