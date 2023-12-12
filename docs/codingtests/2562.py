# https://www.acmicpc.net/problem/2562
# 문제
## 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고
## 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 입력
## 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 출력
## 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

def max_list(num):
    lista = []
    for i in range(num):
        a = int(input())
        lista.append(a)

    max_num = max(lista)
    for i in range(num):
        if max_num == lista[i]:
            c = i+1

    print(max_num)
    print(c)

max_list(9)