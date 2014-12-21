from game import Game


commands = ['start', 'highscores']

message = 'Welcome to the "Do you even math?" game!\n\
Here are your options:\n- start \n- highscores'


def main():
    print(message)
    while True:
        choice = ''
        while choice not in commands:
            choice = input('?> ')
        game = Game()
        getattr(game, choice)()
       
if __name__ == '__main__':
    main()
