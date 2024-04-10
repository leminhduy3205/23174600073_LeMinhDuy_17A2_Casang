input_string = input("Nhập chuỗi ký tự (độ dài > 10): ")

if len(input_string) > 10:
    reversed_string = input_string[::-1]
    print(f"Chuỗi sau khi được đảo ngược: {reversed_string}")
else:
    print("Chuỗi ký tự không đủ độ dài (> 10 ký tự) để đảo ngược.")