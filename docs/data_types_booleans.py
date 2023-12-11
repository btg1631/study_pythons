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

my_score = 75


# 논리(True or False) 연산자(결과값)
# and : 1 and 1 -> 1, 나머지는 0
# or(~도 되고) : 0 or 0 -> 0, 나머지는 1(긍정)
# not : 반대로 변환

# 사람 말로 예, 아니오 판단 근거
# 정의는 정의하기 어렵다.               -> 부정(아니오)
# 정의는 정의하기 어렵지 아니하다.       -> 긍정(예)
# 50점 이상부터 60점 이하는 C 학점이다.  -> 대상이 없어 판단 어려움.

# 컴퓨터는 상태를 확인할 때 논리 연산자(True, False) 사용
# 현재 값이 75점 이상부터 85점 이하는 C 학점이다.
# 75점 ~ 85점 -> and 조건

pass
