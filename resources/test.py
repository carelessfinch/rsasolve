def test(n,e):
    if e>1 and e<n:
        ct=int(input("Enter the cipher test ct = "))
        if e<=5:
            sm_e(ct,n,e)
        else:
            test2(ct,n,e)            

    else:
        print("Wrong values Exiting")

def sm_e(ct,n,e):
    from resources.nthroot import nth
    res=nth(ct,e)
    while(res!=0):
        if res == 1:
            print("Seems like we found it.\n1.Exit\n2.Continue Testing")
            selection=int(input())
            if selection==1:
                exit()
            elif selection==2:
                res=0
            else:
                print("Invalid selection Try again:\n")
    test2(ct,n,e)

def test2(ct,n,e):
    from Crypto.Util.number import inverse
    from resources.decrypt import decrypt
    if e>65537:
        from resources import owiener
        d=owiener.attack(e,n)
        if d is None:
            pass
        else:
            decrypt(ct,d,n)
    from resources.fermant import fer
    val=fer(n)
    if val!=0:
        d=inverse(e,val)
        decrypt(ct,d,n)
        exit()
    from resources.pollard import  pollards
    val=pollards(n)
    if val!=0:
        d=inverse(e,val)
        decrypt(ct,d,n)
        exit()
    
    