# https://www.acmicpc.net/problem/2480
# 문제
## 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
## 1. 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
## 2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
## 3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
## 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다.
## 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다.
## 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
## 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
# 입력
## 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
# 출력
## 첫째 줄에 게임의 상금을 출력 한다.

# A, B, C = input().split()
# A = int(A)
# B = int(B)
# C = int(C)

# # A == B == C
# # A == B / A == C / B == C
# # else

# if A == B == C:
#     print(10000+(A*1000))
# elif A == B:
#     print(1000+(A*100))
# elif A == C:
#     print(1000+(A*100))
# elif C == B:
#     print(1000+(C*100))
# else:
#     if A > B and A > C:
#         print(A*100)
#     elif B > A and B > C:
#         print(B*100)
#     else:
#         print(C*100)



def price(dice_a, dice_b, dice_c):
    if dice_a == dice_b == dice_c:
        print(10000+(dice_a*1000))
    elif dice_a == dice_b or dice_a == dice_c:
        print(1000+(dice_a*100))
    elif dice_c == dice_b:
        print(1000+(dice_c*100))
    else:
        if dice_a > dice_b and dice_a > dice_c:
            print(dice_a*100)
        elif dice_b > dice_a and dice_b > dice_c:
            print(dice_b*100)
        else:
            print(dice_c*100)

a, b, c = map(int, input().split())
price(a, b, c)
        
    
