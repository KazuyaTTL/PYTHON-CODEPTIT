from math import*
# Đọc input
n = int(input("Nhap so phan tu cua A: "))
A = list(map(int, input().split()))
m = []
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1
for i in A:
    for j in A:
        if i < j:
            if gcd(i,j):
                m.append((i,j))
m.sort()
for k in m:
    print(k[0],k[1])

