"""
Ngân hàng thông báo lãi suất là X % mỗi năm.
Với số tiền gửi vào là N. Sau mỗi năm, tiền lãi sẽ được cộng dồn.
Hỏi sau bao nhiêu năm thì số tiền đạt được ít nhất là M.

Input
Dòng đầu ghi số bộ test.

Mỗi test viết 3 số thực (kiểu double) N, X và M. Trong đó 0<N<M<100000.

Output
Ghi ra số năm tính được.
"""
# m=n*(1+x/100)**t
from math import*
def tinh_so_nam(n, x, m):
    t = log(m / n) / log(1 + x / 100)
    return round(t)
# Ví dụ:
m, n, x = map(int, input().split())
print(tinh_so_nam(m, n, x))  