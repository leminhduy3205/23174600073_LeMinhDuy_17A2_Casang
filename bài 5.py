def tinh_tien_dien_gia_dinh(hieu_dien_the, cuong_do_dien, so_gio_su_dung, gia_dien):
    # Tính công suất (W)
    cong_suat = hieu_dien_the * cuong_do_dien
    
    # Tính năng lượng tiêu thụ (kWh)
    nang_luong_tieu_thu = (cong_suat / 1000) * so_gio_su_dung
    
    # Tính số tiền điện phải trả
    tien_dien = nang_luong_tieu_thu * gia_dien
    
    return tien_dien

def main():
    hieu_dien_the = float(input("Nhập hiệu điện thế (V): "))
    cuong_do_dien = float(input("Nhập cường độ dòng điện (A): "))
    so_gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))
    gia_dien = 5000  # Giá điện (đồng/kWh)

    tien_dien = tinh_tien_dien_gia_dinh(hieu_dien_the, cuong_do_dien, so_gio_su_dung, gia_dien)

    print(f"Tổng số tiền điện phải trả là: {tien_dien:.2f} đồng")

if __name__ == "__main__":
    main()