# def hello():
#     print('hello')執行結果:不會有任何輸出
# hello()執行結果:hello

# def hello(name):#name是變數
#     print(f'hello{name}')執行結果:不會有任何輸出
# hello('Jay')執行結果:helloJay

# def m(a, b):
#   if a < b:
#       return a
#   else:
#       return b執行結果:不會有任何輸出
# print(m(1, 2))執行結果:1
import random as r


def a(b):
    re = []
    for i in range(b):
        re.append(r.randint(1, 6))
    return re


d = a(int(input('輸入想擲骰子的次數:')))
for i in range(len(d)):
    print(f'擲第{i+1}次的骰子為{d[i]}點')
print(f"最大值是{max(d)}, 最小值是{min(d)}")
print(f"6出現了{d.count(6)}次")