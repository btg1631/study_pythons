# function만 사용해 적 캐릭터 만들기
# first 적 캐릭터
name = "first"
health = 120
damage = 0

def attack(damage):
    health = health - damage
    return health

damage = attack(5)

# second 적 캐릭터
name = "second"
health = 200
damage = 0

damage = attack(10)


# function만 사용 시 제한 극복 -> class

class Enemy:
    def __init__(self):
        self.name = ''
        self.health = 0
        self.damage = 0
        pass
    
    def attack(damage):
        health = health - damage
        return health
    
    def function_name(self):
        pass
        return 0    