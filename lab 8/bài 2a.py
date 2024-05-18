from math import factorial

def permutations(n, r):
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Ví dụ sử dụng:
n = 7
r = 5

print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần: P({n}, {r}) = {permutations(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần: C({n}, {r}) = {combinations(n, r)}")
