# Khởi tạo các biến ban đầu
initial_amount = 10000  # Số tiền ban đầu
annual_interest_rate = 0.06  # Lãi suất hàng năm

# Tính toán số tiền sau 5 năm và 10 năm
amount_after_5_years = initial_amount * (1 + annual_interest_rate)**5
amount_after_10_years = initial_amount * (1 + annual_interest_rate)**10

# Tính toán tỷ lệ tăng trưởng
growth_rate = (amount_after_10_years - amount_after_5_years) / amount_after_5_years

# In kết quả ra màn hình
print(f"Số tiền sau 5 năm: ${amount_after_5_years:.2f}")
print(f"Số tiền sau 10 năm: ${amount_after_10_years:.2f}")
print(f"Tỷ lệ tăng trưởng sau 10 năm so với sau 5 năm: {growth_rate:.2%}")