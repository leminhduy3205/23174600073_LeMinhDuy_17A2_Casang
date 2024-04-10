so_thap_phan_input = int(input("Nhập số nguyên dương (số thập phân): "))
if so_thap_phan_input < 0:
    print("Số không hợp lệ")
else:
    nhi_phan_output = ""
    if so_thap_phan_input == 0:
        nhi_phan_output = "0"
    else:
        while so_thap_phan_input > 0:
            remainder = so_thap_phan_input % 2
            nhi_phan_output = str(remainder) + nhi_phan_output
            so_thap_phan_input = so_thap_phan_input // 2
    print(f"Số nhị phân tương ứng là: {nhi_phan_output}")