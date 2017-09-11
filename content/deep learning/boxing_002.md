Title:  Deep Learning for Sport Wagering Part 2 of 3
Date: 2017-09-16
Tags: deep learning, sport, wagering
Summary: Modeling

#### Part 2: Modeling


I was fortunate enough to have attended Jeremy Howard's awesome [deep learning certification program](https://www.usfca.edu/data-institute/certificates/deep-learning-part-one) at University of San Francisco. One of the many insightful things Jeremy said, was, and I quote, "In real life, I always start with a variable importance plot" <find video>.

Being smart enough to recognize when smarter people have good ideas, this is exactly what I did.

I built a straightforward Random Forest in scikit-learn (using GridSearchCV) and retrieved this plot:

![VIP](https://github.com/mobbSF/blog/blob/master/images/VIP.png?raw=true)

The plot doesn't have a strong inflection point. 

First let's look at what isn't important:  

- We see that the number of Draw outcomes isn't important, which makes sense, as these are extremely rare outcomes and are fairly irrelevant.  
- We see that the permutations of stances across opponents (complimentary or opposite, left-handed or right-handed) isn't relevant.  
- Finally, the indicator columns aren't useful, which isn't a major surprise. 

Next, let's look at what *is* important. But first, let's take a little detour to think ahead about what might feel right. Let's ignore the VIP for a second.

There is a fundamental axiom in boxing: "Hit and don't get hit." Without adhering to this basic principle, careers will be unnecesarily short, as physical damage sustained will quickly accumulate. So the idea of wear and tear on the body accumulated by a boxer over time seems like a naturally important component of what influences the outcome of a fight. 

This being considered, it should come as no great surprise that the most important feature in the Random Forest is `P1_days_since_ff`. Recall, this variable reports how long it has been since a boxer's career began. This perspective on career length turns out to be a natural fit.

However, it's possible a boxer could fight once, then fight again 10 years later. In this scenario,`P1_days_since_ff` would be a value around 3,650, but this wouldn't be an accurate measurement of that boxer's accumulated wear and tear. Fortunately for us, the next most important features on the plot corresponds to the aggregated number of rounds the opponents have fought. A long 'ring life' can clearly play a large role in a fighter's success (see [Ali vs Holmes](https://www.youtube.com/watch?v=Ja9iovR9B3E) for a tragic example). Conversely, too few rounds can also play a role in predicting losing.

Getting back to the variable importance plot, the two Quality of Opposition (`QOO`) metrics are shown to be important, which is nice because they took a lot of effort to construct.

The `last6_L` and `last6_W` variables have a large amounts of variance as evidenced by the bars. This most likely ties into the discussion about how records, as they stand alone, don't adequately reflect the quality of the opposition. For some boxers, the last 6 are very important; for some, they aren't. This makes sense.

Content with the plot and with these features in mind, I experimented with various subsets of features and various configurations when fitting multilayer perceptrons in Keras.

Because of the small file size of the flat dataset (only 1.85 GB), there were no heavy demands on IO or memory. Thus I could rip through each epoch on a basic AWS cloud GPU painlessly, and iterate on models easily. 

Regarding the actual deep architecture of the MLP, I didn't have major overfitting issues, thus didn't get any advantage with a copious amount of dropout. Batch Normalization didn't give me any advantage, so I discarded it. Fundamentally, it's a remarkably simple dataset and most models I built performed similarly. Epochs around 10 performed fine.

A decent final configuration looked like this: 

    mlp = Sequential()
    mlp.add(Dense(64, activation='relu', input_dim=13))
    mlp.add(Dense(64, activation='relu'))
    mlp.add(Dense(64, activation='relu'))
    mlp.add(Dropout(0.2))
    mlp.add(Dense(64, activation='relu'))
    mlp.add(Dense(3, activation='softmax'))
    mlp.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

    mlp.fit(X_train, y_train, batch_size=64, validation_split=0.2, nb_epoch=10)

The accuracy returned would settle down to roughly 66%. 

OK, so how should I feel about such a low accuracy, in this age of computer vision, self-driving cars, and [Elon Musk's dire warnings](https://www.cnbc.com/2017/08/11/elon-musk-issues-a-stark-warning-about-a-i-calls-it-a-bigger-threat-than-north-korea.html) of [Arnold coming baaack](https://www.youtube.com/watch?v=-WIwQlMesr0)?

I must admit, I feel pretty good about it. Remember, we are trying to get the edge on gambling. Theoretically, anything about a coin flip should be profitable over time. 

Time to move past the accuracy. As briefly noted above, the dataset wasn't appreciably unbalanced. Here's the confusion matrix:

![CM](https://github.com/mobbSF/blog/blob/master/images/CM.png?raw=true)

It's useful to take a step back here and reiterate that the purpose of this project is to make money gambling on boxing. If we were to use this algorithm to indicate to a user when to place a bet, then we would prefer a larger precision at the expense of recall. What this means it that it's better to avoid betting and miss out on opportunities to win (lower recall), as long as we are more confident that when we *DO* bet, we will win. 

Looking at the ROC curve,

![ROC](https://github.com/mobbSF/blog/blob/master/images/ROC.png?raw=true)

...I was inspired to refit the model with a variety of custom precision and recall thresholds and examined the resulting metrics.  

However, by sticking with the default `[precision_threshold(0.5), recall_threshold(0.5)]`
 
I got my best precision and recall scores: 

Precision: 0.71
Recall:    0.78

I could spend some more time exploring this area, but for now I am content with these scores.

Meanwhile, allow me to wander a bit and discuss one of the many experiments I ran that didn't pay off. I went ahead and went for a moonshot. The reality is that as far as wagering on boxing go, it's one thing to wager on a W or L outcome. But if you can win a bet by predicting a more granular types of outcomes, the payouts are several orders of magnitude better. The actual type of outcome -- either a judges decision, or an actual knockout, or a technical knockout -- that's where the big bucks are. And when it comes to knockouts, if it's possible to predict the actual round? The payouts are huge. 

I changed the labels to represent the granular outcomes mentioned above, and I rebuilt the model and crossed my fingers. Unfortunately, and not too surprisingly, accuracy dropped to around 30%. Hummm...well...worth a shot. And definitely worth revisiting again later.

Next up...prediction time!
