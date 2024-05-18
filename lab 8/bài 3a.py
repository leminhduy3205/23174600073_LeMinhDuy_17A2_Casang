def cubesum(n):
    """Trả về tổng của các lập phương của các chữ số riêng lẻ của số nguyên n"""
    total = 0
    for digit in str(n):
        total += int(digit) ** 3
    return total

# Ví dụ sử dụng:
n = 666
print(f"Tổng các lập phương của các chữ số của {n} là: {cubesum(n)}")
