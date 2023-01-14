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
'''
