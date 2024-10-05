# Back Propagation
## Gradient
Let $f: \mathbb{R}^n \to \mathbb{R}$ differentiable. 
$$
\nabla f = \left[ \frac{\partial f}{\partial x_1}, \cdots, \frac{\partial f}{\partial x_n} \right]^{T} 
$$
If $f$ is with values in $\mathbb{R}^m$:
$$
\nabla f = \left( \frac{\partial f_j}{\partial x_i} \right)_{i=1, \cdots, n, j=1, \cdots m}
$$
For $\mathbf{x} \in \mathbb{R}^n$ : $\nabla_{\mathbf{x}}f$ is an $n\times m$ matrice having gradients $\nabla_{\mathbf{x}} f_j$ as columns.

## Gradient of composition
Let $h : \mathbb{R}^n \xrightarrow[\text{}]{g} \mathbb{R}^m  \xrightarrow[\text{}]{f} \mathbb{R}$ and $\mathbf{y} = g(\mathbf{x})$. We have:
$$
\nabla_{\mathbf{x}}h
$$