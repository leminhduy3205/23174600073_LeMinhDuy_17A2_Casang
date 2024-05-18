def sumPdivisors(n):
    """Tính tổng các ước số chính của một số n"""
    return sum([i for i in range(1, n) if n % i == 0])

# Sử dụng hàm sumPdivisors():
number = 66
print(f"Tổng các ước số chính của {number} là: {sumPdivisors(number)}")
