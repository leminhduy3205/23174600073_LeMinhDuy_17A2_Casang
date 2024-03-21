def xep_loai_diem(diem):
    if 0<= diem<5:
        return "Điểm kém"
    elif 5<= diem<=7:
        return "Điểm trung bình"
    elif 7<= diem <=8.5:
        return "Điểm khá"
    elif 8.5<= diem <= 10:
        return "Điểm tốt"
    else:
        return "Điểm không hợp lệ"
#---
diem = float(input("Nhập điểm số của bài kiểm tra: "))
xep_loai= xep_loai_diem(diem)
print("Xếp loại điểm:", xep_loai)