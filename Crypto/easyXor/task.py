from random import randint
from secret import flag

flag+="^"
cipher=[]
for i in range(len(flag)-1):
    cipher.append(ord(flag[i])^ord(flag[i+1]))
print(cipher)
#[72, 63, 38, 12, 8, 30, 30, 6, 82, 4, 84, 88, 92, 7, 79, 29, 8, 90, 85, 26, 25, 87, 80, 10, 20, 20, 9, 4, 80, 73, 31, 5, 82, 0, 1, 92, 0, 0, 94, 81, 4, 85, 27, 35]
