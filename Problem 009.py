def product(r, s):
    return(r**2 - s**2) * 2 * r * s * (r**2 + s**2)

for r in range(1, 25):
    if 500 % r == 0 and(500 / r - r) < r and r < (500 / r):
        print product(r, 500/r - r)
