import tkinter as tk
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.difficulty_label = tk.Label(root, text="Select Difficulty:")
        self.difficulty_label.grid(row=0, columnspan=3)

        self.difficulty = tk.StringVar()
        self.difficulty.set("Easy")

        difficulty_menu = tk.OptionMenu(root, self.difficulty, "Easy", "Medium", "Hard")
        difficulty_menu.grid(row=1, columnspan=3)

        self.first_player_label = tk.Label(root, text="Who goes first?")
        self.first_player_label.grid(row=2, columnspan=3)

        self.first_player = tk.StringVar()
        self.first_player.set("Player")

        player_menu = tk.OptionMenu(root, self.first_player, "Player", "AI")
        player_menu.grid(row=3, columnspan=3)

        start_button = tk.Button(root, text="Start New Game", command=self.start_new_game)
        start_button.grid(row=4, columnspan=3)

        self.buttons = []
        self.create_board()

        self.game_over_label = tk.Label(root, text="", font=('normal', 16), fg="red")
        self.game_over_label.grid(row=6, columnspan=3)

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=' ', font=('normal', 20), width=6, height=3,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i + 7, column=j)
                self.buttons.append(button)

    def start_new_game(self):
        self.game_over_label.config(text="")
        self.root.update()

        for button in self.buttons:
            button.grid_forget()

        self.buttons = []
        self.create_board()

        self.board = [' '] * 9
        self.current_player = 'X' if self.first_player.get() == "Player" else 'O'

        if self.current_player == 'O':
            self.make_ai_move()

    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)
            winner = self.check_winner()
            if winner:
                self.display_winner(winner)
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

                if self.current_player == 'O':
                    self.make_ai_move()

    def make_ai_move(self):
        if self.difficulty.get() == "Easy":
            available_moves = [i for i in range(9) if self.board[i] == ' ']
            move = random.choice(available_moves)
        elif self.difficulty.get() == "Medium":
            move = self.medium_ai_move()
        else:
            move = self.hard_ai_move()

        self.make_move(move // 3, move % 3)

    def medium_ai_move(self):
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                if self.check_winner() == 'O':
                    self.board[i] = ' '
                    return i
                self.board[i] = ' '

        available_moves = [i for i in range(9) if self.board[i] == ' ']
        return random.choice(available_moves)

    def hard_ai_move(self):
        best_score = float('-inf')
        best_move = -1

        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(self.board, 0, False)
                self.board[i] = ' '

                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def minimax(self, board, depth, is_maximizing):
        scores = {'X': -1, 'O': 1, 'Tie': 0}

        winner = self.check_winner(board)
        if winner:
            return scores[winner]

        if is_maximizing:
            max_eval = float('-inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'O'
                    eval = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    eval = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    min_eval = min(min_eval, eval)
            return min_eval

    def check_winner(self, board=None):
        if board is None:
            board = self.board

        for row in range(3):
            if board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2] != ' ':
                self.display_winner_line((row, row * 3), (row, row * 3 + 2))
                return board[row * 3]

        for col in range(3):
            if board[col] == board[col + 3] == board[col + 6] != ' ':
                self.display_winner_line((col, col), (col + 6, col))
                return board[col]

        if board[0] == board[4] == board[8] != ' ':
            self.display_winner_line((0, 0), (8, 8))
            return board[0]
        if board[2] == board[4] == board[6] != ' ':
            self.display_winner_line((2, 6), (6, 2))
            return board[2]

        if ' ' not in board:
            return 'Tie'

        return None

    def display_winner_line(self, start, end):
        x1, y1 = start
        x2, y2 = end
        for i in range(3):
            index = x1 + y1 * 3
            if 0 <= index < len(self.buttons):
                self.buttons[index].config(bg='red')
            x1 += (x2 - x1) // 2
            y1 += (y2 - y1) // 2

        # Draw the red line on the last box
        index = x2 + y2 * 3
        if 0 <= index < len(self.buttons):
            self.buttons[index].config(bg='red')

    def display_winner(self, winner):
        self.game_over_label.config(text=f"GAME OVER! {winner} wins!", fg="red")
        for button in self.buttons:
            button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
