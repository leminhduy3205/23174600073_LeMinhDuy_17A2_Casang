def filter_even_numbers(numbers):
    """Lọc các số chẵn từ danh sách numbers"""
    return [num for num in numbers if not num % 2]

# Danh sách các số cần lọc
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lọc các số chẵn từ danh sách
even_numbers = filter_even_numbers(number_list)

# In kết quả
print("Các số chẵn trong danh sách là:", even_numbers)
