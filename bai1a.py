while True:
    n = int(input("Nhập số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập lại số nguyên dương n.")
    else:
        break
tong = 0
so = 1
for i in range(1, n+1):
    tong += so
    so += 1
print(f"Tổng S1 = {tong}")
