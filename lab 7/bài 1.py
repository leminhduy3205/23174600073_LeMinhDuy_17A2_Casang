#Tạo từ điển
từ_điển = {}
#Nhập số nguyên N
N = int(input("Nhập số nguyên N:"))
#Nhập và lưu giá trị cho từ điển
từ_điển = {x: x**3 for x in range(1, N+1) }
 #Xuất từ ​​điển
print(" từ điển")
for key, value in từ_điển.items():
   print(f"{key} -> {value}")


