def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, 1000):
    if is_prime(i) and is_prime(i + 2):
        print(f"({i}, {i + 2})")
