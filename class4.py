# not False = True
# not True = False
# True and True = True
# True and False = False
# False and True = False
# False and False = False
# True or True = True
# True or False = True
# False or True = True
# # False or False = False
# password = input('請輸入密碼:')
# if password == '0':
#     print(...)
# elif password == '00':
#     print(',')
# else:
#     print('????????????????????')
# a = int(input('請輸入成績:'))
# if a >= 90:
#     print('A')
# elif a >= 80:
#     print('B')
# elif a >= 70:
#     print('C')
# elif a >= 60 and a < 70:
#     print('D')
# elif a < 60:
#     print('E')
a = input('輸入數字:')
a = int(a)
if a % 2 == 0:
    print('是偶數')
else:
    print('是奇數')