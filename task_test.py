from task import Task
import unittest


class TaskTest(unittest.TestCase):

    def setUp(self):
        self.task = Task()

    def test_get_random_numbers(self):
        result = []
        for n in range(100):
            result.append(self.task.get_random_n())

        for number in range(1, 10):
            self.assertIn(str(number), result)

    def test_get_random_operator(self):
        result = []
        for n in range(100):
            result.append(self.task.get_random_operator())

        self.assertIn('+', result)
        self.assertIn('-', result)
        self.assertIn('^', result)
        self.assertIn('x', result)

    def test_set_question(self):
        result = self.task.set_question('1', '2', '+')
        self.assertEqual(result, '1 + 2')

    def test_calculate_answer(self):
        self.task.question = '1 + 2'

        answer = self.task.calculate_answer()
        self.assertEqual(answer, 3)

        self.task.question = '2 - 1'
        answer = self.task.calculate_answer()
        self.assertEqual(answer, 1)

        self.task.question = '2 x 3'
        answer = self.task.calculate_answer()
        self.assertEqual(answer, 6)

        self.task.question = '1 ^ 2'
        answer = self.task.calculate_answer()
        self.assertEqual(answer, 1)

if __name__ == '__main__':
    unittest.main()
