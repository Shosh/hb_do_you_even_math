import random


class Task():
    min_n = 1
    max_n = 10
    operators = ['+', '-', '^', 'x']

    def __init__(self):
        self.first_number = self.get_random_n()
        self.second_number = self.get_random_n()
        self.operator = self.get_random_operator()
        self.answer = self.calculate_answer()

    def get_random_n(self):
        return random.randint(Task.min_n, Task.max_n)

    def get_random_operator(self):
        return random.choice(Task.operators)

    def calculate_answer(self):
        if self.operator == '+':
            return self.first_number + self.second_number
        elif self.operator == '-':
            return self.first_number - self.second_number
        elif self.operator == '^':
            return self.first_number ** self.second_number
        elif self.operator == 'x':
            return self.first_number * self.second_number

    def question(self):
        return 'What is the answer to {} {} {}?'.format(self.first_number, self.operator, self.second_number)

    def check_answer(self, user_answer):
        return self.answer == user_answer
