kho = {"banana": 6, "apple": 5, "orange": 32, "pear": 15}
gia_tien = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

hoa_don = {}
tong_tien = 0

for mat_hang in kho:
    if mat_hang in gia_tien:
        so_luong = min(kho[mat_hang], 1)  
        so_tien = so_luong * gia_tien[mat_hang]
        tong_tien += so_tien
        kho[mat_hang] -= so_luong
        hoa_don[mat_hang] = {"Số lượng": so_luong, "Đơn giá": gia_tien[mat_hang], "Số tiền": so_tien}

print("Hóa đơn mua hàng:")
for mat_hang, thong_tin in hoa_don.items():
    print(f"{mat_hang}: {thong_tin}")

print("\nTổng số tiền của hóa đơn:", tong_tien)
print("\nSố lượng của các mặt hàng trong kho sau khi giao dịch:", kho)
