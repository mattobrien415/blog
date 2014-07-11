Title:  Lebesgue measure #2
Date: 2014-07-17
Tags: math
Summary: Hi

### Show that the sum, difference and product of two BV-functions is a BV-function. ###

Let  $f$, $g$, be two BV functions over $[a, b]$.  Define a partition, $P = \{x_i = 1 \leq i \leq n \}.$  Then,
\begin{align*}
\sum_{i = 1}^{n} | (f + g )(x_i) - (f + g)(x_{i-1}) | &= \sum_{i = 1}^{n} | \{ f(x_i) + g(x_i) \} - \{ f(x_{i - 1} + g(x_{i-1}) \} |
\\  &\leq \sum_{i = 1}^{n} | f(x_i) - f(x_{i - 1} | + \sum_{i = 1}^{n} | g(x_i) - g(x_{i - 1})|
\\  &\leq  V(f, P) + V(g, P)
\end{align*} 
$\Rightarrow V(f + g, P) \leq V(f, P) + V(g, P) \leq V(f, P) + V(g, P)
\Rightarrow V(f + g, P) \leq V(f, P) + V(g, P).$
Thus, $(f + g)$ is a function of bounded variation.


