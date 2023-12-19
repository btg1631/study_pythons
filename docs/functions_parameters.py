# function에 들어가는 값들
def add(first, second):     # 호출 시 변수에 값이 할당됨
    sum = first + second
    return sum      # 상수 대신 변수 사용

if __name__ == "__main__":
    # num_sum = 0
    num_sum = add(5, 4)     # 상수 parameters 사용
    print("add() return 결과 : {}".format(num_sum))
    third = 6
    fourth = 10
    num_sum = add(third, fourth)     # function 부르면 값들만 전달됨
    print("add() return 결과 : {}".format(num_sum))

# 내 점수 넣으면 학점이 나오는 function
def return_grade(my_score):     # 자신을 불렀을 때 값들이 들어감
    my_grade = ''
    if my_score >= 90: # 90점 이상 : A
        my_grade = 'A'
    elif my_score > 80: # 80점 초과 : B
        my_grade = 'B'
    else:   # 나머지 : F
        my_grade = 'C' 
    # return_listbyindex()
    return my_grade

if __name__ == "__main__":
    # str_grade = return_grade(99)      # 호출 시 값들이 넘어감(순서 매칭)
    # print("당신의 학점은 {} 입니다.".format(str_grade))

    my_score = 88
    str_grade = return_grade(my_score)      # 호출 시 값들이 넘어감(순서 매칭)
    print("당신의 학점은 {} 입니다.".format(str_grade))


