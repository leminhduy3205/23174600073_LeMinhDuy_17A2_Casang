n = int(input("Nhập số lượng số Fibonacci muốn tạo: "))

fibonacci_list = [0, 1] + [fibonacci_list[i-1] + fibonacci_list[i-2] for i in range(2, n)]

print(f"Danh sách {n} số Fibonacci đầu tiên là:")
print(fibonacci_list)