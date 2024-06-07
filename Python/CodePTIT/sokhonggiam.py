"""Một số được gọi là số không giảm nếu không có cặp chữ số cạnh nhau (i, i+1) nào mà số thứ i lớn hơn số thứ i+1.

Viết chương trình kiểm tra số nguyên dương có thỏa mãn là số không giảm hay không.
Input:
Dòng đầu ghi số bộ test (không quá 10).
Mỗi dòng ghi một số nguyên dương (không quá 500 chữ số).

Output:
Ghi ra YES nếu đó là số không giảm. NO nếu ngược lại
"""

def kiem_tra_so_khong_giam(n):
    n = str(n)
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True
t = int(input())
for _ in range(t):
    n = int(input())
    if kiem_tra_so_khong_giam(n):
        print("YES")
    else:
        print("NO")