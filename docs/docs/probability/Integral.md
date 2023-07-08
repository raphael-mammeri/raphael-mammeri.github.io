# Basic Definitions and Results of the Integral
In this section $(\Omega, \mathcal{A}, \mu)$ will be a measure space.
Let $\mathbb{E}$ be the set of simple functions on $\Omega$ and 
$\mathbb{E}^+$ the set of positive simple functions (values in $[0, \infty]$).

!!! definiiton
    We define the integral of a positive simple function
    $f = \sum_{i=1}^n \alpha_i\mathbf{1}_{A_i}$
    by:
    $$
    \int{f\\ d\mu} := \sum_{i=1}^{n} \alpha_i \mu(A_i)
    $$
For this definition to be correct we need to make sure it does not depend on
the representation of $f$:

!!! lemma
    If $f = \sum_{i=1}^{m} \beta_i \mathbf{1}_{A_i}$ is another 
    reperesentation of $f$ then: 
    $$
    \sum_{i=1}^{n} \alpha_i \mu(A_i) = \sum_{i=1}^{m} \beta_i \mu(B_i)
    $$
    Moreover the map $f \mapsto \int{f\\ d\mu}$ is positive linear and 
    monotone increasing.

Starting from positive simple functions we now extend the definition of 
the integral to measurable functions.

!!! definiiton
    Let $f: \Omega \to [0, \infty]$ be measurable. We define the 
    **integral** of
    $f$ by:
    $$
    \int{f\\ d\mu} := \underset{g \in \mathbb{E}^+,\\ g\leq f}{\text{sup}}
    \int g\\ d\mu
    $$
    Now let $f$ with values in $\overline{\mathbb{R}}.$
    The function $f$ is called $\mu$-**integrable** if 
    $\int |f| \\ d\mu < \infty$.

    We note $\mathcal{L}^1(\Omega, \mathcal{A}, \mu)$,
    or simply $\mathcal{L}^1(\mu)$, the set of $\mu$-**integrable** functions.

    For $f \in \mathcal{L}^1(\mu)$ we define:
    $$
    \int f \\ d\mu := \int f^+ \\ d\mu - \int f^- \\ d\mu 
    $$
    Finally, if $A \in \mathcal{A}$ we define:
    $$
    \int_A f \\ d\mu := \int (f \cdot \mathbf{1}_A) \\ d\mu
    $$



!!! lemma
    For $i \geq 1$, let $f_i : \Omega \to [0, \infty]$ be measurable.
    If $f_i \uparrow f$ to some measurable function $f : \Omega \to [0, \infty]$
    then $\int{f_i} d\mu \uparrow \int{f d\mu}$

