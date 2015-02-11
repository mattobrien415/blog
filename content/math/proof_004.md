Title:  Convex Optimization #1
Date: 2015-02-8
Tags: math
Summary: Convext Optimization proof #1

I don't think this is an exceptionally groundbreaking proof, but I was going through some papers from when I took [mathematical modeling](http://bulletin.sfsu.edu/sfstatebulletin/courses/40444) some time ago.

###Show from first principles that if $f^1$, $f^2$,...,$f^k$ : $\mathbb{R^n} \rightarrow \mathbb{R}$ are convex (concave) functions with the same domain, and if $\omega_1$,...,$\omega_k$ are non-negative scalars, then the function $\omega_1 f^1 +$...$+ \omega_k f^k$ is also convex (concave).###

Given $f^1$, $f^2$,...,$f^k$ as convex functions and $\omega_1$,...,$\omega_k$ as non-negative scalars, we need to show that $\omega_1 f^1 +$...$+ \omega_k f^k$ is also convex; that is, $\sum_{i = 1}^k \omega_i f_i$ is a convex function.

Using first principles, we consider a linear combination $\lambda x + (1 - \lambda)y$ where $\lambda \in [0, 1]$, $x, y \in $ the domain of all $f^k$.

$$\begin{align\*}
f(\lambda x + (1 - \lambda)y &= \sum_{i=1}^k \omega_i f_i (\lambda x + (1 - \lambda )y) 
\\\\ &\leq \sum_{i=1}^k \omega_i (\lambda f_i (x) + (1- \lambda) f_i(y)) 
\\\\ &= \lambda \sum_{i =1}^k \omega_i f_i(x) = (1 - \lambda) \sum_{i =1}^k \omega f_i(y)
\\\\ &= \lambda f(x) + (1 - \lambda) f(x).
\end{align\*}$$

Thus we have shown that convexity holds under this operation.