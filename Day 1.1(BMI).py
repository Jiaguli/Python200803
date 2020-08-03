KG=input('請輸入你的體重，單位是公斤') 
M=input('請輸入你的身高，單位視公尺')
BMI=float(KG)/(float(M)*float(M))
if float(BMI)<18.5:
    print('體重不足')
elif float(BMI)<24:
    print('正常')
elif float(BMI)<27:
    print('過重')
elif float(BMI)<30:
    print('輕度肥胖')
elif float(BMI)<35:
    print('中度肥胖')
else:
    print('重度肥胖')
