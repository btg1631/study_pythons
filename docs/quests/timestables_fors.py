num_gugudan = int(input("구구단 몇 단을 출력할까요? : "))

for num_count in range(1, 10):
    print("{} * {} = {}".format(num_gugudan, num_count, num_gugudan*num_count))
