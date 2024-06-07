def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
A = list(map(int, input().split()))

prime_counts = {}
for num in A:
    if is_prime(num):
        if num not in prime_counts:
            prime_counts[num] = 1
        else:
            prime_counts[num] += 1

for num, count in prime_counts.items():
    print(num, count)