from TicTac import Game_Tic_Tac
from colorama import Fore, init
from Players import Player
from board import Board
from tictactoe_board import Tic_Tac_Board
# main function
if __name__ == "__main__":
    board = Tic_Tac_Board()
    game = Game_Tic_Tac(board)
    game.play()
