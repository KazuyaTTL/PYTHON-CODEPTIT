"""
Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1.

Cho hai số nguyên dương N và K trong đó 10 < N < 10000; 1 < K < 6.

Hãy liệt kê các số có K chữ số thỏa mãn nguyên tố cùng nhau với N.

Input
Chỉ có một dòng ghi hai số N và K

Output
Ghi ra lần lượt các số thỏa mãn theo thứ tự từ nhỏ đến lớn. Mỗi dòng ghi 10 số.
"""
from math import*
#Hàm xác định ước chung lớn nhất
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def list_coprimes(N, K):
    start = 10**(K-1)
    end = 10**K
    result = []
    for i in range(start, end):
        if gcd(N, i) == 1:
            result.append(i)
            if len(result) == 10:
                print(' '.join(map(str, result)))
                result = []
    if result:
        print(' '.join(map(str, result)))

# Đọc dữ liệu đầu vào
N, K = map(int, input().split())
list_coprimes(N, K)