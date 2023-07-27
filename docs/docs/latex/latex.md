\title{Algebraic Curves}


\maketitle

\phantomsection
\label{section-phantom}

\tableofcontents

###  Introduction

\label{section-introduction}

\noindent
In this chapter we develop some of the theory of algebraic curves.
A reference covering algebraic curves over the complex numbers is
the book \cite{ACGH}.

\medskip\noindent
What we already know. Besides general algebraic geometry, we
have already proved some specific results on algebraic curves.
Here is a list.


1.  We have discussed affine opens of and ample invertible sheaves on
$1$ dimensional Noetherian schemes in
Varieties, Section \ref{varieties-section-dimension-one}.
1.  We have seen a curve is either affine or projective
in Varieties, Section \ref{varieties-section-curves}.
1.  We have discussed degrees of locally free modules on
proper curves in Varieties, Section \ref{varieties-section-divisors-curves}.
1.  We have discussed the Picard scheme of a nonsingular projective
curve over an algebraically closed field in
Picard Schemes of Curves, Section \ref{pic-section-introduction}.






###  Curves and function fields

\label{section-curves-function-fields}

\noindent
In this section we elaborate on the results of
Varieties, Section \ref{varieties-section-varieties-rational-maps}
in the case of curves.

\begin{lemma}
\label{lemma-extend-over-dvr}
Let $k$ be a field. Let $X$ be a curve and $Y$ a proper variety.
Let $U \subset X$ be a nonempty open and let $f : U \to Y$ be a morphism.
If $x \in X$ is a closed point such that $\mathcal{O}_{X, x}$
is a discrete valuation ring, then there exist an open
$U \subset U' \subset X$ containing $x$ and a morphism of
varieties $f' : U' \to Y$ extending $f$.
\end{lemma}

#### Proof

This is a special case of
Morphisms, Lemma \ref{morphisms-lemma-extend-across}.


\begin{lemma}
\label{lemma-extend-over-normal-curve}
Let $k$ be a field. Let $X$ be a normal curve and $Y$ a proper variety.
The set of rational maps from $X$ to $Y$ is the same as the set
of morphisms $X \to Y$.
\end{lemma}

#### Proof

A rational map from $X$ to $Y$ can be extended to a morphism $X \to Y$
by Lemma \ref{lemma-extend-over-dvr}
as every local ring is a discrete valuation ring
(for example by Varieties, Lemma \ref{varieties-lemma-regular-point-on-curve}).
Conversely, if two morphisms $f,g: X \to Y$ are equivalent as rational maps,
then  $f = g$ by Morphisms, Lemma \ref{morphisms-lemma-equality-of-morphisms}.


\begin{lemma}
\label{lemma-flat}
Let $k$ be a field. Let $f : X \to Y$ be a nonconstant morphism
of curves over $k$. If $Y$ is normal, then $f$ is flat.
\end{lemma}

#### Proof

Pick $x \in X$ mapping to $y \in Y$. Then $\mathcal{O}_{Y, y}$ is either a
field or a discrete valuation ring
(Varieties, Lemma \ref{varieties-lemma-regular-point-on-curve}).
Since $f$ is nonconstant it is dominant (as it must map the
generic point of $X$ to the generic point of $Y$). This implies that
$\mathcal{O}_{Y, y} \to \mathcal{O}_{X, x}$ is injective
(Morphisms, Lemma \ref{morphisms-lemma-dominant-between-integral}).
Hence $\mathcal{O}_{X, x}$ is torsion free as a $\mathcal{O}_{Y, y}$-module
and therefore $\mathcal{O}_{X, x}$ is flat as a $\mathcal{O}_{Y, y}$-module
by More on Algebra, Lemma
\ref{more-algebra-lemma-valuation-ring-torsion-free-flat}.


\begin{lemma}
\label{lemma-finite}
Let $k$ be a field. Let $f : X \to Y$ be a morphism of
schemes over $k$. Assume


1.  $Y$ is separated over $k$,
1.  $X$ is proper of dimension $\leq 1$ over $k$,
1.  $f(Z)$ has at least two points for every irreducible
component $Z \subset X$ of dimension $1$.

Then $f$ is finite.
\end{lemma}

#### Proof

The morphism $f$ is proper by
Morphisms, Lemma \ref{morphisms-lemma-image-proper-scheme-closed}.
Thus $f(X)$ is closed and images of closed points are closed.
Let $y \in Y$ be the image of a closed point in $X$.
Then $f^{-1}(\{y\})$ is a closed subset of $X$ not
containing any of the generic points of irreducible components
of dimension $1$ by condition (3). It follows that $f^{-1}(\{y\})$
is finite. Hence $f$ is finite over an open neighbourhood of $y$
by
More on Morphisms, Lemma
\ref{more-morphisms-lemma-proper-finite-fibre-finite-in-neighbourhood}
(if $Y$ is Noetherian, then you can use the easier
Cohomology of Schemes, Lemma
\ref{coherent-lemma-proper-finite-fibre-finite-in-neighbourhood}).
Since we've seen above that there are enough of these points
$y$, the proof is complete.


\begin{lemma}
\label{lemma-extend-to-completion}
Let $k$ be a field. Let $X \to Y$ be a morphism of varieties
with $Y$ proper and $X$ a curve.
There exists a factorization $X \to \overline{X} \to Y$
where $X \to \overline{X}$ is an open immersion
and $\overline{X}$ is a projective curve.
\end{lemma}

#### Proof

This is clear from Lemma \ref{lemma-extend-over-dvr}
and Varieties, Lemma \ref{varieties-lemma-reduced-dim-1-projective-completion}.


\noindent
Here is the main theorem of this section. We will say a morphism
$f : X \to Y$ of varieties is {\it constant} if the image $f(X)$
consists of a single point $y$ of $Y$. If this happens then
$y$ is a closed point of $Y$ (since the image of a closed point
of $X$ will be a closed point of $Y$).

\begin{theorem}
\label{theorem-curves-rational-maps}
Let $k$ be a field. The following categories are canonically equivalent


1.  The category of finitely generated field extensions $K/k$ of
transcendence degree $1$.
1.  The category of curves and dominant rational maps.
1.  The category of normal projective curves and nonconstant morphisms.
1.  The category of nonsingular projective curves and nonconstant morphisms.
1.  The category of regular projective curves and nonconstant morphisms.
1.  The category of normal proper curves and nonconstant morphisms.

\end{theorem}

#### Proof

The equivalence between categories (1) and (2) is the restriction of the
equivalence of
Varieties, Theorem \ref{varieties-theorem-varieties-rational-maps}.
Namely, a variety is a curve if and only if its function field has
transcendence degree $1$, see for example
Varieties, Lemma \ref{varieties-lemma-dimension-locally-algebraic}.

\medskip\noindent
The categories in (3), (4), (5), and (6) are the same. First of all, the
terms ``regular'' and ``nonsingular'' are synonyms, see
Properties, Definition \ref{properties-definition-regular}.
Being normal and regular are the same thing for Noetherian
$1$-dimensional schemes
(Properties, Lemmas \ref{properties-lemma-regular-normal} and
\ref{properties-lemma-normal-dimension-1-regular}). See
Varieties, Lemma \ref{varieties-lemma-regular-point-on-curve}
for the case of curves. Thus (3) is the same as (5). Finally, (6)
is the same as (3) by
Varieties, Lemma \ref{varieties-lemma-dim-1-proper-projective}.

\medskip\noindent
If $f : X \to Y$ is a nonconstant morphism of nonsingular projective curves,
then $f$ sends the generic point $\eta$ of $X$ to the generic point $\xi$ of
$Y$. Hence we obtain a morphism
$k(Y) = \mathcal{O}_{Y, \xi} \to \mathcal{O}_{X, \eta} = k(X)$
in the category (1). If two morphisms $f,g: X \to Y$ gives the same morphism
$k(Y) \to k(X)$, then by the equivalence between (1) and (2),
$f$ and $g$ are equivalent as rational maps, so $f=g$ by
Lemma \ref{lemma-extend-over-normal-curve}.
Conversely, suppose that we have a map
$k(Y) \to k(X)$ in the category (1). Then we obtain a morphism $U \to Y$
for some nonempty open $U \subset X$. By Lemma \ref{lemma-extend-over-dvr}
this extends to all of $X$ and we obtain a morphism in the category (5).
Thus we see that there is a fully faithful functor (5)$\to$(1).

\medskip\noindent
To finish the proof we have to show that every $K/k$ in (1)
is the function field of a normal projective curve.
We already know that $K = k(X)$ for some curve $X$.
After replacing $X$ by its normalization
(which is a variety birational to $X$)
we may assume $X$ is normal
(Varieties, Lemma \ref{varieties-lemma-normalization-locally-algebraic}).
Then we choose $X \to \overline{X}$ with
$\overline{X} \setminus X = \{x_1, \ldots, x_n\}$ as in
Varieties, Lemma \ref{varieties-lemma-reduced-dim-1-projective-completion}.
Since $X$ is normal and since each
of the local rings $\mathcal{O}_{\overline{X}, x_i}$ is normal
we conclude that $\overline{X}$ is a normal projective curve as desired.
(Remark: We can also first compactify using
Varieties, Lemma \ref{varieties-lemma-dim-1-projective-completion}
and then normalize using
Varieties, Lemma \ref{varieties-lemma-normalization-locally-algebraic}.
Doing it this way we avoid using the somewhat tricky
Morphisms, Lemma \ref{morphisms-lemma-relative-normalization-normal-codim-1}.)


\begin{definition}
\label{definition-normal-projective-model}
Let $k$ be a field. Let $X$ be a curve.
A {\it nonsingular projective model of $X$}
is a pair $(Y, \varphi)$ where $Y$ is a nonsingular projective
curve and $\varphi : k(X) \to k(Y)$ is an isomorphism
of function fields.
\end{definition}

\noindent
A nonsingular projective model is determined up to unique
isomorphism by Theorem \ref{theorem-curves-rational-maps}.
Thus we often say ``the nonsingular projective model''.
We usually drop $\varphi$ from the notation.
Warning: it needn't be the case that $Y$ is smooth over $k$
but Lemma \ref{lemma-nonsingular-model-smooth}
shows this can only happen in positive characteristic.

\begin{lemma}
\label{lemma-nonsingular-model-smooth}
Let $k$ be a field. Let $X$ be a curve and let $Y$ be the nonsingular
projective model of $X$. If $k$ is perfect, then $Y$ is a smooth
projective curve.
\end{lemma}

#### Proof

See Varieties, Lemma \ref{varieties-lemma-regular-point-on-curve}
for example.


\begin{lemma}
\label{lemma-smooth-models}
Let $k$ be a field. Let $X$ be a geometrically irreducible curve over $k$.
For a field extension $K/k$ denote $Y_K$ a nonsingular projective model
of $(X_K)_{red}$.


1.  If $X$ is proper, then $Y_K$ is the normalization of $X_K$.
1.  There exists $K/k$ finite purely inseparable such that $Y_K$ is smooth.
1.  Whenever $Y_K$ is smooth\footnote{Or even geometrically reduced.}
we have $H^0(Y_K, \mathcal{O}_{Y_K}) = K$.
1.  Given a commutative diagram
$$
\xymatrix{
\Omega & K' \ar[l] \\\\
K \ar[u] & k \ar[l] \ar[u]
}
$$
of fields such that $Y_K$ and $Y_{K'}$ are smooth, then
$Y_\Omega = (Y_K)_\Omega = (Y_{K'})_\Omega$.

\end{lemma}

#### Proof

Let $X'$ be a nonsingular projective model of $X$. Then $X'$ and
$X$ have isomorphic nonempty open subschemes. In particular
$X'$ is geometrically irreducible as $X$ is (some details omitted).
Thus we may assume that $X$ is projective.

\medskip\noindent
Assume $X$ is proper. Then $X_K$ is proper and hence the normalization
$(X_K)^\nu$ is proper as a scheme finite over a proper scheme
(Varieties, Lemma \ref{varieties-lemma-normalization-locally-algebraic}
and Morphisms, Lemmas \ref{morphisms-lemma-finite-proper} and
\ref{morphisms-lemma-composition-proper}).
On the other hand, $X_K$ is irreducible as $X$ is geometrically
irreducible. Hence $X_K^\nu$ is proper, normal, irreducible, and birational
to $(X_K)_{red}$. This proves (1) because a proper curve is projective
(Varieties, Lemma \ref{varieties-lemma-dim-1-proper-projective}).

\medskip\noindent
Proof of (2). As $X$ is proper and we have (1), we can apply
Varieties, Lemma \ref{varieties-lemma-finite-extension-geometrically-normal}
to find $K/k$ finite purely inseparable such that
$Y_K$ is geometrically normal. Then $Y_K$ is geometrically regular
as normal and regular are the same for curves
(Properties, Lemma \ref{properties-lemma-normal-dimension-1-regular}).
Then $Y$ is a smooth variety by
Varieties, Lemma \ref{varieties-lemma-geometrically-regular-smooth}.

\medskip\noindent
If $Y_K$ is geometrically reduced, then $Y_K$ is geometrically
integral (Varieties, Lemma \ref{varieties-lemma-geometrically-integral})
and we see that $H^0(Y_K, \mathcal{O}_{Y_K}) = K$ by
Varieties, Lemma \ref{varieties-lemma-regular-functions-proper-variety}.
This proves (3) because a smooth variety is geometrically reduced
(even geometrically regular, see
Varieties, Lemma \ref{varieties-lemma-geometrically-regular-smooth}).

\medskip\noindent
If $Y_K$ is smooth, then for every extension $\Omega/K$
the base change $(Y_K)_\Omega$ is smooth over $\Omega$
(Morphisms, Lemma \ref{morphisms-lemma-base-change-smooth}).
Hence it is clear that $Y_\Omega = (Y_K)_\Omega$. This proves (4).







###  Linear series

\label{section-linear-series}

\noindent
We deviate from the classical story
(see Remark \ref{remark-classical-linear-series})
by defining linear series in the following manner.

\begin{definition}
\label{definition-linear-series}
Let $k$ be a field. Let $X$ be a proper scheme of dimension $\leq 1$ over $k$.
Let $d \geq 0$ and $r \geq 0$.
A {\it linear series of degree $d$ and dimension $r$}
is a pair $(\mathcal{L}, V)$ where $\mathcal{L}$ is an
invertible $\mathcal{O}_X$-module of degree $d$
(Varieties, Definition \ref{varieties-definition-degree-invertible-sheaf})
and $V \subset H^0(X, \mathcal{L})$ is a $k$-subvector space
of dimension $r + 1$. We will abbreviate this by saying
$(\mathcal{L}, V)$ is a {\it $\mathfrak g^r_d$} on $X$.
\end{definition}

\noindent
We will mostly use this when $X$ is a nonsingular proper curve.
In fact, the definition above is just one way to generalize the
classical definition of a $\mathfrak g^r_d$. For example, if $X$
is a proper curve, then one can generalize linear series by allowing
$\mathcal{L}$ to be a torsion free coherent $\mathcal{O}_X$-module
of rank $1$. On a nonsingular curve every torsion free
coherent module is locally free, so this agrees with our
notion for nonsingular proper curves.

\medskip\noindent
The following lemma explains the geometric meaning of linear series
for proper nonsingular curves.

\begin{lemma}
\label{lemma-linear-series}
Let $k$ be a field. Let $X$ be a nonsingular proper curve over $k$.
Let $(\mathcal{L}, V)$ be a $\mathfrak g^r_d$ on $X$. Then
there exists a morphism
$$
\varphi : X \longrightarrow \mathbf{P}^r_k = \text{Proj}(k[T_0, \ldots, T_r])
$$
of varieties over $k$ and a map
$\alpha : \varphi^*\mathcal{O}_{\mathbf{P}^r_k}(1) \to \mathcal{L}$
such that $\varphi^*T_0, \ldots, \varphi^*T_r$
are sent to a basis of $V$ by $\alpha$.
\end{lemma}

#### Proof

Let $s_0, \ldots, s_r \in V$ be a $k$-basis. Since $X$ is nonsingular
the image $\mathcal{L}' \subset \mathcal{L}$ of the map
$s_0, \ldots, s_r : \mathcal{O}_X^{\oplus r + 1} \to \mathcal{L}$
is an invertible $\mathcal{O}_X$-module for example by
Divisors, Lemma \ref{divisors-lemma-torsion-free-over-regular-dim-1}.
Then we use
Constructions, Lemma \ref{constructions-lemma-projective-space}
to get a morphism
$$
\varphi = \varphi_{(\mathcal{L}', (s_0, \ldots, s_r))} :
X \longrightarrow \mathbf{P}^r_k
$$
as in the statement of the lemma.


\begin{lemma}
\label{lemma-linear-series-trivial-existence}
Let $k$ be a field. Let $X$ be a proper scheme of dimension $\leq 1$ over $k$.
If $X$ has a $\mathfrak g^r_d$, then $X$ has a $\mathfrak g^s_d$ for
all $0 \leq s \leq r$.
\end{lemma}

#### Proof

This is true because a vector space $V$ of dimension $r + 1$
over $k$ has a linear subspace of dimension $s + 1$ for all
$0 \leq s \leq r$.


\begin{lemma}
\label{lemma-g1d}
Let $k$ be a field. Let $X$ be a nonsingular proper curve over $k$.
Let $(\mathcal{L}, V)$ be a $\mathfrak g^1_d$ on $X$. Then the morphism
$\varphi : X \to \mathbf{P}^1_k$ of Lemma \ref{lemma-linear-series}
either


1.  is nonconstant and has degree $\leq d$, or
1.  factors through a closed point of $\mathbf{P}^1_k$ and in this
case $H^0(X, \mathcal{O}_X) \not = k$.

\end{lemma}

#### Proof

By Lemma \ref{lemma-linear-series} we see that
$\mathcal{L}' = \varphi^*\mathcal{O}_{\mathbf{P}^1_k}(1)$
has a nonzero map $\mathcal{L}' \to \mathcal{L}$.
Hence by Varieties, Lemma \ref{varieties-lemma-check-invertible-sheaf-trivial}
we see that $0 \leq \deg(\mathcal{L}') \leq d$.
If $\deg(\mathcal{L}') = 0$, then the same lemma tells us
$\mathcal{L}' \cong \mathcal{O}_X$ and since we have
two linearly independent sections we find we are in case (2).
If $\deg(\mathcal{L}') > 0$ then $\varphi$ is nonconstant (since the
pullback of an invertible module by a constant morphism is trivial).
Hence
$$
\deg(\mathcal{L}') =
\deg(X/\mathbf{P}^1_k) \deg(\mathcal{O}_{\mathbf{P}^1_k}(1))
$$
by Varieties, Lemma \ref{varieties-lemma-degree-pullback-map-proper-curves}.
This finishes the proof as the degree of
$\mathcal{O}_{\mathbf{P}^1_k}(1)$ is $1$.


\begin{lemma}
\label{lemma-grd-inequalities}
Let $k$ be a field. Let $X$ be a proper curve over $k$ with
$H^0(X, \mathcal{O}_X) = k$. If $X$ has a $\mathfrak g^r_d$, then
$r \leq d$. If equality holds, then $H^1(X, \mathcal{O}_X) = 0$, i.e.,
the genus of $X$ (Definition \ref{definition-genus}) is $0$.
\end{lemma}

#### Proof

Let $(\mathcal{L}, V)$ be a $\mathfrak g^r_d$. Since this will only
increase $r$, we may assume $V = H^0(X, \mathcal{L})$. Choose a
nonzero element $s \in V$.  Then the zero scheme of $s$ is an effective Cartier
divisor $D \subset X$, we have $\mathcal{L} = \mathcal{O}_X(D)$, and
we have a short exact sequence
$$
0 \to \mathcal{O}_X \to \mathcal{L} \to \mathcal{L}|_D \to 0
$$
see Divisors, Lemma \ref{divisors-lemma-characterize-OD} and
Remark \ref{divisors-remark-ses-regular-section}.
By Varieties, Lemma \ref{varieties-lemma-degree-effective-Cartier-divisor}
we have $\deg(D) = \deg(\mathcal{L}) = d$.
Since $D$ is an Artinian scheme we have
$\mathcal{L}|_D \cong \mathcal{O}_D$\footnote{In our case this
follows from Divisors, Lemma
\ref{divisors-lemma-finite-trivialize-invertible-upstairs}
as $D \to \Spec(k)$ is finite.}.
Thus
$$
\dim_k H^0(D, \mathcal{L}|_D) = \dim_k H^0(D, \mathcal{O}_D) = \deg(D) = d
$$
On the other hand, by assumption
$\dim_k H^0(X, \mathcal{O}_X) = 1$ and $\dim H^0(X, \mathcal{L}) = r + 1$.
We conclude that $r + 1 \leq 1 + d$, i.e., $r \leq d$ as in the lemma.

\medskip\noindent
Assume equality holds. Then
$H^0(X, \mathcal{L}) \to H^0(X, \mathcal{L}|_D)$ is surjective.
If we knew that $H^1(X, \mathcal{L})$ was zero, then we would
conclude that $H^1(X, \mathcal{O}_X)$ is zero by the long exact
cohomology sequence and the proof would
be complete. Our strategy will be to replace $\mathcal{L}$ by a
large power which has vanishing. As $\mathcal{L}|_D$ is the
trivial invertible module (see above), we can
find a section $t$ of $\mathcal{L}$ whose restriction
of $D$ generates $\mathcal{L}|_D$.
Consider the multiplication map
$$
\mu :
H^0(X, \mathcal{L}) \otimes_k H^0(X, \mathcal{L})
\longrightarrow
H^0(X, \mathcal{L}^{\otimes 2})
$$
and consider the short exact sequence
$$
0 \to \mathcal{L} \xrightarrow{s}
\mathcal{L}^{\otimes 2} \to \mathcal{L}^{\otimes 2}|_D \to 0
$$
Since $H^0(\mathcal{L}) \to H^0(\mathcal{L}|_D)$ is surjective and since
$t$ maps to a trivialization of $\mathcal{L}|_D$ we see that
$\mu(H^0(X, \mathcal{L}) \otimes t)$ gives a subspace of
$H^0(X, \mathcal{L}^{\otimes 2})$ surjecting onto the global sections of
$\mathcal{L}^{\otimes 2}|_D$. Thus we see that
$$
\dim H^0(X, \mathcal{L}^{\otimes 2}) = r + 1 + d = 2r + 1 =
\deg(\mathcal{L}^{\otimes 2}) + 1
$$
Ok, so $\mathcal{L}^{\otimes 2}$ has the same property as $\mathcal{L}$, i.e.,
that the dimension of the space of global sections is equal to the
degree plus one. Since $\mathcal{L}$ is ample
(Varieties, Lemma \ref{varieties-lemma-ample-curve})
there exists some $n_0$ such that $\mathcal{L}^{\otimes n}$
has vanishing $H^1$ for all $n \geq n_0$
(Cohomology of Schemes, Lemma \ref{coherent-lemma-coherent-proper-ample}).
Thus applying the argument above to $\mathcal{L}^{\otimes n}$
with $n = 2^m$ for some sufficiently large $m$ we conclude the
lemma is true.


\begin{remark}[Classical definition]
\label{remark-classical-linear-series}
Let $X$ be a smooth projective curve over an algebraically closed field $k$.
We say two effective Cartier divisors $D, D' \subset X$ are
{\it linearly equivalent} if and only if
$\mathcal{O}_X(D) \cong \mathcal{O}_X(D')$ as $\mathcal{O}_X$-modules.
Since $\Pic(X) = \text{Cl}(X)$
(Divisors, Lemma \ref{divisors-lemma-local-rings-UFD-c1-bijective})
we see that $D$ and $D'$ are linearly equivalent
if and only if the Weil divisors associated to
$D$ and $D'$ define the same element of $\text{Cl}(X)$.
Given an effective Cartier divisor $D \subset X$ of degree $d$ the
{\it complete linear system} or {\it complete linear series} $|D|$ of $D$
is the set of effective Cartier divisors $E \subset X$
which are linearly equivalent to $D$.
Another way to say it is that $|D|$ is the set of closed
points of the fibre of the morphism
$$
\gamma_d :
\underline{\Hilbfunctor}^d_{X/k}
\longrightarrow
\underline{\Picardfunctor}^d_{X/k}
$$
(Picard Schemes of Curves, Lemma \ref{pic-lemma-picard-pieces})
over the closed point corresponding to $\mathcal{O}_X(D)$.
This gives $|D|$ a natural scheme structure and it
turns out that $|D| \cong \mathbf{P}^m_k$ with
$m + 1 = h^0(\mathcal{O}_X(D))$. In fact, more canonically we have
$$
|D| = \mathbf{P}(H^0(X, \mathcal{O}_X(D))^\vee)
$$
where $(-)^\vee$ indicates $k$-linear dual and $\mathbf{P}$ is as
in Constructions, Example \ref{constructions-example-projective-space}.
In this language a {\it linear system} or a {\it linear series} on
$X$ is a closed subvariety $L \subset |D|$ which can be cut out by
linear equations. If $L$ has dimension $r$, then $L = \mathbf{P}(V^\vee)$
where $V \subset H^0(X, \mathcal{O}_X(D))$ is a linear subspace
of dimension $r + 1$. Thus the classical linear series
$L \subset |D|$ corresponds to the linear series $(\mathcal{O}_X(D), V)$
as defined above.
\end{remark}







###  Duality

\label{section-duality}

\noindent
In this section we work out the consequences of the very general
material on dualizing complexes and duality for proper $1$-dimensional
schemes over fields. If you are interested in the analogous discussion
for higher dimension proper schemes over fields, see
Duality for Schemes, Section \ref{duality-section-duality-proper-over-field}.

\begin{lemma}
\label{lemma-duality-dim-1}
Let $X$ be a proper scheme of dimension $\leq 1$ over a field $k$.
There exists a dualizing complex $\omega_X^\bullet$ with the
following properties


1.  $H^i(\omega_X^\bullet)$ is nonzero only for $i = -1, 0$,
1.  $\omega_X = H^{-1}(\omega_X^\bullet)$
is a coherent Cohen-Macaulay module whose support is the
irreducible components of dimension $1$,
1.  for $x \in X$ closed, the module $H^0(\omega_{X, x}^\bullet)$
is nonzero if and only if either
\begin{enumerate}
1.  $\dim(\mathcal{O}_{X, x}) = 0$ or
1.  $\dim(\mathcal{O}_{X, x}) = 1$
and $\mathcal{O}_{X, x}$ is not Cohen-Macaulay,

\item for $K \in D_\QCoh(\mathcal{O}_X)$ there are functorial
isomorphisms\footnote{This property
characterizes $\omega_X^\bullet$ in $D_\QCoh(\mathcal{O}_X)$
up to unique isomorphism by the Yoneda lemma. Since $\omega_X^\bullet$
is in $D^b_{\textit{Coh}}(\mathcal{O}_X)$ in fact it suffices to consider
$K \in D^b_{\textit{Coh}}(\mathcal{O}_X)$.}
$$
\Ext^i_X(K, \omega_X^\bullet) = \Hom_k(H^{-i}(X, K), k)
$$
compatible with shifts and distinguished triangles,
\item there are functorial isomorphisms
$\Hom(\mathcal{F}, \omega_X) = \Hom_k(H^1(X, \mathcal{F}), k)$
for $\mathcal{F}$ quasi-coherent on $X$,
\item if $X \to \Spec(k)$ is smooth of relative dimension $1$,
then $\omega_X \cong \Omega_{X/k}$.
\end{enumerate}
\end{lemma}

#### Proof

Denote $f : X \to \Spec(k)$ the structure morphism.
We start with the relative dualizing complex
$$
\omega_X^\bullet = \omega_{X/k}^\bullet = a(\mathcal{O}_{\Spec(k)})
$$
as described in Duality for Schemes,
Remark \ref{duality-remark-relative-dualizing-complex}.
Then property (4) holds by construction as $a$ is the right
adjoint for $f_* : D_\QCoh(\mathcal{O}_X) \to D(\mathcal{O}_{\Spec(k)})$.
Since $f$ is proper we have
$f^!(\mathcal{O}_{\Spec(k)}) = a(\mathcal{O}_{\Spec(k)})$ by
definition, see
Duality for Schemes, Section \ref{duality-section-upper-shriek}.
Hence $\omega_X^\bullet$ and $\omega_X$ are as in
Duality for Schemes, Example \ref{duality-example-proper-over-local}
and as in
Duality for Schemes, Example \ref{duality-example-equidimensional-over-field}.
Parts (1) and (2) follow from
Duality for Schemes, Lemma \ref{duality-lemma-vanishing-good-dualizing}.
For a closed point $x \in X$ we see that $\omega_{X, x}^\bullet$ is a
normalized dualizing complex over $\mathcal{O}_{X, x}$, see
Duality for Schemes, Lemma \ref{duality-lemma-good-dualizing-normalized}.
Assertion (3) then follows from
Dualizing Complexes, Lemma \ref{dualizing-lemma-apply-CM}.
Assertion (5) follows from
Duality for Schemes, Lemma \ref{duality-lemma-dualizing-module-proper-over-A}
for coherent $\mathcal{F}$ and in general by unwinding
(4) for $K = \mathcal{F}[0]$ and $i = -1$.
Assertion (6) follows from Duality for Schemes,
Lemma \ref{duality-lemma-smooth-proper}.


\begin{lemma}
\label{lemma-duality-dim-1-CM}
Let $X$ be a proper scheme over a field $k$ which is Cohen-Macaulay
and equidimensional of dimension $1$. The module $\omega_X$
of Lemma \ref{lemma-duality-dim-1} has the following properties


1.  $\omega_X$ is a dualizing module on $X$
(Duality for Schemes, Section \ref{duality-section-dualizing-module}),
1.  $\omega_X$ is a coherent Cohen-Macaulay module whose support is $X$,
1.  there are functorial isomorphisms
$\Ext^i_X(K, \omega_X[1]) = \Hom_k(H^{-i}(X, K), k)$
compatible with shifts for $K \in D_\QCoh(X)$,
1.  there are functorial isomorphisms
$\Ext^{1 + i}(\mathcal{F}, \omega_X) = \Hom_k(H^{-i}(X, \mathcal{F}), k)$
for $\mathcal{F}$ quasi-coherent on $X$.

\end{lemma}

#### Proof

Recall from the proof of Lemma \ref{lemma-duality-dim-1}
that $\omega_X$ is as in Duality for Schemes, Example
\ref{duality-example-proper-over-local} and hence is
a dualizing module. The other statements follow from
Lemma \ref{lemma-duality-dim-1}
and the fact that $\omega_X^\bullet = \omega_X[1]$
as $X$ is Cohen-Macualay (Duality for Schemes, Lemma
\ref{duality-lemma-dualizing-module-CM-scheme}).


\begin{remark}
\label{remark-rework-duality-locally-free}
Let $X$ be a proper scheme of dimension $\leq 1$ over a field $k$.
Let $\omega_X^\bullet$ and $\omega_X$ be as in Lemma \ref{lemma-duality-dim-1}.
If $\mathcal{E}$ is a finite locally free $\mathcal{O}_X$-module
with dual $\mathcal{E}^\vee$ then we have canonical isomorphisms
$$
\Hom_k(H^{-i}(X, \mathcal{E}), k) =
H^i(X, \mathcal{E}^\vee \otimes_{\mathcal{O}_X}^\mathbf{L} \omega_X^\bullet)
$$
This follows from the lemma and
Cohomology, Lemma \ref{cohomology-lemma-dual-perfect-complex}.
If $X$ is Cohen-Macaulay and equidimensional of dimension $1$, then
we have canonical isomorphisms
$$
\Hom_k(H^{-i}(X, \mathcal{E}), k) =
H^{1 + i}(X, \mathcal{E}^\vee \otimes_{\mathcal{O}_X} \omega_X)
$$
by Lemma \ref{lemma-duality-dim-1-CM}. In particular
if $\mathcal{L}$ is an invertible $\mathcal{O}_X$-module, then we have
$$
\dim_k H^0(X, \mathcal{L}) =
\dim_k H^1(X, \mathcal{L}^{\otimes -1} \otimes_{\mathcal{O}_X} \omega_X)
$$
and
$$
\dim_k H^1(X, \mathcal{L}) =
\dim_k H^0(X, \mathcal{L}^{\otimes -1} \otimes_{\mathcal{O}_X} \omega_X)
$$
\end{remark}

\noindent
Here is a sanity check for the dualizing complex.

\begin{lemma}
\label{lemma-sanity-check-duality}
Let $X$ be a proper scheme of dimension $\leq 1$ over a field $k$.
Let $\omega_X^\bullet$ and $\omega_X$ be as in Lemma \ref{lemma-duality-dim-1}.


1.  If $X \to \Spec(k)$ factors as $X \to \Spec(k') \to \Spec(k)$
for some field $k'$, then $\omega_X^\bullet$ and $\omega_X$
satisfy properties (4), (5), (6) with $k$ replaced with $k'$.
1.  If $K/k$ is a field extension, then the pullback of
$\omega_X^\bullet$ and $\omega_X$ to the base change $X_K$
are as in  Lemma \ref{lemma-duality-dim-1} for the morphism
$X_K \to \Spec(K)$.

\end{lemma}

#### Proof

Denote $f : X \to \Spec(k)$ the structure morphism.
Assertion (1) really means that $\omega_X^\bullet$ and $\omega_X$
are as in Lemma \ref{lemma-duality-dim-1} for the morphism
$f' : X \to \Spec(k')$. In the proof of Lemma \ref{lemma-duality-dim-1}
we took $\omega_X^\bullet = a(\mathcal{O}_{\Spec(k)})$
where $a$ be is the right adjoint of
Duality for Schemes, Lemma
\ref{duality-lemma-twisted-inverse-image} for $f$.
Thus we have to show
$a(\mathcal{O}_{\Spec(k)}) \cong a'(\mathcal{O}_{\Spec(k)})$
where $a'$ be is the right adjoint of
Duality for Schemes, Lemma
\ref{duality-lemma-twisted-inverse-image} for $f'$.
Since $k' \subset H^0(X, \mathcal{O}_X)$ we see that $k'/k$ is a finite
extension (Cohomology of Schemes, Lemma
\ref{coherent-lemma-proper-over-affine-cohomology-finite}).
By uniqueness of adjoints we have $a = a' \circ b$ where
$b$ is the right adjoint of Duality for Schemes, Lemma
\ref{duality-lemma-twisted-inverse-image} for $g : \Spec(k') \to \Spec(k)$.
Another way to say this: we have $f^! = (f')^! \circ g^!$.
Thus it suffices to show that $\Hom_k(k', k) \cong k'$ as
$k'$-modules, see Duality for Schemes, Example
\ref{duality-example-affine-twisted-inverse-image}.
This holds because these are $k'$-vector spaces of
the same dimension (namely dimension $1$).

\medskip\noindent
Proof of (2). This holds because we have base change for $a$ by
Duality for Schemes, Lemma \ref{duality-lemma-more-base-change}.
See discussion in Duality for Schemes, Remark
\ref{duality-remark-relative-dualizing-complex}.


\begin{lemma}
\label{lemma-closed-immersion-dim-1-CM}
Let $X$ be a proper scheme of dimension $\leq 1$ over a field $k$.
Let $i : Y \to X$ be a closed immersion.
Let $\omega_X^\bullet$, $\omega_X$, $\omega_Y^\bullet$, $\omega_Y$
be as in Lemma \ref{lemma-duality-dim-1}. Then


1.  $\omega_Y^\bullet = R\SheafHom(\mathcal{O}_Y, \omega_X^\bullet)$,
1.  $\omega_Y = \SheafHom(\mathcal{O}_Y, \omega_X)$ and
$i_*\omega_Y = \SheafHom_{\mathcal{O}_X}(i_*\mathcal{O}_Y, \omega_X)$.

\end{lemma}

#### Proof

Denote $g : Y \to \Spec(k)$ and $f : X \to \Spec(k)$ the structure morphisms.
Then $g = f \circ i$. Denote $a, b, c$ the right adjoint of
Duality for Schemes, Lemma
\ref{duality-lemma-twisted-inverse-image} for $f, g, i$.
Then $b = c \circ a$ by uniqueness of right adjoints
and because $Rg_* = Rf_* \circ Ri_*$.
In the proof of Lemma \ref{lemma-duality-dim-1}
we set
$\omega_X^\bullet = a(\mathcal{O}_{\Spec(k)})$ and
$\omega_Y^\bullet = b(\mathcal{O}_{\Spec(k)})$.
Hence $\omega_Y^\bullet = c(\omega_X^\bullet)$
which implies (1) by Duality for Schemes, Lemma
\ref{duality-lemma-twisted-inverse-image-closed}.
Since $\omega_X = H^{-1}(\omega_X^\bullet)$ and
$\omega_Y = H^{-1}(\omega_Y^\bullet)$ we conclude that
$\omega_Y = \SheafHom(\mathcal{O}_Y, \omega_X)$.
This implies
$i_*\omega_Y = \SheafHom_{\mathcal{O}_X}(i_*\mathcal{O}_Y, \omega_X)$
by Duality for Schemes, Lemma
\ref{duality-lemma-sheaf-with-exact-support-ext}.


\begin{lemma}
\label{lemma-closed-subscheme-reduced-gorenstein}
Let $X$ be a proper scheme over a field $k$ which is
Gorenstein, reduced, and equidimensional of dimension $1$.
Let $i : Y \to X$ be a reduced closed subscheme equidimensional
of dimension $1$. Let $j : Z \to X$ be the scheme theoretic
closure of $X \setminus Y$. Then


1.  $Y$ and $Z$ are Cohen-Macaulay,
1.  if $\mathcal{I} \subset \mathcal{O}_X$,
resp.\ $\mathcal{J} \subset \mathcal{O}_X$ is the ideal sheaf of
$Y$, resp.\ $Z$ in $X$, then
$$
\mathcal{I} = i_*\mathcal{I}'
\quad\text{and}\quad
\mathcal{J} = j_*\mathcal{J}'
$$
where $\mathcal{I}' \subset \mathcal{O}_Z$,
resp.\ $\mathcal{J}' \subset \mathcal{O}_Y$ is the ideal sheaf
of $Y \cap Z$ in $Z$, resp.\ $Y$,
1.  $\omega_Y = \mathcal{J}'(i^*\omega_X)$ and
$i_*(\omega_Y) = \mathcal{J}\omega_X$,
1.  $\omega_Z = \mathcal{I}'(i^*\omega_X)$ and
$i_*(\omega_Z) = \mathcal{I}\omega_X$,
1.  we have the following short exact sequences
\begin{align}
0 \to \omega_X \to i_*i^*\omega_X \oplus j_*j^*\omega_X \to
\mathcal{O}_{Y \cap Z} \to 0 \\\\
0 \to i_*\omega_Y \to \omega_X \to j_*j^*\omega_X \to 0 \\\\
0 \to j_*\omega_Z \to \omega_X \to i_*i^*\omega_X \to 0 \\\\
0 \to i_*\omega_Y \oplus j_*\omega_Z \to \omega_X \to
\mathcal{O}_{Y \cap Z} \to 0 \\\\
0 \to \omega_Y \to i^*\omega_X \to \mathcal{O}_{Y \cap Z} \to 0 \\\\
0 \to \omega_Z \to j^*\omega_X \to \mathcal{O}_{Y \cap Z} \to 0
\end{align}

Here $\omega_X$, $\omega_Y$, $\omega_Z$ are as in
Lemma \ref{lemma-duality-dim-1}.
\end{lemma}

#### Proof

A reduced $1$-dimensional Noetherian scheme is Cohen-Macaulay, so
(1) is true. Since $X$ is reduced, we see that $X = Y \cup Z$
scheme theoretically. With notation as in
Morphisms, Lemma \ref{morphisms-lemma-scheme-theoretic-union}
and by the statement of that lemma
we have a short exact sequence
$$
0 \to \mathcal{O}_X \to
\mathcal{O}_Y \oplus \mathcal{O}_Z \to \mathcal{O}_{Y \cap Z} \to 0
$$
Since $\mathcal{J} = \Ker(\mathcal{O}_X \to \mathcal{O}_Z)$,
$\mathcal{J}' = \Ker(\mathcal{O}_Y \to \mathcal{O}_{Y \cap Z})$,
$\mathcal{I} = \Ker(\mathcal{O}_X \to \mathcal{O}_Y)$, and
$\mathcal{I}' = \Ker(\mathcal{O}_Z \to \mathcal{O}_{Y \cap Z})$
a diagram chase implies (2).
Observe that $\mathcal{I} + \mathcal{J}$ is the ideal sheaf
of $Y \cap Z$ and that $\mathcal{I} \cap \mathcal{J} = 0$.
Hence we have the following exact sequences
\begin{align}
0 \to \mathcal{O}_X \to \mathcal{O}_Y \oplus \mathcal{O}_Z \to
\mathcal{O}_{Y \cap Z} \to 0 \\\\
0 \to \mathcal{J} \to \mathcal{O}_X \to \mathcal{O}_Z \to 0 \\\\
0 \to \mathcal{I} \to \mathcal{O}_X \to \mathcal{O}_Y \to 0 \\\\
0 \to \mathcal{J} \oplus \mathcal{I} \to \mathcal{O}_X \to
\mathcal{O}_{Y \cap Z} \to 0 \\\\
0 \to \mathcal{J}' \to \mathcal{O}_Y \to \mathcal{O}_{Y \cap Z} \to 0 \\\\
0 \to \mathcal{I}' \to \mathcal{O}_Z \to \mathcal{O}_{Y \cap Z} \to 0
\end{align}
Since $X$ is Gorenstein $\omega_X$ is an invertible $\mathcal{O}_X$-module
(Duality for Schemes, Lemma \ref{duality-lemma-gorenstein}).
Since $Y \cap Z$ has dimension $0$ we have
$\omega_X|_{Y \cap Z} \cong \mathcal{O}_{Y \cap Z}$.
Thus if we prove (3) and (4), then we obtain the short exact
sequences of the lemma by tensoring the above
short exact sequence with the invertible module $\omega_X$.
By symmetry it suffices to prove (3) and by
(2) it suffices to prove $i_*(\omega_Y) = \mathcal{J}\omega_X$.

\medskip\noindent
We have
$i_*\omega_Y = \SheafHom_{\mathcal{O}_X}(i_*\mathcal{O}_Y, \omega_X)$
by Lemma \ref{lemma-closed-immersion-dim-1-CM}.
Again using that $\omega_X$ is invertible
we finally conclude that it suffices to show
$\SheafHom_{\mathcal{O}_X}(\mathcal{O}_X/\mathcal{I}, \mathcal{O}_X)$
maps isomorphically to $\mathcal{J}$ by evaluation at $1$.
In other words, that $\mathcal{J}$ is the annihilator of
$\mathcal{I}$. This follows from the above.








###  Riemann-Roch

\label{section-Riemann-Roch}

\noindent
Let $k$ be a field. Let $X$ be a proper scheme of dimension $\leq 1$
over $k$. In Varieties, Section \ref{varieties-section-divisors-curves}
we have defined the degree of a locally free $\mathcal{O}_X$-module
$\mathcal{E}$ of constant rank by the formula
\begin{equation}
\label{equation-degree}
\deg(\mathcal{E}) =
\chi(X, \mathcal{E}) - \text{rank}(\mathcal{E})\chi(X, \mathcal{O}_X)
\end{equation}
see Varieties, Definition \ref{varieties-definition-degree-invertible-sheaf}.
In the chapter on Chow Homology we defined the first Chern class of
$\mathcal{E}$ as an operation on cycles
(Chow Homology, Section
\ref{chow-section-intersecting-chern-classes}) and we proved that
\begin{equation}
\label{equation-degree-c1}
\deg(\mathcal{E}) = \deg(c_1(\mathcal{E}) \cap [X]_1)
\end{equation}
see Chow Homology, Lemma \ref{chow-lemma-degree-vector-bundle}.
Combining (\ref{equation-degree}) and (\ref{equation-degree-c1})
we obtain our first version of the Riemann-Roch formula
\begin{equation}
\label{equation-rr}
\chi(X, \mathcal{E}) =
\deg(c_1(\mathcal{E}) \cap [X]_1) +
\text{rank}(\mathcal{E})\chi(X, \mathcal{O}_X)
\end{equation}
If $\mathcal{L}$ is an invertible $\mathcal{O}_X$-module, then
we can also consider the numerical intersection
$(\mathcal{L} \cdot X)$ as defined in
Varieties, Definition \ref{varieties-definition-intersection-number}.
However, this does not give anything new as
\begin{equation}
\label{equation-numerical-degree}
(\mathcal{L} \cdot X) = \deg(\mathcal{L})
\end{equation}
by Varieties, Lemma
\ref{varieties-lemma-intersection-numbers-and-degrees-on-curves}. If
$\mathcal{L}$ is ample, then this integer is positive and is
called the degree
\begin{equation}
\label{equation-degree-X}
\deg_\mathcal{L}(X) = (\mathcal{L} \cdot X) = \deg(\mathcal{L})
\end{equation}
of $X$ with respect to $\mathcal{L}$, see
Varieties, Definition \ref{varieties-definition-degree}.

\medskip\noindent
To obtain a true Riemann-Roch theorem we would like to write
$\chi(X, \mathcal{O}_X)$ as the degree of a canonical zero cycle on $X$.
We refer to \cite{F} for a fully general version of this. We will use
duality to get a formula in the case where $X$ is Gorenstein; however,
in some sense this is a cheat (for example because this method cannot
work in higher dimension).

\medskip\noindent
We first use Lemmas \ref{lemma-duality-dim-1} and \ref{lemma-duality-dim-1-CM}
to get a relation between the euler
characteristic of $\mathcal{O}_X$ and the euler characteristic
of the dualizing complex or the dualizing module.

\begin{lemma}
\label{lemma-euler}
Let $X$ be a proper scheme of dimension $\leq 1$ over a field $k$.
With $\omega_X^\bullet$ and $\omega_X$ as in Lemma \ref{lemma-duality-dim-1}
we have
$$
\chi(X, \mathcal{O}_X) = \chi(X, \omega_X^\bullet)
$$
If $X$ is Cohen-Macaulay and equidimensional of dimension $1$, then
$$
\chi(X, \mathcal{O}_X) = - \chi(X, \omega_X)
$$
\end{lemma}

#### Proof

We define the right hand side of the first formula as follows:
$$
\chi(X, \omega_X^\bullet) =
\sum\nolimits_{i \in \mathbf{Z}} (-1)^i\dim_k H^i(X, \omega_X^\bullet)
$$
This is well defined because $\omega_X^\bullet$ is in
$D^b_{\textit{Coh}}(\mathcal{O}_X)$, but also because
$$
H^i(X, \omega_X^\bullet) =
\Ext^i(\mathcal{O}_X, \omega_X^\bullet) =
H^{-i}(X, \mathcal{O}_X)
$$
which is always finite dimensional and nonzero only if $i = 0, -1$.
This of course also proves the first formula. The second is a consequence
of the first because $\omega_X^\bullet = \omega_X[1]$ in the CM case, see
Lemma \ref{lemma-duality-dim-1-CM}.


\noindent
We will use Lemma \ref{lemma-euler} to get the desired formula for
$\chi(X, \mathcal{O}_X)$ in the case that $\omega_X$ is
invertible, i.e., that $X$ is Gorenstein.
The statement is that $-1/2$ of the first Chern class of $\omega_X$
capped with the cycle $[X]_1$ associated to $X$ is a natural zero
cycle on $X$ with half-integer coefficients whose degree is
$\chi(X, \mathcal{O}_X)$.
The occurence of fractions in the statement of Riemann-Roch cannot
be avoided.

\begin{lemma}[Riemann-Roch]
\label{lemma-rr}
Let $X$ be a proper scheme over a field $k$ which is Gorenstein and
equidimensional of dimension $1$. Let $\omega_X$ be as in
Lemma \ref{lemma-duality-dim-1}. Then


1.  $\omega_X$ is an invertible $\mathcal{O}_X$-module,
1.  $\deg(\omega_X) = -2\chi(X, \mathcal{O}_X)$,
1.  for a locally free $\mathcal{O}_X$-module $\mathcal{E}$
of constant rank we have
$$
\chi(X, \mathcal{E}) = \deg(\mathcal{E}) -
\textstyle{\frac{1}{2}} \text{rank}(\mathcal{E}) \deg(\omega_X)
$$
and $\dim_k(H^i(X, \mathcal{E})) =
\dim_k(H^{1 - i}(X, \mathcal{E}^\vee \otimes_{\mathcal{O}_X} \omega_X))$
for all $i \in \mathbf{Z}$.

\end{lemma}

\noindent
Nonsingular (normal) curves are Gorenstein, see
Duality for Schemes, Lemma \ref{duality-lemma-regular-gorenstein}.

#### Proof

Recall that Gorenstein schemes are Cohen-Macaulay
(Duality for Schemes, Lemma \ref{duality-lemma-gorenstein-CM})
and hence $\omega_X$ is a dualizing module on $X$, see
Lemma \ref{lemma-duality-dim-1-CM}.
It follows more or less from the definition of the Gorenstein property
that the dualizing sheaf is invertible, see
Duality for Schemes, Section \ref{duality-section-gorenstein}.
By (\ref{equation-rr}) applied to $\omega_X$ we have
$$
\chi(X, \omega_X) =
\deg(c_1(\omega_X) \cap [X]_1) + \chi(X, \mathcal{O}_X)
$$
Combined with Lemma \ref{lemma-euler} this gives
$$
2\chi(X, \mathcal{O}_X) = - \deg(c_1(\omega_X) \cap [X]_1) = - \deg(\omega_X)
$$
the second equality by (\ref{equation-degree-c1}). Putting this back into
(\ref{equation-rr}) for $\mathcal{E}$ gives the displayed formula of the lemma.
The symmetry in dimensions is a consequence of duality for $X$, see
Remark \ref{remark-rework-duality-locally-free}.






###  Some vanishing results

\label{section-vanishing}

\noindent
This section contains some very weak vanishing results.
Please see Section \ref{section-more-vanishing} for
a few more and more interesting results.

\begin{lemma}
\label{lemma-automatic}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Then $X$ is connected, Cohen-Macaulay,
and equidimensional of dimension $1$.
\end{lemma}

#### Proof

Since $\Gamma(X, \mathcal{O}_X) = k$ has no nontrivial idempotents,
we see that $X$ is connected. This already shows that $X$ is
equidimensional of dimension $1$ (any irreducible component
of dimension $0$ would be a connected component).
Let $\mathcal{I} \subset \mathcal{O}_X$
be the maximal coherent submodule supported in closed points.
Then $\mathcal{I}$ exists
(Divisors, Lemma \ref{divisors-lemma-remove-embedded-points})
and is globally generated
(Varieties, Lemma \ref{varieties-lemma-chi-tensor-finite}).
Since $1 \in \Gamma(X, \mathcal{O}_X)$ is not a section
of $\mathcal{I}$ we conclude that $\mathcal{I} = 0$.
Thus $X$ does not have embedded points
(Divisors, Lemma \ref{divisors-lemma-remove-embedded-points}).
Thus $X$ has $(S_1)$ by
Divisors, Lemma \ref{divisors-lemma-S1-no-embedded}.
Hence $X$ is Cohen-Macaulay.


\noindent
In this section we work in the following situation.

\begin{situation}
\label{situation-Cohen-Macaulay-curve}
Here $k$ is a field, $X$ is a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$.
\end{situation}

\noindent
By Lemma \ref{lemma-automatic} the scheme $X$ is Cohen-Macaulay and
equidimensional of dimension $1$. The dualizing module $\omega_X$
discussed in Lemmas \ref{lemma-duality-dim-1} and
\ref{lemma-duality-dim-1-CM} has nonvanishing $H^1$ because in fact
$\dim_k H^1(X, \omega_X) = \dim_k H^0(X, \mathcal{O}_X) = 1$. It turns out
that anything slightly more ``positive'' than $\omega_X$ has vanishing $H^1$.

\begin{lemma}
\label{lemma-vanishing}
In Situation \ref{situation-Cohen-Macaulay-curve}. Given an exact sequence
$$
\omega_X \to \mathcal{F} \to \mathcal{Q} \to 0
$$
of coherent $\mathcal{O}_X$-modules with $H^1(X, \mathcal{Q}) = 0$
(for example if $\dim(\text{Supp}(\mathcal{Q})) = 0$), then
either $H^1(X, \mathcal{F}) = 0$ or
$\mathcal{F} = \omega_X \oplus \mathcal{Q}$.
\end{lemma}

#### Proof

(The parenthetical statement follows from
Cohomology of Schemes, Lemma \ref{coherent-lemma-coherent-support-dimension-0}.)
Since $H^0(X, \mathcal{O}_X) = k$ is dual to $H^1(X, \omega_X)$
(see Section \ref{section-Riemann-Roch})
we see that $\dim H^1(X, \omega_X) = 1$. The sheaf $\omega_X$
represents the functor
$\mathcal{F} \mapsto \Hom_k(H^1(X, \mathcal{F}), k)$
on the category of coherent $\mathcal{O}_X$-modules
(Duality for Schemes, Lemma
\ref{duality-lemma-dualizing-module-proper-over-A}).
Consider an exact sequence as in the statement of the lemma
and assume that $H^1(X, \mathcal{F}) \not = 0$. Since
$H^1(X, \mathcal{Q}) = 0$ we see that
$H^1(X, \omega_X) \to H^1(X, \mathcal{F})$ is an isomorphism.
By the universal property of $\omega_X$ stated above, we conclude there
is a map $\mathcal{F} \to \omega_X$ whose action on $H^1$ is the inverse
of this isomorphism. The composition $\omega_X \to \mathcal{F} \to \omega_X$
is the identity (by the universal property) and the lemma is proved.


\begin{lemma}
\label{lemma-vanishing-twist}
In Situation \ref{situation-Cohen-Macaulay-curve}. Let
$\mathcal{L}$ be an invertible $\mathcal{O}_X$-module which is
globally generated and not isomorphic to $\mathcal{O}_X$. Then
$H^1(X, \omega_X \otimes \mathcal{L}) = 0$.
\end{lemma}

#### Proof

By duality as discussed in Section \ref{section-Riemann-Roch} we have to
show that $H^0(X, \mathcal{L}^{\otimes - 1}) = 0$. If not, then we can
choose a global section $t$ of $\mathcal{L}^{\otimes - 1}$
and a global section $s$ of $\mathcal{L}$ such that $st \not = 0$.
However, then $st$ is a constant multiple of $1$, by our assumption
that $H^0(X, \mathcal{O}_X) = k$. It follows that
$\mathcal{L} \cong \mathcal{O}_X$, which is a contradiction.


\begin{lemma}
\label{lemma-globally-generated}
In Situation \ref{situation-Cohen-Macaulay-curve}. Given an exact sequence
$$
\omega_X \to \mathcal{F} \to \mathcal{Q} \to 0
$$
of coherent $\mathcal{O}_X$-modules with $\dim(\text{Supp}(\mathcal{Q})) = 0$
and $\dim_k H^0(X, \mathcal{Q}) \geq 2$ and such that there is no nonzero
submodule $\mathcal{Q}' \subset \mathcal{F}$ such that
$\mathcal{Q}' \to \mathcal{Q}$ is injective.
Then the submodule of $\mathcal{F}$ generated by global
sections surjects onto $\mathcal{Q}$.
\end{lemma}

#### Proof

Let $\mathcal{F}' \subset \mathcal{F}$ be the submodule generated by
global sections and the image of $\omega_X \to \mathcal{F}$. Since
$\dim_k H^0(X, \mathcal{Q}) \geq 2$ and
$\dim_k H^1(X, \omega_X) = \dim_k H^0(X, \mathcal{O}_X) = 1$,
we see that $\mathcal{F}' \to \mathcal{Q}$ is not zero and
$\omega_X \to \mathcal{F}'$ is not an isomorphism.
Hence $H^1(X, \mathcal{F}') = 0$ by Lemma \ref{lemma-vanishing}
and our assumption on $\mathcal{F}$.
Consider the short exact sequence
$$
0 \to \mathcal{F}' \to \mathcal{F} \to
\mathcal{Q}/\Im(\mathcal{F}' \to \mathcal{Q}) \to 0
$$
If the quotient on the right is nonzero, then we obtain a contradiction
because then $H^0(X, \mathcal{F})$ is bigger than $H^0(X, \mathcal{F}')$.


\noindent
Here is an example global generation statement.

\begin{lemma}
\label{lemma-globally-generated-curve}
In Situation \ref{situation-Cohen-Macaulay-curve} assume that
$X$ is integral. Let $0 \to \omega_X \to \mathcal{F} \to \mathcal{Q} \to 0$
be a short exact sequence of coherent $\mathcal{O}_X$-modules with
$\mathcal{F}$ torsion free, $\dim(\text{Supp}(\mathcal{Q})) = 0$,
and $\dim_k H^0(X, \mathcal{Q}) \geq 2$. Then $\mathcal{F}$
is globally generated.
\end{lemma}

#### Proof

Consider the submodule $\mathcal{F}'$ generated by the global sections. By
Lemma \ref{lemma-globally-generated} we see that $\mathcal{F}' \to \mathcal{Q}$
is surjective, in particular $\mathcal{F}' \not = 0$. Since $X$ is a curve, we
see that $\mathcal{F}' \subset \mathcal{F}$ is an inclusion of rank $1$
sheaves, hence $\mathcal{Q}' = \mathcal{F}/\mathcal{F}'$ is supported in
finitely many points. To get a contradiction, assume that
$\mathcal{Q}'$ is nonzero. Then we see that $H^1(X, \mathcal{F}') \not = 0$.
Then we get a nonzero map $\mathcal{F}' \to \omega_X$ by the universal
property (Duality for Schemes, Lemma
\ref{duality-lemma-dualizing-module-proper-over-A}).
The image of the composition $\mathcal{F}' \to \omega_X \to \mathcal{F}$
is generated by global sections, hence is inside of $\mathcal{F}'$.
Thus we get a nonzero self map $\mathcal{F}' \to \mathcal{F}'$.
Since $\mathcal{F}'$ is torsion free of rank $1$ on a proper curve
this has to be an automorphism (details omitted). But then this implies that
$\mathcal{F}'$ is contained in $\omega_X \subset \mathcal{F}$
contradicting the surjectivity of $\mathcal{F}' \to \mathcal{Q}$.


\begin{lemma}
\label{lemma-tensor-omega-with-globally-generated-invertible}
In Situation \ref{situation-Cohen-Macaulay-curve}. Let $\mathcal{L}$
be a very ample invertible $\mathcal{O}_X$-module with
$\deg(\mathcal{L}) \geq 2$. Then
$\omega_X \otimes_{\mathcal{O}_X} \mathcal{L}$ is globally generated.
\end{lemma}

#### Proof

Assume $k$ is algebraically closed. Let $x \in X$ be a closed point.
Let $C_i \subset X$ be the irreducible components and for each $i$
let $x_i \in C_i$ be the generic point. By
Varieties, Lemma \ref{varieties-lemma-very-ample-vanish-at-point}
we can choose a section $s \in H^0(X, \mathcal{L})$ such that $s$
vanishes at $x$ but not at $x_i$ for all $i$. The corresponding
module map $s : \mathcal{O}_X \to \mathcal{L}$ is injective with
cokernel $\mathcal{Q}$ supported in finitely many points and
with $H^0(X, \mathcal{Q}) \geq 2$. Consider the corresponding
exact sequence
$$
0 \to \omega_X \to \omega_X \otimes \mathcal{L} \to
\omega_X \otimes \mathcal{Q} \to 0
$$
By Lemma \ref{lemma-globally-generated} we see that the module generated
by global sections surjects onto $\omega_X \otimes \mathcal{Q}$.
Since $x$ was arbitrary this proves the lemma. Some details omitted.

\medskip\noindent
We will reduce the case where $k$ is not algebraically closed, to
the algebraically closed field case. We suggest the reader skip
the rest of the proof. Choose an algebraic closure $\overline{k}$
of $k$ and consider the base change $X_{\overline{k}}$. Let us
check that $X_{\overline{k}} \to \Spec(\overline{k})$ is an example
of Situation \ref{situation-Cohen-Macaulay-curve}. By flat base change
(Cohomology of Schemes, Lemma \ref{coherent-lemma-flat-base-change-cohomology})
we see that $H^0(X_{\overline{k}}, \mathcal{O}) = \overline{k}$.
The scheme $X_{\overline{k}}$ is proper over $\overline{k}$ (Morphisms,
Lemma \ref{morphisms-lemma-base-change-proper}) and
equidimensional of dimension $1$
(Morphisms, Lemma \ref{morphisms-lemma-dimension-fibre-after-base-change}).
The pullback of $\omega_X$ to $X_{\overline{k}}$ is the dualizing
module of $X_{\overline{k}}$ by Lemma \ref{lemma-sanity-check-duality}.
The pullback of $\mathcal{L}$ to $X_{\overline{k}}$ is very ample
(Morphisms, Lemma \ref{morphisms-lemma-very-ample-base-change}).
The degree of the pullback of $\mathcal{L}$ to $X_{\overline{k}}$
is equal to the degree of $\mathcal{L}$ on $X$ (Varieties, Lemma
\ref{varieties-lemma-degree-base-change}). Finally, we see that
$\omega_X \otimes \mathcal{L}$ is globally generated if and only
if its base change is so
(Varieties, Lemma \ref{varieties-lemma-globally-generated-base-change}).
In this way we see that the result follows from the result in the
case of an algebraically closed ground field.





###  Very ample invertible sheaves

\label{section-very-ample}

\noindent
An often used criterion for very ampleness of an invertible module
$\mathcal{L}$ on a scheme $X$ of finite type over an algebraically
closed field is: sections of $\mathcal{L}$ separate points and
tangent vectors (Varieties, Section
\ref{varieties-section-separating-points-tangent-vectors}). Here is another
criterion for curves; please compare with
Varieties, Subsection \ref{varieties-subsection-regularity}.

\begin{lemma}
\label{lemma-criterion-very-ample}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Let $\mathcal{L}$ be an invertible
$\mathcal{O}_X$-module. Assume


1.  $\mathcal{L}$ has a regular global section,
1.  $H^1(X, \mathcal{L}) = 0$, and
1.  $\mathcal{L}$ is ample.

Then $\mathcal{L}^{\otimes 6}$ is very ample on $X$ over $k$.
\end{lemma}

#### Proof

Let $s$ be a regular global section of $\mathcal{L}$. Let
$i : Z = Z(s) \to X$ be the zero scheme of $s$, see
Divisors, Section \ref{divisors-section-effective-Cartier-invertible}.
By condition (3) we see that $Z \not = \emptyset$ (small detail omitted).
Consider the short exact sequence
$$
0 \to \mathcal{O}_X \xrightarrow{s} \mathcal{L} \to
i_*(\mathcal{L}|_Z) \to 0
$$
Tensoring with $\mathcal{L}$ we obtain
$$
0 \to \mathcal{L} \to \mathcal{L}^{\otimes 2} \to
i_*(\mathcal{L}^{\otimes 2}|_Z) \to 0
$$
Observe that $Z$ has dimension $0$
(Divisors, Lemma \ref{divisors-lemma-effective-Cartier-makes-dimension-drop})
and hence is the spectrum of an Artinian ring
(Varieties, Lemma \ref{varieties-lemma-algebraic-scheme-dim-0})
hence $\mathcal{L}|_Z \cong \mathcal{O}_Z$
(Algebra, Lemma \ref{algebra-lemma-locally-free-semi-local-free}).
The short exact sequence also shows that
$H^1(X, \mathcal{L}^{\otimes 2}) = 0$ (for example using
Varieties, Lemma \ref{varieties-lemma-chi-tensor-finite}
to see vanishing in the spot on the right). Using induction
on $n \geq 1$ and the sequence
$$
0 \to \mathcal{L}^{\otimes n} \xrightarrow{s}
\mathcal{L}^{\otimes n + 1} \to
i_*(\mathcal{L}^{\otimes n + 1}|_Z) \to 0
$$
we see that $H^1(X, \mathcal{L}^{\otimes n}) = 0$ for $n > 0$
and that there exists a global section $t_{n + 1}$
of $\mathcal{L}^{\otimes n + 1}$ which gives a trivialization of
$\mathcal{L}^{\otimes n + 1}|_Z \cong \mathcal{O}_Z$.

\medskip\noindent
Consider the multiplication map
$$
\mu_n :
H^0(X, \mathcal{L}) \otimes_k H^0(X, \mathcal{L}^{\otimes n})
\oplus
H^0(X, \mathcal{L}^{\otimes 2}) \otimes_k H^0(X, \mathcal{L}^{\otimes n - 1})
\longrightarrow
H^0(X, \mathcal{L}^{\otimes n + 1})
$$
We claim this is surjective for $n \geq 3$.
To see this we consider the short exact sequence
$$
0 \to \mathcal{L}^{\otimes n} \xrightarrow{s}
\mathcal{L}^{\otimes n + 1} \to i_*(\mathcal{L}^{\otimes n + 1}|_Z) \to 0
$$
The sections of $\mathcal{L}^{\otimes n + 1}$ coming from the left in this
sequence are in the image of $\mu_n$. On the other hand, since
$H^0(\mathcal{L}^{\otimes 2}) \to H^0(\mathcal{L}^{\otimes 2}|_Z)$
is surjective (see above) and since $t_{n - 1}$ maps to a trivialization of
$\mathcal{L}^{\otimes n - 1}|_Z$
we see that $\mu_n(H^0(X, \mathcal{L}^{\otimes 2}) \otimes t_{n - 1})$
gives a subspace
of $H^0(X, \mathcal{L}^{\otimes n + 1})$ surjecting onto the global sections of
$\mathcal{L}^{\otimes n + 1}|_Z$. This proves the claim.

\medskip\noindent
From the claim in the previous paragraph we conclude
that the graded $k$-algebra
$$
S = \bigoplus\nolimits_{n \geq 0} H^0(X, \mathcal{L}^{\otimes n})
$$
is generated in degrees $0, 1, 2, 3$ over $k$.
Recall that $X = \text{Proj}(S)$, see
Morphisms, Lemma \ref{morphisms-lemma-proper-ample-is-proj}.
Thus $S^{(6)} = \bigoplus_{n} S_{6n}$ is generated in degree $1$.
This means that $\mathcal{L}^{\otimes 6}$ is very ample as desired.


\begin{lemma}
\label{lemma-criterion-very-ample-bis}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Let $\mathcal{L}$ be an invertible
$\mathcal{O}_X$-module. Assume


1.  $\mathcal{L}$ is globally generated,
1.  $H^1(X, \mathcal{L}) = 0$, and
1.  $\mathcal{L}$ is ample.

Then $\mathcal{L}^{\otimes 2}$ is very ample on $X$ over $k$.
\end{lemma}

#### Proof

Choose basis $s_0, \ldots, s_n$ of $H^0(X, \mathcal{L}^{\otimes 2})$
over $k$. By property (1) we see that $\mathcal{L}^{\otimes 2}$
is globally generated and we get a morphism
$$
\varphi_{\mathcal{L}^{\otimes 2}, (s_0, \ldots, s_n)} :
X \longrightarrow \mathbf{P}^n_k
$$
See Constructions, Section \ref{constructions-section-projective-space}.
The lemma asserts that this morphism is a closed immersion.
To check this we may replace $k$ by its algebraic closure, see
Descent, Lemma \ref{descent-lemma-descending-property-closed-immersion}.
Thus we may assume $k$ is algebraically closed.

\medskip\noindent
Assume $k$ is algebraically closed. For each generic point $\eta_i \in X$
let $V_i \subset H^0(X, \mathcal{L})$ be the $k$-subvector space of
sections vanishing at $\eta_i$. Since $\mathcal{L}$ is globally generated,
we see that $V_i \not = H^0(X, \mathcal{L})$. Since $X$ has only a
finite number of irreducible components and $k$ is infinite, we can find
$s \in H^0(X, \mathcal{L})$ nonvanishing at $\eta_i$ for all $i$.
Then $s$ is a regular section of $\mathcal{L}$ (because $X$ is
Cohen-Macaulay by Lemma \ref{lemma-automatic} and hence $\mathcal{L}$
has no embedded associated points).

\medskip\noindent
In particular, all of the statements given in the proof of
Lemma \ref{lemma-criterion-very-ample} hold with this $s$.
Moreover, as $\mathcal{L}$ is globally generated, we can find
a global section $t \in H^0(X, \mathcal{L})$ such that
$t|_Z$ is nonvanishing (argue as above using the finite number
of points of $Z$). Then in the proof of Lemma \ref{lemma-criterion-very-ample}
we can use $t$ to see that additionally the multiplication map
$$
\mu_n :
H^0(X, \mathcal{L}) \otimes_k H^0(X, \mathcal{L}^{\otimes 2})
\longrightarrow
H^0(X, \mathcal{L}^{\otimes 3})
$$
is surjective. Thus
$$
S = \bigoplus\nolimits_{n \geq 0} H^0(X, \mathcal{L}^{\otimes n})
$$
is generated in degrees $0, 1, 2$ over $k$. Arguing as in the
proof of Lemma \ref{lemma-criterion-very-ample} we find that
$S^{(2)} = \bigoplus_{n} S_{2n}$ is generated in degree $1$.
This means that $\mathcal{L}^{\otimes 2}$ is very ample as desired.
Some details omitted.










###  The genus of a curve

\label{section-genus}

\noindent
If $X$ is a smooth projective geometrically irreducible curve over a field $k$,
then we've previously defined the genus of $X$ as the dimension of
$H^1(X, \mathcal{O}_X)$, see
Picard Schemes of Curves, Definition \ref{pic-definition-genus}.
Observe that $H^0(X, \mathcal{O}_X) = k$ in this case, see
Varieties, Lemma \ref{varieties-lemma-regular-functions-proper-variety}.
Let us generalize this as follows.

\begin{definition}
\label{definition-genus}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having
dimension $1$ and $H^0(X, \mathcal{O}_X) = k$.
Then the {\it genus} of $X$ is $g = \dim_k H^1(X, \mathcal{O}_X)$.
\end{definition}

\noindent
This is sometimes called the {\it arithmetic genus} of $X$.
In the literature the arithmetic genus of a proper curve $X$
over $k$ is sometimes defined as
$$
p_a(X) = 1 - \chi(X, \mathcal{O}_X) =
1 - \dim_k H^0(X, \mathcal{O}_X) + \dim_k H^1(X, \mathcal{O}_X)
$$
This agrees with our definition when it applies because we assume
$H^0(X, \mathcal{O}_X) = k$. But note that


1.  $p_a(X)$ can be negative, and
1.  $p_a(X)$ depends on the base field $k$ and should be written $p_a(X/k)$.

For example if $k = \mathbf{Q}$
and $X = \mathbf{P}^1_{\mathbf{Q}(i)}$ then
$p_a(X/\mathbf{Q}) = -1$ and $p_a(X/\mathbf{Q}(i)) = 0$.

\medskip\noindent
The assumption that $H^0(X, \mathcal{O}_X) = k$ in our definition has
two consequences. On the one hand, it means there is no confusion about
the base field. On the other hand, it implies the scheme $X$ is
Cohen-Macaulay and equidimensional of dimension $1$
(Lemma \ref{lemma-automatic}). If $\omega_X$ denotes the dualizing
module as in Lemmas \ref{lemma-duality-dim-1} and
\ref{lemma-duality-dim-1-CM} we see that
\begin{equation}
\label{equation-genus}
g = \dim_k H^1(X, \mathcal{O}_X) = \dim_k H^0(X, \omega_X)
\end{equation}
by duality, see Remark \ref{remark-rework-duality-locally-free}.

\medskip\noindent
If $X$ is proper over $k$ of dimension $\leq 1$ and $H^0(X, \mathcal{O}_X)$
is not equal to the ground field $k$, instead of using the arithmetic genus
$p_a(X)$ given by the displayed formula above we shall use the invariant
$\chi(X, \mathcal{O}_X)$. In fact, it is advocated in
\cite[page 276]{FAC} and \cite[Introduction]{Hirzebruch}
that we should call $\chi(X, \mathcal{O}_X)$ the arithmetic genus.

\begin{lemma}
\label{lemma-genus-base-change}
Let $k'/k$ be a field extension. Let $X$ be a proper scheme over $k$ having
dimension $1$ and $H^0(X, \mathcal{O}_X) = k$. Then $X_{k'}$ is a
proper scheme over $k'$
having dimension $1$ and $H^0(X_{k'}, \mathcal{O}_{X_{k'}}) = k'$.
Moreover the genus of $X_{k'}$ is equal to the genus of $X$.
\end{lemma}

#### Proof

The dimension of $X_{k'}$ is $1$ for example by
Morphisms, Lemma \ref{morphisms-lemma-dimension-fibre-after-base-change}.
The morphism $X_{k'} \to \Spec(k')$ is proper by
Morphisms, Lemma \ref{morphisms-lemma-base-change-proper}.
The equality $H^0(X_{k'}, \mathcal{O}_{X_{k'}}) = k'$ follows from
Cohomology of Schemes, Lemma
\ref{coherent-lemma-flat-base-change-cohomology}.
The equality of the genus follows from the same lemma.


\begin{lemma}
\label{lemma-genus-gorenstein}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having
dimension $1$ and $H^0(X, \mathcal{O}_X) = k$. If $X$ is Gorenstein,
then
$$
\deg(\omega_X) = 2g - 2
$$
where $g$ is the genus of $X$ and $\omega_X$ is as in
Lemma \ref{lemma-duality-dim-1}.
\end{lemma}

#### Proof

Immediate from Lemma \ref{lemma-rr}.


\begin{lemma}
\label{lemma-genus-smooth}
Let $X$ be a smooth proper curve over a field $k$
with $H^0(X, \mathcal{O}_X) = k$. Then
$$
\dim_k H^0(X, \Omega_{X/k}) = g
\quad\text{and}\quad
\deg(\Omega_{X/k}) = 2g - 2
$$
where $g$ is the genus of $X$.
\end{lemma}

#### Proof

By Lemma \ref{lemma-duality-dim-1} we have $\Omega_{X/k} = \omega_X$.
Hence the formulas hold by (\ref{equation-genus}) and
Lemma \ref{lemma-genus-gorenstein}.







###  Plane curves

\label{section-plane-curves}

\noindent
Let $k$ be a field. A {\it plane curve} will be a curve $X$ which is isomorphic
to a closed subscheme of $\mathbf{P}^2_k$. Often the embedding
$X \to \mathbf{P}^2_k$ will be considered given. By
Divisors, Example \ref{divisors-example-closed-subscheme-of-proj}
a curve is determined by the corresponding homogeneous ideal
$$
I(X) =
\Ker\left(
k[T_0, T_2, T_2] \longrightarrow \bigoplus \Gamma(X, \mathcal{O}_X(n))
\right)
$$
Recall that in this situation we have
$$
X = \text{Proj}(k[T_0, T_2, T_2]/I)
$$
as closed subschemes of $\mathbf{P}^2_k$.
For more general information on these constructions we refer the
reader to Divisors, Example \ref{divisors-example-closed-subscheme-of-proj}
and the references therein.
It turns out that $I(X) = (F)$ for some homogeneous polynomial
$F \in k[T_0, T_1, T_2]$, see Lemma \ref{lemma-equation-plane-curve}.
Since $X$ is irreducible, it follows that $F$ is irreducible, see
Lemma \ref{lemma-plane-curve}. Moreover, looking at the short exact
sequence
$$
0 \to \mathcal{O}_{\mathbf{P}^2_k}(-d) \xrightarrow{F}
\mathcal{O}_{\mathbf{P}^2_k} \to \mathcal{O}_X \to 0
$$
where $d = \deg(F)$ we find that $H^0(X, \mathcal{O}_X) = k$ and that $X$
has genus $(d - 1)(d - 2)/2$, see proof of Lemma \ref{lemma-genus-plane-curve}.

\medskip\noindent
To find smooth plane curves it is easiest to write explicit
equations. Let $p$ denote the characteristic of $k$. If $p$
does not divide $d$, then we can take
$$
F = T_0^d + T_1^d + T_2^d
$$
The corresponding curve $X = V_+(F)$ is called the
{\it Fermat curve} of degree $d$. It is smooth because
on each standard affine piece $D_+(T_i)$ we obtain
a curve isomorphic to the affine curve
$$
\Spec(k[x, y]/(x^d + y^d + 1))
$$
The ring map $k \to k[x, y]/(x^d + y^d + 1)$ is smooth by
Algebra, Lemma \ref{algebra-lemma-relative-global-complete-intersection-smooth}
as $d x^{d - 1}$ and $d y^{d - 1}$ generate the unit ideal
in $k[x, y]/(x^d + y^d + 1)$. If $p | d$ but $p \not = 3$
then you can use the equation
$$
F = T_0^{d - 1}T_1 + T_1^{d - 1}T_2 + T_2^{d - 1}T_0
$$
Namely, on the affine pieces you get $x + x^{d - 1}y + y^{d - 1}$
with derivatives $1 - x^{d - 2}y$ and $x^{d - 1} - y^{d - 2}$
whose common zero set (of all three) is empty\footnote{Namely,
as $x^{d - 1} = y^{d - 2}$, then $0 = x + x^{d - 1}y + y^{d - 1} =
x + 2 x^{d - 1} y$. Since $x \not = 0$ because $1 = x^{d - 2}y$
we get $0 = 1 + 2x^{d - 2}y = 3$ which is absurd unless $3 = 0$.}.
We leave it to the reader to make examples in characteristic $3$.

\medskip\noindent
More generally for any field $k$ and any $n$ and $d$ there exists
a smooth hypersurface of degree $d$ in $\mathbf{P}^n_k$, see
for example \cite{Poonen}.

\medskip\noindent
Of course, in this way we only find smooth curves whose genus
is a triangular number. To get smooth curves of an arbitrary
genus one can look for smooth curves lying on
$\mathbf{P}^1 \times \mathbf{P}^1$ (insert future reference here).

\begin{lemma}
\label{lemma-equation-plane-curve}
Let $Z \subset \mathbf{P}^2_k$ be a closed subscheme which
is equidimensional of dimension $1$ and has no embedded points
(equivalently $Z$ is Cohen-Macaulay).
Then the ideal $I(Z) \subset k[T_0, T_1, T_2]$ corresponding
to $Z$ is principal.
\end{lemma}

#### Proof

This is a special case of
Divisors, Lemma \ref{divisors-lemma-equation-codim-1-in-projective-space}
(see also Varieties, Lemma
\ref{varieties-lemma-equation-codim-1-in-projective-space}).
The parenthetical statement follows from the fact that a
$1$ dimensional Noetherian scheme is Cohen-Macaulay
if and only if it has no embedded points, see
Divisors, Lemma \ref{divisors-lemma-noetherian-dim-1-CM-no-embedded-points}.


\begin{lemma}
\label{lemma-plane-curve}
Let $Z \subset \mathbf{P}^2_k$ be as in Lemma \ref{lemma-equation-plane-curve}
and let $I(Z) = (F)$ for some $F \in k[T_0, T_1, T_2]$.
Then $Z$ is a curve if and only if $F$ is irreducible.
\end{lemma}

#### Proof

If $F$ is reducible, say $F = F' F''$ then let $Z'$ be the closed subscheme
of $\mathbf{P}^2_k$ defined by $F'$. It is clear that $Z' \subset Z$
and that $Z' \not = Z$. Since $Z'$ has dimension $1$ as well, we conclude
that either $Z$ is not reduced, or that $Z$ is not irreducible.
Conversely, write $Z = \sum a_i D_i$ where $D_i$ are the irreducible
components of $Z$, see
Divisors, Lemmas \ref{divisors-lemma-codim-1-part} and
\ref{divisors-lemma-codimension-1-is-effective-Cartier}.
Let $F_i \in k[T_0, T_1, T_2]$ be the homogeneous
polynomial generating the ideal of $D_i$. Then it is clear that
$F$ and $\prod F_i^{a_i}$ cut out the same closed subscheme of
$\mathbf{P}^2_k$. Hence $F = \lambda \prod F_i^{a_i}$ for some
$\lambda \in k^*$ because both generate the ideal of $Z$.
Thus we see that if $F$ is irreducible, then $Z$ is
a prime divisor, i.e., a curve.


\begin{lemma}
\label{lemma-genus-plane-curve}
Let $Z \subset \mathbf{P}^2_k$ be as in Lemma \ref{lemma-equation-plane-curve}
and let $I(Z) = (F)$ for some $F \in k[T_0, T_1, T_2]$.
Then $H^0(Z, \mathcal{O}_Z) = k$ and the genus of $Z$ is
$(d - 1)(d - 2)/2$ where $d = \deg(F)$.
\end{lemma}

#### Proof

Let $S = k[T_0, T_1, T_2]$.
There is an exact sequence of graded modules
$$
0 \to S(-d) \xrightarrow{F} S \to S/(F) \to 0
$$
Denote $i : Z \to \mathbf{P}^2_k$ the given closed immersion.
Applying the exact functor $\widetilde{\ }$
(Constructions, Lemma \ref{constructions-lemma-proj-sheaves})
we obtain
$$
0 \to \mathcal{O}_{\mathbf{P}^2_k}(-d) \to
\mathcal{O}_{\mathbf{P}^2_k} \to i_*\mathcal{O}_Z \to 0
$$
because $F$ generates the ideal of $Z$.
Note that the cohomology groups of $\mathcal{O}_{\mathbf{P}^2_k}(-d)$ and
$\mathcal{O}_{\mathbf{P}^2_k}$ are given in
Cohomology of Schemes, Lemma
\ref{coherent-lemma-cohomology-projective-space-over-ring}.
On the other hand, we have
$H^q(Z, \mathcal{O}_Z) = H^q(\mathbf{P}^2_k, i_*\mathcal{O}_Z)$ by
Cohomology of Schemes, Lemma \ref{coherent-lemma-relative-affine-cohomology}.
Applying the long exact cohomology sequence
we first obtain that
$$
k = H^0(\mathbf{P}^2_k, \mathcal{O}_{\mathbf{P}^2_k}) \longrightarrow
H^0(Z, \mathcal{O}_Z)
$$
is an isomorphism and next that the boundary map
$$
H^1(Z, \mathcal{O}_Z) \longrightarrow
H^2(\mathbf{P}^2_k, \mathcal{O}_{\mathbf{P}^2_k}(-d)) \cong
k[T_0, T_1, T_2]_{d - 3}
$$
is an isomorphism. Since it is easy to see that the dimension of this
is $(d - 1)(d - 2)/2$ the proof is finished.


\begin{lemma}
\label{lemma-smooth-plane-curve-point-over-separable}
Let $Z \subset \mathbf{P}^2_k$ be as in Lemma \ref{lemma-equation-plane-curve}
and let $I(Z) = (F)$ for some $F \in k[T_0, T_1, T_2]$.
If $Z \to \Spec(k)$ is smooth in at least one point and $k$ is infinite, then
there exists a closed point $z \in Z$ contained in the smooth
locus such that $\kappa(z)/k$ is finite separable of degree
at most $d$.
\end{lemma}

#### Proof

Suppose that $z' \in Z$ is a point where $Z \to \Spec(k)$ is smooth.
After renumbering the coordinates if necessary we may assume
$z'$ is contained in $D_+(T_0)$. Set $f = F(1, x, y) \in k[x, y]$.
Then $Z \cap D_+(X_0)$ is isomorphic to the spectrum of $k[x, y]/(f)$.
Let $f_x, f_y$ be the partial derivatives of $f$ with respect to
$x, y$. Since $z'$ is a smooth point of $Z/k$ we see that either
$f_x$ or $f_y$ is nonzero in $z'$ (see discussion in
Algebra, Section \ref{algebra-section-smooth}).
After renumbering the coordinates
we may assume $f_y$ is not zero at $z'$. Hence there is a nonempty
open subscheme $V \subset Z \cap D_{+}(X_0)$ such that the
projection
$$
p : V \longrightarrow \Spec(k[x])
$$
is \'etale. Because the degree of $f$ as a polynomial in $y$
is at most $d$, we see that the degrees of the fibres of the
projection $p$ are at most $d$ (see discussion in
Morphisms, Section \ref{morphisms-section-universally-bounded}).
Moreover, as $p$ is \'etale
the image of $p$ is an open $U \subset \Spec(k[x])$.
Finally, since $k$ is infinite, the set of $k$-rational points
$U(k)$ of $U$ is infinite, in particular not empty. Pick any
$t \in U(k)$ and let $z \in V$ be a point mapping to $t$.
Then $z$ works.






###  Curves of genus zero

\label{section-genus-zero}

\noindent
Later we will need to know what a proper genus zero curve looks like.
It turns out that a Gorenstein proper genus zero curve is a plane
curve of degree $2$, i.e., a conic, see Lemma \ref{lemma-genus-zero}.
A general proper genus zero curve is obtained from a nonsingular one
(over a bigger field) by a pushout procedure, see
Lemma \ref{lemma-genus-zero-singular}.
Since a nonsingular curve is Gorenstein, these two results
cover all possible cases.

\begin{lemma}
\label{lemma-genus-zero-pic}
Let $X$ be a proper curve over a field $k$ with $H^0(X, \mathcal{O}_X) = k$.
If $X$ has genus $0$, then every invertible $\mathcal{O}_X$-module
$\mathcal{L}$ of degree $0$ is trivial.
\end{lemma}

#### Proof

Namely, we have $\dim_k H^0(X, \mathcal{L}) \geq 0 + 1 - 0 = 1$
by Riemann-Roch (Lemma \ref{lemma-rr}), hence $\mathcal{L}$ has a
nonzero section, hence $\mathcal{L} \cong \mathcal{O}_X$ by
Varieties, Lemma \ref{varieties-lemma-check-invertible-sheaf-trivial}.


\begin{lemma}
\label{lemma-genus-zero-positive-degree}
Let $X$ be a proper curve over a field $k$ with $H^0(X, \mathcal{O}_X) = k$.
Assume $X$ has genus $0$. Let $\mathcal{L}$ be an invertible
$\mathcal{O}_X$-module of degree $d > 0$. Then we have


1.  $\dim_k H^0(X, \mathcal{L}) = d + 1$ and $\dim_k H^1(X, \mathcal{L}) = 0$,
1.  $\mathcal{L}$ is very ample and defines a closed immersion into
$\mathbf{P}^d_k$.

\end{lemma}

#### Proof

By definition of degree and genus we have
$$
\dim_k H^0(X, \mathcal{L}) - \dim_k H^1(X, \mathcal{L}) = d + 1
$$
Let $s$ be a nonzero section of $\mathcal{L}$.
Then the zero scheme of $s$ is an effective Cartier
divisor $D \subset X$, we have $\mathcal{L} = \mathcal{O}_X(D)$ and
we have a short exact sequence
$$
0 \to \mathcal{O}_X \to \mathcal{L} \to \mathcal{L}|_D \to 0
$$
see Divisors, Lemma \ref{divisors-lemma-characterize-OD} and
Remark \ref{divisors-remark-ses-regular-section}.
Since $H^1(X, \mathcal{O}_X) = 0$ by assumption, we see that
$H^0(X, \mathcal{L}) \to H^0(X, \mathcal{L}|_D)$ is surjective.
As $\mathcal{L}|_D$ is generated by global sections
(because $\dim(D) = 0$, see
Varieties, Lemma \ref{varieties-lemma-chi-tensor-finite})
we conclude that the invertible module $\mathcal{L}$
is generated by global sections.
In fact, since $D$ is an Artinian scheme we have
$\mathcal{L}|_D \cong \mathcal{O}_D$\footnote{In our case this
follows from Divisors, Lemma
\ref{divisors-lemma-finite-trivialize-invertible-upstairs}
as $D \to \Spec(k)$ is finite.} and hence we can
find a section $t$ of $\mathcal{L}$ whose restriction
of $D$ generates $\mathcal{L}|_D$.
The short exact sequence also shows that $H^1(X, \mathcal{L}) = 0$.

\medskip\noindent
For $n \geq 1$ consider the multiplication map
$$
\mu_n :
H^0(X, \mathcal{L}) \otimes_k H^0(X, \mathcal{L}^{\otimes n})
\longrightarrow
H^0(X, \mathcal{L}^{\otimes n + 1})
$$
We claim this is surjective. To see this we consider the short exact
sequence
$$
0 \to \mathcal{L}^{\otimes n} \xrightarrow{s}
\mathcal{L}^{\otimes n + 1} \to \mathcal{L}^{\otimes n + 1}|_D \to 0
$$
The sections of $\mathcal{L}^{\otimes n + 1}$ coming from the left in this
sequence are in the image of $\mu_n$. On the other hand, since
$H^0(\mathcal{L}) \to H^0(\mathcal{L}|_D)$ is surjective and since
$t^n$ maps to a trivialization of $\mathcal{L}^{\otimes n}|_D$
we see that $\mu_n(H^0(X, \mathcal{L}) \otimes t^n)$ gives a subspace
of $H^0(X, \mathcal{L}^{\otimes n + 1})$ surjecting onto the global sections of
$\mathcal{L}^{\otimes n + 1}|_D$. This proves the claim.

\medskip\noindent
Observe that $\mathcal{L}$ is ample by
Varieties, Lemma \ref{varieties-lemma-ample-curve}.
Hence
Morphisms, Lemma \ref{morphisms-lemma-proper-ample-is-proj}
gives an isomorphism
$$
X \longrightarrow
\text{Proj}\left(
\bigoplus\nolimits_{n \geq 0} H^0(X, \mathcal{L}^{\otimes n})\right)
$$
Since the maps $\mu_n$ are surjective for all $n \geq 1$ we see that
the graded algebra on the right hand side is a quotient of
the symmetric algebra on $H^0(X, \mathcal{L})$. Choosing a $k$-basis
$s_0, \ldots, s_d$ of $H^0(X, \mathcal{L})$ we see that
it is a quotient of a polynomial algebra in $d + 1$ variables.
Since quotients of graded rings correspond to closed immersions
of $\text{Proj}$ (Constructions, Lemma
\ref{constructions-lemma-surjective-graded-rings-generated-degree-1-map-proj})
we find a closed immersion $X \to \mathbf{P}^d_k$. We omit the
verification that this morphism is the morphism of
Constructions, Lemma \ref{constructions-lemma-projective-space}
associated to the sections $s_0, \ldots, s_d$ of $\mathcal{L}$.


\begin{lemma}
\label{lemma-genus-zero}
Let $X$ be a proper curve over a field $k$ with $H^0(X, \mathcal{O}_X) = k$.
If $X$ is Gorenstein and has genus $0$, then $X$
is isomorphic to a plane curve of degree $2$.
\end{lemma}

#### Proof

Consider the invertible sheaf $\mathcal{L} = \omega_X^{\otimes -1}$ where
$\omega_X$ is as in Lemma \ref{lemma-duality-dim-1}. Then
$\deg(\omega_X) = -2$ by Lemma \ref{lemma-genus-gorenstein}
and hence $\deg(\mathcal{L}) = 2$. By
Lemma \ref{lemma-genus-zero-positive-degree}
we conclude that choosing a basis $s_0, s_1, s_2$ of the $k$-vector
space of global sections of $\mathcal{L}$ we obtain a closed immersion
$$
\varphi_{(\mathcal{L}, (s_0, s_1, s_2))} :
X \longrightarrow \mathbf{P}^2_k
$$
Thus $X$ is a plane curve of some degree $d$. Let $F \in k[T_0, T_1, T_2]_d$
be its equation (Lemma \ref{lemma-equation-plane-curve}).
Because the genus of $X$ is $0$ we see that $d$ is $1$ or $2$
(Lemma \ref{lemma-genus-plane-curve}). Observe that
$F$ restricts to the zero section on $\varphi(X)$ and hence
$F(s_0, s_1, s_2)$ is the zero section of $\mathcal{L}^{\otimes 2}$.
Because $s_0, s_1, s_2$ are linearly independent we see that $F$
cannot be linear, i.e., $d = \deg(F) \geq 2$. Thus $d = 2$
and the proof is complete.


\begin{proposition}[Characterization of the projective line]
\label{proposition-projective-line}
Let $k$ be a field. Let $X$ be a proper curve over $k$.
The following are equivalent


1.  $X \cong \mathbf{P}^1_k$,
1.  $X$ is smooth and geometrically irreducible over $k$,
$X$ has genus $0$, and $X$ has an invertible module of odd degree,
1.  $X$ is geometrically integral over $k$, $X$ has genus $0$,
$X$ is Gorenstein, and $X$ has an invertible sheaf of odd degree,
1.  $H^0(X, \mathcal{O}_X) = k$, $X$ has genus $0$, $X$ is Gorenstein,
and $X$ has an invertible sheaf of odd degree,
1.  $X$ is geometrically integral over $k$, $X$ has genus $0$,
and $X$ has an invertible $\mathcal{O}_X$-module of degree $1$,
1.  $H^0(X, \mathcal{O}_X) = k$, $X$ has genus $0$,
and $X$ has an invertible $\mathcal{O}_X$-module of degree $1$,
1.  $H^1(X, \mathcal{O}_X) = 0$ and $X$ has an invertible
$\mathcal{O}_X$-module of degree $1$,
1.  $H^1(X, \mathcal{O}_X) = 0$ and $X$
has closed points $x_1, \ldots, x_n$ such that
$\mathcal{O}_{X, x_i}$ is normal and $\gcd([\kappa(x_i) : k]) = 1$, and
1.  add more here.

\end{proposition}

#### Proof

We will prove that each condition (2) -- (8) implies (1) and we omit
the verification that (1) implies (2) -- (8).

\medskip\noindent
Assume (2). A smooth scheme over $k$ is geometrically reduced
(Varieties, Lemma \ref{varieties-lemma-smooth-geometrically-normal})
and regular (Varieties, Lemma \ref{varieties-lemma-smooth-regular}).
Hence $X$ is Gorenstein (Duality for Schemes, Lemma
\ref{duality-lemma-regular-gorenstein}).
Thus we reduce to (3).

\medskip\noindent
Assume (3). Since $X$ is geometrically integral over $k$ we have
$H^0(X, \mathcal{O}_X) = k$ by
Varieties, Lemma \ref{varieties-lemma-regular-functions-proper-variety}.
and we reduce to (4).

\medskip\noindent
Assume (4). Since $X$ is Gorenstein the dualizing module
$\omega_X$ as in Lemma \ref{lemma-duality-dim-1} has degree
$\deg(\omega_X) = -2$ by Lemma \ref{lemma-genus-gorenstein}.
Combined with the assumed existence of an odd degree invertible
module, we conclude there exists an invertible module of degree $1$.
In this way we reduce to (6).

\medskip\noindent
Assume (5). Since $X$ is geometrically integral over $k$ we have
$H^0(X, \mathcal{O}_X) = k$ by
Varieties, Lemma \ref{varieties-lemma-regular-functions-proper-variety}.
and we reduce to (6).

\medskip\noindent
Assume (6). Then $X \cong \mathbf{P}^1_k$ by
Lemma \ref{lemma-genus-zero-positive-degree}.

\medskip\noindent
Assume (7). Observe that $\kappa = H^0(X, \mathcal{O}_X)$ is a field
finite over $k$ by
Varieties, Lemma \ref{varieties-lemma-regular-functions-proper-variety}.
If $d = [\kappa : k] > 1$, then every invertible sheaf has degree
divisible by $d$ and there cannot be an invertible sheaf of degree $1$.
Hence $d = 1$ and we reduce to case (6).

\medskip\noindent
Assume (8). Observe that $\kappa = H^0(X, \mathcal{O}_X)$ is a field
finite over $k$ by
Varieties, Lemma \ref{varieties-lemma-regular-functions-proper-variety}.
Since $\kappa \subset \kappa(x_i)$ we see that $k = \kappa$
by the assumption on the gcd of the degrees. The same condition
allows us to find integers $a_i$ such that
$1 = \sum a_i[\kappa(x_i) : k]$. Because $x_i$ defines an
effective Cartier divisor on $X$ by
Varieties, Lemma \ref{varieties-lemma-regular-point-on-curve}
we can consider the invertible module $\mathcal{O}_X(\sum a_i x_i)$.
By our choice of $a_i$ the degree of $\mathcal{L}$ is $1$.
Thus $X \cong \mathbf{P}^1_k$ by Lemma \ref{lemma-genus-zero-positive-degree}.


\begin{lemma}
\label{lemma-genus-zero-singular}
Let $X$ be a proper curve over a field $k$ with $H^0(X, \mathcal{O}_X) = k$.
Assume $X$ is singular and has genus $0$. Then there exists a diagram
$$
\xymatrix{
x' \ar[d] \ar[r] & X' \ar[d]^\nu \ar[r] & \Spec(k') \ar[d] \\\\
x \ar[r] & X \ar[r] & \Spec(k)
}
$$
where


1.  $k'/k$ is a nontrivial finite extension,
1.  $X' \cong \mathbf{P}^1_{k'}$,
1.  $x'$ is a $k'$-rational point of $X'$,
1.  $x$ is a $k$-rational point of $X$,
1.  $X' \setminus \{x'\} \to X \setminus \{x\}$ is an isomorphism,
1.  $0 \to \mathcal{O}_X \to \nu_*\mathcal{O}_{X'} \to k'/k \to 0$
is a short exact sequence
where $k'/k = \kappa(x')/\kappa(x)$ indicates the skyscraper sheaf
on the point $x$.

\end{lemma}

#### Proof

Let $\nu : X' \to X$ be the normalization of $X$, see
Varieties, Sections \ref{varieties-section-normalization} and
\ref{varieties-section-normalization-one-dimensional}.
Since $X$ is singular $\nu$ is not an isomorphism.
Then $k' = H^0(X', \mathcal{O}_{X'})$ is a finite extension of $k$
(Varieties, Lemma \ref{varieties-lemma-regular-functions-proper-variety}).
The short exact sequence
$$
0 \to \mathcal{O}_X \to \nu_*\mathcal{O}_{X'} \to \mathcal{Q} \to 0
$$
and the fact that $\mathcal{Q}$ is supported in finitely many
closed points give us that


1.  $H^1(X', \mathcal{O}_{X'}) = 0$, i.e., $X'$ has genus $0$
as a curve over $k'$,
1.  there is a short exact sequence
$0 \to k \to k' \to H^0(X, \mathcal{Q}) \to 0$.

In particular $k'/k$ is a nontrivial extension.

\medskip\noindent
Next, we consider what is often called the {\it conductor ideal}
$$
\mathcal{I} = \SheafHom_{\mathcal{O}_X}(\nu_*\mathcal{O}_{X'}, \mathcal{O}_X)
$$
This is a quasi-coherent $\mathcal{O}_X$-module. We view $\mathcal{I}$
as an ideal in $\mathcal{O}_X$ via the map $\varphi \mapsto \varphi(1)$.
Thus $\mathcal{I}(U)$ is the set of $f \in \mathcal{O}_X(U)$ such that
$f \left(\nu_*\mathcal{O}_{X'}(U)\right) \subset \mathcal{O}_X(U)$. In
other words, the condition is that $f$ annihilates $\mathcal{Q}$.
In other words, there is a defining exact sequence
$$
0 \to \mathcal{I} \to \mathcal{O}_X \to
\SheafHom_{\mathcal{O}_X}(\mathcal{Q}, \mathcal{Q})
$$
Let $U \subset X$ be an affine open containing the support of $\mathcal{Q}$.
Then $V = \mathcal{Q}(U) = H^0(X, \mathcal{Q})$ is a $k$-vector space
of dimension $n - 1$. The image of
$\mathcal{O}_X(U) \to \Hom_k(V, V)$ is a commutative subalgebra,
hence has dimension $\leq n - 1$ over $k$ (this is a property of
commutative subalgebras of matrix algebras; details omitted).
We conclude that we have a short exact sequence
$$
0 \to \mathcal{I} \to \mathcal{O}_X \to \mathcal{A} \to 0
$$
where $\text{Supp}(\mathcal{A}) = \text{Supp}(\mathcal{Q})$
and $\dim_k H^0(X, \mathcal{A}) \leq n - 1$.
On the other hand, the description
$\mathcal{I} = \SheafHom_{\mathcal{O}_X}(\nu_*\mathcal{O}_{X'}, \mathcal{O}_X)$
provides $\mathcal{I}$ with a $\nu_*\mathcal{O}_{X'}$-module structure
such that the inclusion map $\mathcal{I} \to \nu_*\mathcal{O}_{X'}$
is a $\nu_*\mathcal{O}_{X'}$-module map.
We conclude that $\mathcal{I} = \nu_*\mathcal{I}'$
for some quasi-coherent sheaf of ideals
$\mathcal{I}' \subset \mathcal{O}_{X'}$, see
Morphisms, Lemma \ref{morphisms-lemma-affine-equivalence-modules}.
Define $\mathcal{A}'$ as the cokernel:
$$
0 \to \mathcal{I}' \to \mathcal{O}_{X'} \to \mathcal{A}' \to 0
$$
Combining the exact sequences so far we obtain a short exact sequence
$0 \to \mathcal{A} \to \nu_*\mathcal{A}' \to \mathcal{Q} \to 0$.
Using the estimate above,
combined with $\dim_k H^0(X, \mathcal{Q}) = n - 1$, gives
$$
\dim_k H^0(X', \mathcal{A}') =
\dim_k H^0(X, \mathcal{A}) + \dim_k H^0(X, \mathcal{Q}) \leq 2 n - 2
$$
However, since $X'$ is a curve over $k'$ we see that
the left hand side is divisible by $n$
(Varieties, Lemma \ref{varieties-lemma-divisible}).
As $\mathcal{A}$ and $\mathcal{A}'$ cannot be zero, we conclude that
$\dim_k H^0(X', \mathcal{A}') = n$ which means that $\mathcal{I}'$
is the ideal sheaf of a $k'$-rational point $x'$.
By Proposition \ref{proposition-projective-line}
we find $X' \cong \mathbf{P}^1_{k'}$.
Going back to the equalities above, we conclude that
$\dim_k H^0(X, \mathcal{A}) = 1$. This
means that $\mathcal{I}$ is the ideal sheaf of a
$k$-rational point $x$. Then $\mathcal{A} = \kappa(x) = k$
and $\mathcal{A}' = \kappa(x') = k'$ as skyscraper sheaves.
Comparing the exact sequences given above,
this immediately implies the result on structure sheaves
as stated in the lemma.


\begin{example}
\label{example-squish-on-P1}
In fact, the situation described in Lemma \ref{lemma-genus-zero-singular}
occurs for any nontrivial finite extension $k'/k$. Namely, we can consider
$$
A = \{f \in k'[x] \mid f(0) \in k \}
$$
The spectrum of $A$ is an affine curve, which we can glue to
the spectrum of $B = k'[y]$ using the isomorphism
$A_x \cong B_y$ sending $x^{-1}$ to $y$.
The result is a proper curve $X$ with $H^0(X, \mathcal{O}_X) = k$
and singular point $x$ corresponding to the maximal ideal $A \cap (x)$.
The normalization of $X$ is $\mathbf{P}^1_{k'}$ exactly as in the lemma.
\end{example}








###  Geometric genus

\label{section-geometric-genus}

\noindent
If $X$ is a proper and {\bf smooth} curve over $k$ with
$H^0(X, \mathcal{O}_X) = k$, then
$$
p_g(X) = \dim_k H^0(X, \Omega_{X/k})
$$
is called the {\it geometric genus} of $X$. By Lemma \ref{lemma-genus-smooth}
the geometric genus of $X$ agrees with the (arithmetic) genus. However,
in higher dimensions there is a difference between the geometric genus
and the arithmetic genus, see Remark \ref{remark-genus-higher-dimension}.

\medskip\noindent
For singular curves, we will define the geometric genus as follows.

\begin{definition}
\label{definition-geometric-genus}
Let $k$ be a field. Let $X$ be a geometrically irreducible
curve over $k$. The {\it geometric genus} of $X$ is the genus
of a smooth projective model of $X$ possibly defined over
an extension field of $k$ as in
Lemma \ref{lemma-smooth-models}.
\end{definition}

\noindent
If $k$ is perfect, then the nonsingular projective model $Y$ of $X$
is smooth (Lemma \ref{lemma-nonsingular-model-smooth})
and the geometric genus of $X$ is just the genus of $Y$.
But if $k$ is not perfect, this may not be true.
In this case we choose an extension $K/k$ such that
the nonsingular projective model $Y_K$ of $(X_K)_{red}$ is
a smooth projective curve and we define the geometric genus
of $X$ to be the genus of $Y_K$. This is well defined by
Lemmas \ref{lemma-smooth-models} and \ref{lemma-genus-base-change}.

\begin{remark}
\label{remark-genus-higher-dimension}
Suppose that $X$ is a $d$-dimensional proper smooth variety over
an algebraically closed field $k$.
Then the {\it arithmetic genus} is often defined as
$p_a(X) = (-1)^d(\chi(X, \mathcal{O}_X) - 1)$ and the {\it geometric genus}
as $p_g(X) = \dim_k H^0(X, \Omega^d_{X/k})$. In this situation
the arithmetic genus and the geometric genus no longer agree
even though it is still true that $\omega_X \cong \Omega_{X/k}^d$.
For example, if $d = 2$, then we have
\begin{align}
p_a(X) - p_g(X) & =
h^0(X, \mathcal{O}_X) - h^1(X, \mathcal{O}_X) + h^2(X, \mathcal{O}_X) - 1
- h^0(X, \Omega^2_{X/k}) \\\\
& =
- h^1(X, \mathcal{O}_X) + h^2(X, \mathcal{O}_X) - h^0(X, \omega_X) \\\\
& =
- h^1(X, \mathcal{O}_X)
\end{align}
where $h^i(X, \mathcal{F}) = \dim_k H^i(X, \mathcal{F})$ and
where the last equality follows from duality.
Hence for a surface the difference $p_g(X) - p_a(X)$ is always
nonnegative; it is sometimes called the irregularity of the surface.
If $X = C_1 \times C_2$ is a product of smooth projective curves of
genus $g_1$ and $g_2$, then the irregularity is $g_1 + g_2$.
\end{remark}






###  Riemann-Hurwitz

\label{section-riemann-hurewitz}

\noindent
Let $k$ be a field. Let $f : X \to Y$ be a morphism of smooth curves over $k$.
Then we obtain a canonical exact sequence
$$
f^*\Omega_{Y/k} \xrightarrow{\text{d}f} \Omega_{X/k}
\longrightarrow \Omega_{X/Y} \longrightarrow 0
$$
by Morphisms, Lemma \ref{morphisms-lemma-triangle-differentials}.
Since $X$ and $Y$ are smooth, the sheaves $\Omega_{X/k}$ and
$\Omega_{Y/k}$ are invertible modules, see
Morphisms, Lemma \ref{morphisms-lemma-smooth-omega-finite-locally-free}.
Assume the first map is nonzero, i.e., assume $f$ is generically
\'etale, see Lemma \ref{lemma-generically-etale}. Let $R \subset X$
be the closed subscheme cut out by the different $\mathfrak{D}_f$ of $f$.
By Discriminants, Lemma
\ref{discriminant-lemma-discriminant-quasi-finite-morphism-smooth}
this is the same as the vanishing locus of $\text{d}f$, it is
an effective Cartier divisor, and we get
$$
f^*\Omega_{Y/k} \otimes_{\mathcal{O}_X} \mathcal{O}_X(R) = \Omega_{X/k}
$$
In particular, if $X$, $Y$ are projective with
$k = H^0(Y, \mathcal{O}_Y) = H^0(X, \mathcal{O}_X)$
and $X$, $Y$ have genus $g_X$, $g_Y$, then we get the
Riemann-Hurwitz formula
\begin{align}
2g_X - 2 & =
\deg(\Omega_{X/k}) \\\\
& =
\deg(f^*\Omega_{Y/k} \otimes_{\mathcal{O}_X} \mathcal{O}_X(R)) \\\\
& =
\deg(f) \deg(\Omega_{Y/k}) + \deg(R) \\\\
& =
\deg(f) (2g_Y - 2) + \deg(R)
\end{align}
The first and last equality by Lemma \ref{lemma-genus-smooth}.
The second equality by the isomorphism of invertible sheaves given above.
The third equality by additivity of degrees
(Varieties, Lemma \ref{varieties-lemma-degree-tensor-product}),
the formula for the degree of a pullback
(Varieties, Lemma \ref{varieties-lemma-degree-pullback-map-proper-curves}),
and finally the formula for the degree of $\mathcal{O}_X(R)$
(Varieties, Lemma \ref{varieties-lemma-degree-effective-Cartier-divisor}).

\medskip\noindent
To use the Riemann-Hurwitz formula we need to compute
$\deg(R) = \dim_k \Gamma(R, \mathcal{O}_R)$. By the structure
of zero dimensional schemes over $k$ (see for example
Varieties, Lemma \ref{varieties-lemma-algebraic-scheme-dim-0}),
we see that $R$ is a finite disjoint union of spectra of
Artinian local rings $R = \coprod_{x \in R} \Spec(\mathcal{O}_{R, x})$
with each $\mathcal{O}_{R, x}$ of finite dimension over $k$. Thus
$$
\deg(R) = \sum\nolimits_{x \in R} \dim_k \mathcal{O}_{R, x} =
\sum\nolimits_{x \in R} d_x [\kappa(x) : k]
$$
with
$$
d_x = \text{length}_{\mathcal{O}_{R, x}} \mathcal{O}_{R, x} =
\text{length}_{\mathcal{O}_{X, x}} \mathcal{O}_{R, x}
$$
the multiplicity of $x$ in $R$
(see Algebra, Lemma \ref{algebra-lemma-pushdown-module}).
Let $x \in X$ be a closed point with image $y \in Y$.
Looking at stalks we obtain an exact sequence
$$
\Omega_{Y/k, y} \to \Omega_{X/k, x} \to \Omega_{X/Y, x} \to 0
$$
Choosing local generators $\eta_x$ and $\eta_y$ of the
(free rank $1$) modules $\Omega_{X/k, x}$ and $\Omega_{Y/k, y}$
we see that
$
\eta_y \mapsto h \eta_x
$
for some nonzero $h \in \mathcal{O}_{X, x}$. By the exact sequence we see that
$\Omega_{X/Y, x} \cong \mathcal{O}_{X, x}/h\mathcal{O}_{X, x}$
as $\mathcal{O}_{X, x}$-modules. Since the divisor
$R$ is cut out by $h$ (see above) we have
$\mathcal{O}_{R, x} = \mathcal{O}_{X, x}/h\mathcal{O}_{X, x}$.
Thus we find the following equalities
\begin{align}
d_x
& =
\text{length}_{\mathcal{O}_{X, x}}(\mathcal{O}_{R, x}) \\\\
& =
\text{length}_{\mathcal{O}_{X, x}}(\mathcal{O}_{X, x}/h\mathcal{O}_{X, x}) \\\\
& =
\text{length}_{\mathcal{O}_{X, x}}(\Omega_{X/Y, x}) \\\\
& =
\text{ord}_{\mathcal{O}_{X, x}}(h) \\\\
& =
\text{ord}_{\mathcal{O}_{X, x}}(``\eta_y/\eta_x")
\end{align}
The first equality by our definition of $d_x$. The second and third
we saw above. The fourth equality is the definition of $\text{ord}$, see
Algebra, Definition \ref{algebra-definition-ord}. Note that since
$\mathcal{O}_{X, x}$ is a discrete valuation ring, the integer
$\text{ord}_{\mathcal{O}_{X, x}}(h)$ just the valuation of $h$.
The fifth equality is a mnemonic.

\medskip\noindent
Here is a case where one can ``calculate'' the multiplicity $d_x$ in terms
of other invariants. Namely, if $\kappa(x)$ is separable over $k$, then
we may choose $\eta_x = \text{d}s$ and $\eta_y = \text{d}t$ where $s$
and $t$ are uniformizers in $\mathcal{O}_{X, x}$ and $\mathcal{O}_{Y, y}$
(Lemma \ref{lemma-uniformizer-works}).
Then $t \mapsto u s^{e_x}$ for some unit $u \in \mathcal{O}_{X, x}$
where $e_x$ is the ramification index of the extension
$\mathcal{O}_{Y, y} \subset \mathcal{O}_{X, x}$. Hence we get
$$
\eta_y = \text{d}t = \text{d}(u s^{e_x}) =
e s^{e_x - 1} u \text{d}s + s^{e_x} \text{d}u
$$
Writing $\text{d}u = w \text{d}s$ for some $w \in \mathcal{O}_{X, x}$
we see that
$$
``\eta_y/\eta_x" = e s^{e_x - 1} u + s^{e_x} w = (e_x u + s w)s^{e_x - 1}
$$
We conclude that the order of vanishing of this is $e_x - 1$
unless the characteristic of $\kappa(x)$ is $p > 0$ and $p$ divides $e_x$
in which case the order of vanishing is $> e_x - 1$.

\medskip\noindent
Combining all of the above we find that if $k$ has characteristic
zero, then
$$
2g_X - 2 = (2g_Y - 2)\deg(f) +
\sum\nolimits_{x \in X} (e_x - 1)[\kappa(x) : k]
$$
where $e_x$ is the ramification index of $\mathcal{O}_{X, x}$ over
$\mathcal{O}_{Y, f(x)}$. This precise formula will hold if and only
if all the ramification is tame, i.e., when the
residue field extensions $\kappa(x)/\kappa(y)$ are separable and
$e_x$ is prime to the characteristic of $k$, although the
arguments above are insufficient to prove this. We refer the reader
to Lemma \ref{lemma-rhe} and its proof.

\begin{lemma}
\label{lemma-generically-etale}
\begin{slogan}
A morphism of smooth curves is separable iff it is etale almost everywhere
\end{slogan}
Let $k$ be a field. Let $f : X \to Y$ be a morphism of smooth curves over $k$.
The following are equivalent


1.  $\text{d}f : f^*\Omega_{Y/k} \to \Omega_{X/k}$ is nonzero,
1.  $\Omega_{X/Y}$ is supported on a proper closed subset of $X$,
1.  there exists a nonempty open $U \subset X$ such that
$f|_U : U \to Y$ is unramified,
1.  there exists a nonempty open $U \subset X$ such that
$f|_U : U \to Y$ is \'etale,
1.  the extension $k(X)/k(Y)$ of function fields is
finite separable.

\end{lemma}

#### Proof

Since $X$ and $Y$ are smooth, the sheaves $\Omega_{X/k}$ and
$\Omega_{Y/k}$ are invertible modules, see
Morphisms, Lemma \ref{morphisms-lemma-smooth-omega-finite-locally-free}.
Using the exact sequence
$$
f^*\Omega_{Y/k} \longrightarrow \Omega_{X/k}
\longrightarrow \Omega_{X/Y} \longrightarrow 0
$$
of Morphisms, Lemma \ref{morphisms-lemma-triangle-differentials}
we see that (1) and (2) are equivalent and equivalent to the
condition that $f^*\Omega_{Y/k} \to \Omega_{X/k}$ is nonzero
in the generic point. The equivalence of (2) and (3) follows
from Morphisms, Lemma \ref{morphisms-lemma-unramified-omega-zero}.
The equivalence between (3) and (4) follows from
Morphisms, Lemma \ref{morphisms-lemma-flat-unramified-etale}
and the fact that flatness is automatic
(Lemma \ref{lemma-flat}).
To see the equivalence of (5) and (4)
use Algebra, Lemma \ref{algebra-lemma-smooth-at-generic-point}.
Some details omitted.


\begin{lemma}
\label{lemma-rh}
Let $f : X \to Y$ be a morphism of smooth proper curves
over a field $k$ which satisfies the equivalent conditions of
Lemma \ref{lemma-generically-etale}. If
$k = H^0(Y, \mathcal{O}_Y) = H^0(X, \mathcal{O}_X)$
and $X$ and $Y$ have genus $g_X$ and $g_Y$, then
$$
2g_X - 2 = (2g_Y - 2) \deg(f) + \deg(R)
$$
where $R \subset X$ is the effective Cartier divisor cut out by
the different of $f$.
\end{lemma}

#### Proof

See discussion above; we used
Discriminants, Lemma
\ref{discriminant-lemma-discriminant-quasi-finite-morphism-smooth},
Lemma \ref{lemma-genus-smooth}, and
Varieties, Lemmas \ref{varieties-lemma-degree-tensor-product} and
\ref{varieties-lemma-degree-pullback-map-proper-curves}.


\begin{lemma}
\label{lemma-uniformizer-works}
Let $X \to \Spec(k)$ be smooth of relative dimension $1$ at a closed
point $x \in X$. If $\kappa(x)$ is separable over $k$, then for
any uniformizer $s$ in the discrete valuation ring $\mathcal{O}_{X, x}$
the element $\text{d}s$ freely generates $\Omega_{X/k, x}$
over $\mathcal{O}_{X, x}$.
\end{lemma}

#### Proof

The ring $\mathcal{O}_{X, x}$ is a discrete valuation ring by
Algebra, Lemma \ref{algebra-lemma-characterize-smooth-over-field}.
Since $x$ is closed $\kappa(x)$ is finite over $k$. Hence if
$\kappa(x)/k$ is separable, then any uniformizer $s$
maps to a nonzero element of
$\Omega_{X/k, x} \otimes_{\mathcal{O}_{X, x}} \kappa(x)$ by
Algebra, Lemma \ref{algebra-lemma-computation-differential}.
Since $\Omega_{X/k, x}$ is free of rank $1$ over $\mathcal{O}_{X, x}$
the result follows.


\begin{lemma}
\label{lemma-rhe}
Notation and assumptions as in Lemma \ref{lemma-rh}. For a closed point
$x \in X$ let $d_x$ be the multiplicity of $x$ in $R$. Then
$$
2g_X - 2 = (2g_Y - 2) \deg(f) + \sum\nolimits d_x [\kappa(x) : k]
$$
Moreover, we have the following results


1.  $d_x = \text{length}_{\mathcal{O}_{X, x}}(\Omega_{X/Y, x})$,
1.  $d_x \geq e_x - 1$ where $e_x$ is the ramification index
of $\mathcal{O}_{X, x}$ over $\mathcal{O}_{Y, y}$,
1.  $d_x = e_x - 1$ if and only if $\mathcal{O}_{X, x}$ is tamely
ramified over $\mathcal{O}_{Y, y}$.

\end{lemma}

#### Proof

By Lemma \ref{lemma-rh} and the discussion above
(which used
Varieties, Lemma \ref{varieties-lemma-algebraic-scheme-dim-0}
and
Algebra, Lemma \ref{algebra-lemma-pushdown-module})
it suffices to prove the results on the
multiplicity $d_x$ of $x$ in $R$. Part (1) was proved
in the discussion above. In the discussion above
we proved (2) and (3) only in the case where $\kappa(x)$ is
separable over $k$.
In the rest of the proof we give a uniform treatment
of (2) and (3) using material on differents of
quasi-finite Gorenstein morphisms.

\medskip\noindent
First, observe that $f$ is a quasi-finite Gorenstein morphism.
This is true for example because
$f$ is a flat quasi-finite morphism and $X$ is Gorenstein
(see Duality for Schemes, Lemma
\ref{duality-lemma-flat-morphism-from-gorenstein-scheme})
or because it was shown in the proof of
Discriminants, Lemma
\ref{discriminant-lemma-discriminant-quasi-finite-morphism-smooth}
(which we used above). Thus $\omega_{X/Y}$ is invertible by
Discriminants, Lemma \ref{discriminant-lemma-gorenstein-quasi-finite}
and the same remains true after replacing $X$ by opens and after
performing a base change by some $Y' \to Y$. We will use this
below without further mention.

\medskip\noindent
Choose affine opens $U \subset X$ and $V \subset Y$
such that $x \in U$, $y \in V$, $f(U) \subset V$, and $x$ is the only
point of $U$ lying over $y$. Write $U = \Spec(A)$ and $V = \Spec(B)$.
Then $R \cap U$ is the different of $f|_U : U \to V$.
By Discriminants, Lemma \ref{discriminant-lemma-base-change-different}
formation of the different commutes with arbitrary base change
in our case. By our choice of $U$ and $V$ we have
$$
A \otimes_B \kappa(y) =
\mathcal{O}_{X, x} \otimes_{\mathcal{O}_{Y, y}} \kappa(y) =
\mathcal{O}_{X, x}/(s^{e_x})
$$
where $e_x$ is the ramification index as in the statement of the lemma.
Let $C = \mathcal{O}_{X, x}/(s^{e_x})$ viewed as a finite algebra
over $\kappa(y)$. Let $\mathfrak{D}_{C/\kappa(y)}$ be the different
of $C$ over $\kappa(y)$ in the sense of
Discriminants, Definition \ref{discriminant-definition-different}.
It suffices to show: $\mathfrak{D}_{C/\kappa(y)}$
is nonzero if and only if the extension
$\mathcal{O}_{Y, y} \subset \mathcal{O}_{X, x}$ is tamely ramified
and in the tamely ramified case $\mathfrak{D}_{C/\kappa(y)}$
is equal to the ideal generated by $s^{e_x - 1}$ in $C$.
Recall that tame ramification means exactly that $\kappa(x)/\kappa(y)$
is separable and that the characteristic of $\kappa(y)$ does not
divide $e_x$. On the other hand, the different of $C/\kappa(y)$ is nonzero
if and only if $\tau_{C/\kappa(y)} \in \omega_{C/\kappa(y)}$ is nonzero.
Namely, since $\omega_{C/\kappa(y)}$ is an invertible $C$-module
(as the base change of $\omega_{A/B}$)
it is free of rank $1$, say with generator $\lambda$. Write
$\tau_{C/\kappa(y)} = h\lambda$ for some $h \in C$. Then
$\mathfrak{D}_{C/\kappa(y)} = (h) \subset C$ whence the claim.
By Discriminants, Lemma \ref{discriminant-lemma-tau-nonzero}
we have $\tau_{C/\kappa(y)} \not = 0$
if and only if $\kappa(x)/\kappa(y)$
is separable and $e_x$ is prime to the characteristic.
Finally, even if $\tau_{C/\kappa(y)}$ is nonzero, then
it is still the case that $s \tau_{C/\kappa(y)} = 0$
because $s\tau_{C/\kappa(y)} : C \to \kappa(y)$
sends $c$ to the trace of the nilpotent operator $sc$ which is zero.
Hence $sh = 0$, hence $h \in (s^{e_x - 1})$ which proves
that $\mathfrak{D}_{C/\kappa(y)} \subset (s^{e_x - 1})$ always.
Since $(s^{e_x - 1}) \subset C$ is the smallest nonzero ideal,
we have proved the final assertion.







###  Inseparable maps

\label{section-inseparable}

\noindent
Some remarks on the behaviour of the genus under inseparable maps.

\begin{lemma}
\label{lemma-dominated-by-smooth}
Let $k$ be a field. Let $f : X \to Y$ be a surjective morphism
of curves over $k$. If $X$ is smooth over $k$ and
$Y$ is normal, then $Y$ is smooth over $k$.
\end{lemma}

#### Proof

Let $y \in Y$. Pick $x \in X$ mapping to $y$.
By Varieties, Lemma \ref{varieties-lemma-flat-under-smooth}
it suffices to show that $f$ is flat at $x$.
This follows from Lemma \ref{lemma-flat}.


\begin{lemma}
\label{lemma-purely-inseparable}
Let $k$ be a field of characteristic $p > 0$. Let $f : X \to Y$ be a
nonconstant morphism of proper nonsingular curves over $k$.
If the extension $k(X)/k(Y)$ of function fields
is purely inseparable, then there exists a factorization
$$
X = X_0 \to X_1 \to \ldots \to X_n = Y
$$
such that each $X_i$ is a proper nonsingular curve
and $X_i \to X_{i + 1}$ is a degree $p$
morphism with $k(X_{i + 1}) \subset k(X_i)$
inseparable.
\end{lemma}

#### Proof

This follows from Theorem \ref{theorem-curves-rational-maps}
and the fact that a finite purely inseparable extension of fields
can always be gotten as a sequence of (inseparable) extensions of degree $p$,
see Fields, Lemma \ref{fields-lemma-finite-purely-inseparable}.


\begin{lemma}
\label{lemma-inseparable-deg-p-smooth}
Let $k$ be a field of characteristic $p > 0$. Let $f : X \to Y$ be a
nonconstant morphism of proper nonsingular curves over $k$.
If $X$ is smooth and $k(Y) \subset k(X)$ is inseparable of degree $p$,
then there is a unique isomorphism $Y = X^{(p)}$ such that
$f$ is $F_{X/k}$.
\end{lemma}

#### Proof

The relative frobenius morphism $F_{X/k} : X \to X^{(p)}$
is constructed in Varieties, Section \ref{varieties-section-frobenius}.
Observe that $X^{(p)}$ is a smooth proper curve over $k$
as a base change of $X$. The morphism $F_{X/k}$ has degree $p$ by
Varieties, Lemma \ref{varieties-lemma-inseparable-deg-p-smooth}.
Thus $k(X^{(p)})$ and $k(Y)$ are both subfields of $k(X)$
with $[k(X) : k(Y)] = [k(X) : k(X^{(p)})] = p$. To prove the lemma
it suffices to show that $k(Y) = k(X^{(p)})$ inside $k(X)$. See
Theorem \ref{theorem-curves-rational-maps}.

\medskip\noindent
Write $K = k(X)$. Consider the map $\text{d} : K \to \Omega_{K/k}$.
It follows from Lemma \ref{lemma-generically-etale}
that both $k(Y)$ is contained in the
kernel of $\text{d}$. By
Varieties, Lemma \ref{varieties-lemma-relative-frobenius-omega}
we see that $k(X^{(p)})$ is in the kernel of $\text{d}$.
Since $X$ is a smooth curve we know that $\Omega_{K/k}$
is a vector space of dimension $1$ over $K$.
Then More on Algebra, Lemma \ref{more-algebra-lemma-p-basis}.
implies that $\Ker(\text{d}) = kK^p$ and
that $[K : kK^p] = p$.
Thus $k(Y) = kK^p = k(X^{(p)})$ for reasons of degree.


\begin{lemma}
\label{lemma-purely-inseparable-smooth}
Let $k$ be a field of characteristic $p > 0$. Let $f : X \to Y$ be a
nonconstant morphism of proper nonsingular curves over $k$.
If $X$ is smooth and $k(Y) \subset k(X)$ is purely inseparable,
then there is a unique $n \geq 0$ and a unique isomorphism $Y = X^{(p^n)}$
such that $f$ is the $n$-fold relative Frobenius of $X/k$.
\end{lemma}

#### Proof

The $n$-fold relative Frobenius of $X/k$ is defined in
Varieties, Remark \ref{varieties-remark-n-fold-relative-frobenius}.
The lemma follows by combining Lemmas \ref{lemma-inseparable-deg-p-smooth}
and \ref{lemma-purely-inseparable}.


\begin{lemma}
\label{lemma-purely-inseparable-smooth-genus}
Let $k$ be a field of characteristic $p > 0$. Let $f : X \to Y$ be a
nonconstant morphism of proper nonsingular curves over $k$.
Assume


1.  $X$ is smooth,
1.  $H^0(X, \mathcal{O}_X) = k$,
1.  $k(X)/k(Y)$ is purely inseparable.

Then $Y$ is smooth, $H^0(Y, \mathcal{O}_Y) = k$, and the genus of $Y$
is equal to the genus of $X$.
\end{lemma}

#### Proof

By Lemma \ref{lemma-purely-inseparable-smooth}
we see that $Y = X^{(p^n)}$ is the base change of
$X$ by $F_{\Spec(k)}^n$. Thus $Y$ is smooth and the result on the
cohomology and genus follows from
Lemma \ref{lemma-genus-base-change}.


\begin{example}
\label{example-inseparable}
This example will show that the genus can change under a
purely inseparable morphism of nonsingular projective curves.
Let $k$ be a field of characteristic $3$. Assume there exists
an element $a \in k$ which is not a $3$rd power. For example
$k = \mathbf{F}_3(a)$ would work. Let $X$ be the plane curve
with homogeneous equation
$$
F = T_1^2T_0 - T_2^3 + aT_0^3
$$
as in Section \ref{section-plane-curves}.
On the affine piece $D_+(T_0)$ using coordinates $x = T_1/T_0$
and $y = T_2/T_0$ we obtain $x^2 - y^3 + a = 0$ which defines
a nonsingular affine curve. Moreover, the point at infinity
$(0 : 1: 0)$ is a smooth point. Hence $X$ is a nonsingular projective
curve of genus $1$ (Lemma \ref{lemma-genus-plane-curve}).
On the other hand, consider the morphism
$f : X \to \mathbf{P}^1_k$ which on $D_+(T_0)$ sends $(x, y)$ to
$x \in \mathbf{A}^1_k \subset \mathbf{P}^1_k$.
Then $f$ is a morphism of proper nonsingular curves over $k$
inducing an inseparable function field extension of degree $p = 3$
but the genus of $X$ is $1$ and the genus of $\mathbf{P}^1_k$ is $0$.
\end{example}

\begin{proposition}
\label{proposition-unwind-morphism-smooth}
Let $k$ be a field of characteristic $p > 0$. Let $f : X \to Y$ be a
nonconstant morphism of proper smooth curves over $k$.
Then we can factor $f$ as
$$
X \longrightarrow X^{(p^n)} \longrightarrow Y
$$
where $X^{(p^n)} \to Y$ is a nonconstant morphism of proper smooth curves
inducing a separable field extension $k(X^{(p^n)})/k(Y)$, we have
$$
X^{(p^n)} = X \times_{\Spec(k), F_{\Spec(k)}^n} \Spec(k),
$$
and $X \to X^{(p^n)}$ is the $n$-fold relative frobenius of $X$.
\end{proposition}

#### Proof

By Fields, Lemma \ref{fields-lemma-separable-first}
there is a subextension $k(X)/E/k(Y)$ such that
$k(X)/E$ is purely inseparable and $E/k(Y)$ is separable.
By Theorem \ref{theorem-curves-rational-maps}
this corresponds to a factorization
$X \to Z \to Y$ of $f$ with $Z$ a nonsingular proper curve.
Apply Lemma \ref{lemma-purely-inseparable-smooth}
to the morphism $X \to Z$ to conclude.


\begin{lemma}
\label{lemma-inseparable-linear-system}
Let $k$ be a field of characteristic $p > 0$. Let $X$ be a smooth proper
curve over $k$. Let $(\mathcal{L}, V)$ be a $\mathfrak g^r_d$ with $r \geq 1$.
Then one of the following two is true


1.  there exists a $\mathfrak g^1_d$ whose corresponding morphism
$X \to \mathbf{P}^1_k$ (Lemma \ref{lemma-linear-series})
is generically \'etale (i.e., is as in Lemma \ref{lemma-generically-etale}), or
1.  there exists a $\mathfrak g^r_{d'}$ on $X^{(p)}$ where
$d' \leq d/p$.

\end{lemma}

#### Proof

Pick two $k$-linearly independent elements $s, t \in V$.
Then $f = s/t$ is the rational function defining the morphism
$X \to \mathbf{P}^1_k$ corresponding to the linear series
$(\mathcal{L}, ks + kt)$. If this morphism is not
generically \'etale, then $f \in k(X^{(p)})$ by
Proposition \ref{proposition-unwind-morphism-smooth}.
Now choose a basis $s_0, \ldots, s_r$ of $V$ and let
$\mathcal{L}' \subset \mathcal{L}$ be the invertible sheaf
generated by $s_0, \ldots, s_r$. Set $f_i = s_i/s_0$ in $k(X)$.
If for each pair $(s_0, s_i)$ we have $f_i \in k(X^{(p)})$, then
the morphism
$$
\varphi = \varphi_{(\mathcal{L}', (s_0, \ldots, s_r)} :
X
\longrightarrow
\mathbf{P}^r_k = \text{Proj}(k[T_0, \ldots, T_r])
$$
factors through $X^{(p)}$ as this is true over the affine open
$D_+(T_0)$ and we can extend the morphism over the affine part
to the whole of the smooth curve $X^{(p)}$ by
Lemma \ref{lemma-extend-over-normal-curve}.
Introducing notation, say we have the factorization
$$
X \xrightarrow{F_{X/k}} X^{(p)} \xrightarrow{\psi} \mathbf{P}^r_k
$$
of $\varphi$. Then $\mathcal{N} = \psi^*\mathcal{O}_{\mathbf{P}^1_k}(1)$
is an invertible $\mathcal{O}_{X^{(p)}}$-module with
$\mathcal{L}' = F_{X/k}^*\mathcal{N}$ and with
$\psi^*T_0, \ldots, \psi^*T_r$ $k$-linearly independent
(as they pullback to $s_0, \ldots, s_r$ on $X$).
Finally, we have
$$
d = \deg(\mathcal{L}) \geq \deg(\mathcal{L}') =
\deg(F_{X/k}) \deg(\mathcal{N}) = p \deg(\mathcal{N})
$$
as desired. Here we used Varieties, Lemmas
\ref{varieties-lemma-check-invertible-sheaf-trivial},
\ref{varieties-lemma-degree-pullback-map-proper-curves}, and
\ref{varieties-lemma-inseparable-deg-p-smooth}.


\begin{lemma}
\label{lemma-point-over-separable-extension}
Let $k$ be a field. Let $X$ be a smooth proper curve over $k$
with $H^0(X, \mathcal{O}_X) = k$ and genus $g \geq 2$.
Then there exists a closed point $x \in X$ with
$\kappa(x)/k$ separable of degree $\leq 2g - 2$.
\end{lemma}

#### Proof

Set $\omega = \Omega_{X/k}$. By
Lemma \ref{lemma-genus-smooth} this has degree $2g - 2$
and has $g$ global sections. Thus we have a $\mathfrak g^{g - 1}_{2g - 2}$.
By the trivial Lemma \ref{lemma-linear-series-trivial-existence}
there exists a $\mathfrak g^1_{2g - 2}$
and by Lemma \ref{lemma-g1d} we obtain a morphism
$$
\varphi : X \longrightarrow \mathbf{P}^1_k
$$
of some degree $d \leq 2g - 2$. Since $\varphi$ is flat
(Lemma \ref{lemma-flat}) and finite
(Lemma \ref{lemma-finite})
it is finite locally free of degree $d$
(Morphisms, Lemma \ref{morphisms-lemma-finite-flat}).
Pick any rational point $t \in \mathbf{P}^1_k$
and any point $x \in X$ with $\varphi(x) = t$.
Then
$$
d \geq [\kappa(x) : \kappa(t)] = [\kappa(x) : k]
$$
for example by
Morphisms, Lemmas \ref{morphisms-lemma-finite-locally-free-universally-bounded}
and \ref{morphisms-lemma-characterize-universally-bounded}.
Thus if $k$ is perfect (for example has characteristic zero
or is finite) then the lemma is proved. Thus we reduce to the
case discussed in the next paragraph.

\medskip\noindent
Assume that $k$ is an infinite field of characteristic $p > 0$.
As above we will use that $X$ has a $\mathfrak g^{g - 1}_{2g - 2}$.
The smooth proper curve $X^{(p)}$ has the same genus as $X$.
Hence its genus is $> 0$. We conclude that $X^{(p)}$ does not have a
$\mathfrak g^{g - 1}_d$ for any $d \leq g - 1$ by
Lemma \ref{lemma-grd-inequalities}.
Applying Lemma \ref{lemma-inseparable-linear-system}
to our $\mathfrak g^{g - 1}_{2g - 2}$ (and noting that $2g - 2/p \leq g - 1$)
we conclude that possibility (2) does not occur. Hence we obtain a morphism
$$
\varphi : X \longrightarrow \mathbf{P}^1_k
$$
which is generically \'etale (in the sense of the lemma)
and has degree $\leq 2g - 2$. Let $U \subset X$ be the nonempty
open subscheme where $\varphi$ is \'etale. Then
$\varphi(U) \subset \mathbf{P}^1_k$ is a nonempty Zariski open
and we can pick a $k$-rational point $t \in \varphi(U)$ as $k$ is infinite.
Let $u \in U$ be a point with $\varphi(u) = t$.
Then $\kappa(u)/\kappa(t)$ is separable
(Morphisms, Lemma \ref{morphisms-lemma-etale-over-field}),
$\kappa(t) = k$, and $[\kappa(u) : k] \leq 2g - 2$ as before.


\noindent
The following lemma does not really belong in this section
but we don't know a good place for it elsewhere.

\begin{lemma}
\label{lemma-ramification-to-algebraic-closure}
Let $X$ be a smooth curve over a field $k$. Let
$\overline{x} \in X_{\overline{k}}$ be a closed
point with image $x \in X$. The ramification index of
$\mathcal{O}_{X, x} \subset \mathcal{O}_{X_{\overline{k}}, \overline{x}}$
is the inseparable degree of $\kappa(x)/k$.
\end{lemma}

#### Proof

After shrinking $X$ we may assume there is an \'etale morphism
$\pi : X \to \mathbf{A}^1_k$, see
Morphisms, Lemma \ref{morphisms-lemma-smooth-etale-over-affine-space}.
Then we can consider the diagram of local rings
$$
\xymatrix{
\mathcal{O}_{X_{\overline{k}}, \overline{x}} &
\mathcal{O}_{\mathbf{A}^1_{\overline{k}}, \pi(\overline{x})} \ar[l] \\\\
\mathcal{O}_{X, x} \ar[u] &
\mathcal{O}_{\mathbf{A}^1_k, \pi(x)} \ar[l] \ar[u]
}
$$
The horizontal arrows have ramification index $1$ as they correspond to
\'etale morphisms. Moreover, the extension $\kappa(x)/\kappa(\pi(x))$ is
separable hence $\kappa(x)$ and $\kappa(\pi(x))$ have the same
inseparable degree over $k$.
By multiplicativity of ramification indices it suffices to
prove the result when $x$ is a point of the affine line.

\medskip\noindent
Assume $X = \mathbf{A}^1_k$. In this case, the local ring of $X$ at $x$
looks like
$$
\mathcal{O}_{X, x} = k[t]_{(P)}
$$
where $P$ is an irreducible monic polynomial over $k$.
Then $P(t) = Q(t^q)$ for some separable polynomial $Q \in k[t]$, see
Fields, Lemma \ref{fields-lemma-irreducible-polynomials}.
Observe that $\kappa(x) = k[t]/(P)$ has inseparable degree $q$
over $k$. On the other hand, over $\overline{k}$ we can factor
$Q(t) = \prod (t - \alpha_i)$ with $\alpha_i$ pairwise distinct.
Write $\alpha_i = \beta_i^q$ for some unique $\beta_i \in \overline{k}$.
Then our point $\overline{x}$ corresponds to one of the $\beta_i$
and we conclude because the ramification index of
$$
k[t]_{(P)} \longrightarrow \overline{k}[t]_{(t - \beta_i)}
$$
is indeed equal to $q$ as the uniformizer $P$ maps to
$(t - \beta_i)^q$ times a unit.






###  Pushouts

\label{section-pushouts}

\noindent
Let $k$ be a field. Consider a solid diagram
$$
\xymatrix{
Z' \ar[d] \ar[r]_{i'} & X' \ar@{..>}[d]^a \\\\
Z \ar@{..>}[r]^i & X
}
$$
of schemes over $k$ satisfying


1. [(a)] $X'$ is separated of finite type over $k$ of dimension $\leq 1$,
1. [(b)] $i : Z' \to X'$ is a closed immersion,
1. [(c)] $Z'$ and $Z$ are finite over $\Spec(k)$, and
1. [(d)] $Z' \to Z$ is surjective.

In this situation every finite set of points of $X'$ are contained
in an affine open, see Varieties, Proposition
\ref{varieties-proposition-finite-set-of-points-of-codim-1-in-affine}.
Thus the assumptions of
More on Morphisms, Proposition
\ref{more-morphisms-proposition-pushout-along-closed-immersion-and-integral}
are satisfied and we obtain the following


1.  the pushout $X = Z \amalg_{Z'} X'$ exists in the category of schemes,
1.  $i : Z \to X$ is a closed immersion,
1.  $a : X' \to X$ is integral surjective,
1.  $X \to \Spec(k)$ is separated by More on Morphisms, Lemma
\ref{more-morphisms-lemma-pushout-separated}
1.  $X \to \Spec(k)$ is of finite type by
More on Morphisms, Lemmas \ref{more-morphisms-lemma-pushout-finite-type},
1.  thus $a : X' \to X$ is finite by
Morphisms, Lemmas \ref{morphisms-lemma-finite-integral} and
\ref{morphisms-lemma-permanence-finite-type},
1.  if $X' \to \Spec(k)$ is proper, then $X \to \Spec(k)$ is proper
by Morphisms, Lemma \ref{morphisms-lemma-image-proper-is-proper}.


\noindent
The following lemma can be generalized significantly.

\begin{lemma}
\label{lemma-complete-local-ring-pushout}
In the situation above, let $Z = \Spec(k')$ where $k'$ is a field and
$Z' = \Spec(k'_1 \times \ldots \times k'_n)$ with $k'_i/k'$
finite extensions of fields. Let $x \in X$ be the image of $Z \to X$
and $x'_i \in X'$ the image of $\Spec(k'_i) \to X'$.
Then we have a fibre product diagram
$$
\xymatrix{
\prod\nolimits_{i = 1, \ldots, n} k'_i &
\prod\nolimits_{i = 1, \ldots, n} \mathcal{O}_{X', x'_i}^\wedge \ar[l] \\\\
k' \ar[u] &
\mathcal{O}_{X, x}^\wedge \ar[u] \ar[l]
}
$$
where the horizontal arrows are given by the maps to the residue fields.
\end{lemma}

#### Proof

Choose an affine open neighbourhood $\Spec(A)$ of $x$ in $X$.
Let $\Spec(A') \subset X'$ be the inverse image. By construction
we have a fibre product diagram
$$
\xymatrix{
\prod\nolimits_{i = 1, \ldots, n} k'_i &
A' \ar[l] \\\\
k' \ar[u] &
A \ar[u] \ar[l]
}
$$
Since everything is finite over $A$ we see that the diagram remains
a fibre product diagram after completion with respect to the
maximal ideal $\mathfrak m \subset A$ corresponding to $x$
(Algebra, Lemma \ref{algebra-lemma-completion-flat}).
Finally, apply Algebra, Lemma
\ref{algebra-lemma-completion-finite-extension}
to identify the completion of $A'$.





###  Glueing and squishing

\label{section-glueing-squishing}

\noindent
Below we will indicate $k[\epsilon]$ the algebra of dual numbers
over $k$ as defined in
Varieties, Definition \ref{varieties-definition-dual-numbers}.

\begin{lemma}
\label{lemma-no-in-between-over-k}
Let $k$ be an algebraically closed field. Let $k \subset A$ be a ring
extension such that $A$ has exactly two $k$-sub algebras, then
either $A = k \times k$ or $A = k[\epsilon]$.
\end{lemma}

#### Proof

The assumption means $k \not = A$ and any subring $k \subset C \subset A$
is equal to either $k$ or $A$. Let $t \in A$, $t \not \in k$.
Then $A$ is generated by $t$ over $k$. Hence $A = k[x]/I$ for some
ideal $I$. If $I = (0)$, then we have the subalgebra $k[x^2]$
which is not allowed. Otherwise $I$ is generated by a monic polynomial $P$.
Write $P = \prod_{i = 1}^d (t - a_i)$. If $d > 2$, then the subalgebra
generated by $(t - a_1)(t - a_2)$ gives a contradiction.
Thus $d = 2$. If $a_1 \not = a_2$, then $A = k \times k$,
if $a_1 = a_2$, then $A = k[\epsilon]$.


\begin{example}[Glueing points]
\label{example-glue-points}
Let $k$ be an algebraically closed field. Let $f : X' \to X$
be a morphism of algebraic $k$-schemes. We say $X$ is
obtained by glueing $a$ and $b$ in $X'$ if the following are true:


1.  $a, b \in X'(k)$ are distinct points which map to the same
point $x \in X(k)$,
1.  $f$ is finite and
$f^{-1}(X \setminus \{x\}) \to X \setminus \{x\}$ is an isomorphism,
1.  there is a short exact sequence
$$
0 \to \mathcal{O}_X \to f_*\mathcal{O}_{X'} \xrightarrow{a - b} x_*k \to 0
$$
where arrow on the right sends a local section $h$ of $f_*\mathcal{O}_{X'}$
to the difference $h(a) - h(b) \in k$.

If this is the case, then there also is a short exact sequence
$$
0 \to \mathcal{O}_X^* \to f_*\mathcal{O}_{X'}^*
\xrightarrow{ab^{-1}} x_*k^* \to 0
$$
where arrow on the right sends a local section $h$ of $f_*\mathcal{O}_{X'}^*$
to the multiplicative difference $h(a)h(b)^{-1} \in k^*$.
\end{example}

\begin{example}[Squishing a tangent vector]
\label{example-squish-tangent-vector}
Let $k$ be an algebraically closed field. Let $f : X' \to X$
be a morphism of algebraic $k$-schemes. We say $X$ is
obtained by squishing the tangent vector $\vartheta$ in $X'$
if the following are true:


1.  $\vartheta : \Spec(k[\epsilon]) \to X'$ is a closed immersion
over $k$ such that $f \circ \vartheta$ factors through a point $x \in X(k)$,
1.  $f$ is finite and
$f^{-1}(X \setminus \{x\}) \to X \setminus \{x\}$ is an isomorphism,
1.  there is a short exact sequence
$$
0 \to \mathcal{O}_X \to f_*\mathcal{O}_{X'} \xrightarrow{\vartheta} x_*k \to 0
$$
where arrow on the right sends a local section $h$ of $f_*\mathcal{O}_{X'}$
to the coefficient of $\epsilon$ in $\vartheta^\sharp(h) \in k[\epsilon]$.

If this is the case, then there also is a short exact sequence
$$
0 \to \mathcal{O}_X^* \to f_*\mathcal{O}_{X'}^*
\xrightarrow{\vartheta} x_*k \to 0
$$
where arrow on the right sends a local section $h$ of $f_*\mathcal{O}_{X'}^*$
to $\text{d}\log(\vartheta^\sharp(h))$ where
$\text{d}\log : k[\epsilon]^* \to k$
is the homomorphism of abelian groups sending $a + b\epsilon$ to $b/a \in k$.
\end{example}

\begin{lemma}
\label{lemma-factor-almost-isomorphism}
Let $k$ be an algebraically closed field. Let $f : X' \to X$ be a
finite morphism algebraic $k$-schemes such that
$\mathcal{O}_X \subset f_*\mathcal{O}_{X'}$ and such that $f$ is an
isomorphism away from a finite set of points. Then there is a factorization
$$
X' = X_n \to X_{n - 1} \to \ldots \to X_1 \to X_0 = X
$$
such that each $X_i \to X_{i - 1}$ is either the glueing of
two points or the squishing of a tangent vector
(see Examples \ref{example-glue-points} and
\ref{example-squish-tangent-vector}).
\end{lemma}

#### Proof

Let $U \subset X$ be the maximal open set over which $f$ is an isomorphism.
Then $X \setminus U = \{x_1, \ldots, x_n\}$ with $x_i \in X(k)$.
We will consider factorizations $X' \to Y \to X$ of $f$ such that
both morphisms are finite and
$$
\mathcal{O}_X \subset g_*\mathcal{O}_Y \subset f_*\mathcal{O}_{X'}
$$
where $g : Y \to X$ is the given morphism. By assumption
$\mathcal{O}_{X, x} \to (f_*\mathcal{O}_{X'})_x$ is an isomorphism
onless $x = x_i$ for some $i$. Hence the cokernel
$$
f_*\mathcal{O}_{X'}/\mathcal{O}_X = \bigoplus \mathcal{Q}_i
$$
is a direct sum of skyscraper sheaves $\mathcal{Q}_i$ supported at
$x_1, \ldots, x_n$.
Because the displayed quotient is a coherent $\mathcal{O}_X$-module,
we conclude that $\mathcal{Q}_i$ has finite length over
$\mathcal{O}_{X, x_i}$. Hence we can argue
by induction on the sum of these lengths, i.e., the length of
the whole cokernel.

\medskip\noindent
If $n > 1$, then we can define an $\mathcal{O}_X$-subalgebra
$\mathcal{A} \subset f_*\mathcal{O}_{X'}$ by taking the inverse
image of $\mathcal{Q}_1$. This will give a nontrivial factorization
and we win by induction.

\medskip\noindent
Assume $n = 1$. We abbreviate $x = x_1$. Consider the finite
$k$-algebra extension
$$
A = \mathcal{O}_{X, x} \subset (f_*\mathcal{O}_{X'})_x = B
$$
Note that $\mathcal{Q} = \mathcal{Q}_1$ is the skyscraper sheaf
with value $B/A$.
We have a $k$-subalgebra $A \subset A + \mathfrak m_A B \subset B$.
If both inclusions are strict, then we obtain a nontrivial
factorization and we win by induction as above.
If $A + \mathfrak m_A B = B$, then $A = B$ by Nakayama, then
$f$ is an isomorphism and there is nothing to prove.
We conclude that we may assume $B = A + \mathfrak m_A B$.
Set $C = B/\mathfrak m_A B$. If $C$ has more than $2$
$k$-subalgebras, then we obtain a subalgebra between $A$
and $B$ by taking the inverse image in $B$. Thus we may
assume $C$ has exactly $2$ $k$-subalgebras. Thus $C = k \times k$
or $C = k[\epsilon]$ by Lemma \ref{lemma-no-in-between-over-k}.
In this case $f$ is correspondingly the glueing two points or the
squishing of a tangent vector.


\begin{lemma}
\label{lemma-glue-points}
Let $k$ be an algebraically closed field. If $f : X' \to X$ is the
glueing of two points $a, b$ as in Example \ref{example-glue-points}, then
there is an exact sequence
$$
k^* \to \Pic(X) \to \Pic(X') \to 0
$$
The first map is zero if $a$ and $b$ are on different
connected components of $X'$ and injective
if $X'$ is proper and $a$ and $b$ are on the same connected component of $X'$.
\end{lemma}

#### Proof

The map $\Pic(X) \to \Pic(X')$ is surjective
by Varieties, Lemma \ref{varieties-lemma-surjective-pic-birational-finite}.
Using the short exact sequence
$$
0 \to \mathcal{O}_X^* \to f_*\mathcal{O}_{X'}^*
\xrightarrow{ab^{-1}} x_*k^* \to 0
$$
we obtain
$$
H^0(X', \mathcal{O}_{X'}^*) \xrightarrow{ab^{-1}} k^* \to
H^1(X, \mathcal{O}_X^*) \to H^1(X, f_*\mathcal{O}_{X'}^*)
$$
We have $H^1(X, f_*\mathcal{O}_{X'}^*) \subset H^1(X', \mathcal{O}_{X'}^*)$
(for example by the Leray spectral sequence, see
Cohomology, Lemma \ref{cohomology-lemma-Leray}).
Hence the kernel of $\Pic(X) \to \Pic(X')$ is the
cokernel of $ab^{-1} : H^0(X', \mathcal{O}_{X'}^*) \to k^*$.
If $a$ and $b$ are on different connected components of $X'$,
then $ab^{-1}$ is surjective.
Because $k$ is algebraically closed any regular function on a
reduced connected proper scheme over $k$ comes from an element of $k$, see
Varieties, Lemma
\ref{varieties-lemma-proper-geometrically-reduced-global-sections}.
Thus $ab^{-1}$ is zero if $X'$ is proper and $a$ and $b$ are on
the same connected component.


\begin{lemma}
\label{lemma-squish-tangent-vector}
Let $k$ be an algebraically closed field. If $f : X' \to X$ is the
squishing of a tangent vector $\vartheta$ as in
Example \ref{example-squish-tangent-vector}, then
there is an exact sequence
$$
(k, +) \to \Pic(X) \to \Pic(X') \to 0
$$
and the first map is injective if $X'$ is proper and reduced.
\end{lemma}

#### Proof

The map $\Pic(X) \to \Pic(X')$ is surjective
by Varieties, Lemma \ref{varieties-lemma-surjective-pic-birational-finite}.
Using the short exact sequence
$$
0 \to \mathcal{O}_X^* \to f_*\mathcal{O}_{X'}^*
\xrightarrow{\vartheta} x_*k \to 0
$$
of Example \ref{example-squish-tangent-vector} we obtain
$$
H^0(X', \mathcal{O}_{X'}^*) \xrightarrow{\vartheta} k \to
H^1(X, \mathcal{O}_X^*) \to H^1(X, f_*\mathcal{O}_{X'}^*)
$$
We have $H^1(X, f_*\mathcal{O}_{X'}^*) \subset H^1(X', \mathcal{O}_{X'}^*)$
(for example by the Leray spectral sequence, see
Cohomology, Lemma \ref{cohomology-lemma-Leray}).
Hence the kernel of $\Pic(X) \to \Pic(X')$ is the
cokernel of the map $\vartheta : H^0(X', \mathcal{O}_{X'}^*) \to k$.
Because $k$ is algebraically closed any regular function on a
reduced connected proper scheme over $k$ comes from an element of $k$, see
Varieties, Lemma
\ref{varieties-lemma-proper-geometrically-reduced-global-sections}.
Thus the final statement of the lemma.



###  Multicross and nodal singularities

\label{section-multicross}

\noindent
In this section we discuss the simplest possible curve singularities.

\medskip\noindent
Let $k$ be a field. Consider the complete local $k$-algebra
\begin{equation}
\label{equation-multicross}
A = \{(f_1, \ldots, f_n) \in k[[t]] \times \ldots \times k[[t]] \mid
f_1(0) = \ldots = f_n(0)\}
\end{equation}
In the language introduced in
Varieties, Definition \ref{varieties-definition-wedge}
we see that $A$ is a wedge of $n$ copies of the power series
ring in $1$ variable over $k$. Observe that
$k[[t]] \times \ldots \times k[[t]]$
is the integral closure of $A$ in its total ring of fractions.
Hence the $\delta$-invariant of $A$ is $n - 1$.
There is an isomorphism
$$
k[[x_1, \ldots, x_n]]/(\{x_ix_j\}_{i \not = j}) \longrightarrow A
$$
obtained by sending $x_i$ to $(0, \ldots, 0, t, 0, \ldots, 0)$
in $A$. It follows that $\dim(A) = 1$ and
$\dim_k \mathfrak m/\mathfrak m^2 = n$.
In particular, $A$ is regular if and only if $n = 1$.

\begin{lemma}
\label{lemma-multicross-algebra}
Let $k$ be a separably closed field. Let $A$ be a $1$-dimensional
reduced Nagata local $k$-algebra with residue field $k$. Then
$$
\delta\text{-invariant }A \geq \text{number of branches of }A - 1
$$
If equality holds, then $A^\wedge$ is as in (\ref{equation-multicross}).
\end{lemma}

#### Proof

Since the residue field of $A$ is separably closed, the number
of branches of $A$ is equal to the number of geometric branches
of $A$, see
More on Algebra, Definition \ref{more-algebra-definition-number-of-branches}.
The inequality holds by
Varieties, Lemma \ref{varieties-lemma-delta-number-branches-inequality}.
Assume equality holds.
We may replace $A$ by the completion of $A$; this does
not change the number of branches or the $\delta$-invariant, see
More on Algebra, Lemma
\ref{more-algebra-lemma-one-dimensional-number-of-branches}
and Varieties, Lemma \ref{varieties-lemma-delta-same-after-completion}.
Then $A$ is strictly henselian, see
Algebra, Lemma \ref{algebra-lemma-complete-henselian}.
By Varieties, Lemma \ref{varieties-lemma-delta-number-branches-inequality-sh}
we see that $A$ is a wedge of complete discrete valuation rings.
Each of these is isomorphic to $k[[t]]$ by Algebra, Lemma
\ref{algebra-lemma-regular-complete-containing-coefficient-field}.
Hence $A$ is as in (\ref{equation-multicross}).


\begin{definition}
\label{definition-multicross}
Let $k$ be an algebraically closed field. Let $X$ be an algebraic
$1$-dimensional $k$-scheme. Let $x \in X$ be a closed point.
We say $x$ defines a {\it multicross singularity} if the completion
$\mathcal{O}_{X, x}^\wedge$
is isomorphic to (\ref{equation-multicross}) for some $n \geq 2$.
We say $x$ is a {\it node}, or an {\it ordinary double point}, or
{\it defines a nodal singularity} if $n = 2$.
\end{definition}

\noindent
These singularities are in some sense the simplest kind of singularities
one can have on a curve over an algebraically closed field.

\begin{lemma}
\label{lemma-multicross}
Let $k$ be an algebraically closed field. Let $X$ be a reduced algebraic
$1$-dimensional $k$-scheme. Let $x \in X$. The following are equivalent


1.  $x$ defines a multicross singularity,
1.  the $\delta$-invariant of $X$ at $x$ is the
number of branches of $X$ at $x$ minus $1$,
1.  there is a sequence of morphisms
$U_n \to U_{n - 1} \to \ldots \to U_0 = U \subset X$
where $U$ is an open neighbourhood of $x$, where
$U_n$ is nonsingular, and where each $U_i \to U_{i - 1}$
is the glueing of two points as in Example \ref{example-glue-points}.

\end{lemma}

#### Proof

The equivalence of (1) and (2) is Lemma \ref{lemma-multicross-algebra}.

\medskip\noindent
Assume (3). We will argue by descending induction on $i$ that all singularities
of $U_i$ are multicross. This is true for $U_n$ as $U_n$ has no singular points.
If $U_i$ is gotten from $U_{i + 1}$ by glueing $a, b \in U_{i + 1}$
to a point $c \in U_i$, then we see that
$$
\mathcal{O}_{U_i, c}^\wedge \subset
\mathcal{O}_{U_{i + 1}, a}^\wedge \times \mathcal{O}_{U_{i + 1}, b}^\wedge
$$
is the set of elements having the same residue classes in $k$.
Thus the number of branches at $c$ is the sum of the number of
branches at $a$ and $b$, and the $\delta$-invariant at $c$
is the sum of the $\delta$-invariants at $a$ and $b$ plus $1$
(because the displayed inclusion has codimension $1$).
This proves that (2) holds as desired.

\medskip\noindent
Assume the equivalent conditions (1) and (2). We may choose an open
$U \subset X$ such that $x$ is the only singular point of $U$.
Then we apply Lemma \ref{lemma-factor-almost-isomorphism} to
the normalization morphism
$$
U^\nu = U_n \to U_{n - 1} \to \ldots \to U_1 \to U_0 = U
$$
All we have to do is show that in none of the steps we are
squishing a tangent vector. Suppose $U_{i + 1} \to U_i$ is the
smallest $i$ such that this is the squishing of a tangent
vector $\theta$ at $u' \in U_{i + 1}$ lying over $u \in U_i$.
Arguing as above, we see that $u_i$ is a multicross singularity
(because the maps $U_i \to \ldots \to U_0$ are glueing of
pairs of points). But now the number of branches at $u'$ and $u$
is the same and the $\delta$-invariant of $U_i$ at $u$
is $1$ bigger than the $\delta$-invariant of $U_{i + 1}$ at $u'$.
By Lemma \ref{lemma-multicross-algebra}
this implies that $u$ cannot be a multicross singularity which
is a contradiction.


\begin{lemma}
\label{lemma-multicross-gorenstein-is-nodal}
Let $k$ be an algebraically closed field. Let $X$ be a reduced algebraic
$1$-dimensional $k$-scheme. Let $x \in X$ be a multicross singularity
(Definition \ref{definition-multicross}).
If $X$ is Gorenstein, then $x$ is a node.
\end{lemma}

#### Proof

The map $\mathcal{O}_{X, x} \to \mathcal{O}_{X, x}^\wedge$
is flat and unramified in the sense that
$\kappa(x) = \mathcal{O}_{X, x}^\wedge/\mathfrak m_x \mathcal{O}_{X, x}^\wedge$.
(See More on Algebra, Section \ref{more-algebra-section-permanence-completion}.)
Thus $X$ is Gorenstein implies $\mathcal{O}_{X, x}$ is Gorenstein, implies
$\mathcal{O}_{X, x}^\wedge$ is Gorenstein by
Dualizing Complexes, Lemma \ref{dualizing-lemma-flat-under-gorenstein}.
Thus it suffices to show that the ring $A$ in
(\ref{equation-multicross}) with $n \geq 2$
is Gorenstein if and only if $n = 2$.

\medskip\noindent
If $n = 2$, then $A = k[[x, y]]/(xy)$ is a complete intersection
and hence Gorenstein. For example this follows from
Duality for Schemes, Lemma \ref{duality-lemma-gorenstein-lci}
applied to $k[[x, y]] \to A$ and the fact that the regular
local ring $k[[x, y]]$ is Gorenstein by
Dualizing Complexes, Lemma \ref{dualizing-lemma-regular-gorenstein}.

\medskip\noindent
Assume $n > 2$. If $A$ where Gorenstein, then $A$ would be a
dualizing complex over $A$
(Duality for Schemes, Definition \ref{duality-definition-gorenstein}).
Then $R\Hom(k, A)$ would be equal to $k[n]$ for some $n \in \mathbf{Z}$, see
Dualizing Complexes, Lemma \ref{dualizing-lemma-find-function}.
It would follow that $\Ext^1_A(k, A) \cong k$
or $\Ext^1_A(k, A) = 0$ (depending on the value of $n$;
in fact $n$ has to be $-1$ but it doesn't matter to us here).
Using the exact sequence
$$
0 \to \mathfrak m_A \to A \to k \to 0
$$
we find that
$$
\Ext^1_A(k, A) = \Hom_A(\mathfrak m_A, A)/A
$$
where $A \to \Hom_A(\mathfrak m_A, A)$ is given by
$a \mapsto (a' \mapsto aa')$. Let $e_i \in \Hom_A(\mathfrak m_A, A)$
be the element that sends $(f_1, \ldots, f_n) \in \mathfrak m_A$ to
$(0, \ldots, 0, f_i, 0, \ldots, 0)$. The reader verifies easily
that $e_1, \ldots, e_{n - 1}$ are $k$-linearly independent in
$\Hom_A(\mathfrak m_A, A)/A$. Thus
$\dim_k \Ext^1_A(k, A) \geq n - 1 \geq 2$ which
finishes the proof.
(Observe that $e_1 + \ldots + e_n$ is the image of $1$ under the map
$A \to \Hom_A(\mathfrak m_A, A)$.)





###  Torsion in the Picard group

\label{section-torsion-in-pic}

\noindent
In this section we bound the torsion in the Picard group of a $1$-dimensional
proper scheme over a field. We will use this in our
study of semistable reduction for curves.

\medskip\noindent
There does not seem to be an elementary way to obtain the result of
Lemma \ref{lemma-torsion-picard-smooth-projective}.
Analyzing the proof there are two key ingredients:
(1) there is an abelian variety classifying degree zero invertible sheaves on
a smooth projective curve and (2) the structure of torsion points on
an abelian variety can be determined.

\begin{lemma}
\label{lemma-torsion-picard-smooth-projective}
Let $k$ be an algebraically closed field.
Let $X$ be a smooth projective curve of genus $g$ over $k$.


1.  If $n \geq 1$ is invertible in $k$, then
$\Pic(X)[n] \cong (\mathbf{Z}/n\mathbf{Z})^{\oplus 2g}$.
1.  If the characteristic of $k$ is $p > 0$, then there exists
an integer $0 \leq f \leq g$ such that
$\Pic(X)[p^m] \cong (\mathbf{Z}/p^m\mathbf{Z})^{\oplus f}$ for
all $m \geq 1$.

\end{lemma}

#### Proof

Let $\Pic^0(X) \subset \Pic(X)$
denote the subgroup of invertible sheaves of degree $0$.
In other words, there is a short exact sequence
$$
0 \to \Pic^0(X) \to \Pic(X) \xrightarrow{\deg} \mathbf{Z} \to 0.
$$
The group $\Pic^0(X)$ is the $k$-points of
the group scheme $\underline{\Picardfunctor}^0_{X/k}$, see
Picard Schemes of Curves, Lemma \ref{pic-lemma-picard-pieces}.
The same lemma tells us that $\underline{\Picardfunctor}^0_{X/k}$
is a $g$-dimensional abelian variety over $k$ as defined in
Groupoids, Definition \ref{groupoids-definition-abelian-variety}.
Thus we conclude by the results of
Groupoids, Proposition \ref{groupoids-proposition-review-abelian-varieties}.


\begin{lemma}
\label{lemma-torsion-picard-becomes-visible}
Let $k$ be a field. Let $n$ be prime to the characteristic of $k$.
Let $X$ be a smooth proper curve over $k$ with $H^0(X, \mathcal{O}_X) = k$
and of genus $g$.


1.  If $g = 1$ then there exists a finite separable extension
$k'/k$ such that $X_{k'}$ has a $k'$-rational point and
$\Pic(X_{k'})[n] \cong (\mathbf{Z}/n\mathbf{Z})^{\oplus 2}$.
1.  If $g \geq 2$ then there exists a finite separable extension
$k'/k$ with $[k' : k] \leq (2g - 2)(n^{2g})!$
such that $X_{k'}$ has a $k'$-rational point and
$\Pic(X_{k'})[n] \cong (\mathbf{Z}/n\mathbf{Z})^{\oplus 2g}$.

\end{lemma}

#### Proof

Assume $g \geq 2$. First we may choose a finite separable extension
of degree at most $2g - 2$ such that $X$ acquires a rational point, see
Lemma \ref{lemma-point-over-separable-extension}.
Thus we may assume $X$ has a $k$-rational point $x \in X(k)$
but now we have to prove the lemma with
$[k' : k] \leq (n^{2g})!$.
Let $k \subset k^{sep} \subset \overline{k}$ be a separable algebraic
closure inside an algebraic closure.
By Lemma \ref{lemma-torsion-picard-smooth-projective} we have
$$
\Pic(X_{\overline{k}})[n] \cong (\mathbf{Z}/n\mathbf{Z})^{\oplus 2g}
$$
By Picard Schemes of Curves, Lemma \ref{pic-lemma-torsion-descends}
we conclude that
$$
\Pic(X_{k^{sep}})[n] \cong (\mathbf{Z}/n\mathbf{Z})^{\oplus 2g}
$$
By Picard Schemes of Curves, Lemma \ref{pic-lemma-torsion-descends}
there is a continuous action
$$
\text{Gal}(k^{sep}/k)
\longrightarrow
\text{Aut}(\Pic(X_{k^{sep}})[n]
$$
and the lemma is true for the fixed field $k'$ of the kernel of this map.
The kernel is open because the action is continuous which implies
that $k'/k$ is finite. By Galois theory $\text{Gal}(k'/k)$
is the image of the displayed arrow. Since the permutation
group of a set of cardinality $n^{2g}$ has cardinality $(n^{2g})!$
we conclude by Galois theory that $[k' : k] \leq (n^{2g})!$.
(Of course this proves the lemma with the bound
$|\text{GL}_{2g}(\mathbf{Z}/n\mathbf{Z})|$, but all we want
here is that there is some bound.)

\medskip\noindent
If the genus is $1$, then there is no upper bound on the degree of a
finite separable field extension over which $X$ acquires a rational point
(details omitted). Still, there is such an extension for example by
Varieties, Lemma \ref{varieties-lemma-smooth-separable-closed-points-dense}.
The rest of the proof is the same as in the case of $g \geq 2$.


\begin{proposition}
\label{proposition-torsion-picard-reduced-proper}
Let $k$ be an algebraically closed field. Let $X$ be a proper scheme over $k$
which is reduced, connected, and has dimension $1$. Let $g$ be the genus
of $X$ and let $g_{geom}$ be the sum of the geometric genera of the
irreducible components of $X$. For any prime $\ell$ different from
the characteristic of $k$ we have
$$
\dim_{\mathbf{F}_\ell} \Pic(X)[\ell]
\leq g + g_{geom}
$$
and equality holds if and only if all the singularities of $X$
are multicross.
\end{proposition}

#### Proof

Let $\nu : X^\nu \to X$ be the normalization
(Varieties, Lemma \ref{varieties-lemma-prepare-delta-invariant}).
Choose a factorization
$$
X^\nu = X_n \to X_{n - 1} \to \ldots \to X_1 \to X_0 = X
$$
as in Lemma \ref{lemma-factor-almost-isomorphism}.
Let us denote $h^0_i = \dim_k H^0(X_i, \mathcal{O}_{X_i})$
and $h^1_i = \dim_k H^1(X_i, \mathcal{O}_{X_i})$.
By Lemmas \ref{lemma-glue-points} and \ref{lemma-squish-tangent-vector}
for each $n > i \geq 0$ we have
one of the following there possibilities


1.  $X_i$ is obtained by glueing $a, b \in X_{i + 1}$
which are on different connected components: in this case
$\Pic(X_i) = \Pic(X_{i + 1})$,
$h^0_{i + 1} = h^0_i + 1$, $h^1_{i + 1} = h^1_i$,
1.  $X_i$ is obtained by glueing $a, b \in X_{i + 1}$
which are on the same connected component: in this case
there is a short exact sequence
$$
0 \to k^* \to \Pic(X_i) \to \Pic(X_{i + 1}) \to 0,
$$
and $h^0_{i + 1} = h^0_i$, $h^1_{i + 1} = h^1_i - 1$,
1.  $X_i$ is obtained by squishing a tangent vector in $X_{i + 1}$:
in this case there is a short exact sequence
$$
0 \to (k, +) \to \Pic(X_i) \to \Pic(X_{i + 1}) \to 0,
$$
and $h^0_{i + 1} = h^0_i$, $h^1_{i + 1} = h^1_i - 1$.

To prove the statements on dimensions of cohomology groups of the
structure sheaf, use the exact sequences in
Examples \ref{example-glue-points} and \ref{example-squish-tangent-vector}.
Since $k$ is algebraically closed of characteristic prime to $\ell$
we see that $(k, +)$ and $k^*$ are $\ell$-divisible and with
$\ell$-torsion $(k, +)[\ell] = 0$ and $k^*[\ell] \cong \mathbf{F}_\ell$.
Hence
$$
\dim_{\mathbf{F}_\ell} \Pic(X_{i + 1})[\ell] -
\dim_{\mathbf{F}_\ell}\Pic(X_i)[\ell]
$$
is zero, except in case (2) where it is equal to $-1$.
At the end of this process we get the normalization
$X^\nu = X_n$ which is a disjoint union of smooth projective
curves over $k$. Hence we have


1.  $h^1_n = g_{geom}$ and
1.  $\dim_{\mathbf{F}_\ell} \Pic(X_n)[\ell] = 2g_{geom}$.

The last equality by Lemma \ref{lemma-torsion-picard-smooth-projective}.
Since $g = h^1_0$ we see that the number of steps of type
(2) and (3) is at most $h^1_0 - h^1_n = g - g_{geom}$.
By our comptation of the differences in ranks we conclude that
$$
\dim_{\mathbf{F}_\ell} \Pic(X)[\ell] \leq
g - g_{geom} + 2g_{geom} = g + g_{geom}
$$
and equality holds if and only if no steps of type (3) occur.
This indeed means that all singularities of $X$ are multicross
by Lemma \ref{lemma-multicross}. Conversely, if all the singularities
are multicross, then Lemma \ref{lemma-multicross} guarantees that
we can find a sequence $X^\nu = X_n \to \ldots \to X_0 = X$
as above such that no steps of type (3) occur in the sequence
and we find equality holds in the lemma (just glue the local sequences
for each point to find one that works for all singular points of $x$;
some details omitted).






###  Genus versus geometric genus

\label{section-genus-geometric-genus}

\noindent
Let $k$ be a field with algebraic closure $\overline{k}$.
Let $X$ be a proper scheme of dimension $\leq 1$ over $k$.
We define $g_{geom}(X/k)$ to be the sum of the geometric genera
of the irreducible components of $X_{\overline{k}}$ which have dimension $1$.

\begin{lemma}
\label{lemma-bound-geometric-genus}
Let $k$ be a field. Let $X$ be a proper scheme of dimension $\leq 1$ over $k$.
Then
$$
g_{geom}(X/k) = \sum\nolimits_{C \subset X} g_{geom}(C/k)
$$
where the sum is over irreducible components $C \subset X$ of dimension $1$.
\end{lemma}

#### Proof

This is immediate from the definition and the fact that an irreducible
component $\overline{Z}$ of $X_{\overline{k}}$ maps onto an
irreducible component $Z$ of $X$
(Varieties, Lemma \ref{varieties-lemma-image-irreducible})
of the same dimension
(Morphisms, Lemma \ref{morphisms-lemma-dimension-fibre-after-base-change}
applied to the generic point of $\overline{Z}$).


\begin{lemma}
\label{lemma-geometric-genus-normalization}
Let $k$ be a field. Let $X$ be a proper scheme of dimension $\leq 1$ over $k$.
Then


1.  We have $g_{geom}(X/k) = g_{geom}(X_{red}/k)$.
1.  If $X' \to X$ is a birational proper morphism, then
$g_{geom}(X'/k) = g_{geom}(X/k)$.
1.  If $X^\nu \to X$ is the normalization morphism, then
$g_{geom}(X^\nu/k) = g_{geom}(X/k)$.

\end{lemma}

#### Proof

Part (1) is immediate from Lemma \ref{lemma-bound-geometric-genus}.
If $X' \to X$ is proper birational, then it is finite and
an isomorphism over a dense open (see
Varieties, Lemmas \ref{varieties-lemma-finite-in-codim-1} and
\ref{varieties-lemma-modification-normal-iso-over-codimension-1}).
Hence $X'_{\overline{k}} \to X_{\overline{k}}$ is an isomorphism
over a dense open. Thus the irreducible components of $X'_{\overline{k}}$
and $X_{\overline{k}}$ are in bijective correspondence and the
corresponding components have isomorphic function fields.
In particular these components have isomorphic nonsingular projective models
and hence have the same geometric genera.
This proves (2).
Part (3) follows from (1) and (2) and the fact that
$X^\nu \to X_{red}$ is birational
(Morphisms, Lemma \ref{morphisms-lemma-normalization-birational}).


\begin{lemma}
\label{lemma-genus-goes-down}
Let $k$ be a field. Let $X$ be a proper scheme of dimension
$\leq 1$ over $k$. Let $f : Y \to X$ be a finite morphism
such that there exists a dense open $U \subset X$ over
which $f$ is a closed immersion. Then
$$
\dim_k H^1(X, \mathcal{O}_X) \geq \dim_k H^1(Y, \mathcal{O}_Y)
$$
\end{lemma}

#### Proof

Consider the exact sequence
$$
0 \to \mathcal{G} \to \mathcal{O}_X \to f_*\mathcal{O}_Y \to \mathcal{F} \to 0
$$
of coherent sheaves on $X$.
By assumption $\mathcal{F}$ is supported in finitely many closed points
and hence has vanishing higher cohomology
(Varieties, Lemma \ref{varieties-lemma-chi-tensor-finite}).
On the other hand, we have $H^2(X, \mathcal{G}) = 0$ by
Cohomology, Proposition \ref{cohomology-proposition-vanishing-Noetherian}.
It follows formally that the induced map
$H^1(X, \mathcal{O}_X) \to H^1(X, f_*\mathcal{O}_Y)$
is surjective. Since $H^1(X, f_*\mathcal{O}_Y) = H^1(Y, \mathcal{O}_Y)$
(Cohomology of Schemes, Lemma \ref{coherent-lemma-relative-affine-cohomology})
we conclude the lemma holds.


\begin{lemma}
\label{lemma-genus-normalization}
Let $k$ be a field. Let $X$ be a proper scheme of dimension $\leq 1$ over $k$.
If $X' \to X$ is a birational proper morphism, then
$$
\dim_k H^1(X, \mathcal{O}_X) \geq \dim_k H^1(X', \mathcal{O}_{X'})
$$
If $X$ is reduced, $H^0(X, \mathcal{O}_X) \to H^0(X', \mathcal{O}_{X'})$
is surjective, and equality holds, then $X' = X$.
\end{lemma}

#### Proof

If $f : X' \to X$ is proper birational, then it is finite and
an isomorphism over a dense open (see
Varieties, Lemmas \ref{varieties-lemma-finite-in-codim-1} and
\ref{varieties-lemma-modification-normal-iso-over-codimension-1}).
Thus the inequality by Lemma \ref{lemma-genus-goes-down}.
Assume $X$ is reduced. Then $\mathcal{O}_X \to f_*\mathcal{O}_{X'}$
is injective and we obtain a short exact sequence
$$
0 \to \mathcal{O}_X \to f_*\mathcal{O}_{X'} \to \mathcal{F} \to 0
$$
Under the assumptions given in the second statement,
we conclude from the long exact cohomology sequence that
$H^0(X, \mathcal{F}) = 0$. Then $\mathcal{F} = 0$ because
$\mathcal{F}$ is generated by global sections
(Varieties, Lemma \ref{varieties-lemma-chi-tensor-finite}).
and $\mathcal{O}_X = f_*\mathcal{O}_{X'}$. Since $f$ is affine
this implies $X = X'$.


\begin{lemma}
\label{lemma-bound-geometric-genus-curve}
Let $k$ be a field. Let $C$ be a proper curve over $k$.
Set $\kappa = H^0(C, \mathcal{O}_C)$. Then
$$
[\kappa : k]_s \dim_\kappa H^1(C, \mathcal{O}_C) \geq g_{geom}(C/k)
$$
\end{lemma}

#### Proof

Varieties, Lemma \ref{varieties-lemma-regular-functions-proper-variety}
implies $\kappa$ is a field and a finite extension of $k$.
By Fields, Lemma \ref{fields-lemma-separable-degree}
we have $[\kappa : k]_s = |\Mor_k(\kappa, \overline{k})|$
and hence $\Spec(\kappa \otimes_k \overline{k})$ has
$[\kappa : k]_s$ points each with residue field $\overline{k}$.
Thus
$$
C_{\overline{k}} =
\bigcup\nolimits_{t \in \Spec(\kappa \otimes_k \overline{k})} C_t
$$
(set theoretic union). Here
$C_t = C \times_{\Spec(\kappa), t} \Spec(\overline{k})$ where
we view $t$ as a $k$-algebra map $t : \kappa \to \overline{k}$.
The conclusion is that $g_{geom}(C/k) = \sum_t g_{geom}(C_t/\overline{k})$
and the sum is over an index set of size $[\kappa : k]_s$.
We have
$$
H^0(C_t, \mathcal{O}_{C_t}) = \overline{k}
\quad\text{and}\quad
\dim_{\overline{k}} H^1(C_t, \mathcal{O}_{C_t}) =
\dim_\kappa H^1(C, \mathcal{O}_C)
$$
by cohomology and base change
(Cohomology of Schemes, Lemma \ref{coherent-lemma-flat-base-change-cohomology}).
Observe that the normalization $C_t^\nu$ is the disjoint
union of the nonsingular projective models of the
irreducible components of $C_t$
(Morphisms, Lemma \ref{morphisms-lemma-normalization-in-terms-of-components}).
Hence $\dim_{\overline{k}} H^1(C_t^\nu, \mathcal{O}_{C_t^\nu})$
is equal to $g_{geom}(C_t/\overline{k})$.
By Lemma \ref{lemma-genus-goes-down} we have
$$
\dim_{\overline{k}} H^1(C_t, \mathcal{O}_{C_t}) \geq
\dim_{\overline{k}} H^1(C_t^\nu, \mathcal{O}_{C_t^\nu})
$$
and this finishes the proof.


\begin{lemma}
\label{lemma-bound-torsion-simple}
Let $k$ be a field. Let $X$ be a proper scheme of dimension $\leq 1$ over $k$.
Let $\ell$ be a prime number invertible in $k$. Then
$$
\dim_{\mathbf{F}_\ell} \Pic(X)[\ell] \leq
\dim_k H^1(X, \mathcal{O}_X) + g_{geom}(X/k)
$$
where $g_{geom}(X/k)$ is as defined above.
\end{lemma}

#### Proof

The map $\Pic(X) \to \Pic(X_{\overline{k}})$
is injective by Varieties, Lemma \ref{varieties-lemma-change-fields-pic}.
By Cohomology of Schemes, Lemma \ref{coherent-lemma-flat-base-change-cohomology}
$\dim_k H^1(X, \mathcal{O}_X)$ equals
$\dim_{\overline{k}} H^1(X_{\overline{k}}, \mathcal{O}_{X_{\overline{k}}})$.
Hence we may assume $k$ is algebraically closed.

\medskip\noindent
Let $X_{red}$ be the reduction of $X$. Then the surjection
$\mathcal{O}_X \to \mathcal{O}_{X_{red}}$ induces a surjection
$H^1(X, \mathcal{O}_X) \to H^1(X, \mathcal{O}_{X_{red}})$
because cohomology of quasi-coherent sheaves vanishes in degrees
$\geq 2$ by
Cohomology, Proposition \ref{cohomology-proposition-vanishing-Noetherian}.
Since $X_{red} \to X$ induces an isomorphism on irreducible
components over $\overline{k}$ and an isomorphism on
$\ell$-torsion in Picard groups
(Picard Schemes of Curves, Lemma \ref{pic-lemma-torsion-descends})
we may replace $X$ by $X_{red}$. In this way we reduce to
Proposition \ref{proposition-torsion-picard-reduced-proper}.







###  Nodal curves

\label{section-nodal}

\noindent
We have already defined ordinary double points over algebraically
closed fields, see Definition \ref{definition-multicross}. Namely,
if $x \in X$ is a closed point of a $1$-dimensional
algebraic scheme over an algebraically closed field $k$, then
$x$ is an ordinary double point if and only if
$$
\mathcal{O}_{X, x}^\wedge \cong k[[x, y]]/(xy)
$$
See discussion following (\ref{equation-multicross}) in
Section \ref{section-multicross}.

\begin{definition}
\label{definition-nodal}
Let $k$ be a field. Let $X$ be a $1$-dimensional locally algebraic $k$-scheme.


1.  We say a closed point $x \in X$ is a {\it node}, or an
{\it ordinary double point}, or {\it defines a nodal singularity}
if there exists an ordinary double point $\overline{x} \in X_{\overline{k}}$
mapping to $x$.
1.  We say the {\it singularities of $X$ are at-worst-nodal} if
all closed points of $X$ are either in the smooth locus of
the structure morphism $X \to \Spec(k)$ or are ordinary double points.

\end{definition}

\noindent
Often a $1$-dimensional algebraic scheme $X$ is called a {\it nodal curve}
if the singularities of $X$ are at worst nodal. Sometimes a nodal curve
is required to be proper. Since a nodal curve
so defined need not be irreducible, this conflicts with our earlier definition
of a curve as a variety of dimension $1$.

\begin{lemma}
\label{lemma-reduced-quotient-regular-ring-dim-2}
Let $(A, \mathfrak m)$ be a regular local ring of dimension $2$.
Let $I \subset \mathfrak m$ be an ideal.


1.  If $A/I$ is reduced, then $I = (0)$, $I = \mathfrak m$, or
$I = (f)$ for some nonzero $f \in \mathfrak m$.
1.  If $A/I$ has depth $1$, then $I = (f)$ for some nonzero
$f \in \mathfrak m$.

\end{lemma}

#### Proof

Assume $I \not = 0$. Write $I = (f_1, \ldots, f_r)$. As $A$ is a UFD
(More on Algebra, Lemma \ref{more-algebra-lemma-regular-local-UFD})
we can write $f_i = fg_i$ where $f$ is the gcd of $f_1, \ldots, f_r$.
Thus the gcd of $g_1, \ldots, g_r$ is $1$ which means that
there is no height $1$ prime ideal over $g_1, \ldots, g_r$.
Then either $(g_1, \ldots, g_r) = A$ which implies $I = (f)$ or
if not, then $\dim(A) = 2$ implies that
$V(g_1, \ldots, g_r) = \{\mathfrak m\}$, i.e.,
$\mathfrak m = \sqrt{(g_1, \ldots, g_r)}$.

\medskip\noindent
Assume $A/I$ reduced, i.e., $I$ radical. If $f$ is a unit, then since $I$
is radical we see that $I = \mathfrak m$. If $f \in \mathfrak m$, then we
see that $f^n$ maps to zero in $A/I$. Hence $f \in I$ by reducedness and
we conclude $I = (f)$.

\medskip\noindent
Assume $A/I$ has depth $1$. Then $\mathfrak m$ is not an associated
prime of $A/I$. Since the class of $f$ modulo $I$ is annihilated
by $g_1, \ldots, g_r$, this implies that the class of $f$ is zero
in $A/I$. Thus $I = (f)$ as desired.


\noindent
Let $\kappa$ be a field and let $V$ be a vector space over $\kappa$.
We will say $q \in \text{Sym}^2_\kappa(V)$ is {\it nondegenerate}
if the induced $\kappa$-linear map $V^\vee \to V$ is an
isomorphism. If $q = \sum_{i \leq j} a_{ij} x_i x_j$ for some
$\kappa$-basis $x_1, \ldots, x_n$ of $V$, then this means that
the determinant of the matrix
$$
\left(
\begin{matrix}
2a_{11} & a_{12} & \ldots \\\\
a_{12} & 2a_{22} & \ldots \\\\
\ldots & \ldots & \ldots
\end{matrix}
\right)
$$
is nonzero. This is equivalent to the condition that the
partial derivatives of $q$ with respect to the $x_i$ cut out
$0$ scheme theoretically.

\begin{lemma}
\label{lemma-nodal-algebraic}
Let $k$ be a field. Let $(A, \mathfrak m, \kappa)$ be a Noetherian
local $k$-algebra. The following are equivalent


1.  $\kappa/k$ is separable, $A$ is reduced,
$\dim_\kappa(\mathfrak m/\mathfrak m^2) = 2$, and there exists a nondegenerate
$q \in \text{Sym}^2_\kappa(\mathfrak m/\mathfrak m^2)$
which maps to zero in $\mathfrak m^2/\mathfrak m^3$,
1.  $\kappa/k$ is separable, $\text{depth}(A) = 1$,
$\dim_\kappa(\mathfrak m/\mathfrak m^2) = 2$, and there exists a nondegenerate
$q \in \text{Sym}^2_\kappa(\mathfrak m/\mathfrak m^2)$
which maps to zero in $\mathfrak m^2/\mathfrak m^3$,
1.  $\kappa/k$ is separable,
$A^\wedge \cong \kappa[[x, y]]/(ax^2 + bxy + cy^2)$
as a $k$-algebra where $ax^2 + bxy + cy^2$ is a nondegenerate quadratic form
over $\kappa$.

\end{lemma}

#### Proof

Assume (3). Then $A^\wedge$ is reduced because $ax^2 + bxy + cy^2$
is either irreducible or a product of two nonassociated prime elements.
Hence $A \subset A^\wedge$ is reduced. It follows that (1) is true.

\medskip\noindent
Assume (1). Then $A$ cannot be Artinian, since it would not be reduced
because $\mathfrak m \not = (0)$.
Hence $\dim(A) \geq 1$, hence $\text{depth}(A) \geq 1$
by Algebra, Lemma \ref{algebra-lemma-criterion-reduced}.
On the other hand $\dim(A) = 2$ implies $A$ is regular
which contradicts the existence of $q$ by
Algebra, Lemma \ref{algebra-lemma-regular-graded}.
Thus $\dim(A) \leq 1$ and we conclude $\text{depth}(A) = 1$
by Algebra, Lemma \ref{algebra-lemma-bound-depth}.
It follows that (2) is true.

\medskip\noindent
Assume (2). Since the depth of $A$ is the same as the depth of $A^\wedge$
(More on Algebra, Lemma \ref{more-algebra-lemma-completion-depth})
and since the other conditions are insensitive to completion, we may
assume that $A$ is complete. Choose $\kappa \to A$ as in
More on Algebra, Lemma \ref{more-algebra-lemma-lift-residue-field}.
Since $\dim_\kappa(\mathfrak m/\mathfrak m^2) = 2$ we can choose
$x_0, y_0 \in \mathfrak m$ which map to a basis.
We obtain a continuous $\kappa$-algebra map
$$
\kappa[[x, y]] \longrightarrow A
$$
by the rules $x \mapsto x_0$ and $y \mapsto y_0$. Let
$q$ be the class of $ax_0^2 + bx_0y_0 + cy_0^2$ in
$\text{Sym}^2_\kappa(\mathfrak m/\mathfrak m^2)$.
Write $Q(x, y) = ax^2 + bxy + cy^2$ viewed as a polynomial
in two variables. Then we see that
$$
Q(x_0, y_0) = ax_0^2 + bx_0y_0 + cy_0^2 =
\sum\nolimits_{i + j = 3} a_{ij} x_0^iy_0^j
$$
for some $a_{ij}$ in $A$. We want to prove that we can
increase the order of vanishing by changing our choice
of $x_0$, $y_0$. Suppose that $x_1, y_1 \in \mathfrak m^2$.
Then
$$
Q(x_0 + x_1, y_0 + y_1) = Q(x_0, y_0) +
(2ax_0 + by_0)x_1 + (bx_0 + 2cy_0)y_1 \bmod \mathfrak m^4
$$
Nondegeneracy of $Q$ means exactly that $2ax_0 + by_0$ and $bx_0 + 2cy_0$
are a $\kappa$-basis for $\mathfrak m/\mathfrak m^2$, see discussion
preceding the lemma. Hence we can
certainly choose $x_1, y_1 \in \mathfrak m^2$ such that
$Q(x_0 + x_1, y_0 + y_1) \in \mathfrak m^4$.
Continuing in this fashion by induction
we can find $x_i, y_i \in \mathfrak m^{i + 1}$
such that
$$
Q(x_0 + x_1 + \ldots + x_n, y_0 + y_1 + \ldots + y_n) \in \mathfrak m^{n + 3}
$$
Since $A$ is complete we can set
$x_\infty = \sum x_i$ and $y_\infty = \sum y_i$
and we can consider the map $\kappa[[x, y]] \longrightarrow A$
sending $x$ to $x_\infty$ and $y$ to $y_\infty$. This map
induces a surjection $\kappa[[x, y]]/(Q) \longrightarrow A$ by
Algebra, Lemma \ref{algebra-lemma-completion-generalities}.
By Lemma \ref{lemma-reduced-quotient-regular-ring-dim-2}
the kernel of $k[[x, y]] \to A$ is principal.
But the kernel cannot contain a proper divisor of $Q$
as such a divisor would have degree $1$ in $x, y$
and this would contradict $\dim(\mathfrak m/\mathfrak m^2) = 2$.
Hence $Q$ generates the kernel as desired.


\begin{lemma}
\label{lemma-2-branches-delta-1}
Let $k$ be a field. Let $(A, \mathfrak m, \kappa)$ be a
Nagata local $k$-algebra. The following are equivalent


1.  $k \to A$ is as in Lemma \ref{lemma-nodal-algebraic},
1.  $\kappa/k$ is separable, $A$ is reduced of dimension $1$,
the $\delta$-invariant of $A$ is $1$, and $A$ has $2$ geometric branches.

If this holds, then the integral closure $A'$ of $A$
in its total ring of fractions has either $1$ or $2$
maximal ideals $\mathfrak m'$ and the extensions
$\kappa(\mathfrak m')/k$ are separable.
\end{lemma}

#### Proof

In both cases $A$ and $A^\wedge$ are reduced. In case (2)
because the completion of a reduced local Nagata ring is reduced
(More on Algebra, Lemma \ref{more-algebra-lemma-completion-reduced}).
In both cases $A$ and $A^\wedge$ have dimension $1$
(More on Algebra, Lemma \ref{more-algebra-lemma-completion-dimension}).
The $\delta$-invariant and the number of geometric branches of
$A$ and $A^\wedge$ agree by
Varieties, Lemma \ref{varieties-lemma-delta-same-after-completion}
and
More on Algebra, Lemma
\ref{more-algebra-lemma-one-dimensional-number-of-branches}.
Let $A'$ be the integral closure of $A$ in its total ring of fractions
as in Varieties, Lemma \ref{varieties-lemma-pre-delta-invariant}.
By Varieties, Lemma \ref{varieties-lemma-normalization-same-after-completion}
we see that $A' \otimes_A A^\wedge$ plays the same role for $A^\wedge$.
Thus we may replace $A$ by $A^\wedge$ and assume $A$ is complete.

\medskip\noindent
Assume (1) holds. It suffices to show that $A$ has two
geometric branches and $\delta$-invariant $1$.
We may assume $A = \kappa[[x, y]]/(ax^2 + bxy + cy^2)$ with
$q = ax^2 + bxy + cy^2$ nondegenerate. There are two cases.

\medskip\noindent
Case I: $q$ splits over $\kappa$. In this case we may after
changing coordinates assume that $q = xy$. Then we see that
$$
A' = \kappa[[x, y]]/(x) \times \kappa[[x, y]]/(y)
$$

\medskip\noindent
Case II: $q$ does not split. In this case $c \not = 0$ and
nondegenerate means $b^2 - 4ac \not = 0$. Hence
$\kappa' = \kappa[t]/(a + bt + ct^2)$ is a degree $2$
separable extension of $\kappa$. Then $t = y/x$
is integral over $A$ and we conclude that
$$
A' = \kappa'[[x]]
$$
with $y$ mapping to $tx$ on the right hand side.

\medskip\noindent
In both cases one verifies by hand that the $\delta$-invariant
is $1$ and the number of geometric branches is $2$. In
this way we see that (1) implies (2).
Moreover we conclude that the final statement of the lemma holds.

\medskip\noindent
Assume (2) holds.
More on Algebra, Lemma \ref{more-algebra-lemma-number-of-branches-1}
implies $A'$ either has two maximal ideals or $A'$ has one maximal ideal
and $[\kappa(\mathfrak m') : \kappa]_s = 2$.

\medskip\noindent
Case I: $A'$ has two maximal ideals $\mathfrak m'_1$, $\mathfrak m'_2$
with residue fields $\kappa_1$, $\kappa_2$.
Since the $\delta$-invariant is the length of $A'/A$ and
since there is a surjection $A'/A \to (\kappa_1 \times \kappa_2)/\kappa$
we see that $\kappa = \kappa_1 = \kappa_2$. Since $A$ is complete
(and henselian by Algebra, Lemma \ref{algebra-lemma-complete-henselian})
and $A'$ is finite over $A$ we see that $A' = A_1 \times A_2$
(by Algebra, Lemma \ref{algebra-lemma-finite-over-henselian}).
Since $A'$ is a normal ring it follows that $A_1$ and $A_2$ are
discrete valuation rings.
Hence $A_1$ and $A_2$ are isomorphic to $\kappa[[t]]$
(as $k$-algebras) by
More on Algebra, Lemma \ref{more-algebra-lemma-power-series-over-residue-field}.
Since the $\delta$-invariant is $1$ we conclude that $A$
is the wedge of $A_1$ and $A_2$
(Varieties, Definition \ref{varieties-definition-wedge}).
It follows easily that $A \cong \kappa[[x, y]]/(xy)$.

\medskip\noindent
Case II: $A'$ has a single maximal ideal $\mathfrak m'$ with residue
field $\kappa'$ and $[\kappa' : \kappa]_s = 2$. Arguing exactly
as in Case I we see that $[\kappa' : \kappa] = 2$ and $\kappa'$
is separable over $\kappa$. Since $A'$ is normal we see that
$A'$ is isomorphic to $\kappa'[[t]]$ (see reference above).
Since $A'/A$ has length $1$ we conclude that
$$
A = \{f \in \kappa'[[t]] \mid f(0) \in \kappa\}
$$
Then a simple computation shows that $A$ as in case (1).


\begin{lemma}
\label{lemma-fitting-ideal-well-defined}
Let $k$ be a field. Let $A = k[[x_1, \ldots, x_n]]$. Let
$I = (f_1, \ldots, f_m) \subset A$ be an ideal. For any
$r \geq 0$ the ideal in $A/I$ generated by the $r \times r$-minors
of the matrix $(\partial f_j/\partial x_i)$ is independent
of the choice of the generators of $I$ or the
regular system of parameters $x_1, \ldots, x_n$ of $A$.
\end{lemma}

#### Proof

The ``correct'' proof of this lemma is to prove that this ideal
is the $(n - r)$th Fitting ideal of a module of continuous differentials
of $A/I$ over $k$. Here is a direct proof.
If $g_1, \ldots g_l$ is a second set of generators of $I$, then
we can write $g_s = \sum a_{sj}f_j$ and we have the equality of matrices
$$
(\partial g_s/\partial x_i) = (a_{sj}) (\partial f_j/\partial x_i)
+ (\partial a_{sj}/\partial x_i f_j)
$$
The final term is zero in $A/I$.
By the Cauchy-Binet formula we see that the ideal of minors for the
$g_s$ is contained in the ideal for the $f_j$. By symmetry
these ideals are the same. If $y_1, \ldots, y_n \in \mathfrak m_A$
is a second regular system of parameters, then the matrix
$(\partial y_j/\partial x_i)$
is invertible and we can use the chain rule for differentiation.
Some details omitted.


\begin{lemma}
\label{lemma-fitting-ideal}
Let $k$ be a field. Let $A = k[[x_1, \ldots, x_n]]$. Let
$I = (f_1, \ldots, f_m) \subset \mathfrak m_A$ be an ideal. The following
are equivalent


1.  $k \to A/I$ is as in Lemma \ref{lemma-nodal-algebraic},
1.  $A/I$ is reduced and the
$(n - 1) \times (n - 1)$ minors of the matrix
$(\partial f_j/\partial x_i)$ generate $I + \mathfrak m_A$,
1.  $\text{depth}(A/I) = 1$ and the
$(n - 1) \times (n - 1)$ minors of the matrix
$(\partial f_j/\partial x_i)$ generate $I + \mathfrak m_A$.

\end{lemma}

#### Proof

By Lemma \ref{lemma-fitting-ideal-well-defined}
we may change our system of coordinates and the
choice of generators during the proof.

\medskip\noindent
If (1) holds, then we may change coordinates such that
$x_1, \ldots, x_{n - 2}$ map to zero in $A/I$ and
$A/I = k[[x_{n - 1}, x_n]]/(a x_{n - 1}^2 + b x_{n - 1}x_n + c x_n^2)$
for some nondegenerate quadric $a x_{n - 1}^2 + b x_{n - 1}x_n + c x_n^2$.
Then we can explicitly compute to show that both (2) and (3) are true.

\medskip\noindent
Assume the $(n - 1) \times (n - 1)$ minors of the matrix
$(\partial f_j/\partial x_i)$ generate $I + \mathfrak m_A$.
Suppose that for some $i$ and $j$ the partial derivative
$\partial f_j/\partial x_i$ is a unit in $A$. Then
we may use the system of parameters
$f_j, x_1, \ldots, x_{i - 1}, \hat x_i, x_{i + 1}, \ldots, x_n$
and the generators
$f_j, f_1, \ldots, f_{j - 1}, \hat f_j, f_{j + 1}, \ldots, f_m$
of $I$. Then we get a regular system of parameters $x_1, \ldots, x_n$
and generators $x_1, f_2, \ldots, f_m$ of $I$.
Next, we look for an $i \geq 2$ and $j \geq 2$ such that
$\partial f_j/\partial x_i$ is a unit in $A$. If such a pair
exists, then we can make a replacement as above and assume
that we have a regular system of parameters
$x_1, \ldots, x_n$ and generators $x_1, x_2, f_3, \ldots, f_m$ of $I$.
Continuing, in finitely many steps we reach the situation where
we have a regular system of parameters
$x_1, \ldots, x_n$ and generators
$x_1, \ldots, x_t, f_{t + 1}, \ldots, f_m$ of $I$
such that $\partial f_j/\partial x_i \in \mathfrak m_A$
for all $i, j \geq t + 1$.

\medskip\noindent
In this case the matrix of partial derivatives has the following
block shape
$$
\left(
\begin{matrix}
I_{t \times t} & * \\\\
0 & \mathfrak m_A
\end{matrix}
\right)
$$
Hence every $(n - 1) \times (n - 1)$-minor is in $\mathfrak m_A^{n - 1 - t}$.
Note that $I \not = \mathfrak m_A$ otherwise the ideal of minors
would contain $1$. It follows that $n - 1 - t \leq 1$ because there
is an element of $\mathfrak m_A \setminus \mathfrak m_A^2 + I$ (otherwise
$I = \mathfrak m_A$ by Nakayama). Thus $t \geq n - 2$.
We have seen that $t \not = n$ above and similarly if
$t = n - 1$, then there is an invertible $(n - 1) \times (n - 1)$-minor
which is disallowed as well. Hence $t = n - 2$.
Then $A/I$ is a quotient of $k[[x_{n - 1}, x_n]]$ and
Lemma \ref{lemma-reduced-quotient-regular-ring-dim-2}
implies in both cases (2) and (3) that $I$ is generated by
$x_1, \ldots, x_{n - 2}, f$ for some $f = f(x_{n - 1}, x_n)$.
In this case the condition on the minors exactly says that the quadratic
term in $f$ is nondegenerate, i.e., $A/I$ is as in
Lemma \ref{lemma-nodal-algebraic}.


\begin{lemma}
\label{lemma-nodal}
Let $k$ be a field. Let $X$ be a $1$-dimensional algebraic $k$-scheme.
Let $x \in X$ be a closed point. The following are equivalent


1.  $x$ is a node,
1.  $k \to \mathcal{O}_{X, x}$ is as in Lemma \ref{lemma-nodal-algebraic},
1.  any $\overline{x} \in X_{\overline{k}}$ mapping to $x$ defines
a nodal singularity,
1.  $\kappa(x)/k$ is separable, $\mathcal{O}_{X, x}$ is reduced, and
the first Fitting ideal of $\Omega_{X/k}$ generates $\mathfrak m_x$
in $\mathcal{O}_{X, x}$,
1.  $\kappa(x)/k$ is separable, $\text{depth}(\mathcal{O}_{X, x}) = 1$, and
the first Fitting ideal of $\Omega_{X/k}$ generates $\mathfrak m_x$
in $\mathcal{O}_{X, x}$,
1.  $\kappa(x)/k$ is separable and $\mathcal{O}_{X, x}$ is reduced, has
$\delta$-invariant $1$, and has $2$ geometric branches.

\end{lemma}

#### Proof

First assume that $k$ is algebraically closed.
In this case the equivalence of (1) and (3) is trivial.
The equivalence of (1) and (3) with (2) holds because the only
nondegenerate quadric in two variables is $xy$ up to change in
coordinates. The equivalence of (1) and (6) is
Lemma \ref{lemma-multicross-algebra}.
After replacing $X$ by an affine neighbourhood
of $x$, we may assume there is a closed immersion $X \to \mathbf{A}^n_k$
mapping $x$ to $0$. Let $f_1, \ldots, f_m \in k[x_1, \ldots, x_n]$
be generators for the ideal $I$ of $X$ in $\mathbf{A}^n_k$.
Then $\Omega_{X/k}$ corresponds to the $R = k[x_1, \ldots, x_n]/I$-module
$\Omega_{R/k}$ which has a presentation
$$
R^{\oplus m} \xrightarrow{(\partial f_j/\partial x_i)}
R^{\oplus n} \to \Omega_{R/k} \to 0
$$
(See Algebra, Sections \ref{algebra-section-differentials} and
\ref{algebra-section-netherlander}.)
The first Fitting ideal of $\Omega_{R/k}$ is thus the ideal
generated by the $(n - 1) \times (n - 1)$-minors of the
matrix $(\partial f_j/\partial x_i)$. Hence (2), (4), (5)
are equivalent by Lemma \ref{lemma-fitting-ideal} applied
to the completion of $k[x_1, \ldots, x_n] \to R$
at the maximal ideal $(x_1, \ldots, x_n)$.

\medskip\noindent
Now assume $k$ is an arbitrary field.
In cases (2), (4), (5), (6) the residue field $\kappa(x)$ is
separable over $k$. Let us show this holds as well
in cases (1) and (3). Namely, let $Z \subset X$ be the closed subscheme
of $X$ defined by the first Fitting ideal of $\Omega_{X/k}$.
The formation of $Z$ commutes with field extension
(Divisors, Lemma \ref{divisors-lemma-base-change-and-fitting-ideal-omega}).
If (1) or (3) is true, then there exists a point
$\overline{x}$ of $X_{\overline{k}}$ such that $\overline{x}$
is an isolated point of multiplicity $1$ of $Z_{\overline{k}}$ (as we have the
equivalence of the conditions of the lemma over $\overline{k}$).
In particular $Z_{\overline{x}}$ is geometrically reduced at $\overline{x}$
(because $\overline{k}$ is algebraically closed). Hence
$Z$ is geometrically reduced at $x$
(Varieties, Lemma \ref{varieties-lemma-geometrically-reduced-upstairs}).
In particular, $Z$ is reduced at $x$, hence $Z = \Spec(\kappa(x))$
in a neighbourhood of $x$ and $\kappa(x)$ is geometrically reduced
over $k$. This means that $\kappa(x)/k$ is separable
(Algebra, Lemma \ref{algebra-lemma-characterize-separable-field-extensions}).

\medskip\noindent
The argument of the previous paragraph shows that if (1) or (3) holds, then
the first Fitting ideal of $\Omega_{X/k}$ generates $\mathfrak m_x$.
Since $\mathcal{O}_{X, x} \to \mathcal{O}_{X_{\overline{k}}, \overline{x}}$
is flat and since $\mathcal{O}_{X_{\overline{k}}, \overline{x}}$
is reduced and has depth $1$, we see that (4) and (5) hold
(use Algebra, Lemmas \ref{algebra-lemma-descent-reduced} and
\ref{algebra-lemma-apply-grothendieck}).
Conversely, (4) implies (5) by
Algebra, Lemma \ref{algebra-lemma-criterion-reduced}.
If (5) holds, then $Z$ is geometrically reduced at $x$
(because $\kappa(x)/k$ separable and $Z$ is $x$ in a neighbourhood).
Hence $Z_{\overline{k}}$ is reduced at any point $\overline{x}$
of $X_{\overline{k}}$ lying over $x$. In other words, the first
fitting ideal of $\Omega_{X_{\overline{k}}/\overline{k}}$ generates
$\mathfrak m_{\overline{x}}$ in $\mathcal{O}_{X_{\overline{k}, \overline{x}}}$.
Moreover, since
$\mathcal{O}_{X, x} \to \mathcal{O}_{X_{\overline{k}}, \overline{x}}$ is flat
we see that $\text{depth}(\mathcal{O}_{X_{\overline{k}}, \overline{x}}) = 1$
(see reference above).
Hence (5) holds for $\overline{x} \in X_{\overline{k}}$ and we
conclude that (3) holds (because of the equivalence over algebraically
closed fields). In this way we see that (1), (3), (4), (5)
are equivalent.

\medskip\noindent
The equivalence of (2) and (6) follows from
Lemma \ref{lemma-2-branches-delta-1}.

\medskip\noindent
Finally, we prove the equivalence of (2) $=$ (6) with
(1) $=$ (3) $=$ (4) $=$ (5). First we note that the geometric number
of branches of $X$ at $x$ and the geometric number of branches
of $X_{\overline{k}}$ at $\overline{x}$ are equal by
Varieties, Lemma
\ref{varieties-lemma-geometric-branches-and-change-of-fields}.
We conclude from the information available to us at this point
that in all cases this number is equal to $2$.
On the other hand, in case (1) it is clear that $X$ is geometrically
reduced at $x$, and hence
$$
\delta\text{-invariant of }X\text{ at }x \leq
\delta\text{-invariant of }X_{\overline{k}}\text{ at }\overline{x}
$$
by Varieties, Lemma \ref{varieties-lemma-delta-invariant-and-change-of-fields}.
Since in case (1) the right hand side is $1$, this
forces the $\delta$-invariant of $X$ at $x$ to be $1$
(because if it were zero, then $\mathcal{O}_{X, x}$ would
be a discrete valuation ring by
Varieties, Lemma \ref{varieties-lemma-delta-invariant-is-zero}
which is unibranch, a contradiction). Thus (5) holds.
Conversely, if (2) $=$ (5) is true, then assumptions (a), (b), (c) of
Varieties, Lemma \ref{varieties-lemma-geometrically-normal-in-codim-1}
hold for $x \in X$ by
Lemma \ref{lemma-2-branches-delta-1}. Thus
Varieties, Lemma
\ref{varieties-lemma-delta-invariant-and-change-of-fields-better}
applies and shows that we have equality in the above displayed inequality.
We conclude that (5) holds for $\overline{x} \in X_{\overline{k}}$
and we are back in case (1) by the equivalence of the conditions
over an algebraically closed field.


\begin{remark}[The quadratic extension associated to a node]
\label{remark-quadratic-extension}
Let $k$ be a field. Let $(A, \mathfrak m, \kappa)$ be a
Noetherian local $k$-algebra. Assume that either
$(A, \mathfrak m, \kappa)$ is as in Lemma \ref{lemma-nodal-algebraic}, or
$A$ is Nagata as in Lemma \ref{lemma-2-branches-delta-1}, or
$A$ is complete and as in Lemma \ref{lemma-fitting-ideal}.
Then $A$ defines canonically a degree $2$ separable $\kappa$-algebra
$\kappa'$ as follows


1.  let $q = ax^2 + bxy + cy^2$ be a nondegenerate quadric
as in Lemma \ref{lemma-nodal-algebraic} with coordinates $x, y$ chosen
such that $a \not = 0$ and set
$\kappa' = \kappa[x]/(ax^2 + bx + c)$,
1.  let $A' \supset A$ be the integral closure of $A$ in its
total ring of fractions and set $\kappa' = A'/\mathfrak m A'$, or
1.  let $\kappa'$ be the $\kappa$-algebra such that
$\text{Proj}(\bigoplus_{n \geq 0} \mathfrak m^n/\mathfrak m^{n + 1}) =
\Spec(\kappa')$.

The equivalence of (1) and (2) was shown in the proof of
Lemma \ref{lemma-2-branches-delta-1}. We omit the equivalence of
this with (3). If $X$ is a locally Noetherian $k$-scheme and $x \in X$
is a point such that $\mathcal{O}_{X, x} = A$, then (3) shows that
$\Spec(\kappa') = X^\nu \times_X \Spec(\kappa)$ where $\nu : X^\nu \to X$
is the normalization morphism.
\end{remark}

\begin{remark}[Trivial quadratic extension]
\label{remark-trivial-quadratic-extension}
Let $k$ be a field. Let $(A, \mathfrak m, \kappa)$ be as in
Remark \ref{remark-quadratic-extension} and let $\kappa'/\kappa$
be the associated separable algebra of degree $2$.
Then the following are equivalent


1.  $\kappa' \cong \kappa \times \kappa$ as $\kappa$-algebra,
1.  the form $q$ of Lemma \ref{lemma-nodal-algebraic}
can be chosen to be $xy$,
1.  $A$ has two branches,
1.  the extension $A'/A$ of Lemma \ref{lemma-2-branches-delta-1}
has two maximal ideals, and
1.  $A^\wedge \cong \kappa[[x, y]]/(xy)$ as a $k$-algebra.

The equivalence between these conditions has been shown in the
proof of Lemma \ref{lemma-2-branches-delta-1}. If $X$ is a
locally Noetherian $k$-scheme and $x \in X$ is a point such that
$\mathcal{O}_{X, x} = A$, then this means exactly that
there are two points $x_1, x_2$ of the normalization $X^\nu$
lying over $x$ and that $\kappa(x) = \kappa(x_1) = \kappa(x_2)$.
\end{remark}

\begin{definition}
\label{definition-split-node}
Let $k$ be a field. Let $X$ be a $1$-dimensional algebraic $k$-scheme.
Let $x \in X$ be a closed point. We say $x$ is a {\it split node}
if $x$ is a node, $\kappa(x) = k$, and the equivalent assertions of
Remark \ref{remark-trivial-quadratic-extension}
hold for $A = \mathcal{O}_{X, x}$.
\end{definition}

\noindent
We formulate the obligatory lemma stating what we already know
about this concept.

\begin{lemma}
\label{lemma-split-node}
Let $k$ be a field. Let $X$ be a $1$-dimensional algebraic $k$-scheme.
Let $x \in X$ be a closed point. The following are equivalent


1.  $x$ is a split node,
1.  $x$ is a node and there are exactly two points $x_1, x_2$
of the normalization $X^\nu$ lying over $x$ with
$k = \kappa(x_1) = \kappa(x_2)$,
1.  $\mathcal{O}_{X, x}^\wedge \cong k[[x, y]]/(xy)$ as a $k$-algebra, and
1.  add more here.

\end{lemma}

#### Proof

This follows from the discussion in
Remark \ref{remark-trivial-quadratic-extension}
and Lemma \ref{lemma-nodal}.


\begin{lemma}
\label{lemma-node-field-extension}
Let $K/k$ be an extension of fields. Let $X$ be a locally algebraic
$k$-scheme of dimension $1$. Let $y \in X_K$ be a point with image
$x \in X$. The following are equivalent


1.  $x$ is a closed point of $X$ and a node, and
1.  $y$ is a closed point of $Y$ and a node.

\end{lemma}

#### Proof

If $x$ is a closed point of $X$, then $y$ is too (look at residue fields).
But conversely, this need not be the case, i.e., it can happen that a
closed point of $Y$ maps to a nonclosed point of $X$. However, in this
case $y$ cannot be a node. Namely, then $X$ would be geometrically
unibranch at $x$ (because $x$ would be a generic point of $X$ and
$\mathcal{O}_{X, x}$ would be Artinian and any Artinian local ring is
geometrically unibranch), hence $Y$ is geometrically unibranch at $y$
(Varieties, Lemma
\ref{varieties-lemma-geometrically-unibranch-and-change-of-fields}),
which means that $y$ cannot be a node by Lemma \ref{lemma-nodal}.
Thus we may and do assume that both $x$ and $y$ are closed points.

\medskip\noindent
Choose algebraic closures $\overline{k}$, $\overline{K}$
and a map $\overline{k} \to \overline{K}$ extending the
given map $k \to K$. Using the equivalence of (1) and (3)
in Lemma \ref{lemma-nodal}
we reduce to the case where $k$ and $K$ are algebraically closed.
In this case we can argue as in the proof of
Lemma \ref{lemma-nodal} that the geometric number of branches
and $\delta$-invariants of $X$ at $x$ and $Y$ at $y$ are the same.
Another argument can be given by choosing an isomorphism
$k[[x_1, \ldots, x_n]]/(g_1, \ldots, g_m) \to \mathcal{O}_{X, x}^\wedge$
of $k$-algebras as in Varieties, Lemma
\ref{varieties-lemma-complete-local-ring-structure-as-algebra}.
By Varieties, Lemma \ref{varieties-lemma-base-change-complete-local-ring}
this gives an isomorphism
$K[[x_1, \ldots, x_n]]/(g_1, \ldots, g_m) \to \mathcal{O}_{Y, y}^\wedge$
of $K$-algebras. By definition we have to show that
$$
k[[x_1, \ldots, x_n]]/(g_1, \ldots, g_m) \cong k[[s, t]]/(st)
$$
if and only if
$$
K[[x_1, \ldots, x_n]]/(g_1, \ldots, g_m) \cong K[[s, t]]/(st)
$$
We encourage the reader to prove this for themselves.
Since $k$ and $K$ are algebraically closed fields, this is the same as
asking these rings to be as in Lemma \ref{lemma-nodal-algebraic}.
Via Lemma \ref{lemma-fitting-ideal} this translates into a statement
about the $(n - 1) \times (n - 1)$-minors of the matrix
$(\partial g_j/\partial x_i)$ which is clearly independent of the
field used. We omit the details.


\begin{lemma}
\label{lemma-node-etale-local}
Let $k$ be a field. Let $X$ be a locally algebraic
$k$-scheme of dimension $1$. Let $Y \to X$ be an \'etale morphism.
Let $y \in Y$ be a point with image $x \in X$. The following are equivalent


1.  $x$ is a closed point of $X$ and a node, and
1.  $y$ is a closed point of $Y$ and a node.

\end{lemma}

#### Proof

By Lemma \ref{lemma-node-field-extension}
we may base change to the algebraic closure of $k$.
Then the residue fields of $x$ and $y$ are $k$.
Hence the map $\mathcal{O}_{X, x}^\wedge \to \mathcal{O}_{Y, y}^\wedge$
is an isomorphism (for example by
\'Etale Morphisms, Lemma \ref{etale-lemma-characterize-etale-completions} or
More on Algebra, Lemma \ref{more-algebra-lemma-flat-unramified}).
Thus the lemma is clear.


\begin{lemma}
\label{lemma-node-over-separable-extension}
Let $k'/k$ be a finite separable field extension.
Let $X$ be a locally algebraic $k'$-scheme of dimension $1$.
Let $x \in X$ be a closed point. The following are equivalent


1.  $x$ is a node, and
1.  $x$ is a node when $X$ viewed as a locally algebraic $k$-scheme.

\end{lemma}

#### Proof

Follows immediately from the characterization of nodes in
Lemma \ref{lemma-nodal}.


\begin{lemma}
\label{lemma-nodal-lci}
Let $k$ be a field. Let $X$ be a locally algebraic $k$-scheme
equidimensional of dimension $1$.
The following are equivalent


1.  the singularities of $X$ are at-worst-nodal, and
1.  $X$ is a local complete intersection over $k$
and the closed subscheme $Z \subset X$ cut out by the
first fitting ideal of $\Omega_{X/k}$ is unramified over $k$.

\end{lemma}

#### Proof

We urge the reader to find their own proof of
this lemma; what follows is just putting together earlier results
and may hide what is really going on.

\medskip\noindent
Assume (2). Since $Z \to \Spec(k)$ is quasi-finite
(Morphisms, Lemma \ref{morphisms-lemma-unramified-quasi-finite})
we see that the residue fields of points $x \in Z$ are finite
over $k$ (as well as separable) by
Morphisms, Lemma \ref{morphisms-lemma-residue-field-quasi-finite}.
Hence each $x \in Z$ is a closed point of $X$ by
Morphisms, Lemma
\ref{morphisms-lemma-algebraic-residue-field-extension-closed-point-fibre}.
The local ring $\mathcal{O}_{X, x}$ is Cohen-Macaulay by
Algebra, Lemma \ref{algebra-lemma-lci-CM}.
Since $\dim(\mathcal{O}_{X, x}) = 1$ by dimension theory
(Varieties, Section \ref{varieties-section-algebraic-schemes}), we conclude
that $\text{depth}(\mathcal{O}_{X, x})) = 1$. Thus $x$ is a node
by Lemma \ref{lemma-nodal}. If $x \in X$, $x \not \in Z$, then
$X \to \Spec(k)$ is smooth at $x$ by
Divisors, Lemma \ref{divisors-lemma-d-fitting-ideal-omega-smooth}.

\medskip\noindent
Assume (1). Under this assumption $X$ is geometrically reduced
at every closed point (see
Varieties, Lemma \ref{varieties-lemma-geometrically-reduced-upstairs}).
Hence $X \to \Spec(k)$ is smooth on a dense open by
Varieties, Lemma \ref{varieties-lemma-geometrically-reduced-dense-smooth-open}.
Thus $Z$ is closed and consists of closed points.
By Divisors, Lemma \ref{divisors-lemma-d-fitting-ideal-omega-smooth}
the morphism $X \setminus Z \to \Spec(k)$ is smooth.
Hence $X \setminus Z$ is a local complete intersection by
Morphisms, Lemma \ref{morphisms-lemma-smooth-syntomic}
and the definition of a local complete intersection in
Morphisms, Definition \ref{morphisms-definition-syntomic}.
By Lemma \ref{lemma-nodal} for every point $x \in Z$
the local ring $\mathcal{O}_{Z, x}$ is equal to $\kappa(x)$
and $\kappa(x)$ is separable over $k$. Thus $Z \to \Spec(k)$
is unramified (Morphisms, Lemma \ref{morphisms-lemma-unramified-over-field}).
Finally, Lemma \ref{lemma-nodal} via part (3) of
Lemma \ref{lemma-nodal-algebraic}, shows that $\mathcal{O}_{X, x}$
is a complete intersection in the sense of
Divided Power Algebra, Definition \ref{dpa-definition-lci}.
However, Divided Power Algebra, Lemma \ref{dpa-lemma-check-lci-agrees}
and Morphisms, Lemma \ref{morphisms-lemma-local-complete-intersection}
show that this agrees with the notion used to define a local
complete intersection scheme over a field and the proof is complete.


\begin{lemma}
\label{lemma-facts-about-nodal-curves}
Let $k$ be a field. Let $X$ be a locally algebraic $k$-scheme
equidimensional of dimension $1$ whose singularities are at-worst-nodal.
Then $X$ is Gorenstein and geometrically reduced.
\end{lemma}

#### Proof

The Gorenstein assertion follows from Lemma \ref{lemma-nodal-lci}
and Duality for Schemes, Lemma \ref{duality-lemma-gorenstein-lci}.
Or you can use that it suffices to check after passing to the
algebraic closure (Duality for Schemes, Lemma
\ref{duality-lemma-gorenstein-base-change}), then use that
a Noetherian local ring is Gorenstein if and only if its
completion is so (by Dualizing Complexes, Lemma
\ref{dualizing-lemma-flat-under-gorenstein}), and
then prove that the local rings $k[[t]]$ and $k[[x, y]]/(xy)$
are Gorenstein by hand.

\medskip\noindent
To see that $X$ is geometrically reduced, it suffices to show that
$X_{\overline{k}}$ is reduced (Varieties, Lemmas
\ref{varieties-lemma-perfect-reduced} and
\ref{varieties-lemma-geometrically-reduced}).
But $X_{\overline{k}}$ is a nodal curve over an
algebraically closed field. Thus the complete local rings
of $X_{\overline{k}}$ are isomorphic to either
$\overline{k}[[t]]$ or $\overline{k}[[x, y]]/(xy)$
which are reduced as desired.


\begin{lemma}
\label{lemma-closed-subscheme-nodal-curve}
Let $k$ be a field. Let $X$ be a locally algebraic $k$-scheme
equidimensional of dimension $1$ whose singularities are at-worst-nodal.
If $Y \subset X$ is a reduced closed subscheme
equidimensional of dimension $1$, then


1.  the singularities of $Y$ are at-worst-nodal, and
1.  if $Z \subset X$ is the scheme theoretic closure of
$X \setminus Y$, then
\begin{enumerate}
1.  the scheme theoretic intersection $Y \cap Z$ is
the disjoint union of spectra of finite separable extensions of $k$,
1.  each point of $Y \cap Z$ is a node of $X$, and
1.  $Y \to \Spec(k)$ is smooth at every point of $Y \cap Z$.

\end{enumerate}
\end{lemma}

#### Proof

Since $X$ and $Y$ are reduced and equidimensional of dimension $1$,
we see that $Y$ is the scheme theoretic union of a subset of the
irreducible components of $X$ (in a reduced ring $(0)$
is the intersection of the minimal primes).
Let $y \in Y$ be a closed point.
If $y$ is in the smooth locus of
$X \to \Spec(k)$, then $y$ is on a unique irreducible component
of $X$ and we see that $Y$ and $X$ agree in an open neighbourhood
of $y$. Hence $Y \to \Spec(k)$ is smooth at $y$.
If $y$ is a node of $X$ but still lies on a unique irreducible
component of $X$, then $y$ is a node on $Y$ by the same argument.
Suppose that $y$ lies on more than $1$ irreducible component of $X$.
Since the number of geometric branches of $X$ at $y$ is $2$
by Lemma \ref{lemma-nodal},
there can be at most $2$ irreducible components passing through $y$
by Properties, Lemma
\ref{properties-lemma-number-of-branches-irreducible-components}.
If $Y$ contains both of these, then again $Y = X$ in an open neighbourhood
of $y$ and $y$ is a node of $Y$. Finally, assume $Y$ contains only one
of the irreducible components. After replacing $X$ by an open
neighbourhood of $x$ we may assume $Y$ is one of the two
irreducble components and $Z$ is the other. By Properties, Lemma
\ref{properties-lemma-number-of-branches-irreducible-components}
again we see that $X$ has two branches at $y$, i.e., the local ring
$\mathcal{O}_{X, y}$ has two branches and that these branches
come from $\mathcal{O}_{Y, y}$ and $\mathcal{O}_{Z, y}$. Write
$\mathcal{O}_{X, y}^\wedge \cong \kappa(y)[[u, v]]/(uv)$
as in Remark \ref{remark-trivial-quadratic-extension}.
The field $\kappa(y)$ is finite separable over $k$ by
Lemma \ref{lemma-nodal} for example.
Thus, after possibly switching the roles of $u$ and $v$,
the completion of the map
$\mathcal{O}_{X, y} \to \mathcal{O}_{Y, Y}$
corresponds to $\kappa(y)[[u, v]]/(uv) \to \kappa(y)[[u]]$
and the completion of the map
$\mathcal{O}_{X, y} \to \mathcal{O}_{Y, Y}$
corresponds to $\kappa(y)[[u, v]]/(uv) \to \kappa(y)[[v]]$.
The scheme theoretic intersection of $Y \cap Z$ is cut out
by the sum of their ideas which in the completion is $(u, v)$, i.e.,
the maximal ideal. Thus (2)(a) and (2)(b) are clear.
Finally, (2)(c) holds: the completion of $\mathcal{O}_{Y, y}$
is regular, hence $\mathcal{O}_{Y, y}$ is regular
(More on Algebra, Lemma \ref{more-algebra-lemma-completion-regular})
and $\kappa(y)/k$ is separable, hence
smoothness in an open neighbourhood
by Algebra, Lemma \ref{algebra-lemma-separable-smooth}.





###  Families of nodal curves

\label{section-families-nodal}

\noindent
In the Stacks project curves are irreducible varieties of dimension $1$,
but in the literature a ``semi-stable curve'' or a ``nodal curve'' is
usually not irreducible and often assumed to be proper, especially
when used in a phrase such as ``family of semistable curves'' or
``family of nodal curves'', or ``nodal family''. Thus it is a bit
difficult for us to choose a terminology which is consistent with the
literature as well as internally consistent. Moreover, we really want
to first study the notion introduced in the following lemma (which is
local on the source).

\begin{lemma}
\label{lemma-nodal-family}
Let $f : X \to S$ be a morphism of schemes. The following are equivalent


1.  $f$ is flat, locally of finite presentation, every nonempty fibre
$X_s$ is equidimensional of dimension $1$, and $X_s$ has
at-worst-nodal singularities, and
1.  $f$ is syntomic of relative dimension $1$ and the closed subscheme
$\text{Sing}(f) \subset X$ defined by the first Fitting ideal of
$\Omega_{X/S}$ is unramified over $S$.

\end{lemma}

#### Proof

Recall that the formation of $\text{Sing}(f)$ commutes with base
change, see Divisors, Lemma
\ref{divisors-lemma-base-change-and-fitting-ideal-omega}.
Thus the lemma follows from Lemma \ref{lemma-nodal-lci},
Morphisms, Lemma \ref{morphisms-lemma-syntomic-flat-fibres}, and
Morphisms, Lemma \ref{morphisms-lemma-unramified-etale-fibres}.
(We also use the trivial
Morphisms, Lemmas \ref{morphisms-lemma-syntomic-locally-finite-presentation}
and \ref{morphisms-lemma-syntomic-flat}.)


\begin{definition}
\label{definition-nodal-family}
Let $f : X \to S$ be a morphism of schemes. We say $f$ is
{\it at-worst-nodal of relative dimension $1$} if $f$ satisfies
the equivalent conditions of Lemma \ref{lemma-nodal-family}.
\end{definition}

\noindent
Here are some reasons for the cumbersome terminology\footnote{But please
email the maintainer of the Stacks project if you have a better suggestion.}.
First, we want to make sure this notion is not confused with any of the
other notions in the literature (see introduction to this section).
Second, we can imagine several generalizations of this notion to morphisms
of higher relative dimension (for example, one can ask for morphisms
which are \'etale locally compositions of at-worst-nodal morphisms or
one can ask for morphisms whose fibres are higher dimensional but have
at worst ordinary double points).

\begin{lemma}
\label{lemma-smooth-relative-dimension-1}
A smooth morphism of relative dimension $1$ is
at-worst-nodal of relative dimension $1$.
\end{lemma}

#### Proof

Omitted.


\begin{lemma}
\label{lemma-base-change-nodal-family}
Let $f : X \to S$ be at-worst-nodal of relative dimension $1$.
Then the same is true for any base change of $f$.
\end{lemma}

#### Proof

This is true because the base change of a syntomic morphism
is syntomic (Morphisms, Lemma \ref{morphisms-lemma-base-change-syntomic}),
the base change of a morphism of relative dimension $1$ has
relative dimension $1$
(Morphisms, Lemma \ref{morphisms-lemma-base-change-relative-dimension-d}),
the formation of $\text{Sing}(f)$ commutes with base change
(Divisors, Lemma
\ref{divisors-lemma-base-change-and-fitting-ideal-omega}), and
the base change of an unramified morphism is unramified
(Morphisms, Lemma \ref{morphisms-lemma-base-change-unramified}).


\noindent
The following lemma tells us that we can check whether a morphism
is at-worst-nodal of relative dimension $1$ on the fibres.

\begin{lemma}
\label{lemma-locus-where-nodal}
Let $f : X \to S$ be a morphism of schemes which is flat and
locally of finite presentation. Then there is a maximal open
subscheme $U \subset X$ such that $f|_U : U \to S$ is
at-worst-nodal of relative dimension $1$. Moreover, formation
of $U$ commutes with arbitrary base change.
\end{lemma}

#### Proof

By Morphisms, Lemma \ref{morphisms-lemma-set-points-where-fibres-lci}
we find that there is such an open where $f$ is syntomic.
Hence we may assume that $f$ is a syntomic morphism.
In particular $f$ is a Cohen-Macaulay morphism
(Duality for Schemes, Lemmas \ref{duality-lemma-lci-gorenstein} and
\ref{duality-lemma-gorenstein-CM-morphism}).
Thus $X$ is a disjoint union of open and closed subschemes on which
$f$ has given relative dimension, see Morphisms, Lemma
\ref{morphisms-lemma-flat-finite-presentation-CM-fibres-relative-dimension}.
This decomposition is preserved by arbitrary base change, see
Morphisms, Lemma \ref{morphisms-lemma-base-change-relative-dimension-d}.
Discarding all but one piece we may assume $f$ is syntomic of
relative dimension $1$. Let $\text{Sing}(f) \subset X$ be the
closed subscheem defined by the first fitting ideal of
$\Omega_{X/S}$. There is a maximal open subscheme
$W \subset \text{Sing}(f)$ such that $W \to S$ is unramified
and its formation commutes with base change
(Morphisms, Lemma \ref{morphisms-lemma-set-points-where-fibres-unramified}).
Since also formation of $\text{Sing}(f)$ commutes with base change
(Divisors, Lemma
\ref{divisors-lemma-base-change-and-fitting-ideal-omega}),
we see that
$$
U = (X \setminus \text{Sing}(f)) \cup W
$$
is the maximal open subscheme of $X$ such that
$f|_U : U \to S$ is at-worst-nodal of relative dimension $1$
and that formation of $U$ commutes with base change.


\begin{lemma}
\label{lemma-nodal-family-precompose-etale}
Let $f : X \to S$ be at-worst-nodal of relative dimension $1$.
If $Y \to X$ is an \'etale morphism, then the composition $g : Y \to S$
is at-worst-nodal of relative dimension $1$.
\end{lemma}

#### Proof

Observe that $g$ is flat and locally of finite presentation as
a composition of morphisms which are flat and locally of finite
presentation (use
Morphisms, Lemmas \ref{morphisms-lemma-etale-locally-finite-presentation},
\ref{morphisms-lemma-etale-flat},
\ref{morphisms-lemma-composition-finite-presentation}, and
\ref{morphisms-lemma-composition-flat}).
Thus it suffices to prove the fibres have at-worst-nodal singularities.
This follows from Lemma \ref{lemma-node-etale-local}
(and the fact that the composition of an \'etale morphism and
a smooth morphism is smooth by
Morphisms, Lemmas \ref{morphisms-lemma-etale-smooth-unramified} and
\ref{morphisms-lemma-composition-smooth}).


\begin{lemma}
\label{lemma-nodal-family-postcompose-etale}
Let $S' \to S$ be an \'etale morphism of schemes.
Let $f : X \to S'$ be at-worst-nodal of relative dimension $1$.
Then the composition $g : X \to S$
is at-worst-nodal of relative dimension $1$.
\end{lemma}

#### Proof

Observe that $g$ is flat and locally of finite presentation as
a composition of morphisms which are flat and locally of finite
presentation (use
Morphisms, Lemmas \ref{morphisms-lemma-etale-locally-finite-presentation},
\ref{morphisms-lemma-etale-flat},
\ref{morphisms-lemma-composition-finite-presentation}, and
\ref{morphisms-lemma-composition-flat}).
Thus it suffices to prove the fibres of $g$
have at-worst-nodal singularities.
This follows from Lemma \ref{lemma-node-over-separable-extension}
and the analogous result for smooth points.


\begin{lemma}
\label{lemma-nodal-family-etale-local-source}
Let $f : X \to S$ be a morphism of schemes. Let $\{U_i \to X\}$
be an \'etale covering. The following are equivalent


1.  $f$ is at-worst-nodal of relative dimension $1$,
1.  each $U_i \to S$ is at-worst-nodal of relative dimension $1$.

In other words, being at-worst-nodal of relative dimension $1$
is \'etale local on the source.
\end{lemma}

#### Proof

One direction we have seen in Lemma \ref{lemma-nodal-family-precompose-etale}.
For the other direction, observe that being locally of finite
presentation, flat, or to have relative dimension $1$
is \'etale local on the source
(Descent, Lemmas
\ref{descent-lemma-locally-finite-presentation-fppf-local-source},
\ref{descent-lemma-flat-fpqc-local-source}, and
\ref{descent-lemma-dimension-at-point}). Taking fibres we reduce
to the case where $S$ is the spectrum of a field. In this case the
result follows from Lemma \ref{lemma-node-etale-local}
(and the fact that being smooth is \'etale local on the source by
Descent, Lemma \ref{descent-lemma-smooth-smooth-local-source}).


\begin{lemma}
\label{lemma-nodal-family-fpqc-local-target}
Let $f : X \to S$ be a morphism of schemes. Let $\{U_i \to S\}$
be an fpqc covering. The following are equivalent


1.  $f$ is at-worst-nodal of relative dimension $1$,
1.  each $X \times_S U_i \to U_i$ is at-worst-nodal of relative
dimension $1$.

In other words, being at-worst-nodal of relative dimension $1$
is fpqc local on the target.
\end{lemma}

#### Proof

One direction we have seen in Lemma \ref{lemma-base-change-nodal-family}.
For the other direction, observe that being locally of finite
presentation, flat, or to have relative dimension $1$
is fpqc local on the target
(Descent, Lemmas
\ref{descent-lemma-descending-property-locally-finite-presentation},
\ref{descent-lemma-descending-property-flat}, and
Morphisms, Lemma \ref{morphisms-lemma-dimension-fibre-after-base-change}).
Taking fibres we reduce
to the case where $S$ is the spectrum of a field. In this case the
result follows from Lemma \ref{lemma-node-field-extension}
(and the fact that being smooth is fpqc local on the target by
Descent, Lemma \ref{descent-lemma-descending-property-smooth}).


\begin{lemma}
\label{lemma-descend-nodal-family}
Let $S = \lim S_i$ be a limit of a directed system of schemes
with affine transition morphisms.
Let $0 \in I$ and let $f_0 : X_0 \to Y_0$ be a morphism of schemes over $S_0$.
Assume $S_0$, $X_0$, $Y_0$ are quasi-compact and quasi-separated.
Let $f_i : X_i \to Y_i$ be the base change of $f_0$ to $S_i$ and
let $f : X \to Y$ be the base change of $f_0$ to $S$.
If


1.  $f$ is at-worst-nodal of relative dimension $1$, and
1.  $f_0$ is locally of finite presentation,

then there exists an $i \geq 0$ such that $f_i$ is at-worst-nodal
of relative dimension $1$.
\end{lemma}

#### Proof

By Limits, Lemma \ref{limits-lemma-descend-syntomic}
there exists an $i$ such that $f_i$ is syntomic.
Then $X_i = \coprod_{d \geq 0} X_{i, d}$ is a disjoint union of
open and closed subschemes such that $X_{i, d} \to Y_i$
has relative dimension $d$, see
Morphisms, Lemma \ref{morphisms-lemma-syntomic-relative-dimension}.
Because of the behaviour of dimensions of fibres under base change given in
Morphisms, Lemma \ref{morphisms-lemma-dimension-fibre-after-base-change}
we see that $X \to X_i$ maps into $X_{i, 1}$.
Then there exists an $i' \geq i$ such that $X_{i'} \to X_i$
maps into $X_{i, 1}$, see
Limits, Lemma \ref{limits-lemma-limit-contained-in-constructible}.
Thus $f_{i'} : X_{i'} \to Y_{i'}$ is syntomic of relative dimension $1$
(by Morphisms, Lemma \ref{morphisms-lemma-dimension-fibre-after-base-change}
again).
Consider the morphism $\text{Sing}(f_{i'}) \to Y_{i'}$.
We know that the base change to $Y$ is an unramified morphism.
Hence by Limits, Lemma \ref{limits-lemma-descend-unramified}
we see that after increasing $i'$ the morphism
$\text{Sing}(f_{i'}) \to Y_{i'}$ becomes unramified.
This finishes the proof.


\begin{lemma}
\label{lemma-formal-local-structure-nodal-family}
Let $f : T \to S$ be a morphism of schemes. Let $t \in T$
with image $s \in S$. Assume


1.  $f$ is flat at $t$,
1.  $\mathcal{O}_{S, s}$ is Noetherian,
1.  $f$ is locally of finite type,
1.  $t$ is a split node of the fibre $T_s$.

Then there exists an $h \in \mathfrak m_s^\wedge$ and an isomorphism
$$
\mathcal{O}_{T, t}^\wedge \cong
\mathcal{O}_{S, s}^\wedge[[x, y]]/(xy - h)
$$
of $\mathcal{O}_{S, s}^\wedge$-algebras.
\end{lemma}

#### Proof

We replace $S$ by $\Spec(\mathcal{O}_{S, s})$ and $T$ by the base change
to $\Spec(\mathcal{O}_{S, s})$. Then $T$ is locally Noetherian and hence
$\mathcal{O}_{T, t}$ is Noetherian.
Set $A = \mathcal{O}_{S, s}^\wedge$, $\mathfrak m = \mathfrak m_A$, and
$B = \mathcal{O}_{T, t}^\wedge$. By
More on Algebra, Lemma \ref{more-algebra-lemma-flat-completion}
we see that $A \to B$ is flat. Since
$\mathcal{O}_{T, t}/\mathfrak m_s \mathcal{O}_{T, t} = \mathcal{O}_{T_s, t}$
we see that $B/\mathfrak m B = \mathcal{O}_{T_s, t}^\wedge$.
By assumption (4) and Lemma \ref{lemma-split-node}
we conclude there exist $\overline{u}, \overline{v} \in B/\mathfrak m B$
such that the map
$$
(A/\mathfrak m)[[x, y]] \longrightarrow B/\mathfrak m B,\quad
x \longmapsto \overline{u},
x \longmapsto \overline{v}
$$
is surjective with kernel $(xy)$.

\medskip\noindent
Assume we have $n \geq 1$ and $u, v \in B$ mapping to
$\overline{u}, \overline{v}$ such that
$$
u v = h + \delta
$$
for some $h \in A$ and $\delta \in \mathfrak m^nB$.
We claim that there exist $u', v' \in B$ with
$u - u', v - v' \in \mathfrak m^n B$ such that
$$
u' v' = h' + \delta'
$$
for some $h' \in A$ and $\delta' \in \mathfrak m^{n + 1}B$.
To see this, write $\delta = \sum f_i b_i$ with
$f_i \in \mathfrak m^n$ and $b_i \in B$. Then write
$b_i = a_i + u b_{i, 1} + v b_{i, 2} + \delta_i$ with
$a_i \in A$, $b_{i, 1}, b_{i, 2} \in B$ and $\delta_i \in \mathfrak m B$.
This is possible because the residue field of $B$ agrees with the
residue field of $A$ and the images of $u$ and $v$ in $B/\mathfrak m B$
generate the maximal ideal. Then we set
$$
u' = u - \sum b_{i, 2}f_i,\quad
v' = v - \sum b_{i, 1}f_i
$$
and we obtain
$$
u'v' = h + \delta - \sum (b_{i, 1}u + b_{i, 2}v)f_i + \sum
c_{ij}f_if_j =
h + \sum a_if_i + \sum f_i \delta_i + \sum c_{ij}f_if_j
$$
for some $c_{i, j} \in B$.
Thus we get a formula as above with $h' = h + \sum a_if_i$
and $\delta' = \sum f_i \delta_i + \sum c_{ij}f_if_j$.

\medskip\noindent
Arguing by induction and starting with any lifts $u_1, v_1 \in B$
of $\overline{u}, \overline{v}$ the result of the previous paragraph
shows that we find a sequence of elements
$u_n, v_n \in B$ and $h_n \in A$ such that
$u_n - u_{n + 1} \in \mathfrak m^n B$,
$v_n - v_{n + 1} \in \mathfrak m^n B$,
$h_n - h_{n + 1} \in \mathfrak m^n$,
and such that $u_n v_n - h_n \in \mathfrak m^n B$.
Since $A$ and $B$ are complete we can set
$u_\infty = \lim u_n$, $v_\infty = \lim v_n$,  and
$h_\infty = \lim h_n$, and then we obtain $u_\infty v_\infty = h_\infty$
in $B$. Thus we have an $A$-algebra map
$$
A[[x, y]]/(xy - h_\infty) \longrightarrow B
$$
sending $x$ to $u_\infty$ and $v$ to $v_\infty$.
This is a map of flat $A$-algebras which is an
isomorphism after dividing by $\mathfrak m$.
It is surjective modulo $\mathfrak m$ and hence surjective
by completeness and
Algebra, Lemma \ref{algebra-lemma-completion-generalities}.
Then we can apply Algebra, Lemma \ref{algebra-lemma-mod-injective}
to conclude it is an isomorphism.


\noindent
Consider the morphism of schemes
$$
\Spec(\mathbf{Z}[u, v, a]/(uv - a))
\longrightarrow
\Spec(\mathbf{Z}[a])
$$
The next lemma shows that this morphism is a model for
the \'etale local structure of a nodal family of curves.
If you know a proof of this lemma avoiding the use of Artin approximation,
then please email
\href{mailto:stacks.project@gmail.com}{stacks.project@gmail.com}.

\begin{lemma}
\label{lemma-etale-local-structure-nodal-family}
Let $f : X \to S$ be a morphism of schemes. Assume that
$f$ is at-worst-nodal of relative dimension $1$. Let
$x \in X$ be a point which is a singular point of the
fibre $X_s$. Then there exists a commutative diagram of schemes
$$
\xymatrix{
X \ar[d] &
U \ar[rr] \ar[l] \ar[rd] & &
W \ar[r] \ar[ld] &
\Spec(\mathbf{Z}[u, v, a]/(uv - a)) \ar[d] \\\\
S & &
V \ar[ll] \ar[rr] & & \Spec(\mathbf{Z}[a])
}
$$
with $X \leftarrow U$, $S \leftarrow V$, and $U \to W$ \'etale morphisms,
and with the right hand square cartesian, such that there exists
a point $u \in U$ mapping to $x$ in $X$.
\end{lemma}

#### Proof

We first use absolute Noetherian approximation to reduce to the
case of schemes of finite type over $\mathbf{Z}$.
The question is local on $X$ and $S$. Hence we may assume that
$X$ and $S$ are affine. Then we can write $S = \Spec(R)$
and write $R$ as a filtered colimit $R = \colim R_i$
of finite type $\mathbf{Z}$-algebras.
Using Limits, Lemma \ref{limits-lemma-descend-finite-presentation}
we can find an $i$ and a morphism $f_i : X_i \to \Spec(R_i)$ whose base
change to $S$ is $f$. After increasing $i$ we may assume that $f_i$
is at-worst-nodal of relative dimension $1$, see
Lemma \ref{lemma-descend-nodal-family}.
The image $x_i \in X_i$ of $x$ will be a singular
point of its fibre, for example because the formation of
$\text{Sing}(f)$ commutes with base change (Divisors, Lemma
\ref{divisors-lemma-base-change-and-fitting-ideal-omega}).
If we can prove the lemma for $f_i : X_i \to S_i$ and
$x_i$, then the lemma follows for $f : X \to S$ by base
change. Thus we reduce to the case studied in the next
paragraph.

\medskip\noindent
Assume $S$ is of finite type over $\mathbf{Z}$. Let $s \in S$ be the
image of $x$. Recall that $\kappa(x)$ is a finite separable extension
of $\kappa(s)$, for example because $\text{Sing}(f) \to S$
is unramified or because $x$ is a node of the fibre $X_s$
and we can apply Lemma \ref{lemma-nodal}.
Furthermore, let $\kappa'/\kappa(x)$ be the
degree $2$ separable algebra associated to $\mathcal{O}_{X_s, x}$ in
Remark \ref{remark-quadratic-extension}.
By More on Morphisms, Lemma
\ref{more-morphisms-lemma-realize-prescribed-residue-field-extension-etale}
we can choose an \'etale neighbourhood $(V, v) \to (S, s)$
such that the extension $\kappa(v)/\kappa(s)$ realizes either
the extension $\kappa(x)/\kappa(s)$ in case
$\kappa' \cong \kappa(x) \times \kappa(x)$ or
the extension $\kappa'/\kappa(s)$ if $\kappa'$ is a field.
After replacing $X$ by $X \times_S V$ and $S$ by $V$
we reduce to the situation described in the next paragraph.

\medskip\noindent
Assume $S$ is of finite type over $\mathbf{Z}$ and
$x \in X_s$ is a split node, see Definition \ref{definition-split-node}.
By Lemma \ref{lemma-formal-local-structure-nodal-family} we see that there
exists an $\mathcal{O}_{S, s}$-algebra isomorphism
$$
\mathcal{O}_{X, x}^\wedge \cong
\mathcal{O}_{S, s}^\wedge[[s, t]]/(st - h)
$$
for some $h \in \mathfrak m_s^\wedge \subset \mathcal{O}_{S, s}^\wedge$.
In other words, if we consider the homomorphism
$$
\sigma : \mathbf{Z}[a] \longrightarrow \mathcal{O}_{S, s}^\wedge
$$
sending $a$ to $h$, then there exists an $\mathcal{O}_{S, s}$-algebra
isomorphism
$$
\mathcal{O}_{X, x}^\wedge
\longrightarrow
\mathcal{O}_{Y_\sigma, y_\sigma}^\wedge
$$
where
$$
Y_\sigma = \Spec(\mathbf{Z}[u, v, t]/(uv - a))
\times_{\Spec(\mathbf{Z}[a]), \sigma} \Spec(\mathcal{O}_{S, s}^\wedge)
$$
and $y_\sigma$ is the point of $Y_\sigma$ lying over
the closed point of $\Spec(\mathcal{O}_{S, s}^\wedge)$
and having coordinates $u, v$ equal to zero. Since
$\mathcal{O}_{S, s}$ is a G-ring by
More on Algebra, Proposition \ref{more-algebra-proposition-ubiquity-G-ring}
we may apply More on Morphisms, Lemma
\ref{more-morphisms-lemma-relative-map-approximation-pre}
to conclude.


\begin{lemma}
\label{lemma-genus-in-nodal-family-of-curves}
Let $f : X \to S$ be a morphism of schemes. Assume


1.  $f$ is proper,
1.  $f$ is at-worst-nodal of relative dimension $1$, and
1.  the geometric fibres of $f$ are connected.

Then (a) $f_*\mathcal{O}_X = \mathcal{O}_S$ and this holds after
any base change, (b) $R^1f_*\mathcal{O}_X$ is a finite locally free
$\mathcal{O}_S$-module whose formation commutes with any base change,
and (c) $R^qf_*\mathcal{O}_X = 0$ for $q \geq 2$.
\end{lemma}

#### Proof

Part (a) follows from
Derived Categories of Schemes, Lemma
\ref{perfect-lemma-proper-flat-geom-red-connected}.
By Derived Categories of Schemes, Lemma
\ref{perfect-lemma-proper-flat-h0} locally on $S$
we can write $Rf_*\mathcal{O}_X = \mathcal{O}_S \oplus P$
where $P$ is perfect of tor amplitude in $[1, \infty)$.
Recall that formation of $Rf_*\mathcal{O}_X$ commutes
with arbitrary base change
(Derived Categories of Schemes, Lemma
\ref{perfect-lemma-flat-proper-perfect-direct-image-general}).
Thus for $s \in S$ we have
$$
H^i(P \otimes_{\mathcal{O}_S}^\mathbf{L} \kappa(s)) =
H^i(X_s, \mathcal{O}_{X_s})
\text{ for }i \geq 1
$$
This is zero unless $i = 1$ since $X_s$ is a $1$-dimensional
Noetherian scheme, see
Cohomology, Proposition \ref{cohomology-proposition-vanishing-Noetherian}.
Then $P = H^1(P)[-1]$ and $H^1(P)$ is finite locally free
for example by More on Algebra, Lemma
\ref{more-algebra-lemma-lift-perfect-from-residue-field}.
Since everything is compatible with base change we conclude.








###  More vanishing results

\label{section-more-vanishing}

\noindent
Continuation of Section \ref{section-vanishing}.

\begin{lemma}
\label{lemma-h1-nonzero-degree-leq-2g-2}
In Situation \ref{situation-Cohen-Macaulay-curve} assume $X$ is integral and
has genus $g$. Let $\mathcal{L}$ be an invertible $\mathcal{O}_X$-module.
Let $Z \subset X$ be a $0$-dimensional closed subscheme with ideal
sheaf $\mathcal{I} \subset \mathcal{O}_X$. If $H^1(X, \mathcal{I}\mathcal{L})$
is nonzero, then
$$
\deg(\mathcal{L}) \leq 2g - 2 + \deg(Z)
$$
with strict inequality unless $\mathcal{I}\mathcal{L} \cong \omega_X$.
\end{lemma}

#### Proof

Any curve, e.g.\ $X$, is Cohen-Macaulay.
If $H^1(X, \mathcal{I}\mathcal{L})$ is nonzero, then there is a nonzero
map $\mathcal{I}\mathcal{L} \to \omega_X$, see
Lemma \ref{lemma-duality-dim-1-CM}.
Since $\mathcal{I}\mathcal{L}$ is torsion free, this map is injective.
Since a field is Gorenstein and $X$ is reduced, we find
that the Gorenstein locus $U \subset X$ of $X$ is nonempty, see
Duality for Schemes, Lemma \ref{duality-lemma-gorenstein}.
This lemma also tells us that $\omega_X|_U$ is invertible.
In this way we see we have a short exact sequence
$$
0 \to \mathcal{I}\mathcal{L} \to \omega_X \to \mathcal{Q} \to 0
$$
where the support of $\mathcal{Q}$ is zero dimensional.
Hence we have
\begin{align}
0 & \leq \dim \Gamma(X, \mathcal{Q})\\
& =
\chi(\mathcal{Q}) \\\\
& =
\chi(\omega_X) - \chi(\mathcal{I}\mathcal{L}) \\\\
& =
\chi(\omega_X) - \deg(\mathcal{L}) - \chi(\mathcal{I}) \\\\
& =
2g - 2 - \deg(\mathcal{L}) + \deg(Z)
\end{align}
by Lemmas \ref{lemma-euler} and \ref{lemma-rr}, by (\ref{equation-genus}),
and by Varieties, Lemmas \ref{varieties-lemma-chi-tensor-finite}
and \ref{varieties-lemma-degree-on-proper-curve}. We have also used
that $\deg(Z) = \dim_k \Gamma(Z, \mathcal{O}_Z) = \chi(\mathcal{O}_Z)$
and the short exact sequence
$0 \to \mathcal{I} \to \mathcal{O}_X \to \mathcal{O}_Z \to 0$.
The lemma follows.


\begin{lemma}
\label{lemma-degree-more-than-2g-2}
\begin{reference}
\cite[Lemma 2]{Jongmin}
\end{reference}
In Situation \ref{situation-Cohen-Macaulay-curve}
assume $X$ is integral and has genus $g$.
Let $\mathcal{L}$ be an invertible $\mathcal{O}_X$-module.
Let $Z \subset X$ be a $0$-dimensional closed subscheme with ideal
sheaf $\mathcal{I} \subset \mathcal{O}_X$.
If $\deg(\mathcal{L}) > 2g - 2 + \deg(Z)$, then
$H^1(X, \mathcal{I}\mathcal{L}) = 0$ and one of the following possibilities
occurs


1.  $H^0(X, \mathcal{I}\mathcal{L}) \not = 0$, or
1.  $g = 0$ and $\deg(\mathcal{L}) = \deg(Z) - 1$.

In case (2) if $Z = \emptyset$, then $X \cong \mathbf{P}^1_k$ and $\mathcal{L}$
corresponds to $\mathcal{O}_{\mathbf{P}^1}(-1)$.
\end{lemma}

#### Proof

The vanishing of $H^1(X, \mathcal{I}\mathcal{L})$ follows from
Lemma \ref{lemma-h1-nonzero-degree-leq-2g-2}.
If $H^0(X, \mathcal{I}\mathcal{L}) = 0$, then
$\chi(\mathcal{I}\mathcal{L}) = 0$. From the short exact
sequence $0 \to \mathcal{I}\mathcal{L} \to \mathcal{L} \to \mathcal{O}_Z \to 0$
we conclude $\deg(\mathcal{L}) = g - 1 + \deg(Z)$.
Thus $g - 1 + \deg(Z) > 2g - 2 + \deg(Z)$ which implies $g = 0$
hence (2) holds. If $Z = \emptyset$ in case (2),
then $\mathcal{L}^{-1}$ is an invertible sheaf of degree $1$.
This implies there is an isomorphism $X \to \mathbf{P}^1_k$ and
$\mathcal{L}^{-1}$ is the pullback of $\mathcal{O}_{\mathbf{P}^1}(1)$ by
Lemma \ref{lemma-genus-zero-positive-degree}.


\begin{lemma}
\label{lemma-degree-more-than-2g}
\begin{reference}
\cite[Lemma 3]{Jongmin}
\end{reference}
In Situation \ref{situation-Cohen-Macaulay-curve}
assume $X$ is integral and has genus $g$.
Let $\mathcal{L}$ be an invertible $\mathcal{O}_X$-module.
If $\deg(\mathcal{L}) \geq 2g$, then $\mathcal{L}$
is globally generated.
\end{lemma}

#### Proof

Let $Z \subset X$ be the closed subscheme cut out by the
global sections of $\mathcal{L}$. By Lemma \ref{lemma-degree-more-than-2g-2}
we see that $Z \not = X$. Let $\mathcal{I} \subset \mathcal{O}_X$
be the ideal sheaf cutting out $Z$. Consider the short exact sequence
$$
0 \to \mathcal{I}\mathcal{L}
\to \mathcal{L} \to \mathcal{O}_Z \to 0
$$
If $Z \not = \emptyset$, then
$H^1(X, \mathcal{I}\mathcal{L})$ is nonzero
as follows from the long exact sequence of cohomology.
By Lemma \ref{lemma-duality-dim-1-CM} this gives a
nonzero and hence injective map
$$
\mathcal{I}\mathcal{L}
\longrightarrow
\omega_X
$$
In particular, we find an injective map
$H^0(X, \mathcal{L}) = H^0(X, \mathcal{I}\mathcal{L})
\to H^0(X, \omega_X)$. This is impossible as
$$
\dim_k H^0(X, \mathcal{L}) = \dim_k H^1(X, \mathcal{L}) +
\deg(\mathcal{L}) + 1 - g \geq g + 1
$$
and $\dim H^0(X, \omega_X) = g$ by (\ref{equation-genus}).


\begin{lemma}
\label{lemma-degree-more-than-2g-1-and-Z}
In Situation \ref{situation-Cohen-Macaulay-curve}
assume $X$ is integral and has genus $g$.
Let $\mathcal{L}$ be an invertible $\mathcal{O}_X$-module.
Let $Z \subset X$ be a nonempty $0$-dimensional closed subscheme.
If $\deg(\mathcal{L}) \geq 2g - 1 + \deg(Z)$, then $\mathcal{L}$
is globally generated and $H^0(X, \mathcal{L}) \to H^0(X, \mathcal{L}|_Z)$
is surjective.
\end{lemma}

#### Proof

Global generation by Lemma \ref{lemma-degree-more-than-2g}.
If $\mathcal{I} \subset \mathcal{O}_X$ is the ideal sheaf
of $Z$, then $H^1(X, \mathcal{I}\mathcal{L}) = 0$ by
Lemma \ref{lemma-h1-nonzero-degree-leq-2g-2}. Hence surjectivity.


\begin{lemma}
\label{lemma-degree-at-least-2g+1}
In Situation \ref{situation-Cohen-Macaulay-curve},
assume $X$ is geometrically integral over $k$ and has genus $g$.
Let $\mathcal{L}$ be an invertible $\mathcal{O}_X$-module.
If $\deg(\mathcal{L}) \geq 2g + 1$, then $\mathcal{L}$
is very ample.
\end{lemma}

#### Proof

By Lemma \ref{lemma-degree-more-than-2g}, $\mathcal{L}$
is globally generated, and so it determines a morphism
$f : X \to \mathbf{P}^n_k$ where $n = h^0(X,\mathcal{L}) - 1$. To show that
$\mathcal{L}$ is very ample means to show that
$f$ is a closed immersion. It suffices to check that the base change
of $f$ to an algebraic closure $\overline{k}$ of $k$ is a closed immersion
(Descent, Lemma \ref{descent-lemma-descending-property-closed-immersion}).
So we may assume that $k$ is algebraically closed; $X$ remains
integral, by assumption. Lemma \ref{lemma-degree-more-than-2g-1-and-Z}
gives that for every $0$-dimensional closed subscheme
$Z\subset X$ of degree 2,
the restriction map $H^0(X, \mathcal{L}) \to H^0(X, \mathcal{L}|_Z)$
is surjective. By Varieties, Lemma
\ref{varieties-lemma-variant-separate-points-tangent-vectors},
$\mathcal{L}$ is very ample.



\begin{lemma}
\label{lemma-vanishing-on-gorenstein}
\begin{reference}
Weak version of \cite[Lemma 4]{Jongmin}
\end{reference}
Let $k$ be a field. Let $X$ be a proper scheme over $k$
which is reduced, connected, and of dimension $1$.
Let $\mathcal{L}$ be an invertible $\mathcal{O}_X$-module.
Let $Z \subset X$ be a $0$-dimensional closed subscheme with ideal
sheaf $\mathcal{I} \subset \mathcal{O}_X$.
If $H^1(X, \mathcal{I}\mathcal{L}) \not = 0$, then there exists
a reduced connected closed subscheme $Y \subset X$
of dimension $1$ such that
$$
\deg(\mathcal{L}|_Y) \leq -2\chi(Y, \mathcal{O}_Y) + \deg(Z \cap Y)
$$
where $Z \cap Y$ is the scheme theoretic intersection.
\end{lemma}

#### Proof

If $H^1(X, \mathcal{I}\mathcal{L})$ is nonzero, then there is a nonzero map
$\varphi : \mathcal{I}\mathcal{L} \to \omega_X$, see
Lemma \ref{lemma-duality-dim-1-CM}. Let $Y \subset X$
be the union of the irreducible components $C$ of $X$ such that
$\varphi$ is nonzero in the generic point of $C$.
Then $Y$ is a reduced closed subscheme.
Let $\mathcal{J} \subset \mathcal{O}_X$ be the ideal sheaf of $Y$.
Since $\mathcal{J}\mathcal{I}\mathcal{L}$
has no embedded associated points
(as a submodule of $\mathcal{L}$) and as $\varphi$ is zero
in the generic points of the support of $\mathcal{J}$
(by choice of $Y$ and as $X$ is reduced), we find that
$\varphi$ factors as
$$
\mathcal{I}\mathcal{L} \to
\mathcal{I}\mathcal{L}/\mathcal{J}\mathcal{I}\mathcal{L} \to \omega_X
$$
We can view $\mathcal{I}\mathcal{L}/\mathcal{J}\mathcal{I}\mathcal{L}$
as the pushforward of a coherent sheaf on $Y$ which by abuse of
notation we indicate with the same symbol.
Since $\omega_Y = \SheafHom(\mathcal{O}_Y, \omega_X)$
by Lemma \ref{lemma-closed-immersion-dim-1-CM}
we find a map
$$
\mathcal{I}\mathcal{L}/
\mathcal{J}\mathcal{I}\mathcal{L}
\to \omega_Y
$$
of $\mathcal{O}_Y$-modules which is injective in the generic points
of $Y$. Let $\mathcal{I}' \subset \mathcal{O}_Y$ be the ideal
sheaf of $Z \cap Y$. There is a map
$\mathcal{I}\mathcal{L}/\mathcal{J}\mathcal{I}\mathcal{L} \to
\mathcal{I}'\mathcal{L}|_Y$ whose kernel is supported in closed points.
Since $\omega_Y$ is a Cohen-Macaulay module, the map above
factors through an injective map $\mathcal{I}'\mathcal{L}|_Y \to
\omega_Y$. We see that we get
an exact sequence
$$
0 \to \mathcal{I}'\mathcal{L}|_Y \to \omega_Y \to \mathcal{Q} \to 0
$$
of coherent sheaves on $Y$ where $\mathcal{Q}$ is supported in dimension $0$
(this uses that $\omega_Y$ is an invertible module in the generic points
of $Y$). We conclude that
$$
0 \leq \dim \Gamma(Y, \mathcal{Q}) =
\chi(\mathcal{Q}) = \chi(\omega_Y) - \chi(\mathcal{I}'\mathcal{L}) =
-2\chi(\mathcal{O}_Y) - \deg(\mathcal{L}|_Y) + \deg(Z \cap Y)
$$
by Lemma \ref{lemma-euler} and
Varieties, Lemma \ref{varieties-lemma-chi-tensor-finite}.
If $Y$ is connected, then this proves the lemma.
If not, then we repeat the last part of the argument
for one of the connected components of $Y$.


\begin{lemma}
\label{lemma-global-generation}
Let $k$ be a field. Let $X$ be a proper scheme over $k$
which is reduced, connected, and of dimension $1$.
Let $\mathcal{L}$ be an invertible $\mathcal{O}_X$-module.
Assume that for every reduced connected closed subscheme
$Y \subset X$ of dimension $1$ we have
$$
\deg(\mathcal{L}|_Y) \geq 2\dim_k H^1(Y, \mathcal{O}_Y)
$$
Then $\mathcal{L}$ is globally generated.
\end{lemma}

#### Proof

By induction on the number of irreducible components of $X$.
If $X$ is irreducible, then the lemma holds by
Lemma \ref{lemma-degree-more-than-2g}
applied to $X$ viewed as a scheme over the field
$k' = H^0(X, \mathcal{O}_X)$. Assume $X$ is not irreducible.
Before we continue, if $k$ is finite, then we replace $k$
by a purely transcendental extension $K$. This is allowed by
Varieties, Lemmas
\ref{varieties-lemma-globally-generated-base-change},
\ref{varieties-lemma-degree-base-change},
\ref{varieties-lemma-geometrically-reduced-any-base-change}, and
\ref{varieties-lemma-bijection-irreducible-components},
Cohomology of Schemes, Lemma \ref{coherent-lemma-flat-base-change-cohomology},
Lemma \ref{lemma-sanity-check-duality} and the elementary fact that
$K$ is geometrically integral over $k$.

\medskip\noindent
Assume that $\mathcal{L}$ is not globally generated to get a contradiction.
Then we may choose a coherent ideal sheaf
$\mathcal{I} \subset \mathcal{O}_X$ such that
$H^0(X, \mathcal{I}\mathcal{L}) = H^0(X, \mathcal{L})$
and such that $\mathcal{O}_X/\mathcal{I}$ is nonzero with
support of dimension $0$. For example, take $\mathcal{I}$
the ideal sheaf of any closed point in the common
vanishing locus of the global sections of $\mathcal{L}$.
We consider the short exact sequence
$$
0 \to \mathcal{I}\mathcal{L} \to \mathcal{L} \to
\mathcal{L}/\mathcal{I}\mathcal{L} \to 0
$$
Since the support of $\mathcal{L}/\mathcal{I}\mathcal{L}$
has dimension $0$ we see that $\mathcal{L}/\mathcal{I}\mathcal{L}$
is generated by global sections
(Varieties, Lemma \ref{varieties-lemma-chi-tensor-finite}).
From the short exact sequence,
and the fact that $H^0(X, \mathcal{I}\mathcal{L}) = H^0(X, \mathcal{L})$
we get an injection
$H^0(X, \mathcal{L}/\mathcal{I}\mathcal{L}) \to H^1(X, \mathcal{I}\mathcal{L})$.

\medskip\noindent
Recall that the $k$-vector space $H^1(X, \mathcal{I}\mathcal{L})$
is dual to $\Hom(\mathcal{I}\mathcal{L}, \omega_X)$.
Choose $\varphi : \mathcal{I}\mathcal{L} \to \omega_X$.
By Lemma \ref{lemma-vanishing-on-gorenstein} we have
$H^1(X, \mathcal{L}) = 0$. Hence
$$
\dim_k H^0(X, \mathcal{I}\mathcal{L}) = \dim_k H^0(X, \mathcal{L}) =
\deg(\mathcal{L}) + \chi(\mathcal{O}_X) > \dim_k H^1(X, \mathcal{O}_X) =
\dim_k H^0(X, \omega_X)
$$
We conclude that $\varphi$ is not injective on global sections, in particular
$\varphi$ is not injective. For every generic point $\eta \in X$
of an irreducible component of $X$ denote
$V_\eta \subset \Hom(\mathcal{I}\mathcal{L}, \omega_X)$ the $k$-subvector
space consisting of those $\varphi$ which are zero at $\eta$.
Since every associated point of $\mathcal{I}\mathcal{L}$
is a generic point of $X$, the above shows that
$\Hom(\mathcal{I}\mathcal{L}, \omega_X) = \bigcup V_\eta$.
As $X$ has finitely many generic points and $k$ is infinite, we conclude
$\Hom(\mathcal{I}\mathcal{L}, \omega_X) = V_\eta$ for some $\eta$.
Let $\eta \in C \subset X$ be the corresponding irreducible component.
Let $Y \subset X$ be the union of the other irreducible components
of $X$. Then $Y$ is a nonempty reduced closed subscheme not equal to $X$.
Let $\mathcal{J} \subset \mathcal{O}_X$ be the ideal sheaf of $Y$.
Please keep in mind that the support of $\mathcal{J}$ is $C$.

\medskip\noindent
Let $\varphi : \mathcal{I}\mathcal{L} \to \omega_X$ be arbitrary.
Since $\mathcal{J}\mathcal{I}\mathcal{L}$
has no embedded associated points
(as a submodule of $\mathcal{L}$) and as $\varphi$ is zero
in the generic point $\eta$ of the support of $\mathcal{J}$, we find that
$\varphi$ factors as
$$
\mathcal{I}\mathcal{L} \to
\mathcal{I}\mathcal{L}/\mathcal{J}\mathcal{I}\mathcal{L} \to \omega_X
$$
We can view $\mathcal{I}\mathcal{L}/\mathcal{J}\mathcal{I}\mathcal{L}$
as the pushforward of a coherent sheaf on $Y$ which by abuse of
notation we indicate with the same symbol.
Since $\omega_Y = \SheafHom(\mathcal{O}_Y, \omega_X)$
by Lemma \ref{lemma-closed-immersion-dim-1-CM}
we find a factorization
$$
\mathcal{I}\mathcal{L} \to
\mathcal{I}\mathcal{L}/
\mathcal{J}\mathcal{I}\mathcal{L}
\xrightarrow{\varphi'} \omega_Y \to \omega_X
$$
of $\varphi$. Let $\mathcal{I}' \subset \mathcal{O}_Y$ be the
image of $\mathcal{I} \subset \mathcal{O}_X$. There is a surjective map
$\mathcal{I}\mathcal{L}/\mathcal{J}\mathcal{I}\mathcal{L} \to
\mathcal{I}'\mathcal{L}|_Y$ whose kernel is supported in closed points.
Since $\omega_Y$ is a Cohen-Macaulay module on $Y$, the map $\varphi'$
factors through a map
$\varphi'' : \mathcal{I}'\mathcal{L}|_Y \to \omega_Y$.
Thus we have commutative diagrams
$$
\vcenter{
\xymatrix{
0 \ar[r] &
\mathcal{I}\mathcal{L} \ar[r] \ar[d] &
\mathcal{L} \ar[r] \ar[d] &
\mathcal{L}/\mathcal{I}\mathcal{L} \ar[r] \ar[d] &
0 \\\\
0 \ar[r] &
\mathcal{I}'\mathcal{L}|_Y \ar[r] &
\mathcal{L}|_Y \ar[r] &
\mathcal{L}|_Y/\mathcal{I}'\mathcal{L}|_Y \ar[r] &
0
}
}
\quad\text{and}\quad
\vcenter{
\xymatrix{
\mathcal{I}\mathcal{L} \ar[r]_\varphi \ar[d] & \omega_X \\\\
\mathcal{I}'\mathcal{L}|_Y \ar[r]^{\varphi''} & \omega_Y \ar[u]
}
}
$$
Now we can finish the proof as follows:
Since for every $\varphi$ we have a $\varphi''$ and since
$\omega_X \in \textit{Coh}(\mathcal{O}_X)$
represents the functor $\mathcal{F} \mapsto \Hom_k(H^1(X, \mathcal{F}), k)$,
we find that
$H^1(X, \mathcal{I}\mathcal{L}) \to H^1(Y, \mathcal{I}'\mathcal{L}|_Y)$
is injective. Since the boundary
$H^0(X, \mathcal{L}/\mathcal{I}\mathcal{L}) \to H^1(X, \mathcal{I}\mathcal{L})$
is injective, we conclude the composition
$$
H^0(X, \mathcal{L}/\mathcal{I}\mathcal{L}) \to
H^0(X, \mathcal{L}|_Y/\mathcal{I}'\mathcal{L}|_Y) \to
H^1(X, \mathcal{I}'\mathcal{L}|_Y)
$$
is injective. Since
$\mathcal{L}/\mathcal{I}\mathcal{L} \to
\mathcal{L}|_Y/\mathcal{I}'\mathcal{L}|_Y$
is a surjective map of coherent modules whose supports have
dimension $0$, we see that the first map
$H^0(X, \mathcal{L}/\mathcal{I}\mathcal{L}) \to
H^0(X, \mathcal{L}|_Y/\mathcal{I}'\mathcal{L}|_Y)$
is surjective (and hence bijective).
But by induction we have that $\mathcal{L}|_Y$ is globally
generated (if $Y$ is disconnected this still works of course)
and hence the boundary map
$$
H^0(X, \mathcal{L}|_Y/\mathcal{I}'\mathcal{L}|_Y) \to
H^1(X, \mathcal{I}'\mathcal{L}|_Y)
$$
cannot be injective.
This contradiction finishes the proof.






###  Contracting rational tails

\label{section-contracting-rational-tails}

\noindent
In this section we discuss the simplest possible case of contracting
a scheme to improve positivity properties of its canonical sheaf.

\begin{example}[Contracting a rational tail]
\label{example-rational-tail}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Assume the singularities of $X$ are
at-worst-nodal.
A {\it rational tail} will be an irreducible component $C \subset X$
(viewed as an integral closed subscheme) with the following properties


1.  $X' \not = \emptyset$ where $X' \subset X$ is the scheme theoretic closure
of $X \setminus C$,
1.  the scheme theoretic intersection $C \cap X'$ is a single
reduced point $x$,
1.  $H^0(C, \mathcal{O}_C)$ maps isomorphically to the
residue field of $x$, and
1.  $C$ has genus zero.

Since there are at least two irreducible components of $X$ passing through
$x$, we conclude that $x$ is a node.
Set $k' = H^0(C, \mathcal{O}_C) = \kappa(x)$.
Then $k'/k$ is a finite separable extension of fields
(Lemma \ref{lemma-nodal}). There is a canonical morphism
$$
c : X \longrightarrow X'
$$
inducing the identity on $X'$ and mapping $C$ to $x \in X'$
via the canonical morphism $C \to \Spec(k') = x$. This follows from
Morphisms, Lemma \ref{morphisms-lemma-scheme-theoretic-union}
since $X$ is the scheme theoretic union of $C$ and $X'$ (as $X$ is reduced).
Moreover, we claim that
$$
c_*\mathcal{O}_X = \mathcal{O}_{X'}
\quad\text{and}\quad
R^1c_*\mathcal{O}_X = 0
$$
To see this, denote $i_C : C \to X$, $i_{X'} : X' \to X$ and $i_x : x \to X$
the embeddings and use the exact sequence
$$
0 \to \mathcal{O}_X \to
i_{C, *}\mathcal{O}_C \oplus i_{X', *}\mathcal{O}_{X'} \to
i_{x, *}\kappa(x) \to 0
$$
of Morphisms, Lemma \ref{morphisms-lemma-scheme-theoretic-union}.
Looking at the long exact sequence of higher direct images,
it follows that it suffices to show $H^0(C, \mathcal{O}_C) = k'$
and $H^1(C, \mathcal{O}_C) = 0$ which follows from the assumptions.
Observe that $X'$ is also a proper scheme over $k$, of dimension $1$
whose singularities are at-worst-nodal
(Lemma \ref{lemma-closed-subscheme-nodal-curve})
has $H^0(X', \mathcal{O}_{X'}) = k$, and
$X'$ has the same genus as $X$.
We will say $c : X \to X'$ is the
{\it contraction of a rational tail}.
\end{example}

\begin{lemma}
\label{lemma-rational-tail-negative}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Assume the singularities of $X$ are
at-worst-nodal. Let $C \subset X$ be a rational tail
(Example \ref{example-rational-tail}). Then $\deg(\omega_X|_C) < 0$.
\end{lemma}

#### Proof

Let $X' \subset X$ be as in the example. Then we have a short exact
sequence
$$
0 \to \omega_C \to \omega_X|_C \to \mathcal{O}_{C \cap X'} \to 0
$$
See Lemmas \ref{lemma-closed-subscheme-reduced-gorenstein},
\ref{lemma-facts-about-nodal-curves}, and
\ref{lemma-closed-subscheme-nodal-curve}.
With $k'$ as in the example we see that $\deg(\omega_C) = -2[k' : k]$
as $C \cong \mathbf{P}^1_{k'}$ by Proposition \ref{proposition-projective-line}
and $\deg(C \cap X') = [k' : k]$.
Hence $\deg(\omega_X|_C) = -[k' : k]$ which is negative.


\begin{lemma}
\label{lemma-rational-tail-field-extension}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Assume the singularities of $X$ are
at-worst-nodal. Let $C \subset X$ be a rational tail
(Example \ref{example-rational-tail}).
For any field extension $K/k$ the base change $C_K \subset X_K$
is a finite disjoint union of rational tails.
\end{lemma}

#### Proof

Let $x \in C$ and $k' = \kappa(x)$ be as in the example.
Observe that $C \cong \mathbf{P}^1_{k'}$ by
Proposition \ref{proposition-projective-line}.
Since $k'/k$ is finite separable, we see that
$k' \otimes_k K = K'_1 \times \ldots \times K'_n$
is a finite product of finite separable extensions $K'_i/K$.
Set $C_i = \mathbf{P}^1_{K'_i}$ and denote $x_i \in C_i$
the inverse image of $x$. Then $C_K = \coprod C_i$ and
$X'_K \cap C_i = x_i$ as desired.


\begin{lemma}
\label{lemma-no-rational-tail}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Assume the singularities of $X$ are
at-worst-nodal. If $X$ does not have a rational tail
(Example \ref{example-rational-tail}),
then for every reduced connected closed subscheme
$Y \subset X$, $Y \not = X$ of dimension $1$ we have
$\deg(\omega_X|_Y) \geq \dim_k H^1(Y, \mathcal{O}_Y)$.
\end{lemma}

#### Proof

Let $Y \subset X$ be as in the statement. Then $k' = H^0(Y, \mathcal{O}_Y)$
is a field and a finite extension of $k$ and $[k' : k]$
divides all numerical invariants below associated to $Y$ and
coherent sheaves on $Y$, see
Varieties, Lemma \ref{varieties-lemma-divisible}.
Let $Z \subset X$ be as in
Lemma \ref{lemma-closed-subscheme-reduced-gorenstein}.
We will use the results of this lemma and of
Lemmas \ref{lemma-facts-about-nodal-curves} and
\ref{lemma-closed-subscheme-nodal-curve} without further mention.
Then we get a short exact sequence
$$
0 \to \omega_Y \to \omega_X|_Y \to \mathcal{O}_{Y \cap Z} \to 0
$$
See Lemma \ref{lemma-closed-subscheme-reduced-gorenstein}.
We conclude that
$$
\deg(\omega_X|_Y) = \deg(Y \cap Z) + \deg(\omega_Y) =
\deg(Y \cap Z) - 2\chi(Y, \mathcal{O}_Y)
$$
Hence, if the lemma is false, then
$$
2[k' : k] > \deg(Y \cap Z) + \dim_k H^1(Y, \mathcal{O}_Y)
$$
Since $Y \cap Z$ is nonempty and by the divisiblity mentioned above,
this can happen only if $Y \cap Z$ is a single $k'$-rational point
of the smooth locus of $Y$ and $H^1(Y, \mathcal{O}_Y) = 0$.
If $Y$ is irreducible, then this implies $Y$ is a rational tail.
If $Y$ is reducible, then since $\deg(\omega_X|_Y) = -[k' : k]$
we find there is some irreducible component $C$ of $Y$
such that $\deg(\omega_X|_C) < 0$, see
Varieties, Lemma \ref{varieties-lemma-degree-in-terms-of-components}.
Then the analysis above applied
to $C$ gives that $C$ is a rational tail.


\begin{lemma}
\label{lemma-no-rational-tail-semiample-genus-geq-2}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Assume the singularities of $X$ are
at-worst-nodal. Assume $X$ does not have a rational tail
(Example \ref{example-rational-tail}). If


1.  the genus of $X$ is $0$, then $X$ is isomorphic to an
irreducible plane conic and $\omega_X^{\otimes -1}$ is very ample,
1.  the genus of $X$ is $1$, then $\omega_X \cong \mathcal{O}_X$,
1.  the genus of $X$ is $\geq 2$, then
$\omega_X^{\otimes m}$ is globally generated for $m \geq 2$.

\end{lemma}

#### Proof

By Lemma \ref{lemma-facts-about-nodal-curves} we find that $X$ is
Gorenstein, i.e., $\omega_X$ is an invertible $\mathcal{O}_X$-module.

\medskip\noindent
If the genus of $X$ is zero, then $\deg(\omega_X) < 0$, hence if
$X$ has more than one irreducible component, we get a contradiction
with Lemma \ref{lemma-no-rational-tail}. In the irreducible case
we see that $X$ is isomorphic to an irreducible plane conic and
$\omega_X^{\otimes -1}$ is very ample by Lemma \ref{lemma-genus-zero}.

\medskip\noindent
If the genus of $X$ is $1$, then $\omega_X$ has a global section and
$\deg(\omega_X|_C) = 0$ for all irreducible components.
Namely, $\deg(\omega_X|_C) \geq 0$ for all irreducible components $C$
by Lemma \ref{lemma-no-rational-tail}, the sum of these numbers is
$0$ by Lemma \ref{lemma-genus-gorenstein}, and we can apply
Varieties, Lemma \ref{varieties-lemma-degree-in-terms-of-components}.
Then $\omega_X \cong \mathcal{O}_X$ by
Varieties, Lemma \ref{varieties-lemma-no-sections-dual-nef}.

\medskip\noindent
Assume the genus $g$ of $X$ is greater than or equal to $2$.
If $X$ is irreducible, then we are done by
Lemma \ref{lemma-degree-more-than-2g}.
Assume $X$ reducible.
By Lemma \ref{lemma-no-rational-tail} the
inequalities of Lemma \ref{lemma-global-generation}
hold for every $Y \subset X$ as in the statement, except for
$Y = X$. Analyzing the proof of Lemma \ref{lemma-global-generation}
we see that (in the reducible case) the only inequality
used for $Y = X$ are
$$
\deg(\omega_X^{\otimes m}) > -2 \chi(\mathcal{O}_X)
\quad\text{and}\quad
\deg(\omega_X^{\otimes m}) + \chi(\mathcal{O}_X) > \dim_k H^1(X, \mathcal{O}_X)
$$
Since these both hold under the assumption $g \geq 2$ and $m \geq 2$ we win.


\begin{lemma}
\label{lemma-contracting-rational-tails}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ of dimension $1$
with $H^0(X, \mathcal{O}_X) = k$. Assume the singularities of $X$ are
at-worst-nodal. Consider a sequence
$$
X = X_0 \to X_1 \to \ldots \to X_n = X'
$$
of contractions of rational tails (Example \ref{example-rational-tail})
until none are left. Then


1.  if the genus of $X$ is $0$, then $X'$ is an irreducible
plane conic,
1.  if the genus of $X$ is $1$, then $\omega_{X'} \cong \mathcal{O}_X$,
1.  if the genus of $X$ is $> 1$, then
$\omega_{X'}^{\otimes m}$ is globally generated for $m \geq 2$.

If the genus of $X$ is $\geq 1$, then the morphism $X \to X'$
is independent of choices and formation of this morphism
commutes with base field extensions.
\end{lemma}

#### Proof

We proceed by contracting rational tails until there are none
left. Then we see that (1), (2), (3) hold by
Lemma \ref{lemma-no-rational-tail-semiample-genus-geq-2}.

\medskip\noindent
Uniqueness. To see that $f : X \to X'$ is independent of the choices
made, it suffices to show: any rational tail $C \subset X$ is
mapped to a point by $X \to X'$; some details omitted.
If not, then we can find a section
$s \in \Gamma(X', \omega_{X'}^{\otimes 2})$ which does
not vanish in the generic point of the irreducible component $f(C)$.
Since in each of the contractions $X_i \to X_{i + 1}$
we have a section $X_{i + 1} \to X_i$, there is a section
$X' \to X$ of $f$. Then we have an exact sequence
$$
0 \to \omega_{X'} \to \omega_X \to \omega_X|_{X''} \to 0
$$
where $X'' \subset X$ is the union of the irreducible components
contracted by $f$. See Lemma \ref{lemma-closed-subscheme-reduced-gorenstein}.
Thus we get a map $\omega_{X'}^{\otimes 2} \to \omega_X^{\otimes 2}$
and we can take the image of $s$ to get a section of
$\omega_X^{\otimes 2}$ not vanishing in the generic point of $C$.
This is a contradiction with the fact that the restriction of
$\omega_X$ to a rational tail has negative degree
(Lemma \ref{lemma-rational-tail-negative}).

\medskip\noindent
The statement on base field extensions follows from
Lemma \ref{lemma-rational-tail-field-extension}. Some details omitted.






###  Contracting rational bridges

\label{section-contracting-rational-bridges}

\noindent
In this section we discuss the next simplest possible case (after the case
discussed in Section \ref{section-contracting-rational-tails}) of contracting
a scheme to improve positivity properties of its canonical sheaf.

\begin{example}[Contracting a rational bridge]
\label{example-rational-bridge}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Assume the singularities of $X$ are
at-worst-nodal.
A {\it rational bridge} will be an irreducible component $C \subset X$
(viewed as an integral closed subscheme) with the following properties


1.  $X' \not = \emptyset$ where $X' \subset X$ is the scheme theoretic closure
of $X \setminus C$,
1.  the scheme theoretic interesection $C \cap X'$
has degree $2$ over $H^0(C, \mathcal{O}_C)$, and
1.  $C$ has genus zero.

Set $k' = H^0(C, \mathcal{O}_C)$ and
$k'' = H^0(C \cap X', \mathcal{O}_{C \cap X'})$.
Then $k'$ is a field (Varieties, Lemma
\ref{varieties-lemma-proper-geometrically-reduced-global-sections})
and $\dim_{k'}(k'') = 2$. Since there are at least
two irreducible components of $X$ passing through
each point of $C \cap X'$, we conclude these points are nodes of $X$
and smooth points on both $C$ and $X'$
(Lemma \ref{lemma-closed-subscheme-nodal-curve}).
Hence $k'/k$ is a finite separable extension of fields
and $k''/k'$ is either a degree $2$ separable extension of fields
or $k'' = k' \times k'$ (Lemma \ref{lemma-nodal}). By
Section \ref{section-pushouts} there exists a pushout
$$
\xymatrix{
C \cap X' \ar[r] \ar[d] &
X' \ar[d]^a \\\\
\Spec(k') \ar[r] &
Y
}
$$
with many good properties (all of which we will use below without
futher mention). Let $y \in Y$ be the image of $\Spec(k') \to Y$.
Then
$$
\mathcal{O}_{Y, y}^\wedge \cong k'[[s, t]]/(st)
\quad\text{or}\quad
\mathcal{O}_{Y, y}^\wedge \cong
\{f \in k''[[s]] : f(0) \in k'\}
$$
depending on whether $C \cap X'$ has $2$ or $1$ points.
This follows from Lemma \ref{lemma-complete-local-ring-pushout}
and the fact that $\mathcal{O}_{X', p} \cong \kappa(p)[[t]]$
for $p \in C \cap X'$ by More on Algebra, Lemma
\ref{more-algebra-lemma-power-series-over-residue-field}.
Thus we see that $y \in Y$ is a node, see Lemmas \ref{lemma-nodal}
and \ref{lemma-2-branches-delta-1} and in particular the discussion
of Case II in the proof of (2) $\Rightarrow$ (1) in
Lemma \ref{lemma-2-branches-delta-1}.
Thus the singularities of $Y$ are at-worst-nodal.

\medskip\noindent
We can extend the commutative diagram above to a diagram
$$
\xymatrix{
C \cap X' \ar[r] \ar[d] &
X' \ar[d]^a \ar[r] & X \ar[ld]^c &
C \ar[ld] \ar[l] \\\\
\Spec(k') \ar[r] &
Y &
\Spec(k') \ar[l]
}
$$
where the two lower horizontal arrows are the same. Namely, $X$ is the
scheme theoretic union of $X'$ and $C$ (thus a pushout by
Morphisms, Lemma \ref{morphisms-lemma-scheme-theoretic-union})
and the morphisms $C \to Y$ and $X' \to Y$ agree on $C \cap X'$.
Finally, we claim that
$$
c_*\mathcal{O}_X = \mathcal{O}_Y
\quad\text{and}\quad
R^1c_*\mathcal{O}_X = 0
$$
To see this use the exact sequence
$$
0 \to \mathcal{O}_X \to
\mathcal{O}_C \oplus \mathcal{O}_{X'} \to
\mathcal{O}_{C \cap X'} \to 0
$$
of Morphisms, Lemma \ref{morphisms-lemma-scheme-theoretic-union}.
The long exact sequence of higher direct images is
$$
0 \to c_*\mathcal{O}_X \to c_*\mathcal{O}_C \oplus c_*\mathcal{O}_{X'} \to
c_*\mathcal{O}_{C \cap X'} \to
R^1c_*\mathcal{O}_X \to
R^1c_*\mathcal{O}_C \oplus R^1c_*\mathcal{O}_{X'}
$$
Since $c|_{X'} = a$ is affine we see that
$R^1c_*\mathcal{O}_{X'} = 0$.
Since $c|_C$ factors as $C \to \Spec(k') \to X$ and since
$C$ has genus zero, we find that $R^1c_*\mathcal{O}_C = 0$.
Since $\mathcal{O}_{X'} \to \mathcal{O}_{C \cap X'}$ is
surjective and since $c|_{X'}$ is affine, we see that
$c_*\mathcal{O}_{X'} \to c_*\mathcal{O}_{C \cap X'}$
is surjective. This proves that $R^1c_*\mathcal{O}_X = 0$.
Finally, we have
$\mathcal{O}_Y = c_*\mathcal{O}_X$ by
the exact sequence and
the description of the structure sheaf of the pushout
in More on Morphisms, Proposition
\ref{more-morphisms-proposition-pushout-along-closed-immersion-and-integral}.

\medskip\noindent
All of this means that $Y$ is also a proper scheme over $k$
having dimension $1$ and $H^0(Y, \mathcal{O}_Y) = k$
whose singularities are at-worst-nodal
(Lemma \ref{lemma-closed-subscheme-nodal-curve})
and that $Y$ has the same genus as $X$.
We will say $c : X \to Y$ is the
{\it contraction of a rational bridge}.
\end{example}

\begin{lemma}
\label{lemma-rational-bridge-zero}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Assume the singularities of $X$ are
at-worst-nodal. Let $C \subset X$ be a rational bridge
(Example \ref{example-rational-bridge}). Then $\deg(\omega_X|_C) = 0$.
\end{lemma}

#### Proof

Let $X' \subset X$ be as in the example. Then we have a short exact
sequence
$$
0 \to \omega_C \to \omega_X|_C \to \mathcal{O}_{C \cap X'} \to 0
$$
See Lemmas \ref{lemma-closed-subscheme-reduced-gorenstein},
\ref{lemma-facts-about-nodal-curves}, and
\ref{lemma-closed-subscheme-nodal-curve}.
With $k''/k'/k$ as in the example we see that
$\deg(\omega_C) = -2[k' : k]$ as $C$ has genus $0$
(Lemma \ref{lemma-rr})
and $\deg(C \cap X') = [k'' : k] = 2[k' : k]$.
Hence $\deg(\omega_X|_C) = 0$.


\begin{lemma}
\label{lemma-rational-bridge-field-extension}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Assume the singularities of $X$ are
at-worst-nodal. Let $C \subset X$ be a rational bridge
(Example \ref{example-rational-bridge}).
For any field extension $K/k$ the base change $C_K \subset X_K$
is a finite disjoint union of rational bridges.
\end{lemma}

#### Proof

Let $k''/k'/k$ be as in the example.
Since $k'/k$ is finite separable, we see that
$k' \otimes_k K = K'_1 \times \ldots \times K'_n$
is a finite product of finite separable extensions $K'_i/K$.
The corresponding product decomposition
$k'' \otimes_k K = \prod K''_i$ gives degree $2$
separable algebra extensions $K''_i/K'_i$.
Set $C_i = C_{K'_i}$. Then $C_K = \coprod C_i$
and therefore each $C_i$ has genus $0$ (viewed as a curve
over $K'_i$), because $H^1(C_K, \mathcal{O}_{C_K}) = 0$
by flat base change.
Finally, we have $X'_K \cap C_i = \Spec(K''_i)$ has degree $2$
over $K'_i$ as desired.


\begin{lemma}
\label{lemma-rational-bridge-canonical}
Let $c : X \to Y$ be the contraction of a rational bridge
(Example \ref{example-rational-bridge}).
Then $c^*\omega_Y \cong \omega_X$.
\end{lemma}

#### Proof

You can prove this by direct computation, but we prefer to use the
characterization of $\omega_X$ as the coherent $\mathcal{O}_X$-module
which represents the functor
$\textit{Coh}(\mathcal{O}_X) \to \textit{Sets}$,
$\mathcal{F} \mapsto \Hom_k(H^1(X, \mathcal{F}), k) =
H^1(X, \mathcal{F})^\vee$, see
Lemma \ref{lemma-duality-dim-1-CM} or
Duality for Schemes, Lemma
\ref{duality-lemma-dualizing-module-proper-over-A}.

\medskip\noindent
To be precise, denote $\mathcal{C}_Y$ the category whose objects are
invertible $\mathcal{O}_Y$-modules and whose maps are
$\mathcal{O}_Y$-module homomorphisms. Denote $\mathcal{C}_X$ the category
whose objects are invertible $\mathcal{O}_X$-modules $\mathcal{L}$ with
$\mathcal{L}|_C \cong \mathcal{O}_C$ and whose maps are
$\mathcal{O}_Y$-module homomorphisms. We claim that the functor
$$
c^* : \mathcal{C}_Y \to \mathcal{C}_X
$$
is an equivalence of categories. Namely, by
More on Morphisms, Lemma \ref{more-morphisms-lemma-bijection-on-Pic}
it is essentially surjective. Then the projection formula
(Cohomology, Lemma \ref{cohomology-lemma-projection-formula})
shows $c_*c^*\mathcal{N} = \mathcal{N}$ and hence $c^*$
is an equivalence with quasi-inverse given by $c_*$.

\medskip\noindent
We claim $\omega_X$ is an object of $\mathcal{C}_X$. Namely, we have a
short exact sequence
$$
0 \to \omega_C \to \omega_X|_C \to \mathcal{O}_{C \cap X'} \to 0
$$
See Lemma \ref{lemma-closed-subscheme-reduced-gorenstein}.
Taking degrees we find $\deg(\omega_X|_C) = 0$ (small detail omitted).
Thus $\omega_X|_C$ is trivial by Lemma \ref{lemma-genus-zero-pic}
and $\omega_X$ is an object of $\mathcal{C}_X$.

\medskip\noindent
Since $R^1c_*\mathcal{O}_X = 0$ the projection formula shows that
$R^1c_*c^*\mathcal{N} = 0$ for $\mathcal{N} \in \Ob(\mathcal{C}_Y)$.
Therefore the Leray spectral sequence
(Cohomology, Lemma \ref{cohomology-lemma-apply-Leray})
the diagram
$$
\xymatrix{
\mathcal{C}_Y \ar[rr]_{c^*} \ar[dr]_{H^1(Y, -)^\vee} & &
\mathcal{C}_X \ar[ld]^{H^1(X, -)^\vee} \\\\
& \textit{Sets}
}
$$
of categories and functors is commutative. Since
$\omega_Y \in \Ob(\mathcal{C}_Y)$ represents the south-east arrow and
$\omega_X \in \Ob(\mathcal{C}_X)$ represents the south-east arrow
we conclude by the Yoneda lemma
(Categories, Lemma \ref{categories-lemma-yoneda}).


\begin{lemma}
\label{lemma-no-rational-bridge-ample-genus-geq-2}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ having dimension $1$
and $H^0(X, \mathcal{O}_X) = k$. Assume


1.  the singularities of $X$ are at-worst-nodal,
1.  $X$ does not have a rational tail
(Example \ref{example-rational-tail}),
1.  $X$ does not have a rational bridge
(Example \ref{example-rational-bridge}),
1.  the genus $g$ of $X$ is $\geq 2$.

Then $\omega_X$ is ample.
\end{lemma}

#### Proof

It suffices to show that $\deg(\omega_X|_C) > 0$ for every irreducible
component $C$ of $X$, see Varieties, Lemma
\ref{varieties-lemma-ampleness-in-terms-of-degrees-components}.
If $X = C$ is irreducible, this follows from $g \geq 2$
and Lemma \ref{lemma-genus-gorenstein}.
Otherwise, set $k' = H^0(C, \mathcal{O}_C)$. This
is a field and a finite extension of $k$ and $[k' : k]$
divides all numerical invariants below associated to $C$ and
coherent sheaves on $C$, see
Varieties, Lemma \ref{varieties-lemma-divisible}.
Let $X' \subset X$ be the closure of $X \setminus C$ as in
Lemma \ref{lemma-closed-subscheme-reduced-gorenstein}.
We will use the results of this lemma and of
Lemmas \ref{lemma-facts-about-nodal-curves} and
\ref{lemma-closed-subscheme-nodal-curve} without further mention.
Then we get a short exact sequence
$$
0 \to \omega_C \to \omega_X|_C \to \mathcal{O}_{C \cap X'} \to 0
$$
See Lemma \ref{lemma-closed-subscheme-reduced-gorenstein}.
We conclude that
$$
\deg(\omega_X|_C) = \deg(C \cap X') + \deg(\omega_C) =
\deg(C \cap X') - 2\chi(C, \mathcal{O}_C)
$$
Hence, if the lemma is false, then
$$
2[k' : k] \geq \deg(C \cap X') + 2\dim_k H^1(C, \mathcal{O}_C)
$$
Since $C \cap X'$ is nonempty and by the divisiblity mentioned above,
this can happen only if either


1. [(a)] $C \cap X'$ is a single $k'$-rational point of $C$ and
$H^1(C, \mathcal{O}_C) = 0$, and
1. [(b)] $C \cap X'$ has degree $2$ over $k'$ and
$H^1(C, \mathcal{O}_C) = 0$.

The first possibility means $C$ is a rational tail
and the second that $C$ is a rational bridge.
Since both are excluded the proof is complete.


\begin{lemma}
\label{lemma-contracting-rational-bridges}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ of dimension $1$
with $H^0(X, \mathcal{O}_X) = k$ having genus $g \geq 2$.
Assume the singularities of $X$ are at-worst-nodal and that
$X$ has no rational tails. Consider a sequence
$$
X = X_0 \to X_1 \to \ldots \to X_n = X'
$$
of contractions of rational bridges
(Example \ref{example-rational-bridge}) until none are left.
Then $\omega_{X'}$ ample.
The morphism $X \to X'$ is independent of choices and
formation of this morphism commutes with base field extensions.
\end{lemma}

#### Proof

We proceed by contracting rational bridges until there are none
left. Then $\omega_{X'}$ is ample by
Lemma \ref{lemma-no-rational-bridge-ample-genus-geq-2}.

\medskip\noindent
Denote $f : X \to X'$ the composition. By
Lemma \ref{lemma-rational-bridge-canonical} and induction we see that
$f^*\omega_{X'} = \omega_X$.
We have $f_*\mathcal{O}_X = \mathcal{O}_{X'}$
because this is true for contraction of a rational bridge.
Thus the projection formula says that
$f_*f^*\mathcal{L} = \mathcal{L}$ for all invertible
$\mathcal{O}_{X'}$-modules $\mathcal{L}$.
Hence
$$
\Gamma(X', \omega_{X'}^{\otimes m}) = \Gamma(X, \omega_X^{\otimes m})
$$
for all $m$. Since $X'$ is the Proj of the direct sum of these
by Morphisms, Lemma \ref{morphisms-lemma-proper-ample-is-proj}
we conclude that the morphism $X \to X'$ is completely canonical.

\medskip\noindent
Let $K/k$ be an extension of fields, then
$\omega_{X_K}$ is the pullback of $\omega_X$
(Lemma \ref{lemma-sanity-check-duality}) and we have
$\Gamma(X, \omega_X^{\otimes m}) \otimes_k K$
is equal to
$\Gamma(X_K, \omega_{X_K}^{\otimes m})$
by
Cohomology of Schemes, Lemma \ref{coherent-lemma-flat-base-change-cohomology}.
Thus formation of $f : X \to X'$ commutes with base change by
$K/k$ by the arguments given above. Some details omitted.







###  Contracting to a stable curve

\label{section-contracting-to-stable}

\noindent
In this section we combine the contraction morphisms found in
Sections \ref{section-contracting-rational-tails} and
\ref{section-contracting-rational-bridges}.
Namely, suppose that $k$ is a field and let $X$ be a proper scheme over $k$
of dimension $1$ with $H^0(X, \mathcal{O}_X) = k$ having genus $g \geq 2$.
Assume the singularities of $X$ are at-worst-nodal. Composing
the morphism of Lemma \ref{lemma-contracting-rational-tails}
with the morphism of Lemma \ref{lemma-contracting-rational-bridges}
we get a morphism
$$
c : X \longrightarrow Y
$$
such that $Y$ also is a proper scheme over $k$ of dimension $1$
whose singularities are at worst nodal, with $k = H^0(Y, \mathcal{O}_Y)$
and having genus $g$, such that
$\mathcal{O}_Y = c_*\mathcal{O}_X$ and $R^1c_*\mathcal{O}_X = 0$,
and such that $\omega_Y$ is ample on $Y$.
Lemma \ref{lemma-characterize-contraction-to-stable}
shows these conditions in fact characterize
this morphism.

\begin{lemma}
\label{lemma-contract-gorenstein-canonical}
Let $k$ be a field. Let $c : X \to Y$ be a morphism of proper schemes over $k$
Assume


1.  $\mathcal{O}_Y = c_*\mathcal{O}_X$ and $R^1c_*\mathcal{O}_X = 0$,
1.  $X$ and $Y$ are reduced, Gorenstein, and have dimension $1$,
1.  $\exists\ m \in \mathbf{Z}$ with
$H^1(X, \omega_X^{\otimes m}) = 0$ and $\omega_X^{\otimes m}$
generated by global sections.

Then $c^*\omega_Y \cong \omega_X$.
\end{lemma}

#### Proof

The fibres of $c$ are geometrically connected by
More on Morphisms, Theorem
\ref{more-morphisms-theorem-stein-factorization-Noetherian}.
In particular $c$ is surjective.
There are finitely many closed points $y = y_1, \ldots, y_r$ of $Y$ where
$X_y$ has dimension $1$ and over $Y \setminus \{y_1, \ldots, y_r\}$
the morphism $c$ is an isomorphism.
Some details omitted; hint: outside of $\{y_1, \ldots, y_r\}$
the morphism $c$ is finite, see
Cohomology of Schemes, Lemma \ref{coherent-lemma-characterize-finite}.

\medskip\noindent
Let us carefully construct a map $b : c^*\omega_Y \to \omega_X$.
Denote $f : X \to \Spec(k)$ and $g : Y \to \Spec(k)$ the structure
morphisms. We have $f^!k = \omega_X[1]$ and $g^!k = \omega_Y[1]$, see
Lemma \ref{lemma-duality-dim-1} and its proof. Then
$f^! = c^! \circ g^!$ and hence $c^!\omega_Y = \omega_X$.
Thus there is a functorial isomorphism
$$
\Hom_{D(\mathcal{O}_X)}(\mathcal{F}, \omega_X)
\longrightarrow
\Hom_{D(\mathcal{O}_Y)}(Rc_*\mathcal{F}, \omega_Y)
$$
for coherent $\mathcal{O}_X$-modules $\mathcal{F}$ by definition
of $c^!$\footnote{As the restriction of the right adjoint of
Duality for Schemes, Lemma \ref{duality-lemma-twisted-inverse-image} to
$D^+_\QCoh(\mathcal{O}_Y)$.}.
This isomorphism is induced by a trace map $t : Rc_*\omega_X \to \omega_Y$
(the counit of the adjunction). By the projection formula
(Cohomology, Lemma \ref{cohomology-lemma-projection-formula})
the canonical map $a : \omega_Y \to Rc_*c^*\omega_Y$ is an isomorphism.
Combining the above we see there is a canonical map
$b : c^*\omega_Y \to \omega_X$ such that
$$
t \circ Rc_*(b) = a^{-1}
$$
In particular, if we restrict $b$ to $c^{-1}(Y \setminus \{y_1, \ldots, y_r\})$
then it is an isomorphism (because it is a map between invertible modules
whose composition with another gives the isomorphism $a^{-1}$).

\medskip\noindent
Choose $m \in \mathbf{Z}$ as in (3) consider the map
$$
b^{\otimes m} :
\Gamma(Y, \omega_Y^{\otimes m})
\longrightarrow
\Gamma(X, \omega_X^{\otimes m})
$$
This map is injective because $Y$ is reduced and by the last
property of $b$ mentioned in its construction.
By Riemann-Roch (Lemma \ref{lemma-rr}) we have
$\chi(X, \omega_X^{\otimes m}) =\chi(Y, \omega_Y^{\otimes m})$.
Thus
$$
\dim_k \Gamma(Y, \omega_Y^{\otimes m}) \geq
\dim_k \Gamma(X, \omega_X^{\otimes m}) = \chi(X, \omega_X^{\otimes m})
$$
and we conclude $b^{\otimes m}$ induces an isomorphism on global
sections. So
$b^{\otimes m} : c^*\omega_Y^{\otimes m} \to \omega_X^{\otimes m}$
is surjective as generators of $\omega_X^{\otimes m}$ are in the image.
Hence $b^{\otimes m}$ is an isomorphism. Thus $b$ is an isomorphism.


\begin{lemma}
\label{lemma-characterize-contraction-to-stable}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ of dimension
$1$ with $H^0(X, \mathcal{O}_X) = k$ having genus $g \geq 2$.
Assume the singularities of $X$ are at-worst-nodal.
There is a unique morphism (up to unique isomorphism)
$$
c : X \longrightarrow Y
$$
of schemes over $k$ having the following properties:


1.  $Y$ is proper over $k$, $\dim(Y) = 1$, the singularities of $Y$
are at-worst-nodal,
1.  $\mathcal{O}_Y = c_*\mathcal{O}_X$ and $R^1c_*\mathcal{O}_X = 0$, and
1.  $\omega_Y$ is ample on $Y$.

\end{lemma}

#### Proof

Existence: A morphism with all the properties listed exists by
combining Lemmas \ref{lemma-contracting-rational-tails} and
\ref{lemma-contracting-rational-bridges} as discussed in the
introduction to this section.
Moreover, we see that it can be written as a composition
$$
X \to X_1 \to X_2 \ldots \to X_n \to X_{n + 1} \to \ldots \to X_{n + n'}
$$
where the first $n$ morphisms are contractions of rational tails
and the last $n'$ morphisms are contractions of rational bridges.
Note that property (2) holds for each contraction of a rational
tail (Example \ref{example-rational-tail}) and contraction of a
rational bridge (Example \ref{example-rational-bridge}).
It is easy to see that this property is inherited by compositions of morphisms.

\medskip\noindent
Uniqueness: Let $c : X \to Y$ be a morphism satisfying conditions
(1), (2), and (3). We will show that there is a unique isomorphism
$X_{n + n'} \to Y$ compatible with the morphisms $X \to X_{n + n'}$ and $c$.

\medskip\noindent
Before we start the proof we make some observations about $c$.
We first observe that the fibres of $c$ are geometrically connected by
More on Morphisms, Theorem
\ref{more-morphisms-theorem-stein-factorization-Noetherian}.
In particular $c$ is surjective.
For a closed point $y \in Y$ the fibre $X_y$ satisfies
$$
H^1(X_y, \mathcal{O}_{X_y}) = 0
\quad\text{and}\quad
H^0(X_y, \mathcal{O}_{X_y}) = \kappa(y)
$$
The first equality by More on Morphisms, Lemma
\ref{more-morphisms-lemma-check-h1-fibre-zero}
and the second by More on Morphisms, Lemma
\ref{more-morphisms-lemma-h1-fibre-zero-check-h0-kappa}.
Thus either $X_y = x$ where $x$ is the unique point of $X$ mapping to
$y$ and has the same residue field as $y$, or $X_y$ is a $1$-dimensional
proper scheme over $\kappa(y)$. Observe that in the second case
$X_y$ is Cohen-Macaulay (Lemma \ref{lemma-automatic}).
However, since $X$ is reduced, we see that $X_y$ must be reduced
at all of its generic points (details omitted), and hence $X_y$
is reduced by Properties, Lemma \ref{properties-lemma-criterion-reduced}.
It follows that the singularities of $X_y$ are at-worst-nodal
(Lemma \ref{lemma-closed-subscheme-nodal-curve}).
Note that the genus of $X_y$ is zero (see above).
Finally, there are only a finite number of points $y$ where
the fibre $X_y$ has dimension $1$, say
$\{y_1, \ldots, y_r\}$, and $c^{-1}(Y \setminus \{y_1, \ldots, y_r\})$
maps isomorphically to $Y \setminus \{y_1, \ldots, y_r\}$ by $c$.
Some details omitted; hint: outside of $\{y_1, \ldots, y_r\}$
the morphism $c$ is finite, see
Cohomology of Schemes, Lemma \ref{coherent-lemma-characterize-finite}.

\medskip\noindent
Let $C \subset X$ be a rational tail.
We claim that $c$ maps $C$ to a point. Assume that this
is not the case to get a contradiction. Then the image
of $C$ is an irreducible component $D \subset Y$.
Recall that $H^0(C, \mathcal{O}_C) = k'$ is a finite separable
extension of $k$ and that $C$ has a $k'$-rational point $x$
which is also the unique intersection of $C$ with the ``rest'' of $X$.
We conclude from the general discussion above that
$C \setminus \{x\} \subset c^{-1}(Y \setminus \{y_1, \ldots, y_r\})$
maps isomorphically to an open $V$ of $D$. Let $y = c(x) \in D$.
Observe that $y$ is the only point of $D$ meeting the
``rest'' of $Y$. If $y \not \in \{y_1, \ldots, y_r\}$, then $C \cong D$
and it is clear that $D$ is a rational tail of $Y$ which is
a contradiction with the ampleness of $\omega_Y$
(Lemma \ref{lemma-rational-tail-negative}).
Thus $y \in \{y_1, \ldots, y_r\}$ and $\dim(X_y) = 1$.
Then $x \in X_y \cap C$ and $x$ is a smooth point of $X_y$ and $C$
(Lemma \ref{lemma-closed-subscheme-nodal-curve}).
If $y \in D$ is a singular point of $D$, then $y$ is a node
and then $Y = D$ (because there cannot be another component of
$Y$ passing through $y$ by Lemma \ref{lemma-closed-subscheme-nodal-curve}).
Then $X = X_y \cup C$ which means $g = 0$ because it is
equal to the genus of $X_y$ by the discussion in
Example \ref{example-rational-tail}; a contradiction.
If $y \in D$ is a smooth point of $D$, then
$C \to D$ is an isomorphism (because the nonsingular projective
model is unique and $C$ and $D$ are birational, see
Section \ref{section-curves-function-fields}). Then $D$ is
a rational tail of $Y$ which is a contradiction with
ampleness of $\omega_Y$.

\medskip\noindent
Assume $n \geq 1$. If $C \subset X$ is the rational tail contracted
by $X \to X_1$, then we see that $C$ is mapped to a point of $Y$ by
the previous paragraph. Hence $c : X \to Y$ factors through $X \to X_1$
(because $X$ is the pushout of $C$ and $X_1$, see discussion in
Example \ref{example-rational-tail}).
After replacing $X$ by $X_1$ we have decreased
$n$. By induction we may assume $n = 0$, i.e., $X$ does not have
a rational tail.

\medskip\noindent
Assume $n = 0$, i.e., $X$ does not have any rational tails.
Then $\omega_X^{\otimes 2}$ and $\omega_X^{\otimes 3}$ are
globally generated by Lemma \ref{lemma-no-rational-tail-semiample-genus-geq-2}.
It follows that $H^1(X, \omega_X^{\otimes 3}) = 0$ by
Lemma \ref{lemma-vanishing-twist}.
By Lemma \ref{lemma-contract-gorenstein-canonical} applied with $m = 3$
we find that $c^*\omega_Y \cong \omega_X$.
We also have that $\omega_X = (X \to X_{n'})^*\omega_{X_{n'}}$ by
Lemma \ref{lemma-rational-bridge-canonical} and induction.
Applying the projection formula for both $c$ and
$X \to X_{n'}$ we conclude that
$$
\Gamma(X_{n'}, \omega_{X_{n'}}^{\otimes m}) =
\Gamma(X, \omega_X^{\otimes m}) =
\Gamma(Y, \omega_Y^{\otimes m})
$$
for all $m$.
Since $X_{n'}$ and $Y$ are the Proj of the direct sum of these
by Morphisms, Lemma \ref{morphisms-lemma-proper-ample-is-proj}
we conclude that there is a canonical isomorphism $X_{n'} = Y$
as desired. We omit the verification that this is the unique
isomorphism making the diagram commute.


\begin{lemma}
\label{lemma-tricanonical}
Let $k$ be a field. Let $X$ be a proper scheme over $k$ of dimension $1$ with
$H^0(X, \mathcal{O}_X) = k$ having genus $g \geq 2$. Assume the singularities
of $X$ are at-worst-nodal and $\omega_X$ is ample. Then
$\omega_X^{\otimes 3}$ is very ample and $H^1(X, \omega_X^{\otimes 3}) = 0$.
\end{lemma}

#### Proof

Combining Varieties, Lemma
\ref{varieties-lemma-ampleness-in-terms-of-degrees-components} and
Lemmas \ref{lemma-rational-tail-negative} and \ref{lemma-rational-bridge-zero}
we see that $X$ contains no rational tails or bridges.
Then we see that $\omega_X^{\otimes 3}$ is globally generated
by Lemma \ref{lemma-contracting-rational-tails}.
Choose a $k$-basis $s_0, \ldots, s_n$ of
$H^0(X, \omega_X^{\otimes 3})$. We get a morphism
$$
\varphi_{\omega_X^{\otimes 3}, (s_0, \ldots, s_n)} :
X \longrightarrow \mathbf{P}^n_k
$$
See Constructions, Section \ref{constructions-section-projective-space}.
The lemma asserts that this morphism is a closed immersion.
To check this we may replace $k$ by its algebraic closure, see
Descent, Lemma \ref{descent-lemma-descending-property-closed-immersion}.
Thus we may assume $k$ is algebraically closed.

\medskip\noindent
Assume $k$ is algebraically closed.
We will use Varieties, Lemma
\ref{varieties-lemma-variant-separate-points-tangent-vectors}
to prove the lemma.
Let $Z \subset X$ be a closed subscheme of degree $2$ over $Z$
with ideal sheaf $\mathcal{I} \subset \mathcal{O}_X$.
We have to show that
$$
H^0(X, \mathcal{L}) \to H^0(Z, \mathcal{L}|_Z)
$$
is surjective. Thus it suffices to show that
$H^1(X, \mathcal{I}\mathcal{L}) = 0$.
To do this we will use Lemma \ref{lemma-vanishing-on-gorenstein}.
Thus it suffices to show that
$$
3\deg(\omega_X|_Y) > -2\chi(Y, \mathcal{O}_Y) + \deg(Z \cap Y)
$$
for every reduced connected closed subscheme $Y \subset X$.
Since $k$ is algebraically closed and $Y$ connected and reduced
we have $H^0(Y, \mathcal{O}_Y) = k$ (Varieties, Lemma
\ref{varieties-lemma-proper-geometrically-reduced-global-sections}).
Hence $\chi(Y, \mathcal{O}_Y) = 1 - \dim H^1(Y, \mathcal{O}_Y)$.
Thus we have to show
$$
3\deg(\omega_X|_Y) > -2 + 2\dim H^1(Y, \mathcal{O}_Y) + \deg(Z \cap Y)
$$
which is true by Lemma \ref{lemma-no-rational-tail}
except possibly if $Y = X$ or if $\deg(\omega_X|_Y) = 0$.
Since $\omega_X$ is ample the second possibility does not
occur (see first lemma cited in this proof). Finally, if
$Y = X$ we can use Riemann-Roch (Lemma \ref{lemma-rr})
and the fact that $g \geq 2$ to see that the inquality holds.
The same argument with $Z = \emptyset$ shows that
$H^1(X, \omega_X^{\otimes 3}) = 0$.








###  Vector fields

\label{section-vector-fields}

\noindent
In this section we study the space of vector fields on a curve.
Vector fields correspond to infinitesimal automorphisms, see
More on Morphisms, Section \ref{more-morphisms-section-action-by-derivations},
hence play an important role in moduli theory.

\medskip\noindent
Let $k$ be an algebraically closed field.
Let $X$ be a finite type scheme over $k$.
Let $x \in X$ be a closed point.
We will say an element $D \in \text{Der}_k(\mathcal{O}_X, \mathcal{O}_X)$
{\it fixes $x$} if $D(\mathcal{I}) \subset \mathcal{I}$ where
$\mathcal{I} \subset \mathcal{O}_X$ is the ideal sheaf of $x$.

\begin{lemma}
\label{lemma-smooth-vector-fields}
Let $k$ be an algebraically closed field.
Let $X$ be a smooth, proper, connected curve over $k$.
Let $g$ be the genus of $X$.


1.  If $g \geq 2$, then $\text{Der}_k(\mathcal{O}_X, \mathcal{O}_X)$
is zero,
1.  if $g = 1$ and $D \in \text{Der}_k(\mathcal{O}_X, \mathcal{O}_X)$
is nonzero, then $D$ does not fix any closed point of $X$, and
1.  if $g = 0$ and $D \in \text{Der}_k(\mathcal{O}_X, \mathcal{O}_X)$
is nonzero, then $D$ fixes at most $2$ closed points of $X$.

\end{lemma}

#### Proof

Recall that we have a universal $k$-derivation
$d : \mathcal{O}_X \to \Omega_{X/k}$ and hence $D = \theta \circ d$
for some $\mathcal{O}_X$-linear map $\theta : \Omega_{X/k} \to \mathcal{O}_X$.
Recall that $\Omega_{X/k} \cong \omega_X$, see
Lemma \ref{lemma-duality-dim-1}.
By Riemann-Roch we have $\deg(\omega_X) = 2g - 2$
(Lemma \ref{lemma-rr}).
Thus we see that $\theta$ is forced to be zero
if $g > 1$ by Varieties, Lemma
\ref{varieties-lemma-check-invertible-sheaf-trivial}.
This proves part (1).
If $g = 1$, then a nonzero $\theta$ does not vanish anywhere and if
$g = 0$, then a nonzero $\theta$ vanishes in a divisor of degree $2$.
Thus parts (2) and (3) follow if we show that
vanishing of $\theta$ at a closed point $x \in X$ is
equivalent to the statement that $D$ fixes $x$ (as defined above).
Let $z \in \mathcal{O}_{X, x}$ be a uniformizer.
Then $dz$ is a basis element for $\Omega_{X, x}$, see
Lemma \ref{lemma-uniformizer-works}.
Since $D(z) = \theta(dz)$ we conclude.


\begin{lemma}
\label{lemma-nodal-vector-fields}
Let $k$ be an algebraically closed field.
Let $X$ be an at-worst-nodal, proper, connected
$1$-dimensional scheme over $k$. Let $\nu : X^\nu \to X$ be the normalization.
Let $S \subset X^\nu$ be the set of points where $\nu$ is not an
isomorphism. Then
$$
\text{Der}_k(\mathcal{O}_X, \mathcal{O}_X) =
\{D' \in \text{Der}_k(\mathcal{O}_{X^\nu}, \mathcal{O}_{X^\nu}) \mid
D' \text{ fixes every }x^\nu \in S\}
$$
\end{lemma}

#### Proof

Let $x \in X$ be a node. Let $x', x'' \in X^\nu$ be the inverse images
of $x$. (Every node is a split node since $k$ is algebriacally closed, see
Definition \ref{definition-split-node} and
Lemma \ref{lemma-split-node}.)
Let $u \in \mathcal{O}_{X^\nu, x'}$ and $v \in \mathcal{O}_{X^\nu, x''}$
be uniformizers. Observe that we have an exact sequence
$$
0 \to \mathcal{O}_{X, x} \to
\mathcal{O}_{X^\nu, x'} \times \mathcal{O}_{X^\nu, x''} \to k \to 0
$$
This follows from Lemma \ref{lemma-multicross}.
Thus we can view $u$ and $v$ as elements of $\mathcal{O}_{X, x}$
with $uv = 0$.

\medskip\noindent
Let $D \in \text{Der}_k(\mathcal{O}_X, \mathcal{O}_X)$. Then
$0 = D(uv) = vD(u) + uD(v)$. Since $(u)$ is annihilator of
$v$ in $\mathcal{O}_{X, x}$ and vice versa, we see that $D(u) \in (u)$ and
$D(v) \in (v)$. As $\mathcal{O}_{X^\nu, x'} = k + (u)$
we conclude that we can extend $D$ to $\mathcal{O}_{X^\nu, x'}$
and moreover the extension fixes $x'$. This produces a $D'$
in the right hand side of the equality. Conversely, given a
$D'$ fixing $x'$ and $x''$ we find that $D'$ preserves
the subring $\mathcal{O}_{X, x} \subset
\mathcal{O}_{X^\nu, x'} \times \mathcal{O}_{X^\nu, x''}$
and this is how we go from right to left in the equality.


\begin{lemma}
\label{lemma-stable-vector-fields}
Let $k$ be an algebraically closed field.
Let $X$ be an at-worst-nodal, proper, connected
$1$-dimensional scheme over $k$. Assume the genus of $X$ is at least
$2$ and that $X$ has no rational tails
or bridges. Then
$\text{Der}_k(\mathcal{O}_X, \mathcal{O}_X) = 0$.
\end{lemma}

#### Proof

Let $D \in \text{Der}_k(\mathcal{O}_X, \mathcal{O}_X)$.
Let $X^\nu$ be the normalization of $X$.
Let $D' \in \text{Der}_k(\mathcal{O}_{X^\nu}, \mathcal{O}_{X^\nu})$
be the element corresponding to $D$ via Lemma \ref{lemma-nodal-vector-fields}.
Let $C \subset X^\nu$ be an irreducible component.
If the genus of $C$ is $> 1$, then $D'|_{\mathcal{O}_C} = 0$
by Lemma \ref{lemma-smooth-vector-fields} part (1).
If the genus of $C$ is $1$, then there is at least one closed point $c$ of $C$
which maps to a node on $X$ (since otherwise $X \cong C$ would have genus $1$).
By the correspondence this means that
$D'|_{\mathcal{O}_C}$ fixes $c$ hence is zero by
Lemma \ref{lemma-smooth-vector-fields} part (2).
Finally, if the genus of $C$ is zero, then there are at least
$3$ pairwise distinct closed points $c_1, c_2, c_3 \in C$
mapping to nodes in $X$, since otherwise either
$X$ is $C$ with two points glued (two points of $C$ mapping
to the same node), or
$C$ is a rational bridge (two points mapping to different nodes of $X$), or
$C$ is a rational tail (one point mapping to a node of $X$).
These three possibilities are not permitted since
$C$ has genus $\geq 2$ and has no rational bridges, or rational tails.
Whence $D'|_{\mathcal{O}_C}$ fixes $c_1, c_2, c_3$ hence is zero by
Lemma \ref{lemma-smooth-vector-fields} part (3).






\input{chapters}

\bibliography{my}
\bibliographystyle{amsalpha}