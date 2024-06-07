"""
Cho hai số nguyên dương a và b. Hãy kiểm tra xem ước số chung lớn nhất của hai số này có tổng chữ số là nguyên tố hay không.

Ví dụ a = 42, b = 28, ước số chung lớn nhất = 14. Tổng chữ số của ước số chung là 1+4=5 là một số nguyên tố.

Input

Dòng đầu ghi số bộ test. Mỗi test ghi trên một dòng hai số nguyên dương a,b (không quá 6 chữ số)

Output

Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
"""
from math import*
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a
def IsPrime(n):
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return False
    return True
def splt(n):
    tong = 0
    while n != 0:
        tong += n %10
        n //= 10
    return tong
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if IsPrime(splt(gcd(a,b))):
        print("YES")
    else:
        print("NO")