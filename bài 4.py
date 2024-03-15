import math

def tinh_dien_tich_xung_quanh(canh_day, chieu_cao):
    chu_vi_day = 4 * canh_day
    dien_tich_xung_quanh = 0.5 * chu_vi_day * chieu_cao
    return dien_tich_xung_quanh

def tinh_dien_tich_toan_phan(canh_day, chieu_cao):
    dien_tich_day = canh_day**2
    dien_tich_xung_quanh = tinh_dien_tich_xung_quanh(canh_day, chieu_cao)
    dien_tich_toan_phan = dien_tich_xung_quanh + dien_tich_day
    return dien_tich_toan_phan

def tinh_the_tich(canh_day, chieu_cao):
    dien_tich_day = canh_day**2
    the_tich = (1/3) * dien_tich_day * chieu_cao
    return the_tich

def main():
    canh_day = float(input("Nhập độ dài cạnh đáy của hình chóp đều: "))
    chieu_cao = float(input("Nhập chiều cao của hình chóp đều: "))

    dien_tich_xung_quanh = tinh_dien_tich_xung_quanh(canh_day, chieu_cao)
    dien_tich_toan_phan = tinh_dien_tich_toan_phan(canh_day, chieu_cao)
    the_tich = tinh_the_tich(canh_day, chieu_cao)

    print(f"Diện tích xung quanh của hình chóp là: {dien_tich_xung_quanh:.2f} đơn vị vuông")
    print(f"Diện tích toàn phần của hình chóp là: {dien_tich_toan_phan:.2f} đơn vị vuông")
    print(f"Thể tích của hình chóp là: {the_tich:.2f} đơn vị khối")

if __name__ == "__main__":
    main()