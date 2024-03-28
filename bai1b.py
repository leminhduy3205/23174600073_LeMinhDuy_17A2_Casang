# Nhập số nguyên dương n từ người dùng
while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập lại số nguyên dương n.")
    else:
        break

# Khởi tạo biến tổng S2
tong_s2 = 0

# Tính tổng S2 = 1/1 + 1/2 + 1/3 + ... + 1/n
for i in range(1, n+1):
    tong_s2 += 1/i

# Hiển thị kết quả
print(f"Tổng S2 = {tong_s2}")
