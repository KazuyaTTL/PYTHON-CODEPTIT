"""
Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1. Một bộ ba số (a, b, c) 
được gọi là bộ ba nguyên tố cùng nhau nếu a < b < c và các cặp (a,b), (b,c), (a,c) đều nguyên tố cùng nhau.

Cho hai số nguyên dương L và R (10 < L < R < 200). Hãy viết chương trình liệt kê các bộ ba số nguyên tố cùng nhau trong đoạn 
[L, R].

Input
Chỉ có 2 số L và R

Output
Ghi ra các bộ ba số nguyên tố cùng nhau, mỗi bộ ba trên một dòng theo định dạng như trong ví dụ.
Các bộ ba được liệt kê theo thứ tự từ điển tăng dần.
"""
from math import*
#Hàm xác định ước chung lớn nhất
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
L, R = map(int, input().split())
for a in range(L, R+1):
    for b in range(a+1, R+1):
        for c in range(b+1, R+1):    
            if gcd(a,b) == 1 and  gcd(a,c) == 1 and gcd(b,c) == 1:
                print(f"({a} {b} {c})")