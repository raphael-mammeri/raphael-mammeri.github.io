---
description: Nullam urna elit, malesuada eget finibus ut, ac tortor. 
---

!!!warning
    Page in progress. There may be typos and the content is subject to change.

<a href="../integral/#1.1"><b>definition</b></a>

# Measure Theory Basics
## Introduction
Measure theory is a branch of mathematics that provides a rigorous framework for understanding and quantifying the concept of "size" or "measure" of sets. It deals with the study of measures, which are functions that assign a non-negative real number to subsets of a given set.


In probability theory,  measure theory introduces key concepts such as 
probability spaces, sample spaces and events. The numerical values that are 
assigned to events will capture the likelihood or uncertainty of outcomes.
These concepts establish a solid foundation for studying probabilistic 
models and their properties.

Let's see an illustration in the case of real number $\mathbb{R}.$

### Lebesgue Measure on Real Numbers
Consider an interval  $I = [a, b] \subset \mathbb{R}$  where $b>a.$ 
The most 
natural measure one would assign to the interval $I$ would be $b-a.$ 
This would also have been the natural measure if 
one or 
its two sides of $I$ were open. Let's note this "measure" $\mu.$


We also would want this definition to be extended to any set that can be 
expressed as the disjoint
union of intervals as follows : if $E \subset \mathbb{R}$ can be writen as 
a disjoint union of intervals $I_i$ for $i$ in some index set $S,$ then we 
would 
define the measure of $E$ as the sum measures of the different 
intervals $I_i$ :

$$
\mu(E) = \sum_{i \in S} \mu(I_i) = \sum_{i \in S} (b_i - a_i)
$$
where $a_i < b_i \in \mathbb{R}$ are the sides of the interval $I_i.$

* Is this definition mathematically coherent, meaning does it lead to 
  mathematical contradictions ?
* Does it make sens if the index set $S$ is infinite ?
* Can we extend this definition to any subset of $\mathbb{R}$ ?
* If it can not be extended to all subsets of $\mathbb{R}$ is there a 
  smaller collection of subsets of $\mathbb{R}$ to which we can extend the 
  definition of $\mu$ ?

These questions are addressed by defining the notions of $\sigma$-algebras, 
measurable spaces and a proper 
definition of a measure and with some tools like the measure 
extension theorem.
In this example the collection of sets on which we can extend the set 
function $\mu$ is called the Borel $\sigma$-algebra and $\mu$ is called the 
Lebesgue measure. We will develop their construction in the next subsections.

## Classes of sets
!!! definiiton
    A class $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ is called  a **semiring**
    if:

    * $\emptyset \in \mathcal{A}$,
    * for $A, B \in \mathcal{A}$ the difference $B \setminus A$ is a finite 
    union of mutually disjoint sets in $\mathcal{A}$,
    * the class $\mathcal{A}$ is $\cap$-closed.

## Measure Spaces
  Let $\mathcal{A} \subseteq \mathcal{P}(\Omega)$,
  $\mu: \mathcal{A} \to [0, \infty]$ a set function,
  $I$ an index set and $(A_i)_{i \in I}$ such that $A_i \in \mathcal{A}$ for any $i \in I$.
!!! definiiton
    We say that $\mu$ is :

    * **monotone** if $\mu(A) \leq \mu(B)$ for any $A \subseteq B$  in $\mathcal{A}$,
    * **additive** if $\mu(\cup_{i \in I}A_i) = \sum_{i \in I}\mu(A_i)$ for $I$ finite and $(A_i)_{i \in I}$ mutually disjoint,
    * **$\sigma$-additive** if $\mu(\cup_{i \in I}A_i) = \sum_{i \in I}\mu(A_i)$ for $I$ countable and $(A_i)_{i \in I}$ mutually disjoint,
    * **subadditive** if for any $A\subseteq \cup_{i \in I}A_i$ and $I$ finite we have $\mu(A) \leq \sum_{i \in I}A_i$
    * **$\sigma$-subadditive** if for any $A\subseteq \cup_{i \in I}A_i$ and $I$ countable we have $\mu(A) \leq \sum_{i \in I}A_i$
    
## Measure Extension Theorem

!!! thm
    Let $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ be a semiring and  $\mu: \mathcal{A} \to [0, \infty]$ additive, $\sigma$-subadditive and $\sigma$-finite such that $\mu(\emptyset)=0$.
    There exists a unique $\sigma$-finite measure $\tilde{\mu }$ on $\sigma(\mathcal{A})$ such that for any $A \in \mathcal{A}$:
    $$
    \tilde{\mu }(A) = \mu(A)
    $$

??? proof
    The proof of this theorem is beyond the scope of these lectures however we give a sketch here of the construction of the extended measure $\tilde{\mu }$.
    From $\mu$ a set function $\mu^*$ on $\mathcal{P}(\Omega)$ is defined as follows: for any $A \subseteq \Omega$:

    $$
    \mu^*(A):= \inf_{(A_i)_{i \in I} \in \mathcal{U}(A)} \sum_{i \in I} \mu(A_i)
    $$

    where $\mathcal{U}(A)$ is the set of countable coverings $(A_i)_{i \in I}$ of $A$ (i.e. $A \subseteq \cup_{i \in I}A_i$) with $A_i \in \mathcal{A}$ for all $i \in I$.
    The set function $\mu^*$ is an *outer measure* that defines a measure on the $\sigma$-algebra $\mathcal{M}(\mu^*)$ of $\mu^*$-measurable sets. Moreover for any $A \in \mathcal{A}$, $\mu(A) = \mu^*(A)$, $\mathcal{A} \subseteq \mathcal{M}(\mu^*)$ hence $\sigma(\mathcal{A}) \subseteq \mathcal{M}(\mu^*)$  and $\mu^*$ is the unique measure that extends $\mu$ to $\sigma(\mathcal{A})$.
