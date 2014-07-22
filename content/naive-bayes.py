#!/usr/bin/env python

#### HW 6  Matt O'Brien
#### This code is based on the pseudocode found in page 260, chapter 13.

import argparse
import os
import random
import math
import collections

# Reuse the stopwords list from HW 5
stopWords = ['a', 'i', 'b', 'r', 'able', 'about', 'across', 'after', 'all', 'almost', 'also',
             'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be',
             'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear',
             'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for',
             'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers',
             'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is',
             'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may',
             'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor',
             'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our',
             'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since',
             'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then',
             'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us',
             've', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which',
             'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet',
             'you', 'your', ':', ',', '.', '"', "'","it's", "(", ")", ";", "!",
             "--", "-", "?"]

def parseArgument():
    """
    Code for parsing arguments
    """
    parser = argparse.ArgumentParser(description='Parsing a file.')
    parser.add_argument('-d', nargs=1, required=True)
    args = vars(parser.parse_args())
    return args



###  This function takes the directory path and divides the file names found in the pos / neg directories
###  into the proper proportions, stored into a dict named 'D'.
def CreateD(directory):
    pos_train = []
    pos_test = []
    neg_train = []
    neg_test = []

    pos = directory + '/pos'
    neg = directory + '/neg'

    pos_names = os.listdir(pos)
    neg_names = os.listdir(neg)
    random.shuffle(pos_names)
    random.shuffle(neg_names)

    while pos_names:
        pos_train.append(pos_names.pop())
        if pos_names:
            pos_train.append(pos_names.pop())
        if pos_names:
            pos_test.append(pos_names.pop())

    while neg_names:
        neg_train.append(neg_names.pop())
        if neg_names:
            neg_train.append(neg_names.pop())
        if neg_names:
            neg_test.append(neg_names.pop())

    fileDict = {}
    fileDict["pos_train"] = pos_train
    fileDict["pos_test"] = pos_test
    fileDict["neg_train"] = neg_train
    fileDict["neg_test"] = neg_test
    return fileDict

### This function used a counter object to count the number of documents in the class 'pos' or 'neg'.  This is used
### for printing summary statistics at the end.
def CountDocsInClass(directory,subdir,file_list):
    cntr = collections.Counter()
    for file in file_list:
        f = open(directory+'/'+subdir+'/'+file)#open each File
        cntr = cntr + collections.Counter([t for t in (f.read()).split() if not t in stopWords])#add word counts to counter object
        f.close()#Close each File
    return cntr




def main():
    args = parseArgument()
    directory = args['d'][0]
    # variable for calculating average accuracy
    tot_acc = 0
    # Iterations
    for step in range(1,4):

### Here is the training code:
### First we create the dictionary of filenames using the CreateD function.
        file_dict = CreateD(directory)

### Here we count the number of documents in the 'pos' and 'neg' class using the CountDocsInClass function.
        positive_counter = CountDocsInClass(directory,'pos',file_dict['pos_train'])
        negative_counter = CountDocsInClass(directory,'neg',file_dict['neg_train'])

### These 2 lines find a total count in the counters for each class.
        tot_cnt_pos=float(sum(positive_counter.values()))
        tot_cnt_neg=float(sum(negative_counter.values()))

### We create V, as specified in the Vocabulary list
        V = set(positive_counter.keys()+ negative_counter.keys())

### The final_dict will hold the conditional probabilities for each t in V
        final_dict = {}
        for t in V:
            final_dict[t] = {'pos':(positive_counter[t]+1.0)/(tot_cnt_pos+len(V)+1),'neg':(negative_counter[t]+1.0)/(tot_cnt_neg+len(V)+1)}

### calculating prior probabilities for each class
        pos_prior = len(file_dict['pos_train'])/float(len(file_dict['pos_train']) + float(len(file_dict['neg_train'])))
        neg_prior = len(file_dict['neg_train'])/float(len(file_dict['pos_train']) + float(len(file_dict['neg_train'])))

### This code is for the Testing part of the Naive Bayes algorithm

### We create a list of classes
        C = ['pos','neg']

### initializing filescore dictionary to keep track of test data - has the test file as key and four other associated
        # parameters namely:
        #                   orig    -  is file originally +ve or -ve
        #                   pos     -  sum of log probs for +ve class
        #                   neg     -  sum of log probs for +ve class
        #                   output  -  output file classification after comparing 'pos' and 'neg'
        filescore = {}

        # for all test files combined run loop
        for file in (file_dict['pos_test']+file_dict['neg_test']):
            # initialize  the file dictionary within filescore dictionary
            filescore[file] = {}
            # populate 'orig' attribute for each file i.e. filescore[file]['orig']
            if file in file_dict['pos_test']:
                f = open(directory+'/pos/'+file)#open each File
                filescore[file]['orig'] = 'pos'
            else:
                f = open(directory+'/neg/'+file)#open each File
                filescore[file]['orig'] = 'neg'
            # extract all words for the given file into t_list after removing stopwords
            t_list = [t for t in (f.read()).split() if not t in stopWords]
            # within a file run the below loop for each class to sum the log probabilities for each class
            for clss in C:
                # initializing score variable with prior probbabilities
                if (clss == 'pos'):
                    score = math.log(pos_prior)
                else:
                    score = math.log(neg_prior)

### The code below takes logs as per pseudocode
                for t in t_list:
                    if final_dict.has_key(t):
                        score = score + math.log(final_dict[t][clss])
                    # handling unknown words in test file
                    else:
                        if clss=='pos':
                            score = score + (1/(tot_cnt_pos+len(V)+1))
                        if clss=='neg':
                            score = score + (1/(tot_cnt_neg+len(V)+1))
                filescore[file][clss] = score

###   Counting the results
            if (filescore[file]['pos'] > filescore[file]['neg']):
                filescore[file]['output'] = 'pos'
            else:
                filescore[file]['output'] = 'neg'
            f.close()

###   Create some counters to track the numbers of successes for each class
        count_positive_success = 0
        count_negative_success = 0
        for fl in filescore:
            if ((filescore[fl]['orig'] == 'pos') and (filescore[fl]['output'] == filescore[fl]['orig'])):
                count_positive_success = count_positive_success + 1
            if ((filescore[fl]['orig'] == 'pos') and (filescore[fl]['output'] == filescore[fl]['orig'])):
                count_negative_success = count_negative_success + 1

### Print results to screem
        print "iteration ",step,":"
        print "num_pos_test_docs:",len(file_dict['pos_test'])
        print "num_pos_training_docs:",len(file_dict['pos_train'])
        print "num_pos_correct_docs:",count_positive_success
        print "num_neg_test_docs:",len(file_dict['neg_test'])
        print "num_neg_training_docs:",len(file_dict['neg_train'])
        print "num_neg_correct_docs:",count_negative_success
        acc = 100 * (count_positive_success+count_negative_success)/(len(file_dict['pos_test'])+len(file_dict['neg_test']))
        print "accuracy:",acc,'%'
        tot_acc = tot_acc + acc
    print "ave_accuracy:",tot_acc/3.0

main()