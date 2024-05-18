def is_odd(n):
    """Kiểm tra xem một số có phải là số lẻ hay không"""
    return n % 2 != 0

def filter_odd_numbers(numbers):
    """Lọc các số lẻ từ danh sách numbers"""
    return list(filter(is_odd, numbers))

# Danh sách các số cần lọc
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lọc các số lẻ từ danh sách
odd_numbers = filter_odd_numbers(number_list)

# In kết quả
print("Các số lẻ trong danh sách là:", odd_numbers)
