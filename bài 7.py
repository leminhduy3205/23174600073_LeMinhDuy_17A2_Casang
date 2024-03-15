def giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2):
    # Tính định thức
    det = a1 * b2 - a2 * b1
    # Tính x và y
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return x, y

def main():
    # Nhập các hệ số từ người dùng
    a1 = float(input("Nhập hệ số a1: "))
    b1 = float(input("Nhập hệ số b1: "))
    c1 = float(input("Nhập hệ số c1: "))
    a2 = float(input("Nhập hệ số a2: "))
    b2 = float(input("Nhập hệ số b2: "))
    c2 = float(input("Nhập hệ số c2: "))

    # Gọi hàm giải hệ phương trình
    x, y = giai_he_phuong_trinh(a1, b1, c1, a2, b2, c2)

    # Hiển thị kết quả
    print(f"Giải hệ phương trình:")
    print(f"{a1}x + {b1}y = {c1}")
    print(f"{a2}x + {b2}y = {c2}")
    print(f"Có nghiệm x = {x:.2f}, y = {y:.2f}")

if __name__ == "__main__":
    main()
