numbers = input("Nhập dãy số, cách nhau bởi dấu cách: ").split()
numbers = [int(num) for num in numbers]

differences = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]
is_arithmetic_progression = all(diff == differences[0] for diff in differences)

if is_arithmetic_progression:
    print("Dãy số", numbers, "tạo thành cấp số cộng.")
else:
    print("Dãy số", numbers, "không tạo thành cấp số cộng.")
    