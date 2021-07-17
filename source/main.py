from random import sample, choice, shuffle
from io import StringIO


# lines = """padre,father
# madre,mother
# genitori,parents
# fratello,brother
# sorella,sister
# marito,husband
# moglie,wife""".splitlines()
#
#
# italian_word_to_english_translation = {}
#
# for line in lines:
#     italian_word, english_translation = line.split(",")
#     italian_word_to_english_translation[italian_word] = english_translation
#
#
# all_italian_words = list(italian_word_to_english_translation.keys())
# all_english_translations = list(italian_word_to_english_translation.values())
#
# random_italian_word = choice(all_italian_words)
# correct_english_translation = italian_word_to_english_translation[random_italian_word]
#
# all_wrong_english_translations = list(set(all_english_translations) - {correct_english_translation})
#
# random_wrong_english_translations = sample(all_wrong_english_translations, 3)


def ask_question(question, correct_answer, wrong_answers):
    possible_answers_list = [correct_answer] + wrong_answers
    shuffle(possible_answers_list)
    correct_answer_number = possible_answers_list.index(correct_answer) + 1

    question_text_string_io = StringIO()
    print(question, file=question_text_string_io, end="\n")
    for answer_number, answer in enumerate(possible_answers_list, 1):
        answer_line = f" {answer_number}. {answer}"
        print(answer_line, file=question_text_string_io, end="\n")
    print(">> ", file=question_text_string_io, end="\n")

    question_text = question_text_string_io.getvalue()

    print(question_text)
    user_input_string = input()
    correct_answer_number_string = str(correct_answer_number)

    if user_input_string == correct_answer_number_string:
        return True
    else:
        return False


result = ask_question("a", "a", list("bcd"))
print(result)
