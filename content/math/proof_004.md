Title:  Convex Optimization
Date: 2015-02-8
Tags: math
Summary: Convext Optimization proof #1

I don't think this is an exceptionally groundbreaking proof, but I was going through some papers from when I took [mathematical modeling](http://bulletin.sfsu.edu/sfstatebulletin/courses/40444) some time ago.

###Show from first principles that if $f^1$, $f^2$,...,$f^k$ : $\mathbb{R^n} \rightarrow \mathbb{R}$ are convex (concave) functions with the same domain, and if $\omega_1$,...,$\omega_k$ are non-negative scalars, then the function $\omega_1 f^1 +$...$+ \omega_k f^k$ is also convex (concave).###


First we examine the righthand implication, that is:  
$C \subset A$ and $C \subset B \rightarrow C \subset (A \cup B)$.   

Let $x \in C $. Then $x \in A $. So, $x \in A$ or $x \in B$. Hence $x \in (A \cup B)$.  

Second, we examine the lefthand implication, that is
$C \subset A$ and $C \subset B \leftarrow C \subset (A \cup B)$.  

This second statement is false as demonstrated by the following simple counterexample:  

Choose:  

$A = [1, 2]$, $B =[1, 3]$, and $C =[2, 3]$.  

Then, $A\cup B =[1,2,3]$.  
Hence, $C \subset A \cup B$, but, $C \not\subset A$, and $C \not\subset B$.
