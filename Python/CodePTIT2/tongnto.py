"""
Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

Hãy kiểm tra xem tổng các chữ số của N có phải là một số nguyên tố hay không.

Input

Dòng đầu ghi số bộ test (không quá 20).

Mỗi test ghi số N (không quá 500 chữ số)

Output

Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
"""
def Sum_Digit(n):
    sudi = 0
    while n != 0:
        sudi += n % 10
        n //= 10
    return sudi
def IsPrime(so):
    if so < 2:
        return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return False
    return True
t = int(input())
for _ in range(t):
    n = int(input())
    if IsPrime(Sum_Digit(n)):
        print("YES")
    else:
        print("NO")