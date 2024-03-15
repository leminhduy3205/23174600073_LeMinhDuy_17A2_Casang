class Sach:
    def __init__(self, ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong):
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.nam_xuat_ban = nam_xuat_ban
        self.so_luong = so_luong

    def hien_thi_thong_tin(self):
        print(f"Thư viện ĐHKTKTCN có {self.so_luong} sách {self.ten_sach} với mã số {self.ma_sach}.")
        print(f"Cuốn sách của tác giả {self.tac_gia} được xuất bản vào năm {self.nam_xuat_ban}")

def nhap_thong_tin_sach():
    ma_sach = input("Nhập mã sách (mã sinh viên): ")
    ten_sach = input("Nhập tên sách: ")
    tac_gia = input("Nhập tác giả: ")
    nam_xuat_ban = input("Nhập năm xuất bản: ")
    so_luong = input("Nhập số lượng sách (ngày sinh của sinh viên): ")

    return Sach(ma_sach, ten_sach, tac_gia, nam_xuat_ban, so_luong)

def main():
    sach = nhap_thong_tin_sach()
    sach.hien_thi_thong_tin()

if __name__ == "__main__":
    main()
