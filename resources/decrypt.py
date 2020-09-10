def decrypt(ct,d,n):
    from Crypto.Util.number import long_to_bytes
    print("Soln = ",long_to_bytes(pow(ct,d,n)))