@tag(semi)
!!! definition "Semi"
    Let $\mathcal{A} \subseteq \mathcal{P}(\Omega)$. The class $\mathcal{A}$ is called  a **semiring** if :

    * $\emptyset \in \mathcal{A}$,
    * for any $A, B \in \mathcal{A}$ then $B \setminus A$ is a finite union of mutually disjoint sets in $\mathcal{A}$,
    * $\mathcal{A}$ is $\cap$-closed i.e. closed under finite intersections.



!!! definition "Definition @tag(semi-new)"
    Let $\mathcal{A} \subseteq \mathcal{P}(\Omega)$. The class $\mathcal{A}$ is called  a semi-ring if :

    * $\emptyset \in \mathcal{A}$,
    * for any $A, B \in \mathcal{A}$ then $B \setminus A$ is a finite union of mutually disjoint sets in $\mathcal{A}$,
    * $\mathcal{A}$ is $\cap$-closed i.e. closed under finite intersections.


<h1 id="section-introduction">Introduction</h1>
<p>In this chapter we develop some of the theory of algebraic curves. A
reference covering algebraic curves over the complex numbers is the book
<span class="citation" data-cites="ACGH">[@ACGH]</span>.</p>
<p>What we already know. Besides general algebraic geometry, we have
already proved some specific results on algebraic curves. Here is a
list.</p>
<ol type="1">
<li><p>We have discussed affine opens of and ample invertible sheaves on
<span class="math inline">1</span> dimensional Noetherian schemes in
Varieties, Section <a href="#varieties-section-dimension-one"
data-reference-type="ref"
data-reference="varieties-section-dimension-one">[varieties-section-dimension-one]</a>.</p></li>
<li><p>We have seen a curve is either affine or projective in Varieties,
Section <a href="#varieties-section-curves" data-reference-type="ref"
data-reference="varieties-section-curves">[varieties-section-curves]</a>.</p></li>
<li><p>We have discussed degrees of locally free modules on proper
curves in Varieties, Section <a
href="#varieties-section-divisors-curves" data-reference-type="ref"
data-reference="varieties-section-divisors-curves">[varieties-section-divisors-curves]</a>.</p></li>
<li><p>We have discussed the Picard scheme of a nonsingular projective
curve over an algebraically closed field in Picard Schemes of Curves,
Section <a href="#pic-section-introduction" data-reference-type="ref"
data-reference="pic-section-introduction">[pic-section-introduction]</a>.</p></li>
</ol>