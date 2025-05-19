"""
Created on Mon May 19 12:11:37 2025

@author: Kunal Kaushik
"""


import tkinter as tk
import random

CELL_SIZE = 30
COLUMNS = 10
ROWS = 20

SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'L': [[1, 0, 0],
          [1, 1, 1]],
    'J': [[0, 0, 1],
          [1, 1, 1]],
}

COLORS = {
    'I': 'cyan', 'O': 'yellow', 'T': 'purple',
    'S': 'green', 'Z': 'red', 'L': 'orange', 'J': 'blue'
}

class Tetris:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CELL_SIZE * COLUMNS, height=CELL_SIZE * ROWS, bg='black')
        self.canvas.pack()
        self.board = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.game_over = False
        self.spawn_new_piece()
        self.bind_events()
        self.update()

    def spawn_new_piece(self):
        self.piece_type = random.choice(list(SHAPES.keys()))
        self.piece = SHAPES[self.piece_type]
        self.color = COLORS[self.piece_type]
        self.x = COLUMNS // 2 - len(self.piece[0]) // 2
        self.y = 0
        if self.collision(self.x, self.y, self.piece):
            self.game_over = True

    def draw_block(self, x, y, color):
        self.canvas.create_rectangle(
            x * CELL_SIZE, y * CELL_SIZE,
            (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
            fill=color, outline="grey"
        )

    def draw(self):
        self.canvas.delete("all")
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.board[y][x]:
                    self.draw_block(x, y, self.board[y][x])
        for y, row in enumerate(self.piece):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_block(self.x + x, self.y + y, self.color)

    def collision(self, new_x, new_y, piece):
        for y, row in enumerate(piece):
            for x, cell in enumerate(row):
                if cell:
                    if (
                        new_x + x < 0 or
                        new_x + x >= COLUMNS or
                        new_y + y >= ROWS or
                        self.board[new_y + y][new_x + x]
                    ):
                        return True
        return False

    def merge_piece(self):
        for y, row in enumerate(self.piece):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.y + y][self.x + x] = self.color
        self.clear_lines()
        self.spawn_new_piece()

    def clear_lines(self):
        new_board = [row for row in self.board if any(cell is None for cell in row)]
        cleared_lines = ROWS - len(new_board)
        for _ in range(cleared_lines):
            new_board.insert(0, [None for _ in range(COLUMNS)])
        self.board = new_board

    def rotate(self):
        rotated = list(zip(*self.piece[::-1]))
        if not self.collision(self.x, self.y, rotated):
            self.piece = rotated

    def move(self, dx):
        if not self.collision(self.x + dx, self.y, self.piece):
            self.x += dx

    def drop(self):
        if not self.collision(self.x, self.y + 1, self.piece):
            self.y += 1
        else:
            self.merge_piece()

    def bind_events(self):
        self.root.bind("<Left>", lambda e: self.move(-1))
        self.root.bind("<Right>", lambda e: self.move(1))
        self.root.bind("<Down>", lambda e: self.drop())
        self.root.bind("<Up>", lambda e: self.rotate())

    def update(self):
        if not self.game_over:
            self.drop()
            self.draw()
            self.root.after(300, self.update)
        else:
            self.canvas.create_text(CELL_SIZE * COLUMNS // 2, CELL_SIZE * ROWS // 2,
                                    text="GAME OVER", fill="white", font=("Arial", 24))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tetris - Tkinter")
    game = Tetris(root)
    root.mainloop()
