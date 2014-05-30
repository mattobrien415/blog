Title:  Hello! Date: 2014-05-29 Tags: misc Summary: Some proofs I'm fond of  

Here's an old favorite:  

\begin{comment}
\textbf{Let X be a closed subset of [0,1] such that m(X) = 1.  Prove that X = [0, 1].}
\newline
\newline
Let $X$ be closed subset of $[0,1]$ such that $m(X) = 1$.  We need to show that $X= [0,1]$.  Let $a=inf(X)$ and let $b=sup(X)$.  Suppose, by contradiction, that $X \neq [0, 1]$.  Then, there a 3 cases for which $X=[0, 1]$.
\newline
Case 1:  $a > 0$.  By definition of measure, $m(X) = (b -a) - m([a, b]\backslash X) = 1$, but $(b - a) < 1$ and $m(X)$ cannot equal $1$.
\newline
Case 2:  $b > 1$.  Again, be definition of measure, we fnd that $(b - a) < 1$ and $m(X)$ cannot equal $1$.
\newline
Case 3:  $a = 0, and b = 0$, since $b - a = 1$, and since $X = [0, 1]$, then $[0, 1]\textbackslash X = 0$ which implies that $X$ must be equal to $[0, 1]$.
\end{comment}