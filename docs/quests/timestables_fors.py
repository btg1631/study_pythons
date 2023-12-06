num_first = int(input("구구단 몇 단을 출력할까요? : "))

for num_second in range(1, 10):
    print("{} * {} = {}".format(num_first, num_second, num_first*num_second))
