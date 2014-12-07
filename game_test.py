import unittest
from game import Game


class GameTest(unittest.TestCase):

    def test_start(self):
        g = Game()
        g.start()
        g.highscores()


if __name__ == '__main__':
    unittest.main()
