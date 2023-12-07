def calculation(user_input1, user_input2):
    result = user_input1 * user_input2
    print(result)
    
while True:
    user_input = input()

    if user_input == 'q':
        break
    else:
        user_input1, user_input2 = map(int, user_input.split())
        calculation(user_input1, user_input2)














    

