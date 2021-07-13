# Non-Negative Matrix Factorization
- **Principle** 
  * we first find the k- dimension approximation in terms of non-negative facotrs W and H
      - the **W** matrix is the (n x k) matrix
      - the **H** matrix is the (k x m) matrix
  * Objective function of the NNMF is given as follows :-
```r
 \begin{align*}
a & = b \\
X &\sim {\sf Norm}(10, 3) \\
5 & \le 10
\end{align*}
```

1/2 || A - WH ||<sup>2</sup> = &sim {&sim {(**A**<sub>ij</sub> - (**WH**)<sub>ij</sub>)<sup>2</sup>}(j =1, m)}(i = 1, n)
