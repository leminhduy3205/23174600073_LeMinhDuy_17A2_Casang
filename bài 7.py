def xep_loai_chi_so_BMI(chi_so):
    if chi_so<18.5:
        return "Gầy"
    elif 18.5<chi_so<24.9:
        return "Bình thường"
    elif 25.0<chi_so<29.9:
        return "Hơi béo"
    elif chi_so>=30.0:
        return "Béo"
    return "Chỉ số"
        
#-----
chi_so = float(input("nhập chỉ số: "))
xep_loai = xep_loai_chi_so_BMI(chi_so)
print("Xếp loại chỉ số", xep_loai)
