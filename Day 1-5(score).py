score=input('你的成績')
if int(score)>=0 and int(score)<=100:
    if int(score)>=0 and int(score)<60:
        print('E')
    elif int(score)>=60 and int(score)<70:
        print('D')
    elif int(score)>=70 and int(score)<80:
            print('C')
    elif int(score)>=80 and int(score)<90:
        print('B')
    else:
        print('A')
else:
    print('請好好回答')

