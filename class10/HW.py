# 功能清單
# 1. 新增科目與成績
# 2. 刪除某個科目的成績
# 3. 關閉系統
# 每回合都要顯示目前的成績以及功能清單
a = ['1.新增科目與成績', '2. 刪除某個科目的成績', '3. 關閉系統']
b = {}
p = 0
while True:
    print(f'{b}')
    for i in a:
        print(i)
    try:
        f = int(input('請輸入功能選項:'))
    except:
        print('請輸入功能選項編號')
    else:
        if f == 3:
            keys = b.values()
            g = len(b)
            for key in keys:
                p += key
            print(f'總平均={g/p}')
            break

        if f == 1:
            x = input('請輸入要新增的科目:')
            y = int(input('請輸入要新增的成績:'))
            b[x] = y
        if f == 2:
            m = input('請輸入想移除的科目')
            n = b.pop(m, 'error')
