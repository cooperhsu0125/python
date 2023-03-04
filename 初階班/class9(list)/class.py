# l = ['a', 'b', 'c']
# l[0] = 'A'

# a = [1, 2, 3]
# b = a
# b[0] = 2
# print(a)

# l = [1, 2, 3]
# l.append(4)
# print(l)執行結果:[1,2,3,4]

# l = [9, 1, -4, 3, 7, 11, 3]
# print(l.count(3))執行結果:2

# l = ['a', 'b', 'c', 'a']
# l.remove('a')
# print(l)執行結果:['b', 'c', 'a']
# l = ['a','b', 'a', 'c']
# if 'a' in l:
#   print(true)
# else:
#   print(false)
# while 'a' in l:
#   l.remove('a')
# print(l)執行結果:['b', 'c']

# l = [1, 2, 3]
# l.insert(0, 'A')
# print(l)執行結果:['A', 1, 2, 3]

# l = [1, 2, 3]
# l.pop()
# print(l)執行結果:[1,2]

# l = [1, 2, 3]
# l.pop(0)
# print(l)執行結果:[2,3]

# l = [3, 1, 5, 4, 2]
# l.sort()
# print(l)執行結果:[1, 2, 3, 4, 5]

# l = [3, 1, 5, 4, 2]
# l.sort(reverse=True)
# print(l)執行結果:[5, 4, 3, 2, 1]

# l = [3, 1, 5, 4, 2]
# l.reverse()
# print(l)執行結果:[2, 4, 5, 1, 3]

# l = ['a', 'b', 'c', 'a']
# print(l.index('a'))執行結果:0
# l = []

# while True:
#     a = input("輸入e就離開程式，請輸入想新增的資料:")
#     if a == 'e':
#         break
#     else:
#         l.append(a)
#         print(l)
# while True:
#     a = input("輸入e就離開程式，請輸入想移除的資料:")
#     if a == 'e':
#         break
#     else:
#         while a in l:
#             l.remove(a)
#         print(l)
# b = []
# for i in l:
#     if not (i in b):
#         b.append(i)
# for i in b:
#     print(f'{i}有{l.count(i)}個')
