numbers = input("Nhập dãy số, cách nhau bởi dấu cách: ").split()
numbers = [float(num) for num in numbers]

max_number = max(numbers)
min_number = min(numbers)

print("Số lớn nhất trong dãy số:", max_number)
print("Số nhỏ nhất trong dãy số:", min_number)