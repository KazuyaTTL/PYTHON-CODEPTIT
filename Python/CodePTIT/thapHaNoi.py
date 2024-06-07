def diChuyen(nguon, dich):
    print("Chuyen tu", nguon, "sang", dich)

def thapHaNoi(n, nguon, dich, trungGian):
    if n == 1:
        diChuyen(nguon, dich)
    else:
        thapHaNoi(n-1, nguon, trungGian, dich)
        diChuyen(nguon, dich)
        thapHaNoi(n-1, trungGian, dich, nguon)

fn = input()
eval(fn)(int(input()), 'A', 'B', 'C')