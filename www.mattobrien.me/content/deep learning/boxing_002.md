Title:  Deep Learning for Sport Wagering Part 2 of 3
Date: 2017-09-16
Tags: deep learning, sport, wagering
Summary: Modeling

#### Part 2: Modeling
[Part 1: Characteristics of the dataset](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-1-of-3.html)  
[Part 3: Modeling](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-3-of-3.html)


I was fortunate enough to have attended Jeremy Howard's awesome [deep learning certification program](https://www.usfca.edu/data-institute/certificates/deep-learning-part-one) at University of San Francisco. One of the many insightful things Jeremy said was, and I quote verbatium, ["The first thing I do, is try to get a feature importance plot printed."](https://youtu.be/1-NYPQw5THU?t=1h19m11s)

Being just smart enough to recognize when smarter people have smart ideas, this is exactly what I did.

I built a straightforward Random Forest in scikit-learn, using CV to select hyperparameters and using general best procedures. I retrieved this plot:

![VIP](https://github.com/mobbSF/blog/blob/master/images/VIP.png?raw=true)

The plot doesn't have a strong inflection point, making it difficult to decide where to draw a line in the sand about what is important to include and what isn't. Let's see if we can deduce where this cutoff might fall, by first let's look at what isn't important:  

- We see that the number of Draw outcomes isn't important, which makes sense, as these are rare outcomes and are fairly irrelevant. The number of draws a boxer has doesn't have much bearing on the rest of their records.  
- We see that the permutations of stances across opponents (complimentary or opposite, [southpaw](https://en.wikipedia.org/wiki/Southpaw_stance) or [orthodox](https://en.wikipedia.org/wiki/Orthodox_stance)) isn't relevant.  
- Finally, the indicator columns aren't useful, which isn't a major surprise. 

Next, let's look at what *is* important. But first, let's take a little detour to think ahead about what might feel right. Let's ignore the variable importance plot for a moment.

There is a fundamental axiom in boxing: "Hit and don't get hit." For boxers who fail to adhere to this basic principle, careers will be unnecesarily short, as physical damage sustained will quickly accumulate. So the idea of wear and tear on the body accumulated by a boxer over time seems like a naturally important component of what influences the outcome of a fight. 

This being considered, it should come as no great surprise that the most important feature in the Random Forest is `P1_days_since_ff`. Recall, this variable reflects how long it has been since a boxer's career began. This perspective on career length turns out to be a natural fit.

However, it's possible a boxer could fight once, then fight once again 10 years later. In this scenario,`P1_days_since_ff` would be a value around 3,650, but this wouldn't be an accurate measurement of that boxer's accumulated wear and tear. The boxer would only have fought twice within that period. Fortunately for us, the next most important features on the plot corresponds to the aggregated number of rounds the opponents have fought. A long 'ring life' can clearly play a large role in a fighter's success (see [Ali vs Holmes](https://www.youtube.com/watch?v=Ja9iovR9B3E) for a tragic example). Conversely, too few rounds can also play a role in predicting losing.

Getting back to the variable importance plot, the two Quality of Opposition (`QOO`) metrics are shown to be important, which is nice not at the very least because they took a lot of effort to construct!

The `last6_L` and `last6_W` variables have a large amounts of variance as evidenced by the bars. This most likely ties into the discussion about how records, as they stand alone, don't adequately reflect the quality of the opposition. For some boxers, the last 6 are very important; for some, they aren't. This makes sense.

Content with the plot and with these features in mind, I experimented with various subsets of features and various configurations when fitting multilayer perceptrons in Keras.

On a positive note, because of the small file size of the flat dataset (only 1.85 GB), there were no heavy demands on IO or memory. Thus I could rip through each epoch on a basic AWS cloud GPU painlessly, and iterate on models easily. 

Regarding the actual deep architecture of the MLP, I didn't have major overfitting issues, thus didn't get any advantage with a copious amount of dropout. Batch Normalization didn't give me any advantage, so I discarded it. Fundamentally, it's a remarkably simple dataset and most models I built performed very similarly. Epochs around 10 performed just fine.

A decent final configuration looked like this: 

	mlp_004 = Sequential()
	mlp_004.add(Dense(64, activation='relu', input_dim=13))
	mlp_004.add(Dense(64, activation='relu'))
	mlp_004.add(Dense(64, activation='relu'))
	mlp_004.add(Dropout(0.2))
	mlp_004.add(Dense(64, activation='relu'))
	mlp_004.add(Dense(1, activation='sigmoid'))  

	mlp_004.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])  

	mlp_004.fit(X_train, y_train, batch_size=64, validation_split=0.2, nb_epoch=10)

The validation set accuracy returned was 73%. 

Here's the confusion matrix:

![CM](https://github.com/mobbSF/blog/blob/master/images/CM.png?raw=true)

Here's the ROC curve:  

![ROC](https://github.com/mobbSF/blog/blob/master/images/ROC.png?raw=true)

OK, so how should I feel about such relatively modest scores, in this age of a solved MNIST, self-driving cars, and [Elon Musk's dire warnings](https://www.cnbc.com/2017/08/11/elon-musk-issues-a-stark-warning-about-a-i-calls-it-a-bigger-threat-than-north-korea.html) of [Arnold coming baaack](https://www.youtube.com/watch?v=-WIwQlMesr0)?

I must admit, I feel pretty good about it. It's useful to take a step back here and reiterate that the purpose of this project is to make money gambling on boxing. If we were to use this algorithm to indicate when to place a bet, then we would prefer a larger precision at the expense of recall. What this means it that it's better to avoid betting and miss out on opportunities to win (lower recall), as long as we are more confident that when we *DO* bet, we will win. More in the third post about this approach.

Meanwhile, allow me to wander a bit (yet again!) and discuss one of the many experiments I ran that didn't pay off. I went ahead and went for a moonshot. The reality is that as far as wagering on boxing go, it's one thing to wager on a W or L outcome. But if you can win a bet by predicting a more granular types of outcomes, the payouts are several orders of magnitude better. The actual type of outcome -- either a judges decision, or an actual knockout, or a technical knockout -- that's where the big bucks are. And when it comes to knockouts, if it's possible to predict the actual round? The payouts are huge. 

I changed the labels to represent the granular outcomes mentioned above, and I rebuilt the model and crossed my fingers. Unfortunately, and not too surprisingly, accuracy dropped to around 30%. Hummm...well...worth a shot. And definitely worth revisiting again later.

Next up...prediction time!  

[Part 3: Modeling](http://www.mattobrien.me/deep-learning-for-sport-wagering-part-3-of-3.html)