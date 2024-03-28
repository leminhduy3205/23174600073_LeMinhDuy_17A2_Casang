
a, b = 0, 1
print(a, end=" ")
print(b, end=" ")
while a + b < 100:
    c = a + b
    print(c, end=" ")
    a, b = b, c
