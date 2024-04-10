input_string = input("Nhập chuỗi ký tự: ")
numeric_string = ''.join(filter(str.isdigit, input_string))

if numeric_string:
    number = int(numeric_string)
    

    if number <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

    if is_prime:
        print(f"Chuỗi ký tự '{numeric_string}' là một số nguyên tố.")
    else:
        print(f"Chuỗi ký tự '{numeric_string}' không phải là một số nguyên tố.")
else:
    print("Không có số nào trong chuỗi ký tự đã cho.")