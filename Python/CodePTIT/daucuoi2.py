t = int(input())
for _ in range(t):
    n = int(input())
    m = str(n)
    if m[:2] == m[-2:]:
        print("YES")
    else:
        print("NO")