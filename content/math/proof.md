Title:  Lebseque measure #1
Date: 2014-05-29
Tags: math
Summary: Lebesque measure #1
Here is a fun proof that illuminates an important property of Lebesque measure.  Note that the function $m()$ refers to measure.

### Let $X$ be a closed subset of $[0,1]$ such that $m(X) = 1$.  Prove that $X = [0, 1]$. ###

Let $X$ be closed subset of $[0,1]$ such that $m(X) = 1$.  We need to show that $X= [0,1]$.  Let $a=inf(X)$ and let $b=sup(X)$.  Suppose, by contradiction, that $X \neq [0, 1]$.  Then, there are 3 cases for which $X=[0, 1]$.  

**Case 1:**  $a > 0$.  By definition of measure, $m(X) = (b -a) - m([a, b]\backslash X) = 1$, but $(b - a) < 1$ and $m(X)$ cannot equal $1$.  

**Case 2:**  $b > 1$.  Again, be definition of measure, we fnd that $(b - a) < 1$ and $m(X)$ cannot equal $1$.  

**Case 3:**  $a = 0$, and b = $0$, since $b - a = 1$, and since $X = [0, 1]$, then $[0, 1]$ \ $X = 0$ which implies that $X$ must be equal to $[0, 1]$.