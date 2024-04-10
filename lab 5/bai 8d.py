input_string = input("Nhập chuỗi ký tự (độ dài > 10): ")

if len(input_string) > 10:
    lowercase_string = input_string.lower()
    print(f"Chuỗi sau khi chuyển đổi thành chữ thường: {lowercase_string}")
else:
    print("Chuỗi ký tự không đủ độ dài (> 10 ký tự) để chuyển đổi.")