Title:  Lebesgue measure #2
Date: 2014-07-17
Tags: math
Summary: This is a proof of basic closure-type properties with respect to functions of bounded variation. I had the chance to study these when I took a class by Dr. Ovchinnikov, who was in the process of writing a [book](http://www.amazon.com/Measure-Integral-Derivative-Lebesgues-Universitext/dp/1461471958) on the subject at the time.  

### Show that the sum, difference and product of two BV-functions is a BV-function. ###

Let  $f$, $g$, be two BV functions over $[a, b]$.  Define a partition, $P = \{x_i = 1 \leq i \leq n \}.$  Then,  

$$
\begin{align*}
\sum_{i = 1}^{n} | (f + g )(x_i) - (f + g)(x_{i-1}) | &= \sum_{i = 1}^{n} | \{ f(x_i) + g(x_i) \} - \{ f(x_{i - 1} + g(x_{i-1}) \} |
\\  &\leq \sum_{i = 1}^{n} | f(x_i) - f(x_{i - 1} | + \sum_{i = 1}^{n} | g(x_i) - g(x_{i - 1})|
\\  &\leq  V(f, P) + V(g, P)
\end{align*}$ 
$\Rightarrow V(f + g, P) \leq V(f, P) + V(g, P) \leq V(f, P) + V(g, P)
\Rightarrow V(f + g, P) \leq V(f, P) + V(g, P).
$$  

Thus, $(f + g)$ is a function of bounded variation.

To show that $(f - g)$ is of bounded variation, the proof is the same and $V(f - g) \leq V(f) + V(g)$

To show that the product of two functions of bounded variation is also of bounded variation, notice that both $f$ and $g$ are bounded, and thus there exists $K \in \mathbb{N}$ such that
$|f(x)| \leq k, |g(x) | \leq k, \forall x \in P$.

Thus, 
$$\begin{align*}
\sum_{i = 1}^{n} | (fg)(x_i) - (fg)(x_{i - 1}|&= \sum_{i = 1}^{n} | f(x_i)g(x_i) - f(x_{i -1}g(x{i - 1})|
\\ &= \sum_{i = 1}^{n} |f(x_i) \{g(x_i) - g(x_{i - 1} \} + g(x_{i-1} \{ f(x_i) - f(x_{i - 1}) \} |
\\ &\leq \sum_{i = 1}^{n} \{ | f(x_i) | |g(x_i)  - g(x_{i - 1} | + | g(x_{i - 1} | | f(x_i) - f(x_{i - 1}) | \}
\\ &\leq k \sum_{i = 1}^{n} |g(x_i) - g(x_{i-1}) | + k \sum_{i = 1}^{n} | f(x_i) - f(x_{i -1})|
\\ &\leq k V(g) + kV(f).
\end{align*}$$
and so the product of two functions of bounded variation is also of bounded variation.
