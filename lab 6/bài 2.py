n = int(input("Nhập số phần tử của mảng: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

prime_numbers = [num for num in arr if num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
perfect_numbers = [num for num in arr if num > 1 and num == sum(i for i in range(1, num) if num % i == 0)]

print("Các số nguyên tố trong mảng:", prime_numbers)
print("Các số hoàn hảo trong mảng:", perfect_numbers)