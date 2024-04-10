input_string = input("Nhập chuỗi ký tự: ")

lowercase_count = 0
uppercase_count = 0
digit_count = 0
special_count = 0

for char in input_string:
    if char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print(f"Số lượng chữ thường: {lowercase_count}")
print(f"Số lượng chữ hoa: {uppercase_count}")
print(f"Số lượng chữ số: {digit_count}")
print(f"Số lượng ký tự đặc biệt: {special_count}")