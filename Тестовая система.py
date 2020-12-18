from tkinter import *
from decimal import *
from math import *

root = Tk()
root.title('ТС "БІОЛІМП"')
root.resizable(False, False)

simple_questions = ['До якої групи речовин належать \n молекули розщепленного альбуміну?',
                   'Укажіть немембранну органелу:',
                   'Метод ПЛР можно застосувати для:',
                   'Укажіть органелу, характерну \n для прокаріотичної клітини']

simple_answers = [['нуклеотиди', 'дисахариди', 'амінокислоти', 'моносахариди'],
                   ['мітохондрії', 'лізосоми', 'пластиди', 'рибосоми'],
                   ['лік. ендокринних захв.', 'діагн. порушень постави', 'профілактики серцевих захв.', 'виявлення інф. захв.'],
                   ['ендоплазматична сітка', 'апарат Гольджі', 'мітохондрія', 'рибосома']]

hard_questions = ['Тестовый вопрос #1',
                  'Тестовый вопрос #2',
                  'Тестовый вопрос #3',]

hard_answers = [['№1 Ответ 1', '№1 Ответ 2', '№1 Ответ 3', '№1 Ответ 4'],
                ['№2 Ответ 1', '№2 Ответ 2', '№2 Ответ 3', '№2 Ответ 4'],
                ['№3 Ответ 1', '№3 Ответ 2', '№3 Ответ 3', '№3 Ответ 4']]

answers = ['амінокислоти', 'рибосоми', 'виявлення інф. захв.', 'рибосома']

hard_answers_true = [['№1 Ответ 1', '№1 Ответ 2'],
                     ['№2 Ответ 3', '№2 Ответ 4'],
                     ['№3 Ответ 2', '№3 Ответ 3']]

result_redraw = ['Пройти заново',
                 'Напечатать результаты',
                 'Ok']

answer_number = 0
question_number = 0
score = 0
stack = []
stack_false = []
score_false = 0
lst = []

def score_count():

    global stack_false
    global score
    global stack
    global label

    texts = 0
    text_number = 0
    score_hard = 0
    result = 0

    for i in stack:
        score_hard += 1
    for i in stack_false:
        score_hard -= 1

    if score_hard > 0:
        score_hard = score_hard * 2
    else:
        score_hard = 0

    lst = root.grid_slaves()
    for l in lst:
        l.destroy()

    result = score + score_hard
    print(result)

    for texts in result_redraw:
        button = Button(root,
                        font=("Times New Roman", 15, "bold"),
                        bg="#e5ebee",
                        foreground='#215b7a',
                        text=result_redraw[text_number],
                        command=lambda text_number=text_number:
                                       click(result_redraw[text_number]))

        button.grid(row=text_number + 1,
                    columnspan=2,
                    sticky="nsew")
        text_number += 1

    label = Label(root,
                  text=f'Ваш результат: {result}',
                  font=("Times New Roman", 15, "bold"),
                  bg="#f6f8f9",
                  foreground="#455660",
                  width=40)

    label.grid(row=0,
               column=0,
               columnspan=2,
               sticky="nsew")

def hard_redraw(text_redraw):

    global question_number
    global button

    answer_number = 0

    if question_number == 2:
        score_count()
    elif question_number == -1:
        question_number += 1
        for answer_number in range(4):
            button = Button(root,
                            font=("Times New Roman", 15, "bold"),
                            bg="#e5ebee",
                            foreground='#215b7a',
                            text=hard_answers[0][answer_number],
                            command=lambda  question_number=question_number,
                                            answer_number=answer_number:
                                            click(hard_answers[question_number][answer_number]))
            button.grid(row=answer_number + 1,
                        columnspan=2,
                        sticky="nsew")
            answer_number += 1
        button = Button(root,
                        font=("Times New Roman", 15, "bold"),
                        bg="#e5ebee",
                        foreground='#215b7a',
                        text='OK',
                        command=lambda: click('OK'))

        button.grid(row=5,
                    columnspan=2,
                    sticky="nsew")
    else:
        question_number += 1
        for answer_number in range(4):
            button = Button(root,
                            font=("Times New Roman", 15, "bold"),
                            bg="#e5ebee",
                            foreground='#215b7a',
                            text=hard_answers[question_number][answer_number],
                            command=lambda question_number=question_number,
                                            answer_number=answer_number:
                                            click(hard_answers[question_number][answer_number]))

            button.grid(row=answer_number + 1,
                        columnspan=2,
                        sticky="nsew")
            answer_number += 1
        label.configure(text=hard_questions[question_number])

def simple_redraw(text_redraw):

    global question_number

    answer_number = 0

    if question_number == 3:
        question_number = -1
        hard_redraw(0)
        label.configure(text=hard_questions[0])
    else:
        question_number += 1
        for answer_number in range(4):
            button = Button(root,
                            font=("Times New Roman", 15, "bold"),
                            bg="#e5ebee",
                            foreground='#215b7a',
                            text=simple_answers[question_number][answer_number],
                            command=lambda question_number=question_number,
                                           answer_number=answer_number:
                                           click(simple_answers[question_number][answer_number]))

            button.grid(row=answer_number + 1,
                        columnspan=2,
                        sticky="nsew")
            answer_number += 1
        label.configure(text=simple_questions[question_number])

def click(text):

    global question_number
    global score
    global score_false
    global result

    if label['text'] in simple_questions:
        if text in answers:
            score += 1
        simple_redraw(0)

    if label['text'] in hard_questions:
        if text in hard_answers_true[question_number]:
            if text in stack:
                stack.remove(text)
            else:
                stack.append(text)
            print(stack)
        elif text in hard_answers[question_number]:
            stack_false.append(text)
            print(stack_false)
        if text == 'OK':
            hard_redraw(text)

    if text in result_redraw:
        if text == result_redraw[0]:
            basic_redraw()
        if text == result_redraw[1]:
            print(f'Ваш результат: {result}')
        if text == result_redraw[2]:
            root.destroy()

def basic_redraw():

    answer_number = 0
    question_number = 0
    for row in range(4):
        button = Button(root,
                        font=("Times New Roman", 15, "bold"),
                        bg="#e5ebee",
                        foreground='#215b7a',
                        text=simple_answers[question_number][answer_number],
                        command=lambda question_number=question_number,
                                       answer_number=answer_number:
                                       click(simple_answers[question_number][answer_number]))

        button.grid(row=row + 1,
                    columnspan=2,
                    sticky="nsew")
        answer_number += 1

    label = Label(root,
                  text=simple_questions[0],
                  font=("Times New Roman", 12, "bold"),
                  bg="#f6f8f9",
                  foreground="#455660",
                  width=40)

    label.grid(row=0,
               column=0,
               columnspan=2,
               sticky="nsew")

for row in range(4):
    button = Button(root,
                    font=("Times New Roman", 15, "bold"),
                    bg="#e5ebee",
                    foreground='#215b7a',
                    text=simple_answers[question_number][answer_number],
                    command=lambda question_number=question_number,
                                   answer_number=answer_number:
                                   click(simple_answers[question_number][answer_number]))

    button.grid(row=row + 1,
                columnspan=2,
                sticky="nsew")
    answer_number += 1

label = Label(root,
              text=simple_questions[0],
              font=("Times New Roman", 12, "bold"),
              bg="#f6f8f9",
              foreground="#455660",
              width=40)

label.grid(row=0,
           column=0,
           columnspan=2,
           sticky="nsew")

root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(5, weight=1)

root.mainloop()