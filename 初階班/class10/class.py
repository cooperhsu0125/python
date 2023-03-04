x = {}
y = int(input('number:'))
for i in range(y):
    key = input('key:')
    value = input('value:')
    x[key] = value
    print(x)

z = input('delete key:')
f = x.pop(z, 'error')
print(f'delete:{f}')

for key, value in x.items():
    print(f'{key}={value}')
e = input('search key:')
print(f'{e in x}')