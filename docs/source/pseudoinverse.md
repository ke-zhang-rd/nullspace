SVD pseudo inverse
The pseudoinverse gives a “least squared error, minimum-norm” solution: Out of all $\dot{q}$ vectors at your current $q$, the vector 

$$\dot{q}_{s} = J^{+}(q)\dot{p}_{\text{in}}$$

satisfies two conditions:

1. Least squared error: There is no $\dot{q}$ vector which will get closer to $\dot{p}$ when passed through $J(q)$. (I.e. for $\dot{p}_{s} = J(q)\dot{q}_{s}$, the normed difference $\lvert \dot{p}_{\text{in}}-\dot{p}_{s} \rvert$ is smaller than any other $\lvert \dot{p}_{\text{in}} - \dot{p} \rvert$.

2. Minimum-norm: Out of all $\dot{q}$ that satisfy the first condition, $\dot{q}_{s}$ is the smallest of those vectors. (I.e. $\lvert \dot{q_{s}}\rvert$ is smaller than $\lvert \dot{q} \rvert$ for all $\dot{q}$ that minimize error in $\dot{p}$.

At the singularity, the set of achievable velocities loses one dimension (so that there are $\dot{p}$ that cannot be exactly produced by a $\dot{q}$), but for any $\dot{p}_{\text{in}}$ there is a set of $\dot{q}$ that all come equally close to producing $\dot{p}_{\text{in}}$, and the pseudoinverse picks the smallest (in $\dot{q}$-space) of these vectors.
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDk4MDMwNzE4LC0xMzQ5MzA4NDE5XX0=
-->