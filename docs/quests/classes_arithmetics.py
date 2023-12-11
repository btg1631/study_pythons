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
subtraction = arithmetics.sub(5, 6)     # 뺄셈
print(subtraction)
multiplication = arithmetics.mul(5, 6)  # 곱셈
print(multiplication)
division = arithmetics.div(5, 6)        # 나눗셈
print(division)