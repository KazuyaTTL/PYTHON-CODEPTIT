# Hàm để tính dãy số Fibonacci
def fibonacci(n):
    # Khởi tạo hai số đầu tiên
    fib = [1, 1]
    # Tính các số tiếp theo trong dãy
    for i in range(3, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib

# Hàm để giải quyết bài toán
def solve(test_cases):
    # Tính dãy số Fibonacci
    fib = fibonacci(93)
    # Duyệt qua từng bộ test
    for a, b in test_cases:
        # In ra các số Fibonacci từ a đến b
        print(' '.join(str(fib[i]) for i in range(a, b+1)))

# Nhập số lượng bộ test
t = int(input().strip())
# Khởi tạo danh sách các bộ test
test_cases = []
for _ in range(t):
    # Nhập từng bộ test
    a, b = map(int, input().strip().split())
    test_cases.append((a, b))

# Gọi hàm giải quyết bài toán
solve(test_cases)