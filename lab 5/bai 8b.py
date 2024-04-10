input_string = input("Nhập chuỗi ký tự (độ dài > 10): ")

if len(input_string) > 10:
    substring = input_string[4:9]
    print(f"Chuỗi ký tự con gồm 5 ký tự kể từ vị trí 5 là: {substring}")
else:
    print("Chuỗi ký tự không đủ độ dài (> 10 ký tự) để trích xuất chuỗi con.")