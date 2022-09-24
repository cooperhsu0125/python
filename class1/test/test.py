weight=float(input("請輸入體重(公斤)"))
height=float(input("請輸入身高(公分)"))
bmi=weight/(height/100)**2
print("你的BMI指數是" + str(bmi))