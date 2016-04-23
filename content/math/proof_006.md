Title:  Functions of unbounded variation
Date: 2015-11-11
Tags: math
Summary: Proof regarding a function of bounded variation

This proof relies on the fact that a harmonic series is divergent.  

Title:  Functions of unbounded variation
Date: 2015-11-11
Tags: math
Summary: Proof regarding a function of bounded variation

This is a nice proof that relies on the fact that a harmonic series is divergent.  

###Show that the function###
$f(x) = 
\begin{cases}
xcos\frac{\pi}{x}& \text{if }x \in (0,1] \\
0, & \text{if } x =0
\end{cases}$ 
### is not a function of bounded variation.###
 
To show this function is not BV, we construct a sequence of partitions as follows:

For each $m \in \mathbb{N}$ define $P_m = \{0, \frac{1}{2m}, \frac{1}{2m-1}, \dots, \frac{1}{3}, \frac{1}{2}, 1 \}$.  To check the function we evaluate it at those partition points and find $f(P_m) = \{0, \frac{1}{2m}, \frac{1}{2m-1}, \dots, -\frac{1}{3}, -\frac{1}{2}, -1 \}$ 

Next we consider the variation of $f$:  

$\begin{align*}
\sum_{i=1}^{n} \left| f(x_i) - f(x_{i-1} \right| &= \left| \frac{1}{2m} - 0) \right| + \left|-\frac{1}{2m-1} - \frac{1}{2m} \right| + \left|\frac{1}{2m-2} \right| + \dots + \left| -\frac{1}{3} - \frac{1}{4} \right| + \left| \frac{1}{2} + \frac{1}{3} \right| + \left| -1 -\frac{1}{2} \right|
\\\\ &= \frac{1}{2m} + \frac{1}{2m-1} + \frac{1}{2m} + \frac{1}{2m} + \frac{1}{2m-2m} + \frac{1}{2m-1} + \dots + \frac{1}{3} + \frac{1}{4} + \frac{1}{2} + \frac{1}{3} + 1 + \frac{1}{2}
\\\\ &= 2(\frac{1}{2m} + \frac{1}{2m-1} + \dots +  \frac{1}{2}) + 1
\end{align*} $  


This is a harmonic series in the form of $\sum_{n=2}^{\infty} \frac{1}{n}$ which is divergent.  So no matter what $M$ we choose for a bound, we can construct a partition for which the variation is unbounded.