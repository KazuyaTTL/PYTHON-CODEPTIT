"""
Cho dãy số A[] chỉ có các giá trị nhị phân 0 và 1.

Hãy đếm xem có bao nhiêu cặp số khác nhau đứng cạnh nhau trong dãy.

Input

Dòng 1 ghi số N là số phần tử của dãy (không quá 100).

Dòng 2 ghi N số nhị phân.

Output

Ghi ra kết quả bài toán.

Ví dụ 
Input:

6
1 0 0 1 1 1

Output:

2
"""
n = int(input())
uet = list(map(int, input().split()))
cnt = 0
for i in range(1, len(uet)):
    if uet[i] != uet[i-1]:
        cnt += 1
print(cnt)