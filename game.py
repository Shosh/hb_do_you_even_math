from connection import Base, engine
from sqlalchemy.orm import Session
from create_db import Score
from player import Player
from task import Task


class Game():
   
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session(bind=engine)
        
        self.player = None
        self.score = None
        
    def calculate_score(self):
        score = self.player.current_score
        self.score = score * score

    def ask_for_name(self):
        ui = input('Your name: ')
        self.player = Player(ui)

    def add_score(self, username, score):
        hscore = Score(user=username, score=score)
        self.session.add(hscore)
        self.session.commit()

    def show_top_ten(self):
        result = self.session.query(Score).order_by(Score.score.desc()).limit(10)
        return result

    def ask_user(self):
        user_input = input('?> ')
        try:
            user_input = int(user_input)
        except ValueError:
            return self.ask_user()
        return user_input
        
    def start(self):
        self.ask_for_name()
        playing = True
        while playing:
            t = Task()
            print(t.question())
            answer = self.ask_user()
            if t.check_answer(answer):
                self.player.current_score += 1
                print('Correct!')
            else:
                self.calculate_score()
                print('Incorrect! Ending game. You score is: {}'
                      .format(self.score))
                self.add_score(self.player.name, self.score)
                break
                
    def highscores(self):
        scores = self.show_top_ten()
        for index, row in enumerate(scores):
            print('{}. {}'.format(index + 1, row))
        
