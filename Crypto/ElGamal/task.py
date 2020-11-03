from Crypto.Util.number import *
from Crypto.PublicKey import ElGamal
from random import randint
from secret import flag


def notSquare(p):
    r = randint(2, p-2)
    while pow(r, (p-1)//2, p) == 1:
        r = randint(2, p-2)
    return r


def Square(p):
    return pow(randint(2, p-2), 2, p)


flag = bin(bytes_to_long(flag.encode()))[2:]
key = ElGamal.generate(512, Random.new().read)
y=int(key.y)
while (pow(y, (int(key.p)-1)//2, int(key.p)) == 1):
    x=randint(1,int(key.p)-2)
    if x%2==0:
        x+=1
    y=pow(int(key.g),x,int(key.p))
    

f = open("data", "w")
for i in flag:
    plaintexts = {"0": Square(int(key.p)), "1": notSquare(int(key.p))}
    c = key._encrypt(plaintexts[i], randint(1, int(key.p)-2))
    f.writelines(hex(c[0])[2:]+", "+hex(c[1])[2:]+"\n")
f.close()

print("y =", key.y)
print("g =", key.g)
print("p =", key.p)

# y = 2101136318398982764494355697982735290351867853540128399809061806690701481465143258501856786165972388085070268979718711434744226290744692988395355120277617
# g = 8401562798890834492298947403582806359769363301996138198850077614144023393945770711612546197987255078645962298286362268504959833530010137313108031112774451
# p = 10946148224653120484646906462803901217745837751637974066354601688874051778651193811412739372059281847771491564589986518154039493312147458591216351424346123
