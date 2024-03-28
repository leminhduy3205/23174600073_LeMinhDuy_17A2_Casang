print("Các số chính phương từ 1 đến 1000 là:")
for num in range(1, 1001):
    if int(num**0.5) ** 2 == num:
        print(num, end=" ")
