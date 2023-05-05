from Player import HumanPlayer, RandomComputerPlayer
import time
import math

class TicTacToe():
    def __init__(self):
        self.board = self.make_board() #3x3 plansza
        self.current_winner = None #tracker kto wygrywa
    
    @staticmethod
    def make_board():
        return[' 'for _ in range (9)]
    
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3]for i in range(3)]:
            print("| " + "| ".join(row) + "| ")

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    def make_move(self, square, letter):
        #jesli ruch mozliwy, przypisz puste miejsce literze i zwroc prawde, jesli nie falsz
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #sprawdza wiersz 
        row_index = math.floor(square / 3)
        row = self.board[row_index*3:(row_index+1)*3]#lista rzeczy w wybranym wierszu
        if all([spot == letter for spot in row]): 
            return True
        #sprawdza kolumne 
        column_index = square % 3
        column = [self.board[column_index + i *3] for i in range (3)]# do kazdego rzedu i dodaje kolumne by uzyskac wartosc kolumny
        if all([spot == letter for spot in column]): 
            return True
        #sprawdza przekatna
        #moze byc tylko dla parzystej liczby miejsca (0,2,4,6,8)
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #przekatna od lewej gory do prawego dolu
            if all([spot == letter for spot in diagonal1]): 
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #przekatna od prawej gory do lewego dolu
            if all([spot == letter for spot in diagonal2]): 
                return True   
            #gdy nie ma wygranej
        return False
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
 

def play(game, x_player, o_player, print_game = True):
    
    if print_game:
        game.print_board_nums()

    letter = 'X' #poczatkowa litera
    while game.empty_squares():
        #powtarza dopolki sa wolne miejsca 
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' robi ruch do {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wygrywa')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player
        
        time.sleep(.8)
    #jesli nie bedzie wolnych miejsc
    if print_game:  
        print("remis")


if __name__ == '__main__':
    x_player = RandomComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)