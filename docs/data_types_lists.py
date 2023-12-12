# 사용 이유 : 값들의 모임을 쉽게 전달

# 숫자 5개로 이루어진 리스트
list_numerics = [0, 1, 2, 3, 4]
# 문자 3개로 이루어진 리스트
list_fruits = ["apple", "banana", "cherry"]
# 숫자와 문자 섞은 리스트
list_mixs = [0, 1, 2, 3, "apple", "banana"]

len(list_numerics)
# 5
len(list_mixs)
# 6

## for문 활용 후 다시오기

# index(색인, 위치값)
list_fruits = ["melon", "apple", "banana", "cherry"]
## index로 값 가져오기
list_fruits[0] # 단일 변수로 여김 1차원(행)
# 'melon'
list_fruits[3]
# 'cherry'

## error 발생
# list_fruits[4]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# IndexError: list index out of range


# list 초기화 방식
list_fruits_primitive = ["melon", "apple", "banana", "cherry"]
tuple_fruits = ("melon", "apple", "banana", "cherry")
list_fruits_constructor = list(("melon", "apple", "banana", "cherry"))
# append
list_fruits_primitive.append("strawberry")
list_fruits_constructor.append("watermelon")

# 삭제 대상이 해당 값에 있는 item
list_fruits_primitive.remove('apple')
list_fruits_constructor.remove('melon')

# 삭제 대상이 전체 item
list_fruits_primitive.clear()

pass