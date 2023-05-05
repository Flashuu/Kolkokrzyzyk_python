import random
import math

class Player(): 
    def __init__(self, letter):
        #litera x albo o 
        self.letter = letter
    #ruch gracza
    def get_move(self,game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + 'ruch w przedziale (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('zle dane, sprobuj ponownie')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) 
    def get_move(self, game):
        square = random.choice(game.available_moves())#ruch komputera randomowo
        return square