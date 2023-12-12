# function 3개 사용

def user_input_answer():

    list_answer_input = []

    for _ in range(4):
        answer_input = input("답항 입력: ")
        list_answer_input.append(answer_input)
    return list_answer_input


def user_input(num):

    list_answer_result = []

    for num_count in range(num):

        list_user_input = []

        question_input = input("{}번 문제 입력: ".format(num_count+1))
        list_user_input.append(question_input)

        list_answer_input = user_input_answer()
        list_user_input.append(list_answer_input)

        correct_input = int(input("정답 입력: "))
        list_user_input.append(correct_input)

        score_input = int(input("점수 입력: "))
        list_user_input.append(score_input)

        list_answer_result.append(list_user_input)

    return list_answer_result    # ['1번문제', ['1', '2', '3', '4'], 0, 10],[...],[...]



def dict_questions(num):

    mixed_questions = []

    list_result = user_input(3)

    for i in range(num):

        dict_question_mix = {}

        dict_question_mix["question"] = list_result[i][0]
        dict_question_mix["answer"] = list_result[i][1]
        dict_question_mix["correct_index"] = list_result[i][2]
        dict_question_mix["score"] = list_result[i][3]

        mixed_questions.append(dict_question_mix)

    return mixed_questions



result = dict_questions(3)
print(result)








# def questions(num):
#     mixed_questions = []

#     for num_count in range(num):

#         dict_question_mix = {}
#         list_answer_input = []

#         # 문제 입력
#         question_input = input("{}번 문제 입력: ".format(num_count+1))
#         dict_question_mix["question"] = question_input

#         # 답항 4개 입력
#         for _ in range(4):
#             answer_input = input("답항 입력: ")
#             list_answer_input.append(answer_input)
#         dict_question_mix["answer"] = list_answer_input

#         # 정답 입력
#         correct_input = int(input("정답 입력: "))
#         dict_question_mix["correct_index"] = correct_input 

#         # 점수 입력
#         score_input = int(input("점수 입력: "))
#         dict_question_mix["score"] = score_input

#         mixed_questions.append(dict_question_mix)

#     return mixed_questions



# result = questions(3)
# print(result)