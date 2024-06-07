import math
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def prime_pairs(A):
    A.sort()
    pairs = []
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if gcd(A[i], A[j]) == 1:
                pairs.append((A[i], A[j]))
    return pairs
n = int(input())
A = list(map(int, input().split()))
pairs = prime_pairs(A)
for pair in pairs:
    print(pair[0], pair[1])