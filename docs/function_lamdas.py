# 기존 문법을 압축
# for, if
# lambda
# (lambda param: param + 2)(param)

def function_name(param):
    pass
    return 0

# 압축된 for문
numerics = [0, 1, 2, 3, 4]    # 5개 값으로 이루어진 리스트
print([number+2 for number in numerics])
pass
print([(lambda param: param + 2)(number) for number in numerics])
pass

# 각 숫자의 제곱을 계산
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # [1, 4, 9, 16, 25]