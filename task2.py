import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text="", font=('Arial', 20), width=6, height=3,
                                   command=lambda i=i, j=j: self.handle_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def handle_click(self, row, col):
        if self.board[row][col] is None:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Winner!", f"{self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Draw!", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] is not None or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] is not None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] is not None or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] is not None:
            return True
        return False

    def check_draw(self):
        return all(all(cell is not None for cell in row) for row in self.board)

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = None
                self.buttons[i][j].config(text="")
        self.current_player = 'X'


def main():
    root = tk.Tk()
    tic_tac_toe_gui = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
