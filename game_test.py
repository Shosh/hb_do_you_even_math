import unittest
from game import Game
from create_db import Score
from player import Player


class GameTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()
        self.p = Player('shosh')

    def test_calculate_score(self):
        self.g.calculate_score(4)
        self.assertEqual(self.g.score, 16)

    def test_add_score_to_db(self):
        self.g.add_score_to_db('shosh', 148)
        q = self.g.session.query(Score).order_by(Score.id.desc()).first()
        self.assertEqual(q.user, 'shosh')
        self.assertEqual(q.score, 148)
        self.g.session.delete(q)
        self.g.session.commit()

    def test_is_input_valid(self):
        result = self.g.is_input_valid('5')
        self.assertTrue(result)

        result = self.g.is_input_valid('answer')
        self.assertFalse(result)

    def test_set_player(self):
        self.g.set_player('shosh')
        self.assertEqual(self.g.player.name, 'shosh')
        self.assertEqual(self.g.player.current_score, 0)

    def test_get_question(self):
        question = '1 + 2'
        msg = self.g.get_question(question)
        self.assertEqual(msg, 'What is the answer to 1 + 2 ?')
        
    def test_get_incorrect(self):
        score = 123
        msg = self.g.get_incorrect(score)
        self.assertEqual(msg, 'Incorrect! Ending game. Your score is: 123')
        
        
if __name__ == '__main__':
    unittest.main()
