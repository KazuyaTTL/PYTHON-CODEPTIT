def sum_of_digits(n):
    sudi = 0
    while n != 0:
        sudi += n % 10
        n //= 10
    return sudi
def sort_by_digit_sum(A):
    return sorted(A, key=lambda x: (sum_of_digits(x), x))
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sort_by_digit_sum(a)
    for i in b:
        print(i, end = " ")