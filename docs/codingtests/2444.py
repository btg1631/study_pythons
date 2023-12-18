# https://www.acmicpc.net/problem/2444
# 문제
## 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 입력
## 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력
## 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

N = int(input())


for i in range(N):
    print(" "*(N-i-1)+"*"*(i*2+1))

for i in range(N-1, 0, -1):
    print(" "*(N-i)+"*"*(i*2-1))



