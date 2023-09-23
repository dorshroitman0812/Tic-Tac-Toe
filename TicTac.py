from colorama import Fore, init
from Players import Player
from board import Board
from tictactoe_board import Tic_Tac_Board


class Game_Tic_Tac(object):
    def __init__(self, board, player1=None, player2=None):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = None

    def play(self):
        print('Welcome to Tic Tac Toe!')
        # Print the board (you need to implement this)
        self.create_the_players()
        while (self.board.win_draw_check(self) == -1):
            self.board.print_board()
            print('Player {} turn'.format(self.current_player.getname()))
            try:
                cell = int(input('Please provide the cell number: '))
                if not self.board.cell_check(cell, self):
                    raise ValueError
                if self.current_player == self.player1:
                    self.current_player = self.player2
                else:
                    self.current_player = self.player1

            except ValueError:
                # Print the board (you need to implement this)
                print('Please provide a valid cell number')
                self.board.print_board()
                continue
        if self.board.win_draw_check(self) == 0:
            print('The game is over! It was a draw.')
            game.board.print_board()
            return
        else:
            self.board.print_board()
            if self.current_player == self.player1:
                print('The game is over! {} won!'.format(self.player2.getname()))

            else:
                print('The game is over! {} won!'.format(self.player1.getname()))

    def create_the_players(self):
        p1, p2 = input(
            'Please provide the name of the players (p1, p2): ').split(',')
        self.player1 = Player(p1, 'X', 1)
        self.player2 = Player(p2, 'O', 2)
        self.current_player = self.player1
        print('The game is about to start!')
