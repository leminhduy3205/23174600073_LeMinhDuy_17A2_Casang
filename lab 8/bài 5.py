def sum_of_divisors(n):
    """Tính tổng các ước số chính của số n"""
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def are_amicable(num1, num2):
    """Kiểm tra xem hai số có phải là cặp số amicable hay không"""
    return sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1

# Sử dụng hàm are_amicable():
number1 = 666
number2 = 666

if are_amicable(number1, number2):
    print(f"{number1} và {number2} là một cặp số amicable")
else:
    print(f"{number1} và {number2} không phải là một cặp số amicable")
