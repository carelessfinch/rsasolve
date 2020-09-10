def nth(ct,e):
    from gmpy2 import iroot
    from Crypto.Util.number import long_to_bytes
    m=iroot(ct,e)[0]
    ch=long_to_bytes(m)
    ll=len(ch)
    if ch[0] >= 32 and ch[0] <= 126 and ch[ll-2] >= 32 and ch[ll-2] <= 126:
        print(ch)
        return(1)
    else: 
        return(0)