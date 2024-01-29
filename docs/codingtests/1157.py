# https://www.acmicpc.net/problem/1157
# 문제
## 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
## 단, 대문자와 소문자를 구분하지 않는다.
# 입력
## 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력
## 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
## 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

word = input()
word = word.upper()


x = [] # 처음 등장한 값인지 판별하는 리스트
new_a = [] # 중복된 원소만 넣는 리스트

for i in word:
    if i not in x: # 처음 등장한 원소
        x.append(i)
    else:
        if i not in new_a: # 이미 중복 원소로 판정된 경우는 제외
            new_a.append(i)

if len(new_a) >= 2:
    print("?")
else:
    print(max(word))

