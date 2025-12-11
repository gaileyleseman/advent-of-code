# Optimization

## Linear Algebra

### scipy.optimize.linprog

Linear programming minimizes a linear objective function subject to linear constraints.

$$
\min_x c^T x \quad \text{s.t.} \quad Ax = b
$$

For example:

$$
\begin{bmatrix} 3 & 1 \\ 2 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 7 \\ 10 \end{bmatrix}
$$

```python
from scipy.optimize import linprog

result = linprog(
    c,                # cost vector (minimize c^T @ x)
    A_eq=A,b_eq=b,    # equality: A_eq @ x == b_eq
    integrality=1     # 0=continuous, 1=integer
)

result.x    # optimal solution (x)
result.fun  # optimal value
```

Note, this function always **minimizes** — to maximize, negate `c`, for example:
```python
result = linprog(-c, A_eq=A, b_eq=b)
maximum = -result.fun
```

Sources:
[1](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html)

Relevant AoC problems:
[2025, day 10](https://adventofcode.com/2025/day/10)