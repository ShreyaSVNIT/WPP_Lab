import numpy as np

def magic(n):
    if n % 2 == 1:
        m = np.zeros((n, n), dtype=int)
        x, y = 0, n // 2
        for num in range(1, n * n + 1):
            m[x, y] = num
            x, y = (x - 1) % n, (y + 1) % n
            if m[x, y]:
                x = (x + 2) % n
                y = (y - 1) % n
        return m

    elif n % 4 == 0:
        m = np.arange(1, n * n + 1).reshape(n, n)
        i = np.arange(n)
        j = i[:, None]
        mask = (i % 4 == j % 4) | ((i + j) % 4 == 3)
        m[mask] = (n * n + 1) - m[mask]
        return m

    else:
        h = n // 2
        s = magic(h)
        m = np.zeros((n, n), dtype=int)
        a = [0, 1, 2, 3]
        for idx, (i, j) in zip(a, [(0, 0), (0, 1), (1, 0), (1, 1)]):
            m[i*h:(i+1)*h, j*h:(j+1)*h] = s + idx * (h*h)

        k = h // 2
        cols = list(range(k)) + list(range(n - k, n))
        for i in range(h):
            for j in cols:
                if j == k and i == k:
                    continue
                m[i, j], m[i + h, j] = m[i + h, j], m[i, j]

        return m

for n in range(4, 9):
    print(f"\nMagic Square for N = {n}:\n{magic(n)}\n")
