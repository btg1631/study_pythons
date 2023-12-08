def multiply(user_input, num_count):
    result_multiply = user_input * num_count
    return result_multiply

def gugudan(user_input):
    for num_count in range(1, 10):
        result = multiply(user_input, num_count)
        print("{} * {} = {}".format(user_input, num_count, result))
    return

while True:
    user_input = input("구구단 몇 단을 출력할까요? : ")
    if user_input != 'q':
        user_input = int(user_input)
        gugudan(user_input)
    else:
        break
    



