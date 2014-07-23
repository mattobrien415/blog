Title:  sentiment prediction with Naive Bayes
Date: 2014-05-01
Tags: machine learning
Summary: Predicting positive or negative Amazon movie reviews  


This project consists of two sets of labelled text reviews ([positive](https://www.dropbox.com/sh/n2r4e929ahzx84o/AABdDVQ1Rlygs-XkjTytn3bAa) and [negative](https://www.dropbox.com/sh/scnnjiotbltm2za/AAAGz7NsEoG61ojzgZZQPfV-a)) for movies.  

These are used as the training set; the words are split into unigrams, and the words are classified as either positive or negative given their frequencies. 

Once the model is built, the test set is used to help determine the accuracy of the model.  

This is an early project I did some time ago, please forgive some of the less graceful elements.  

The algorithm uses these steps:  

1. For each iteration  
(a) Randomly divide your data in training and testing using 1/3 for
testing and 2/3 for training.  
(b) Use the training set to estimate the parameters $P(w|c)$ and $P(c)$ as per the naive bayes statement  
(c) For every document in the training set use the equation $$c^{*}=argmax_{c}log(P(c)) + \sum_{i=1}^{M}n_{i}(d) * log(P(w_{i}|c))$$ to compute $P(c|d)$ and predict the class c.  
(d) Compute the accuracy of the testing set.

2. Do at least 3 iterations to compute the average accuracy as your performance metric.  

The output will print results for each iteration, giving key metrics like this:

iteration 1:  
    num pos test_docs:333  
    num pos training docs:667  
    num pos correct_docs:267  
    num neg test_docs:331  
    num neg training_docs:669  
    num neg correct_docs:261  
    accuracy:79%  
iteration 2:  
    ...  
iteration 3:  
    ...  
ave_accuracy:80.3%  




Make sure to include the command line parameters `python naive-bayes.py -d my_directory` where `my_directory` is the path to the directory that holds the positive and negative reviews along with the python script.


    :::python
    #!/usr/bin/env python
    import argparse
    import os
    import random
    import math
    import collections

    def parseArgument():
        ### Code for parsing arguments
        parser = argparse.ArgumentParser(description='Parsing a file.')
        parser.add_argument('-d', nargs=1, required=True)
        args = vars(parser.parse_args())
        return args 
