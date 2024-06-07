"""
Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:
Số chữ số của nó là một số nguyên tố
Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

Input
Dòng đầu ghi số bộ test, không quá 20.
Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số

Output
Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
"""
from math import*
def IsPrime(n):
    if n < 2:
        return False
    for i in range(2,isqrt(n)+1):
        if n % i == 0:
            return False
    return True
def solve1(n):
    if IsPrime(len(str(n))):
        return True
    else:
        return False
def solve2(n):
    m = str(n)
    count1 = 0
    count2 = 0
    for i in m:
        if IsPrime(int(i)):
            count1 += 1
        else:
            count2 += 1
    if count1 > count2 :
        return True
    else:
        return False
t = int(input())
for _ in range(t):
    n = int(input())
    if solve1(n) and solve2(n):
        print("YES")
    else:
        print("NO")