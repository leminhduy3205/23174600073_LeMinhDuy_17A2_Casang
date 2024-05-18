def is_armstrong(n):
    """Kiểm tra xem một số có phải là số Armstrong hay không"""
    total = 0
    num = n
    num_digits = len(str(n))
    
    while num > 0:
        digit = num % 10
        total += digit ** num_digits
        num //= 10
    
    return total == n

def PrintArmstrong():
    """In ra tất cả các số Armstrong từ 1 đến 999"""
    for number in range(1, 1000):
        if is_armstrong(number):
            print(number)

# Sử dụng hàm PrintArmstrong():
PrintArmstrong()
