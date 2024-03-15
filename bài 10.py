import math

def tinh_xac_suat_bi_do(so_bi_rut, tong_so_bi):
    return so_bi_rut / tong_so_bi

def tinh_xac_suat_it_nhat_mot_bi_xanh(so_bi_xanh_rut, tong_so_bi):
    return 1 - so_bi_xanh_rut / tong_so_bi

def tinh_xac_suat_2_bi_vang(so_bi_vang, tong_so_bi):
    return math.comb(so_bi_vang, 2) / math.comb(tong_so_bi, 2)

def main():
    so_bi_do = 20
    so_bi_xanh = 15
    so_bi_vang = 15
    tong_so_bi = 50

    so_bi_rut = int(input("Nhập số lượng bi bạn muốn rút ra từ hộp: "))

    # Tính xác suất cho mỗi trường hợp
    xac_suat_bi_do = tinh_xac_suat_bi_do(so_bi_do, so_bi_rut)
    xac_suat_it_nhat_mot_bi_xanh = tinh_xac_suat_it_nhat_mot_bi_xanh(so_bi_rut - so_bi_xanh, so_bi_rut)
    xac_suat_2_bi_vang = tinh_xac_suat_2_bi_vang(so_bi_vang, so_bi_rut)

    # Hiển thị kết quả
    print(f"Xác suất để rút ra tất cả là bi đỏ: {xac_suat_bi_do:.4f}")
    print(f"Xác suất để ít nhất một viên là bi xanh: {xac_suat_it_nhat_mot_bi_xanh:.4f}")
    print(f"Xác suất để rút chính xác hai viên bi vàng: {xac_suat_2_bi_vang:.4f}")

if __name__ == "__main__":
    main()
