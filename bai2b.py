 
tong = 0
for num in range(500, 1001):
    if num % 4 == 0 and num % 6 != 0:
        tong += num
print(f"Tổng các số chia hết cho 4 nhưng không chia hết cho 6 từ 500 đến 1000 là: {tong}")
