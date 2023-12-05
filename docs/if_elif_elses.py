# 기본 if else 구문
if True :
    pass
elif True:
    pass
else:
    pass

# 문자 비교
str_name = "young ji"

# 질문 형식(condition) = 변수 + 부등호 + 기준값
# 문자에 대한 긍정으로 질문
if str_name == "young ji":
    pass
    print("name is {}.".format(str_name))   
    
# 문자에 대한 부정으로 질문
if str_name != "young ji":
    pass
    print("name is not {}.".format(str_name))  


# if - else
# num_first >= 4   -> True : 큼, False : 작음
num_first = 5
# if num_first >= 4 : # 무조건 둘 중 하나 표현
if num_first >= 6 : # 무조건 둘 중 하나 표현
    pass    # condition이 True
    print("{}는 4보다 크다.".format(num_first))
else:
    pass    # condition이 False
    print("{}는 4보다 작다.".format(num_first))


# if - elif - else
# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B, 나머지 : F
my_score = 90
my_score >= 90
# True
my_score = 89
my_score >= 90
# False
my_score = 80
my_score > 80
# False


pass
if my_score >= 90: # 90점 이상 : A
    pass
    print("{}은 90점 이상으로 A학점".format())
elif my_score > 80: # 80점 초과 : B
    pass
    print("{}은 80점 초과로 B학점".format())
else:   # 나머지 : F
    pass
    print("{}은 80점 이하이므로 F학점".format())




print("End Program!")



