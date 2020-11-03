from Crypto.Util.number import *
from string import ascii_letters, digits
from random import randint
from secret import flag

assert flag.startswith("0xGame{") and flag.endswith("}")
table = ascii_letters+digits
MOD = len(table)

def affine(x, a, b): return a*x+b

def genKey():
    a = [randint(1, 64) for _ in range(3)]
    b = [randint(1, 64) for _ in range(3)]
    while GCD(MOD, a[0]*a[1]*a[2]) != 1:
        a = [randint(1, 64) for _ in range(3)]
    return a, b


cipher = ""
A, B = genKey()
for i in flag:
    if i not in table:
        cipher += i
    else:
        cipher += table[affine(affine(affine(table.find(i),A[0], B[0]), A[1], B[1]), A[2], B[2]) % MOD]

print("cipher =", cipher)
# cipher = t6b7Tn{2GByBZBB-aan2-JRWn-GnZB-Jyf7a722ffnZ}
