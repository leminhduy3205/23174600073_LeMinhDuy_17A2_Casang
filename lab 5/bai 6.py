input_string = input("Nhập chuỗi ký tự: ")

special_characters_count = {}
total_characters = len(input_string)

for char in input_string:
    if not char.isalnum():
        if char in special_characters_count:
            special_characters_count[char] += 1
        else:
            special_characters_count[char] = 1

print("Số lần xuất hiện của từng ký tự đặc biệt trong chuỗi:")
for char, count in special_characters_count.items():
    print(f"'{char}': {count}")

print("\nTỷ lệ phần trăm của mỗi ký tự đặc biệt trong chuỗi:")
for char, count in special_characters_count.items():
    percentage = (count / total_characters) * 100
    print(f"'{char}': {percentage:.2f}%")