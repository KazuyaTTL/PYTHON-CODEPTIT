p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    str = input()
    if(str == '0'): 
        break
    else:
        k, s = str.split()
        k = int(k)
        n = ""
        for i in s:
            x = 0
            for j in p:
                if i == j: 
                    break
                x += 1
            x = (x + k) % 28
            n = p[x] + n
        print(n)
