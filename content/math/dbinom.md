###pbinom is not the  probability distribution function for the binomial distribution  

I love R. But it does has some things that are a bit irksome.  For example, I have found it somewhat difficult to remember which prefix corresponds to which function, when working with distributions. 

Here is a quick quiz:  

**Given a binomial distribution:**  
 **dbinom ---> ?**  
 **pbinom --->  ?**  

1.  probability distribution function  
cumulative mass function

2.   cumulative mass function  
 probability distribution function  

*Answer:  1*  
 
I am temped to choose 2, since pbinom feels like it should correspond with pdf.  After all, ‘p’ is the first initial of the first word in the phrase “probability density function.”  However, that is not the case.
