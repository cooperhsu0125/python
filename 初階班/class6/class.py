# a = int(input())
# c = 0
# for b in range(a):
#     c = b + c

# print(c + a)
# for a in range(1, 10):
#     for b in range(1, 10):
#         c = a * b
#         print(f'{a}x{b}={c}')
a = int(input())
b = 2
while a % b != 0 and b != a:
    b += 1
if a == b:
    print('yes')
else:
    print('no')
