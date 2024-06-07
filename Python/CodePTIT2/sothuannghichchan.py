"""
Cho số nguyên dương N không quá 6 chữ số.

Hãy liệt kê các số nhỏ hơn N thỏa mãn cả ba điều kiện:

N là số thuận nghịch
Tất cả các chữ số của N đều chẵn
Số chữ số của N cũng là một số chẵn
Input

Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)

Output

Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.

Ví dụ:
Input:

2
30
100

Output:

22
22 44 66 88
"""
def reverse(n):
    m = n
    lat = 0
    while n != 0:
        lat = lat * 10 + n % 10
        n = n // 10
    return lat == m

def check_even_digits(n):
    while n != 0:
        a = n % 10
        if a % 2 != 0:
            return False
        n //= 10
    return True

def sum_digit(n):
    m = str(n)
    so_cs = len(m)
    return so_cs % 2 == 0

def solve(n):
    uet = []
    cn16 = []
    for i in range(22, n):
        if reverse(i):
            uet.append(i)
    for j in uet:
        if sum_digit(j) and check_even_digits(j):
            cn16.append(j)
    for k in cn16:
        print(k, end=" ")
    print()

t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)