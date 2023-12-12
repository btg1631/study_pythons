def questions(num):

    mixed_questions = []
    dict_question_mix = {}
    list_answer_input = []


    for num_count in range(num):
        question_input = input("{}번 문제 입력: ".format(num_count+1))
        dict_question_mix["question"] = question_input

        for _ in range(4):
            answer_input = input("답항 입력: ")
            list_answer_input.append(answer_input)
        dict_question_mix["answer"] = list_answer_input
        list_answer_input = []

        correct_input = int(input("정답 입력: "))
        dict_question_mix["correct_index"] = correct_input 

        score_input = int(input("점수 입력: "))
        dict_question_mix["score"] = score_input

        mixed_questions.append(dict_question_mix)
        dict_question_mix = {}
    return mixed_questions


result = questions(3)
print(result)