def chu_so_hang_ngan(so_nguyen):
    if len(str(so_nguyen)) >=4:
        chu_so_hang_ngan = int(str(so_nguyen)[-4])
    else:
        chu_so_hang_ngan = 0
        return chu_so_hang_ngan
#---
so_nguyen=int(input("Nhập một số nguyên: "))

chu_so_hang_ngan = chu_so_hang_ngan(so_nguyen)
print("Chữ số hàng nghìn của số", so_nguyen, "là:", chu_so_hang_ngan)