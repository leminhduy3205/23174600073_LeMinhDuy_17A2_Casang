so_nguoi = int(input("Nhập số lượng người: "))
gia_ve = 120000
tong_tien = so_nguoi * gia_ve

if 2 <= so_nguoi <= 4:
    tong_tien *= 0.95
elif 4 < so_nguoi <= 10:
    tong_tien *= 0.9
elif so_nguoi > 10:
    tong_tien *= 0.8

print("Tổng số tiền phải trả là:", tong_tien, "đồng")


