str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

shortest_substring = ""
min_length = min(len(str1), len(str2))

for i in range(min_length):
    if str1[i] == str2[i]:
        shortest_substring += str1[i]
    else:
        break

print(f"Chuỗi ký tự con chung có độ dài ngắn nhất là: {shortest_substring}")