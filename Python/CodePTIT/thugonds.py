"""
Cho dãy số A[] chỉ bao gồm các số nguyên dương. Người ta thu gọn dần dãy số bằng cách loại bỏ các cặp phần tử 
kề nhau mà có tổng là chẵn. Sau khi cặp phần tử đó bị loại ra thì dãy số được dồn lại. Cứ tiếp tục như vậy cho 
đến khi không còn cặp phần tử nào kề nhau có tổng chẵn nữa.
Hãy tính xem cuối cùng dãy A[] còn bao nhiêu phần tử.

Input
Dòng đâu ghi số N là số phần tử của dãy (1 ≤ N ≤ 105 tức là dãy A có thể có đến 10 nghìn phần tử).
Dòng tiếp theo ghi N số của dãy A (1 ≤ A[i] ≤ 100).

Output
Ghi ra trên một dòng số phần tử còn lại trong dãy A[].
"""
n = int(input("Nhap so luong dau vao : "))
a = [int(input("Nhap cac phan tu : ")) for _ in range(n)]
while True:
    new_a = []
    i = 0
    while i < len(a):
        if i < len(a) - 1 and (a[i] + a[i+1]) % 2 == 0:
            i += 2
        else:
            new_a.append(a[i])
            i += 1
    if len(new_a) == len(a):
        break
    a = new_a
print(len(a))
