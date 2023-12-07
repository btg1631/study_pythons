## 나오는 값 처리
def add():
    first = 5
    second = 4
    sum = first + second
    return sum      # 상수 대신 변수 사용

# num_sum = 0
num_sum = add()
print("add() return 결과 : {}".format(num_sum))


# 두 수를 곱해서 결과 return
def multipay():
    num_first = 4
    num_second = 5
    # 곱셈 연산
    result = num_first * num_second
    return result

num_multipay = multipay
print("num_multiply return value : {}".format(num_multipay))



# list_fruits = ["apple", "banana", "cherry"]
# list_fruits[0]

def return_list() :
    list_fruits = ["melon", "apple", "banana", "cherry"]
    return list_fruits
print("return_list() return result : {}".format(return_list()))

# list 중에 index로 값
#  return
def return_listbyindex():
    list_fruits = ["apple", "banana", "cherry"]
    return list_fruits[0]

print("return_listbyindex() return result : {}".format(return_listbyindex()))



# if my_score >= 90: # 90점 이상 : A
#     pass
#     print("{}은 90점 이상으로 A학점".format())
# elif my_score > 80: # 80점 초과 : B
#     pass
#     print("{}은 80점 초과로 B학점".format())
# else:   # 나머지 : F
#     pass
#     print("{}은 80점 이하이므로 F학점".format())

# 반복 print 작업을 줄이기 위한 function 만들기
def return_grade():
    my_score = 99
    my_grade = ''
    if my_score >= 90: # 90점 이상 : A
        my_grade = 'A'
    elif my_score > 80: # 80점 초과 : B
        my_grade = 'B'
    else:   # 나머지 : F
        my_grade = 'C' 
    # return_listbyindex()
    return my_grade

str_grade = return_grade()
print("당신의 학점은 {} 입니다.".format(str_grade))
