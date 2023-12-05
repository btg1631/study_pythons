weight = int(input("몸무게를 입력하세요. : "))
height = int(input("키를 입력하세요. : "))

BMI = weight/((height/100)**2)

if 25 <= BMI:
    print("{}으로 비만입니다.".format(BMI))
elif 23 <= BMI <= 24:
    print("{}으로 과체중입니다.".format(BMI))
elif 18 <= BMI <= 22:
    print("{}으로 정상입니다.".format(BMI))
else:
    print("{}으로 저체중입니다.".format(BMI))


