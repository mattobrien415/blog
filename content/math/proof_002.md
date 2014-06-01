Title: Numerical Analysis 
Date: 2014-05-31 
Tags: math 
Summary: Numerical Analysis #1 


For Lagrange interpolation on the nodes
$x_0 < x_1 < \cdots < x_{n-1} < x_n$
of the data $\{(x_i, f(x_i))\}_{i=0}^n$, the interpolating polynomial is
$p(x) = \sum_{i  = 0}^n f(x_i)L_{n, i}(x)$,
where
\begin{align*}
L_{n,i}(x) = \frac{(x-x_{0}) \cdots (x-x_{i-1})(x-x_{i+1})\cdots(x-x_{n})}{(x_{i}-x_{0}) \cdots (x_{i}-x_{i-1})(x_{i}-x_{i+1})\cdots(x_{i}-x_{n})}
\end{align*}
Prove that
\begin{align*}
L_{n,0}(x) = 1 + \frac{(x-x_{0})}{(x_{0}-x_{1})} + \frac{(x-x_{0})(x-x_{1})}{(x_{0}-x_{1})(x_{0}-x_{2})} + \cdots + \frac{(x-x_{0})(x-x_{1})\cdots (x-x_{n-1})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})}
\end{align*}
and state the general result for $L_{n,i}(x)$.

\begin{proof}
For
$i=0$
, 
\begin{align*}
L_{n,0}(x) = \frac{(x-x_{1})(x-x_{2})\cdots (x-x_{n})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})}
\end{align*}

Now, let

\begin{align*}
L_{n, 0}^{*} = 1 + \frac{(x-x_{0})}{(x_{0}-x_{1})} + \frac{(x-x_{0})(x-x_{1})}{(x_{0}-x_{1})(x_{0}-x_{2})} + \cdots + \frac{(x-x_{0})\cdots(x-x_{n-1})}{(x_{0}-x_{1})\cdots(x_{0}-x_{n})}
\end{align*}

We will use induction.  We need to show that 

\begin{align*}
L_{n,0}(x) &= L^{*}_{n, 0}(x) \text{   . So, we will prove that }
\\ L_{n+1, 0}(x) &= L_{n+1, 0}^{*}(x).
\end{align*}

\begin{align*}
L_{n+1, 0}(x) &= \frac{(x-x_{1}(x-x_{2})\cdots(x-x_{n})(x-x_{n+1})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})(x_{0}-x_{n+1})}.
\\ \text{ Now,}\\L_{n+1, 0}^{*}(x) &= 1 + \frac{(x-x_{0})}{(x_{0}-x_{1})}+ \frac{(x-x_{0})(x-x_{1})}{(x_{0}-x_{1})(x_{0}-x_{2})} + \cdots + \frac{(x-x_{0})\cdots(x-x_{n-1})}{(x_{0}-x_{1})\cdots(x_{0}-x_{n})} + \frac{(x-x_{0})(x-x_{1})\cdots(x-x_{n-1})(x-x_{n})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})(x_{0}-x_{n+1})}
\\ &= L_{n, 0}^{*}(x) + \frac{(x-x_{0})(x-x_{1})\cdots(x-x_{n-1})(x-x_{n})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})(x_{0}-x_{n+1})}\text{.}
\end{align*}

Since by assumption $L_{n,0}(x) = L^{*}_{n, 0}(x)$, we have
\begin{align*}
L_{n+1,0}^{*}(x) &= \frac{(x-x_{1})\cdots(x-x_{n})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})} + \frac{(x-x_{0})(x-x_{1})\cdots(x-x_{n-1})(x-x_{n})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})(x_{0}-x_{n+1})}
\\ &= \frac{(x-x_{1})(x-x_{2})\cdots(x-x_{n})(x_{0}-x_{n+1})+(x-x_{0})(x-x_{1})(x-x_{n-1})(x-x_{n-1})(x-x_{n})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})(x_{0}-x_{n+1})}
\\ &= \frac{(x_{0}-x_{n+1}+x-x_{0})[(x-x_{1})\cdots(x-x_{n})]}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})(x_{0}-x_{n+1})}
\\ &= \frac{(x-x_{n+1})(x-x_{1})(x-x_{2})\cdots(x-x_{n})}{(x_{0}-x_{1})(x_{0}-x_{2})\cdots(x_{0}-x_{n})(x_{0}-x_{n+1})}
\\ &=L_{n+1,0}(x)
\end{align*}

Since $L_{n+1, 0}(x) = L_{n+1,0}^{*}(x)$, we can deduce that our assumption holds true for $L_{n,0}(x) = L_{n, 0}^{*}(x)$.
\\Note that every $x_{0}$ term in $L_{n,0}^{*}(x)$ disappears.  So,

\begin{align*}
L_{n, i}^{*}(x) = 1 + \frac{(x-x_{i})}{(x_{i}-x_{1})}+ \cdots + \frac{(x-x_{1})(x-x_{2})\cdots(x-x_{n-1})}{(x_{i}-x_{1})(x_{i}-x_{2})\cdots(x_{i}-x_{i-1})(x_{i}-x_{i+1})\cdots(x_{i}-x_{n})}.
\end{align*}

With the same induction technique,
\begin{align*}
L_{n+1,i=1}^{*} = \frac{(x-x_{i})}{(x_{i}-x_{1})}&+\cdots+\frac{(x-x_{i})(x-x_{2})\cdots(x-x_{n-1})}{(x_{i}-x_{1})(x_{i}-x_{2})\cdots(x_{i}-x_{i-1})(x_{i}-x_{i+1})\cdots(x_{i}-x_{n})} 
\\  &+ \frac{(x-x_{1})(x-x_{2})\cdots(x-x_{n-1})(x-x_{n})}{(x_{i}-x_{1})(x_{i}-x_{2})\cdots(x_{i}-x_{i-1})(x_{i}-x_{i+1})\cdots(x_{i}-x_{n})(x_{i}-x_{n+1})}.
\end{align*}

Now,
\begin{align*}
L_{n+1,i}(x) &= \frac{(x-x_{i})\cdots(x-x_{i-1})(x-x_{i+1})\cdots(x-x_{n})(x-x_{n+i})}{(x_{i}-x_{i})\cdots(x_{i}-x_{i-1})(x_{i}-x_{i+1})\cdots(x_{i}-x_{n})(x_{i}-x_{n+i})}.
\\ \text{Now,}
\\ L_{n+1, i}^{*}(x) &= \frac{L_{n,i}^{*}(x) +(x- x_{1})(x- x_{2})\cdots(x- x_{n-i})(x- x_{n})}{(x_{i}- x_{1})\cdots(x_{i}- x_{i-1})(x_{i}- x_{i+1})\cdots(x_{i}- x_{n})(x_{i}- x_{n+i})}
\\ &= \frac{(x- x_{1})\cdots(x- x_{i-1})(x- x_{i+1})\cdots(x- x_{n})}{(x_{i} -x_{1})\cdots(x_{i} -x_{i-1})(x_{i} -x_{i+1})\cdots(x_{i} -x_{n})} +
\frac{(x-x_{1})(x-x_{2})\cdots(x-x_{n-1})(x-x_{n})}{(x_{i}-x_{1})\cdots(x_{i}-x_{i-1})(x_{i}-x_{i+1})\cdots(x_{i}-x_{n})(x_{i}-x_{n+1})}.
\\ L_{n+1,i}^{*}(x) &= \frac{(x-x_{i}+x_{i}-x_{n+1})[(x-x_{1})\cdots(x-x_{i-1})(x-x_{i+1})\cdots(x-x_{n})]}{(x_{i}-x_{1})\cdots(x_{i}-x_{i-1})(x_{i}-x_{i+1})\cdots(x_{i}-x_{n})(x_{i}-x_{n+1})}
\\&= L_{n+1, i}(x).
\end{align*}

Thus $L_{n+1,i}(x) = L_{n+1,i}^{*}(x)$.
\end{proof}