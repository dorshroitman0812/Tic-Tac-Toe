from abc import ABC, abstractmethod

class Board(ABC):
    def __init__(self,board):
        self.board = board
    @abstractmethod
    def print_board(self):
        pass
    @abstractmethod
    def set_cell(self,row,col):
        pass
    @abstractmethod
    def cell_check(self,cell):
        pass
    @abstractmethod
    def win_draw_check(self):
        pass
   
