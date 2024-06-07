"""
Cho một số nguyên dương N. Mỗi bước bạn thực hiện tính tổng của N với giá trị số đảo ngược của N. Bạn sẽ dừng lại khi gặp giá 
trị chia hết cho 7 hoặc khi đã thực hiện quá 1000 bước lặp.

Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên hoặc ghi ra -1 nếu không thể tìm ra đáp án.

Input:
Dòng đầu ghi số bộ test (không quá 1000).
Mỗi test ghi số N (1 ≤ N ≤ 1018)

Output:
Ghi ra giá trị chia hết cho 7 đầu tiên tìm được. Hoặc số -1 nếu không thể tìm được đáp án.
"""
# Giải thích test 1: 1 -> 2 -> 4 -> 8 -> 16 -> 77
def solve1(n):
    return int(str(n)[::-1])
def solve2(n):    
    count = 0
    while count < 1000:
        n += solve1(n)
        if n % 7 == 0:
            return n
        count += 1
    return -1
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve2(n))
    