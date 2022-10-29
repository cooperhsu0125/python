c = int(input())
d = c - 1
for a in range(c):
    b = a * 2 + 1
    print(f' ' * d + "*" * b)
    d -= 1
for e in range(c):
    print(f' ' * (c - 1) + "*")
