def factorial(n):
    """Tính giai thừa của n"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def permutations(n, r):
    """Tính số hoán vị của n phần tử lấy r phần tử mỗi lần"""
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    """Tính số tổ hợp của n phần tử lấy r phần tử mỗi lần"""
    return permutations(n, r) // factorial(r)

# Ví dụ sử dụng:
n = 5
r = 3

print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần: P({n}, {r}) = {permutations(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần: C({n}, {r}) = {combinations(n, r)}")
