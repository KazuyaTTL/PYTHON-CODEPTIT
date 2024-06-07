from math import*
#Hàm xác định ước chung lớn nhất
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
####
def solve():
    t = int(input("Nhập số lượng bộ test: ").strip())
    for j in range(t):
        n = int(input("Nhập giá trị N: ").strip())
        count = 0
        for i in range(1, n):
            if gcd(i, n) == 1:
                count += 1
        if is_prime(count):
            print('YES')
        else:
            print('NO')
solve()