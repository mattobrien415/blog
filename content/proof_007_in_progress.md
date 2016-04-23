Title:  Measurability Proof
Date: 2016-01-28
Tags: in progress
Summary: Proof by induction

Note: I can't finish this till I get Dr Ov's book so I can use Thm 2.4i, 2.4iii, 2.48

###Prove that a function $f $on $[a,b]$ is measurable iff $f$ inverse($U$) is measurable for any open set $U$ of $R$.###

$\Rightarrow$
\newline
By Theorem 2.4i, and Theorem 2.4iii, we have 2 open sets:
\newline
$ J = \{ x:  f(x) <j \}$
\newline
$K = \{ x:  f(x) > k \} ,$ where $j<k$.
\newline
Consider $J \cap K$ which is also open.
\newline
Let $U = J \bigcap K = \bigcup_{i=1}^{n}. (j_i, k_i)$, so that $f^{-1} \left( \bigcup \{ x \in [a, b] : f(x) \in U  \} \right) = f^{-}(U)$. 
\newline
\newline
$\Leftarrow$
\newline
Let $f^{-1}(U)$ be measurable.
\newline
Let $U = \left( c, \infty \right)$.
\newline
Then, $f^{-1}(U)$ measurable $\rightarrow \left\{x: f(x) > c \right\}$ is measurable.
\newline
By Theorem 2.48, $f$ is measurable.