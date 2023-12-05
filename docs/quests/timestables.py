num_first = int(input("구구단 몇 단을 출력할까요? : "))
num_second = 0
while num_second < 9:
    num_second += 1
    result = num_first*num_second
    print("{} * {} = {}".format(num_first, num_second, result))