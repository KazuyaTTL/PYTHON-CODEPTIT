t = int(input())

while(t>0):
    t -= 1
    s = input()+' '
    d = 1
    for i in range (1,len(s)):
        if(s[i]!=s[i-1]):
            print(d,s[i-1],end="",sep="")
            d = 1
        else:
            d += 1
    print()