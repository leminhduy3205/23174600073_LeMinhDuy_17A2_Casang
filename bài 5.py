def tinh_tong_tien_ve(n):
    gia_ve= 120000

    tong_tien = n * gia_ve
    if n >= 2 and n <=4:
        tong_tien= 0.05*tong_tien 
    elif n>=4 and n<=10:
        tong_tien= 0.1*tong_tien
    elif n>=10:
        tong_tien=0.2*tong_tien
    return tong_tien
#-----
so_luong= int(input("Nhập số lượng vé mua: "))
tong_tien_ve= tinh_tong_tien_ve(so_luong)
print("Tổng số tiền phải trả là:", tong_tien_ve, "Đồng")


