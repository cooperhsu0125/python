'''
for i in range(2, 6):
    print(i)
else:
    print("迴圈正常結束")

i = 2
while i < 6:
    print(i)
    i += 1
else:
    print("迴圈正常結束")

i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1

for i in range(1, 6):
    if i == 3:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
a = ('1.蘋果汁')
b = ('2.柳橙汁')
c = ('3.葡萄汁')
d = ('4.系統關閉')
while True:
    print(a)
    print(b)
    print(c)
    print(d)
    x = input('請輸入編號:')
    if x == '1':
        print('您點的商品是' + a)
    if x == '2':
        print('您點的商品是' + b)
    if x == '3':
        print('您點的商品是' + c)
    if x == '4':
        print(d)
        break
    if x != '1' and '2' and '3' and '4':
        print('沒有這項商品')
        '''
import random as r
import time as t
# while True:
#     print(r.randrange(7))
#     t.sleep(3)
x = (r.randrange(101))
while True:

    a = int(input('請輸入1~100的整數'))
    if a > x:
        print('再小一點')
    if a < x:
        print('再大一點')
    if a == x:
        print('猜中了')
        break
