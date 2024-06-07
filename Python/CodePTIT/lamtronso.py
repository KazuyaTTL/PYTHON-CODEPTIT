def round_number(n):
    power = 0
    while n > 10:
        n = round(n, -power)
        power += 1
    return int(n)

# Nhập dữ liệu
t = int(input("Nhập số bộ test: "))
for _ in range(t):
    n = int(input("Nhập số nguyên dương N: "))
    print(round_number(n))