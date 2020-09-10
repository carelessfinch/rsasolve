def fer(n):
    from gmpy2 import iroot
    a=iroot(n,2)[0]
    b=a*a-n
    if b<0:
        a=a+1
        b=a*a-n
    z=iroot(b,2)[0]
    p=a-z
    q=n//p
    if p*q==n:
        return (p-1)*(q-1)
    else:
        return 0