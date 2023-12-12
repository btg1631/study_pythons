# https://www.acmicpc.net/problem/10807
# 문제
## 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
# 입력
## 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다.
## 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다.
## 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
# 출력
## 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

def program():
    N = int(input())
    count = 0
    b = input()
    v = int(input())

    for i in range(N):      # a리스트에 공백을 기준으로 문자열 입력받기
        a = b.split()

    a = list(map(int, a))   # a리스트 문자열 -> 정수로 바꿈

    for i in range(N):      # a리스트의 0부터 N-1까지
        
        if a[i] == v:       # a리스트의 i번째가 v와 일치한다면
            count += 1      # count에 1을 누적

    print(count)

program()



