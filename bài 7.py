chieu_cao = float(input("Nhập chiều cao của bạn (mét): "))
can_nang = float(input("Nhập cân nặng của bạn (kg): "))

bmi = can_nang / (chieu_cao ** 2)
print("Chỉ số BMI của bạn là:", bmi)

if bmi < 18.5:
    print("Phân loại BMI: Gầy")
elif 18.5 <= bmi <= 24.9:
    print("Phân loại BMI: Bình thường")
elif 25.0 <= bmi <= 29.9:
    print("Phân loại BMI: Hơi béo")
else:
    print("Phân loại BMI: Béo")


