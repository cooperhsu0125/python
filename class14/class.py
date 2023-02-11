'''
練習1(Ref MTA2:P2)
請問下列變數哪一些有問題?問題出在哪裡?第4.個有問題，問題出在數字
1. Var = "Data"                     第2.個有問題，問題出在語句必須用換行符或分號分隔
2. Your Name = "Data"
3. Date = "Data"問題出在數字
4. 3Name = "Data"
5. S12345 = "Data"
6. YourPythonareVeryVeryGood = "Data"
2
A = input("輸入您要的數值") 
#e.g. A = 1234
1.將 A 格式化成整數，並使用print顯示出來print(int(A))
2.以 5 個字元寬度顯示整數A，不滿 5 個則補空白print('%5d'% A)
3.以 5 個字元寬度顯示整數A，不滿 5 個則補零print('%05d'% A)
3
A = input("輸入您要的浮點數值") 
#e.g. A = 123.456
1.將 A 格式化成浮點數，並使用print顯示出來print(float(A))
2.以 2 個字元寬度顯示浮點數A，不滿 2 個則補空白print('%2f'%A)
3.以 2 個字元寬度顯示浮點數A，不滿 2 個則補零print('%02f'%A)
4
• 請排列下方執行的先後順序
(4) 加減法( +, - )
(3) 乘除法( *, / )
(2) 次方( ** )
(1) 括弧( ( ) )
(5) 且，或( and, or, &, | )
5
• 你有4個list, 
list1裡有3個元素: 1, 2 ,3
list2裡有3個元素: 4, 5 ,6
list3等於list1加list2
list4等於list3*2
請問程式執行結果為何:list4[1, 2 ,3, 4, 5 ,6, 1, 2 ,3, 4, 5 ,6]
6
• 有一個list = ["Savage", "Orz", "Apple" ]
1.請將"94"加在list的最前面list.insert(0, "94")
2.請將"Pen"加在list的最後面list.append("Pen")
3.請印出"Orz" 的index print(list.index("Orz"))
4.請印出倒數第2個元素的值 print(list[-2])
5.請將"Orz" 改成"GG" list[1]='GG'
6.請移除"GG" list.remove('GG')
7
• A="123456789abcdefg"
1.只顯示出efg，請將?代換掉
print( A[ -3 : ] )
print( A[ 13 : ] )
print( A[ -3 : 1] )
2.只顯示出147adg，請將?代換掉
print( A[ :: 3] )
8
• A="123456789abcdefg"
3.只顯示出47a，請將?代換掉
print( A[ 3 : -6 : 3 ] )
4.只顯示出a74，請將?代換掉
print( A[ -7 : 2 : 3 ] )
9
有一個list_a 記錄了10個學生的分數 [60, 94, 78, 80 ,99, 
59, 70, 90, 88, 83] ，讓使用輸入需查尋的學生代號的範圍，
顯示出學生分數
list_a = [60, 94, 78, 80, 99, 59, 70, 90, 88, 83]
print(list_a[int(input()) - 1])
10
A = "123456789abcdefg"
print("1" in A):True
print("2" in A):True
print("11" in A):False
print("12" in A):False
print("H" in A):False
print(a in A):Error
11
B = ["a", True ,8, False]
print("b" in B):False
print(8 in B):True
print(True in B):True
print(10 in B):False
print(False in B):True
12
讓使用者輸入兩個數值A and B，
•如果A大於B則顯示，"A的值為xx 大於B的值xx"
•如果B大於A則顯示，"B的值為xx 大於A的值xx"
•如果A等於B則顯示，"A的值為xx 等於B的值xx"
A=int(input())
B=int(input())
if A > B:
    print(f"A的值為{A} 大於B的值{B}")
if A < B:
    print(f"B的值為{B} 大於A的值{A}")
if A = B:
    print(f"A的值為{A} 等於B的值{B}")
13
•請檢查使用者輸入的數字為1位數，2位數，
•或2位以上，且必需檢查輸入的數是不是正整數。
try:
    a = int(input())
except:
    print('不是整數')
else:
    if a < 0:
        print('不是正數')
    if a >= 0 and a < 10:
        print('1位數')
    if a >= 10 and a < 100:
        print('2位數')
    if a >= 100:
        print('2位以上')
14
•請設計電影收票系統，讓使用者輸入年齡和身份。
•4歲以下50元
•5歲以上不滿18，且是學生70元
•5歲以上不滿18，且不是學生120元
•18歲以上，且是學生160元
•18歲以上，且不是學生200元
a=int(input())
b=input()
if a >= 4:
    print('50元')
if a >= 5 and a < 18 and b == '學生':
    print('70元')
if a >= 5 and a < 18 and b != '不是學生':
    print('120元')
if a >= 18 and b == '學生':
    print('160元')
if a >= 18 and b == '不是學生':
    print('200元')
15
a=float(input())
b=input()
if a >= 37.5 or b = '沒有':
    print('不能進入')
if a >= 38.5 or a <= 34:
    print('須送醫')
else:
    print('施打疫苗')
16
import random as r

a = r.randint(1, 100)
b = 1
while b <= 10:
    c = int(input())
    if c == a:
        print('correct')
        break
    else:
        print('wrong')
    b += 1
17
a = 0
while a <= 4:
    a += 1
    print('*' * a + '\n')
18
a = 0
while a <= 4:
    a += 1
    print(''*(5-a)+'*' * a + '\n')
'''
