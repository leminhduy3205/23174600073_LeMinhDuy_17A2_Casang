n = int(input("Nhập số phần tử của mảng: "))
arr = []
for i in range(n):
   arr.append(int(input(f"Nhập phần tử thứ {i+1}: ")))

sum_even = sum(num for num in arr if num % 2 == 0)
sum_odd = sum(num for num in arr if num % 2 != 0)

print("Tổng các số chẵn trong mảng:", sum_even)
print("Tổng các số lẻ trong mảng:", sum_odd)