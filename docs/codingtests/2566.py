# https://www.acmicpc.net/problem/2566
# 문제
## <그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.
# 입력
## 첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.
# 출력
## 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다.
## 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.

def Lst():
    lst = []
    for _ in range(9):
        line = list(map(int, input().split()))
        lst.append(line)
    return lst

def mmax(lst):
    index1 = []
    result_max = []
    for i in range(9):
        result_max.append(max(lst[i]))
        index1.append(lst[i].index(max(lst[i])))

    j = result_max.index(max(result_max))
    print(max(result_max))
    print('{} {}'.format((j)+1, index1[j]+1))

lst = Lst()
mmax(lst)
