Title:  Word frequencies for web pages
Date: 2014-06-20
Tags: text, python
Summary: Using a few select Python packages, it's fairly painless to find top word counts  

This script will take any particular webpage (in this case, the wikipedia page for Machine Learning) and do a quick a dirty scrape then count of the words on the page. It is not particularly sophisticated and can be further customized and improved for whatever your purpose may be. 


    :::python
    import urllib
    from bs4 import BeautifulSoup
    from nltk.corpus import stopwords
    from collections import Counter
    
    ## read contents from webpage
    f = urllib.urlopen('http://en.wikipedia.org/wiki/Machine_learning')
    contents = f.read()

    # create BS object
    soup = BeautifulSoup(contents)

    # clean text: lower case, remove trailing commas, remove words less than 2 characters long 
    mytext = soup.get_text()
    mytext = mytext.lower()
    mytext = mytext.replace(",", " ")
    mytext = ' '.join(word for word in mytext.split() if len(word)>2)

    # remove stopwords
    filtered_words = [w for w in mytext.split() if not w in stopwords.words('english')]

    # return counts using counter object
    mycounts = Counter(filtered_words)
    print mycounts.most_common(10)
