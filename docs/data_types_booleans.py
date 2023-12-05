bool_flag = True # yes와 동일
pass

type(bool)
# <class 'type'>
type(bool_flag)
# <class 'bool'>

# 문자 판단
# 같음에 대한 기호 '=='
str_name = "young ji"
str_name == "young ji"
# True
str_name == "youngji"
# False
## 같지 않음 기호 '!='
str_name != "youngji"
# True
str_name != "young ji"
# False

# 숫자에 대한 판단 (변수 + 부등호 + 기준값)
# 컴퓨터 입장
# True = Yes = 1, False = No = 0
5 == 4
# False
num_first = 5
num_first == 4
# False
num_first != 4
# True
num_first > 4   # 초과
# True
num_first >= 4  # 이상
# True
pass
