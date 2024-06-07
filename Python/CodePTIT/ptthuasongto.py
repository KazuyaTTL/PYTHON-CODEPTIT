"""
Cho số nguyên dương N. Hãy phân tích N thành tích các thừa số nguyên tố. Kết quả được in ra theo mẫu trong ví dụ, trong đó thêm 
số thừa số 1 (không phải nguyên tố) ở đầu kết quả phân tích.

Input
Dòng đầu ghi số bộ test, mỗi test ghi trên một dòng số nguyên dương N không quá 6 chữ số.

Output
Ghi ra kết quả phân tích theo mẫu như trong ví dụ.

Ví dụ
28 : 1 * 2^2 * 7^1
100 : 1 * 2^2 * 5^2
"""
#Phân tích thừa số nguyên tố 2.0
from math import*
def pt(n):
    print(1, end=" * ")
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            mu = 0 
            while n % i == 0:
                mu += 1
                n //= i
            print(i, mu , sep = "^", end = "")
            if n != 1: #Chưa phân tích xong
                print(" * ", end = "")
    if n > 1 :
        print(n, 1 , sep = "^")
t = int(input())
for _ in range(t):
    n = int(input())
    print(pt(n))


