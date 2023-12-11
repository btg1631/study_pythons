# https://www.acmicpc.net/problem/25314
# 문제
## “만약, 입출력이 N바이트 크기의 정수라면 프로그램을 어떻게 구현해야 할까요?”
## long int는 4바이트 정수까지 저장할 수 있는 정수 자료형이고
## long long int는 8바이트 정수까지 저장할 수 있는 정수 자료형이다.
## int 앞에 long을 하나씩 더 붙일 때마다 4바이트씩 저장할 수 있는 공간이 늘어나는 걸까?
## N바이트 정수까지 저장할 수 있다고 생각해서 쓴 정수 자료형의 이름은 무엇일까?
# 입력
## 첫 번째 줄에는 문제의 정수 N이 주어진다. 
# 출력
## N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름을 출력하여라.

# N = int(input())
# n = N//4
# print("{}int".format("long "*n))


def problem(num):
    long = "long "*(num//4) + "int"

    return print(long)

N = int(input())
problem(N)
