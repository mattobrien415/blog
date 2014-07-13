Title:  using pi as a pseudorandom number generator
Date: 2014-03-05
Tags: simulation, R
Summary: Can the digits of $\pi$ be used as a pesudorandom number generator?   


The digits of transcendental numbers such as $\pi = 3.14159 \dots$ pass many tests for randomness. So, take the first 1000 digits and use it to simulate 500 tosses of a coin, taking even digits to represent Heads and odd digits to represent Tails. Is this simulation consistent with 500 independent tosses of a fair coin?  

First, get the digits [here:](https://www.dropbox.com/s/purpzv0tzdsca08/PI.txt), download the file and read it into `R` as Pi.  


> PI <- read.table("\your_path\PI.txt",quote="\"")  

> pi_digits <- unlist(strsplit(as.character(PI[1,]),""))[2:1000]  

The proportion of even numbers in the first 1000 digits of pi is:  

is_even <- function(x) x %% 2 == 0
is_odd <- function(x) x %% 2 != 0  

> pi_digits <- as.numeric(pi_digits)  

> indices_for_evens <- pi_digits[is_even(pi_digits)]  

> indices_for_odds <- pi_digits[is_odd(pi_digits)]

> length(indices_for_evens) / 1000 

Now we will do a t-test to see if there is a significant difference between the probability of getting a heads on a coin flip, and getting an even digit of pi, by seeing if there is any significant differene between the mean for a coin flip (0.50) and the mean of getting an even (0.516). We should expect that these aren't significantly different since they are so close:  

> flips <- c(rep(1, 500), rep(0, 500))
> evens_for_t_test <- c(rep(1, each=length(indices_for_evens)),  rep(0, each=length(indices_for_odds)) )
> t.test(flips, evens_for_t_test, alternative="two.sided")

The p-value is 0.4881.  At a 0.05 significance level, we fail to reject the null hypothesis.Thus, we infer that the digits of pi have passed a test for randomness.  

So why aren't the digits of $\pi$ used to generate random numbers?  One problem may be the choice of a seed -- in one sense, each time you re-run your simulation based on the digits of $\pi$, you will have to pick up where you left off last time.  This invariably will lead to the requirement of having to calculated $\pi$ to a huge number of decimal places.  In the end, that computational requirement is the major bottleneck and that bottleneck can probably can be arrived at in a number of novel and unfortunate ways. 
