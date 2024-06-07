def kiem_tra_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            return False
    return True
def uet(n):
    cn1 = 0
    for i in range(4):
        cn1 = cn1 * 10 + n % 10
        n //= 10
    m = str(cn1)
    return int(m[::-1])
t = int(input())
for _ in range(t):
    n = int(input())
    if kiem_tra_nguyen_to(uet(n)):
        print("YES")
    else:
        print("NO")
