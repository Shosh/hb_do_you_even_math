import random


class Task():
    min_n = 1
    max_n = 10
    operators = ['+', '-', '^', 'x']

    def __init__(self):
        self.question = self.set_question(self.get_random_n(),
                                          self.get_random_n(),
                                          self.get_random_operator())
        self.answer = self.calculate_answer()

    def get_random_n(self):
        number = random.randint(Task.min_n, Task.max_n)
        return str(number)
        
    def get_random_operator(self):
        return random.choice(Task.operators)

    def calculate_answer(self):
        question = self.question
        question = question.replace('x', '*')
        question = question.replace('^', '**')
        return eval(question)

    def set_question(self, first, second, operator):
        question = '{} {} {}'.format(first, operator, second)
        return question

    def check_answer(self, user_answer):
        return self.answer == user_answer
