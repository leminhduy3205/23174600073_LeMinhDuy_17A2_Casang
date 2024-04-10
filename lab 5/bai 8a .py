input_string = input("Nhập chuỗi ký tự (độ dài > 10): ")

if len(input_string) > 10:
    substring = input_string[1:8]
    print(f"Chuỗi ký tự con từ vị trí 2 đến vị trí 8 là: {substring}")
else:
    print("Chuỗi ký tự không đủ độ dài (> 10 ký tự) để trích xuất chuỗi con.")