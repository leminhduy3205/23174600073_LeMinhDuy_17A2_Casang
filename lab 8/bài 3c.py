def isArmstrong(n):
    """Kiểm tra xem một số n có phải là số Armstrong hay không"""
    num_str = str(n)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == n

# Sử dụng hàm isArmstrong():
number = 153
if isArmstrong(number):
    print(f"{number} là số Armstrong")
else:
    print(f"{number} không phải là số Armstrong")
