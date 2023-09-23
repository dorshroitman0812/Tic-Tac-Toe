from board import Board
class Tic_Tac_Board(Board):
    def __init__(self):
        Board.__init__(self,self)
        self.board = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
  
    def print_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ')
            print() 
            
    
    def set_cell(self, row,col ,game):
        # Set the given cell to the mark of the current player
        if game.current_player == game.player1 and self.board[row][col] != 'O':
            self.board[row][col] = 'X'
        elif game.current_player == game.player2 and self.board[row][col] != 'X':
            self.board[row][col] = 'O'

    def cell_check(self,cell,game):
        if cell < 1 or cell > 9:
            return False
        if 1 <=cell <= 3:
            row ,col= 0, cell-1
        elif 4 <=cell <= 6:
            row ,col= 1, cell-4
        elif 7 <=cell <= 9:
            row ,col = 2, cell-7

        if self.board[row][col] == 'X' or self.board[row][col] == 'O': 
            return False
        self.set_cell(row,col,game)
        return True
    #returns : if there is a win 1 , if draw 0 , if not finished -1
    def win_draw_check(self,game):
        if self.line_win(game) or self.col_win(game) or self.diagonal_win(game):
            return 1
        elif self.draw(game):
            return 0
        return -1


    #separation of concerns : check for different win conditions
            
    def line_win(self,game):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
        return False
    def col_win(self,game):
          for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return True
          return False
    def diagonal_win(self,game):
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        return False
    def draw(self,game):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 'X' and self.board[i][j] != 'O':
                    return False
        return True