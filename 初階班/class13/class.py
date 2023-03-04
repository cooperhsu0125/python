# import datetime as d

# day = input()
# bir = d.datetime.strptime(day, '%Y/%m/%d').date()
# a = d.date.today()
# print(f'{bir-a}')

# while True:
#     Time = d.datetime.now()
#     print(Time)
# print(Time.hour)
# print(Time.minute)
# print(Time.second)

# #1. 要開啟的檔名
# fileName = "class13/test.txt"
# #2. 指定w/ r /a mode
# Mode = "w"
# #3. 開啟檔案
# myFile = open(fileName, Mode)
# #4. 寫入檔案 \n 換行符號
# myFile.write("Hi\n")
# myFile.write("How old are you?\n")
# #5. 關閉檔案
# myFile.close()

# #1. 要開啟的檔名
# fileName = "class13/test.txt"
# #2. 指定w/ r /a mode
# Mode = "a"
# # 3. 開啟檔案
# myFile = open(fileName, Mode)
# #4. 寫入檔案 \n 換行符號
# myFile.write("Hi\n")
# myFile.write("My age is 18\n")
# #5. 關閉檔案
# myFile.close()

# #1. 要開啟的檔名
# path = "Class13/test.txt"
# #2. 指定w/ r /a mode
# f = open(path, 'r')
# #3. 讀取檔案並顯示
# line = f.readline()
# f.close()

# f = open(path, 'r')
# lines = f.readlines()
# print(lines)
# print(line)
# #4. 關閉檔案
# f.close()

a = 'class13/score.txt'
b = open(a, 'w')
b.write('Peter:90\n')
b.write('Tom:70\n')
b.write('John:80\n')
b.close()
b = open(a, 'a')
b.write('Rob:95')
b.close()
b = open(a, 'r')
d = b.read()
print(d)
b.close()