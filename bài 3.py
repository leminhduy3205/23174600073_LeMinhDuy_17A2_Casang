a = int(input("Nhap vao mot so nguyen bat ki co 3 chu so: "))
a1 = a//100
a2 = (a//10)%10
a3 = a%10
if a1 == 1:
    a1 = "one hundred"
elif a1 == 2:
    a1 = "two hundred"
elif a1 == 3:
    a1 = "three hundred"
elif a1 == 4:
    a1 = "four hundred"
elif a1 == 5:
    a1 = "five hundred"
elif a1 == 6:
    a1 = "six hundred"
elif a1 == 7:
    a1 = "seven hundred"
elif a1 == 8:
    a1 = "eight hundred"
elif a1 == 9:
    a1 = "nine hundred"
if a2 == 1:
    a2 = "ten"
elif a2 == 2:
    a2 = "twenty"
elif a2 == 3:
    a2 = "thirty"
elif a2 == 4:
    a2 = "forty"
elif a2 == 5:
    a2 = "fifty"
elif a2 == 6:
    a2 = "sixty"
elif a2 == 7:
    a2 = "seventy"
elif a2 == 8:
    a2 = "eighty"
elif a2 == 9:
    a2 = "ninety"
elif a2 == 0 and a3!=0:
    a2 = ""
if a3 ==1:
    a3 ="one"
if a3 ==2:
    a3 ="two"
if a3 ==3:
    a3 ="three"
if a3 ==4:
    a3 ="four"
if a3 ==5:
    a3 ="five"
if a3 ==6:
    a3 ="six"
if a3 ==7:
    a3 ="seven"
if a3 ==8:
    a3 ="eight"
if a3 ==9:
    a3 ="nine"
if a3 ==0:
    a3 =""
print("Cach doc la:", a1,a2,a3)
