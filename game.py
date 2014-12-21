from connection import Base, engine
from sqlalchemy.orm import Session
from create_db import Score
from player import Player
from task import Task


class Game():
    messages = {'name': 'Your name: ',
                'answer': '?> ',
                'correct': 'Correct!',
                'incorrect': 'Incorrect! Ending game. Your score is: ',
                'question': 'What is the answer to '}
   
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session(bind=engine)
        
        self.player = None
        self.score = None
        
    def calculate_score(self, current_score):
        self.score = current_score * current_score
        return self.score

    def add_score_to_db(self, username, score):
        hscore = Score(user=username, score=score)
        self.session.add(hscore)
        self.session.commit()

    def show_top_ten(self):
        result = self.session.query(Score)\
                             .order_by(Score.score.desc())\
                             .limit(10)
        return result

    def is_input_valid(self, user_input):
        try:
            int(user_input)
        except ValueError:
            return False
        return True

    def get_user_input(self, message):
        uinput = input(message)
        return uinput

    def set_player(self, name):
        self.player = Player(name)
        
    def get_question(self, task_question):
        return Game.messages['question'] + task_question + ' ?'

    def get_incorrect(self, score):
        return Game.messages['incorrect'] + str(score)

    def printing(self, message):
        print(message)

    def start(self):
        name = self.get_user_input(Game.messages['name'])
        self.set_player(name)
        playing = True
        while playing:
            t = Task()
            self.printing(self.get_question(t.question))
            answer = ''
            while not self.is_input_valid(answer):
                answer = self.get_user_input(Game.messages['answer'])
            if t.check_answer(int(answer)):
                self.player.current_score += 1
                self.printing(Game.messages['correct'])
            else:
                self.calculate_score(self.player.current_score)
                self.printing(self.get_incorrect(self.score))
                self.add_score_to_db(self.player.name, self.score)
                break
                
    def highscores(self):
        scores = self.show_top_ten()
        for index, row in enumerate(scores):
            print('{}. {}'.format(index + 1, row))
        
