def check_property(n):
    str_n = str(n)
    first_two_digits = str_n[:2]
    last_two_digits = str_n[-2:]
    return first_two_digits == last_two_digits

def main():
    t = int(input("Nhập số lượng test: "))
    for _ in range(t):
        n = int(input("Nhập số nguyên dương N: "))
        if len(str(n)) < 4:
            print("NO")
        else:
            result = "YES" if check_property(n) else "NO"
            print(result)

if __name__ == "__main__":
    main()