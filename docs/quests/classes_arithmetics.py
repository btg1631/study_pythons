class Arithmetics:

    def __init__(self):
        pass

    def add(self, first, second):
        add = first + second
        return add

    def sub(self, first, second):
        sub = first - second
        return sub
    
    def mul(self, first, second):
        mul = first * second
        return mul

    def div(self, first, second):
        div = first / second
        return div
    
arithmetics = Arithmetics()

input_a = int(input("숫자 입력 1: "))
input_b = int(input("숫자 입력 2: "))

subtraction = arithmetics.sub(input_a, input_b)     # 뺄셈
print("{} - {} = {}".format(input_a, input_b, subtraction))
multiplication = arithmetics.mul(input_a, input_b)  # 곱셈
print("{} * {} = {}".format(input_a, input_b, multiplication))
division = arithmetics.div(input_a, input_b)        # 나눗셈
print("{} / {} = {}".format(input_a, input_b, division))
