Title:  Set Theory #1
Date: 2014-04-10
Tags: math  git 
Summary: Set theory proof #1

A great little proof that is simple and a nice way to practice your $\\Latex$.

###Demonstrate that this is a false claim: $C \subset A$ and $C \subset B \Leftrightarrow C \subset (A \cup B)$.###


First we show the proof for the righthand implication, that is  
$C \subset A$ and $C \subset B \rightarrow C \subset (A \cup B)$   

Let $x \in C $ then $x \in A $. So, $x \in A$ or $x \in B$. Hence $x \in (A \cup B)$.  

Second, we show the proof for the lefthand implication, that is
$C \subset A$ and $C \subset B \leftarrow C \subset (A \cup B)$.  

This second statement is false as demonstrated by the following simple counterexample:  

Let

$\being{\align\*}
A &= [ 1, 2]\\\\ 
  B &=[1.3]\\\\
  C&=[2, 3]\\\\
 \text{then, } A\cup B &=[1,2,3]\\\\
 \text{hence, } C &\subset A \cup B\\\\
 \text{but,  } C &\not\subset A\\\\
 C &\not\subset B\\\\
 \end{align\*}$
