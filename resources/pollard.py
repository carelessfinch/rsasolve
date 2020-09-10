def pollards(n):
    from fractions import gcd
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x); y = f(f(y))
        d = gcd(abs(x-y), n)
    if d != n:
        p=d
        q=n//p
        if p*q==n:
            return (p-1)*(q-1)
    else:
        return 0