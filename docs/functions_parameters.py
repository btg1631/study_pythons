# function에 들어가는 값들
def add(first, second):     # 호출 시 변수에 값이 할당됨
    sum = first + second
    return sum      # 상수 대신 변수 사용

# num_sum = 0
num_sum = add(5, 4)     # 상수 parameters 사용
print("add() return 결과 : {}".format(num_sum))
third = 6
fourth = 10
num_sum = add(third, fourth)     # function 부르면 값들만 전달됨
print("add() return 결과 : {}".format(num_sum))


