from Crypto.Util.number import *
from Crypto.PublicKey import RSA

def intro():
    print(" ____  ____    _      ____        _\n|  _ \/ ___|  / \    / ___|  ___ | |\n| |_) \___ \ / _ \   \___ \ / _ \| |\n|  _ < ___) / ___ \   ___) | (_) | |\n|_| \_\____/_/   \_\ |____/ \___/|_|")
    print("\n1.Public Key as decimal\n2.Read from file")
    selection=int(input("Enter your selection: "))
    if selection==1:
        get_vals()
    elif selection==2:
        read_vals()
    else:
        print("Invalid entry Exiting")
        exit(1)

def get_vals():
    n=int(input("n = "))
    e=int(input("e = "))
    pt_2(n,e)

def read_vals():
    file_path=input("Enter path to file : ")
    f=open(file_path,'rb').read()
    n=RSA.importKey(f).n
    e=RSA.importKey(f).e
    pt_2(n,e)

def pt_2(n,e):
    print("Values:")
    print('n = ',n,'\ne = ',e)
    from resources.test import test
    test(n,e)

if __name__ == "__main__":
    print("test")
    intro()