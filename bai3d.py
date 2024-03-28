print("Các số hoàn hảo bé hơn 500 là:")
for num in range(2, 501):
    tong_uoc = 1  
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            tong_uoc += i
            if i != num // i:  
                tong_uoc += num // i
    if tong_uoc == num:
        print(num, end=" ")
