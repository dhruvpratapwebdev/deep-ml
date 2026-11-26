import numpy as np

def svd_2x2_singular_values(A):
    B = A.T @ A

    theta = 0.5 * np.arctan2(
        2 * B[0, 1],
        B[0, 0] - B[1, 1]
    )

    c = np.cos(theta)
    s = np.sin(theta)

    V = np.array([
        [c, -s],
        [s,  c]
    ])

    D = V.T @ B @ V

    eigenvalues = np.diag(D)
    S = np.sqrt(np.maximum(eigenvalues, 0))

    indices = np.argsort(S)[::-1]

    S = S[indices]
    V = V[:, indices]

    U = (A @ V) / S[np.newaxis, :]

    Vt = V.T

    return U, S, Vt