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

!!! lemma
    Let $f, g \in \mathbb{E}^+$ and $\alpha > 0$. We have:

    * $\int \alpha f = \alpha \int f$
    * $\int f + g = \int f + \int g$
    * if $f \leq g$ then $\int f \leq \int g$

!!! lemma
    For $i \geq 1$, let $f_i : \Omega \to [0, \infty]$ be measurable.
    If $f_i \uparrow f$ to some measurable function $f : \Omega \to [0, \infty]$
    then $\int{f_i} d\mu \uparrow \int{f d\mu}$

!!! Lemma "Cauchy-Schwarz Inequatlity"
    Let $X$, $Y$ in $\mathcal{L}^2(\mathbf{P})$, then :
    $$
    \left(\mathbf{Cov}[X,Y] \right)^2 \leq \mathbf{Var}[X] \mathbf{Var}[Y]
    $$

Let $X$, $Y$ in $\mathcal{L}^2(\mathbf{P})$, then :
$$
\left(\mathbf{Cov}[X,Y] \right)^2 \leq \mathbf{Var}[X] \mathbf{Var}[Y]
$$
