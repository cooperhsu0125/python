"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
​
hint:可以使用%取餘數進行判斷
​
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""
a = int(input())
b = 1
while b <= a:
    if b % 3 == 0 or b % 7 == 0:
        print(b)
    b += 1
