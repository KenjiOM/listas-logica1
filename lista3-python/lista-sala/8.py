b = 1
c = 0
for a in range (1, 16):
    d = b + c
    e = d + b
    print(b)
    c = b
    b = d
    d = e