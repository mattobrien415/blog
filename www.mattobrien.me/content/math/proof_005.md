Title:  Proof by induction
Date: 2015-11-11
Tags: math
Summary: Proof by induction

Good example of a proof by induction. The problem is from a chapter in the book [The Art of Proof](http://bulletin.sfsu.edu/sfstatebulletin/courses/40444).

###For $x\not = 1$ and $k \in\mathbb{Z_{{\geq}0}}$, prove that $\displaystyle\sum\limits_{j=0}^k x^j =\frac {1-x^{k+1}}{1-x}$###

We proceed by proof by Induction.  
Let $P(k)$ denote the statement  $\displaystyle\sum\limits_{j=0}^k x^j =\frac {1-x^{k+1}}{1-x}$.  
Checking the base case, in this case $k=0$, we show that  \begin{align\*}  
P(0) &=\displaystyle\sum\limits_{j=0}^0 x^j \\\\
&=\frac {1-x^{0+1}}{1-x}\\\\
&=\frac {1-x}{1-x}\\\\
&=1.
\end{align\*}
Now, we assume $P(k)$ to be true, that is $\displaystyle\sum\limits_{j=0}^k x^j =\frac {1-x^{k+1}}{1-x}$. 
Next we show  $P(k+1)$ to be true, that is
\begin{align\*}
\displaystyle\sum\limits_{j=0}^{k+1} x^j &= \displaystyle\sum\limits_{j=0}^k x^j + x^{k+1}\\\\
&= \frac {1-x^{k+1}}{1-k} +   {x^{k+1}}   \text{             by the induction hypothesis}\\\\
&=  \frac {1-x^{k+1}}{1-x} +  \frac {x^{k+1}*({1-x})}{1-x}\\\\
&=\frac{1-x^{k+1}+x^{k+1}-x^{k+1+1}}{1-x}\\\\
&=\frac{1-x^{k+2}}{1-x}.\\\\
\end{align\*}. 