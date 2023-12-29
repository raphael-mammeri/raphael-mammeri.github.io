---
#template: home.html
#icon: material/alert-outline
description: Nullam urna elit, malesuada eget finibus ut, ac tortor. 
hide:
  - footer

# use here to add options to pages in numbering and style
---


## Introduction
Measure theory is a branch of mathematics that provides a rigorous framework for understanding and quantifying the concept of size or measure of sets. It deals with the study of measures, which are functions that assign a non-negative real number to subsets of a given set.
In probability theory,  measure theory introduces key concepts such as 
probability spaces, sample spaces and events. The numerical values that are 
assigned to events will capture the likelihood or uncertainty of outcomes.
These concepts establish a solid foundation for studying probabilistic 
models and their properties.

In this section we will start by defining some classes of sets like algebras, $\sigma$-algebras...etc. These classes will define the subsets on which measures will be defined (and extended).
They are important to ensure that if we can measure some sets of a space, then the sets resulting from unions, intersections, or other operations that will be specified in the next subsections, will also be measurable. This will result in the definition of measurable spaces.

After that we will give definitions and properties of set functions and define measures spaces and probability spaces then state the measure extension theorem which is crucial for the construction of many measures espacially in the case of real numbers.

Finally, using the results of the previous subsections we introduce the Lebesgue-Borel measure in the case of real numbers $\mathbb{R}$ and more generally $\mathbb{R}^n$.




Before we dive into the technical definitions and results let's consider the example of real numbers which is interesting as it illustrates well the process of measures construction. Suppose we want to measure subsets of $\mathbb{R}.$ To start we can consider the "simple" subsets of intervals $\mathcal{A} = \{ I \subseteq \mathbb{R}\ |\ I \text{ is an interval in }\mathbb{R} \}$
and $\mu : \mathcal{A} \to [0, \infty]$ the set function defined for an interval $I$ with sides $a$ and $b$ (either open or closed on the sides) by:
$$
\mu(I) = b - a
$$
This gives a natural and intuitive sens of a measure on such sets. However can we extend this definition to a broader set of subsets of $\mathbb{R}$ ? We can easily extend it to finite unions of such intervals. For example for two disjoint intervals $I$ and $J$ in $\mathcal{A}$ we define:
$$
\mu(I \cup J) = \mu(I) + \mu(J) 
$$
and so on for the union of more than two intervals. We can eaily check that this definition does not depend on the representation of the finite unions as a disjoint union of intervals.
Before continuing the discussion on the extension of such a set function we can start to see some properties that measures will have:

* the measure of the empty set ($]a, a[$ for some $a \in \mathbb{R}$) is equal to $a-a = 0$,
* if $A$ and $B$ are finite unions of intervals such that $A \subseteq B$ then $\mu(A) \leq \mu(B)$ and
* the measure of disjoint unions of sets is the sum of the measures of theses sets.

Back to the extension of the set function $\mu$, the questions we could have are:

* can $\mu$ be extended to all subsets of $\mathbb{R}$ ?
* If not can we extend it more than to the finite unions of intervals ?
* What about defining similar measures for $\mathbb{R}^n$ where $n > 1$ ?

 The precise answers to these questions will be given in subsections [Measure Extension Theorem](Measure Extension Theorem) and [Lebesgue-Borel Measure](lebesgue-Borel).


# Classes of sets

The most important class of sets is the class of $\sigma$-algebras. It is the class on which measures and probability measures are defined. However, as we will see, measures on $\sigma$-algebras are usually defined on a smaller class then extended to the generated $\sigma$-algebra.
One of these smaller classes is the class of semi-rings.

We will note $\Omega$ a non-empty set.

@tag(semi-rings)
!!! definition "Semi-rings"
    Let $\mathcal{A} \subseteq \mathcal{P}(\Omega)$. The class $\mathcal{A}$ is called  a **semiring** if :

    * $\emptyset \in \mathcal{A}$,
    * for any $A, B \in \mathcal{A}$ then $B \setminus A$ is a finite union of mutually disjoint sets in $\mathcal{A}$,
    * $\mathcal{A}$ is $\cap$-closed i.e. closed under finite intersections.

!!! definition 
    An **algebra** (resp. **$\sigma$-algebra**) if :

    * $\Omega \in \mathcal{A}$,
    * $\mathcal{A}$ is closed under complements,
    * Closed under finite (resp. countable) unions, and we write $\mathcal{A}$ is $\cup$-closed (resp. $\sigma$-$\cup$-closed).

@tag(sigma)
The $\sigma$-algebras are the classes of sets that will be considered as ***events*** in probability theory, and more generally the classes on which measures are defined.


!!! lemma
    @tag(algebra definition)
    The class $\mathcal{A}$ is an **algebra** if and only if:

    * $\Omega \in \mathcal{A}$,
    * $\mathcal{A}$ is $\setminus$-closed i.e. for any $A, B \in \mathcal{A}$ then $A \setminus B \in \mathcal{A}$,
    * $\mathcal{A}$ is $\cup$-closed.

    If $\mathcal{A}$ is an algebra (resp. $\sigma$-algebra) then $\mathcal{A}$ is $\cap$-closed (resp. $\sigma$-$\cap$-closed).

!!! proof
    We leave the proof of the first part to the reader.
    The second part is a consequence of de Morgan's rule: $(\cup A_i)^c = \cap A_i^c$.

It is easy to show that for any arbitrary non-empty index set $I$ and $(\mathcal{A}_i)_{i \in I}$ a family of algebras (resp. $\sigma$-algeras) the intersection $\cap_I\mathcal{A}_i$ is also an algebra (resp. $\sigma$-algebra).

!!! definition "" 
    Let $\mathcal{E} \subseteq \mathcal{P}(\Omega)$ and $I$ the set of $\sigma$-algebras of $\Omega$ containing $\mathcal{E}.$
    The $\sigma$-algebra
    $$
    \sigma(\mathcal{E}):= \cap_{\mathcal{A} \in I}\mathcal{A}
    $$
    is called the $\sigma$-algebra generated by $\mathcal{E}$ and $\mathcal{E}$ is called a generator of $\sigma(\mathcal{E}).$

Note that in the definition above the index set $I$ is never empty since it contains the $\sigma$-algebra $\mathcal{P}(\Omega).$
It is also clear from the definiton above that if $\mathcal{E}$ is a $\sigma$-algebra then $\mathcal{E}=\sigma(\mathcal{E})$
and if $\mathcal{E'} \subseteq \mathcal{E}$ then $\sigma(\mathcal{E'}) \subseteq \sigma(\mathcal{E})$.

!!! definition
    Let $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ and $A \subseteq \Omega$ non-empty.
    The class
    $$
    \mathcal{A}\vert_A := \\{A \cap B \\ ; B \in \mathcal{A} \\}
    $$
    is called the trace of $\mathcal{A}$ on $A$ or the restriction of $\mathcal{A}$ to $A$.

It can easily be shown that if $\mathcal{A}$ is an algebra (resp. $\sigma$-algebra) on $\Omega$ then
$\mathcal{A}\vert_A$ is an algebra (resp. $\sigma$-algebra) on $A$ for any non-empty $A \subseteq \Omega$.

## Measure Spaces
  Let $\mathcal{A} \subseteq \mathcal{P}(\Omega)$,
  $\mu: \mathcal{A} \to [0, \infty]$ a set function,
  $I$ an index set and $(A_i)_{i \in I}$ such that $A_i \in \mathcal{A}$ for any $i \in I$.
!!! definition
    We say that $\mu$ is :

    * **monotone** if $\mu(A) \leq \mu(B)$ for any $A \subseteq B$  in $\mathcal{A}$,
    * **additive** if $\mu(\cup_{i \in I}A_i) = \sum_{i \in I}\mu(A_i)$ for $I$ finite and $(A_i)_{i \in I}$ mutually disjoint,
    * **$\sigma$-additive** if $\mu(\cup_{i \in I}A_i) = \sum_{i \in I}\mu(A_i)$ for $I$ countable and $(A_i)_{i \in I}$ mutually disjoint,
    * **subadditive** if for any $A\subseteq \cup_{i \in I}A_i$ and $I$ finite we have $\mu(A) \leq \sum_{i \in I}\mu(A_i)$,
    * **$\sigma$-subadditive** if for any $A\subseteq \cup_{i \in I}A_i$ and $I$ countable we have $\mu(A) \leq \sum_{i \in I}\mu(A_i)$,
    * a **content** if $\mathcal{A}$ is a semiring, $\mu(\emptyset)=0$ and $\mu$ is additive.

!!! definition
    A set function $\mu : \mathcal{A} \to [0, \infty]$ is called a **measure** on $(\Omega, \mathcal{A})$ if $\mathcal{A}$ is a $\sigma$-algebra, $\mu(\emptyset)=0$ and $\mu$ is $\sigma$-additive.

Let $\mu$ be a content on a semiring $\mathcal{A}$. 

!!! definition
    We say that $\mu$ is **finite** if $\mu(\Omega) < \infty$ and  **$\sigma$-finite** if there exists a family $(\Omega_n)_{n \in \mathbb{N}}$ in $\mathcal{A}$ such that $\Omega = \cup_{n \in \mathbb{N}}\Omega_n$ and $\mu(\Omega_n) < \infty$ for all $n \in \mathbb{N}$.

Let $\Omega$ be a non-empty set and $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ and $\mu : \mathcal{A} \to [0, \infty]$ a set function.

!!! definition
    * We say that the pair $(\Omega, \mathcal{A})$ is a **measurable space** if $\mathcal{A}$ is a $\sigma$-algebra and $\mu$ a measure on $\mathcal{A}$.
    * If $(\Omega, \mathcal{A})$ is a measurable space subsets of $\Omega$ in $\mathcal{A}$ are called **measurable sets**.
    * A measurable space $(\Omega, \mathcal{A})$ is called **discrete** if $\Omega$ is at most countable and $\mathcal{A}=\mathcal{P}(\Omega)$.
    * The set of finite (resp. $\sigma$-finite) measures on a measurable space $(\Omega, \mathcal{A})$ is denoted $\mathcal{M}_f(\Omega, \mathcal{A})$ (resp. $\mathcal{M}_{\sigma}(\Omega, \mathcal{A})$).

Let $\mu$ be a content on a $\sigma$-algebra $\mathcal{A}$

!!! lemma
    The following three properties are equivalent 

    * $\mu$ is a measure (it is a $\sigma$-additive)
    * $\mu$ is $\sigma$-subadditive
    * $\mu$ is lower semicontinuous


@tag(Measure Extension Theorem)
## Measure Extension Theorem

!!! danger "Measure Extension Theorem" @tag(measure_extension_theorem)
    Let $\mathcal{A} \subseteq \mathcal{P}(\Omega)$ be a semiring and  $\mu: \mathcal{A} \to [0, \infty]$ additive, $\sigma$-subadditive, $\sigma$-finite and $\mu(\emptyset)=0$.
    There exists a unique $\sigma$-finite measure $\tilde{\mu }$ on $\sigma(\mathcal{A})$ such that for any $A \in \mathcal{A}$:
    $$
    \tilde{\mu }(A) = \mu(A)
    $$

???+ proof "Sketch of the proof"
    The proof of this theorem is beyond the scope of these lectures however we give a sketch here of the construction of the extended measure $\tilde{\mu }$.
    From $\mu$ a set function $\mu^*$ on $\mathcal{P}(\Omega)$ is defined as follows: for any $A \subseteq \Omega$:

    $$
    \mu^*(A):= \inf_{(A_i)_{i \in I} \in \mathcal{U}(A)} \sum_{i \in I} \mu(A_i)
    $$

    where $\mathcal{U}(A)$ is the set of countable coverings $(A_i)_{i \in I}$ of $A$ (i.e. $A \subseteq \cup_{i \in I}A_i$) with $A_i \in \mathcal{A}$ for all $i \in I$.
    The set function $\mu^*$ is an *outer measure* that defines a measure on the $\sigma$-algebra $\mathcal{M}(\mu^*)$ of $\mu^*$-measurable sets. Moreover for any $A \in \mathcal{A}$, $\mu(A) = \mu^*(A)$, $\mathcal{A} \subseteq \mathcal{M}(\mu^*)$ hence $\sigma(\mathcal{A}) \subseteq \mathcal{M}(\mu^*)$  and $\mu^*$ is the unique measure that extends $\mu$ to $\sigma(\mathcal{A})$.

@tag(lebesgue-Borel)
## Lebesgue-Borel Measure
* Borel sigma algebra of a topological space
* The example of $\mathbb{R}^n$
* List of generators of the Borel sigma algebra on $\mathbb{R}^n$
* Make the remark that the classes of generator cited are countable and that this is a very crucial property