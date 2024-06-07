"""
Cho số nguyên dương N. Hãy kiểm tra xem N có thỏa mãn đồng thời hai tính chất sau đây hay không?

Tổng chữ số của N chia hết cho 10
Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị
Input

Dòng đầu ghi số bộ test. Mỗi bộ test ghi trên một dòng số nguyên dương N. N có ít nhất 3 chữ số nhưng không quá 18 chữ số.

Output

Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra
"""
from math import*
def tongchuso(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong % 10 == 0
def check(n):
    a = n % 10
    n //= 10
    while n != 0:
        b = n % 10
        if abs(a - b) != 2:
            return False
        a = b
        n //= 10
    return True
t = int(input("Nhập bộ số test : "))
for i in range(t):
    n = int(input())
    if tongchuso(n):
        if check(n):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    