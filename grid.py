import pygame
from Colours import Colours

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_col = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_col)] for j in range(self.num_rows)]
        self.colours = Colours.get_colours()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_col):
                print(self.grid[row][column], end=" ")
            print()
    
    def is_inside(self, row, column):
        return 0 <= row < self.num_rows and 0 <= column < self.num_col
    
    def is_empty(self, row, column):
        return self.grid[row][column] == 0
    
    def is_row_full(self, row):
        for column in range(self.num_col):
            if self.grid[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.num_col):
            self.grid[row][column] = 0  # ✅ FIXED (assignment)
    
    def move_row_down(self, row, num_rows):
        for column in range(self.num_col):
            self.grid[row + num_rows][column] = self.grid[row][column]  # ✅ FIXED (assignment)
            self.grid[row][column] = 0

    def clear_full_rows(self):
        completed = 0
        # ✅ loop bottom → top
        for row in range(self.num_rows - 1, -1, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_col):
                self.grid[row][column] = 0

    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_col):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(
                    column * self.cell_size + 11,
                    row * self.cell_size + 11,
                    self.cell_size - 1,
                    self.cell_size - 1
                )
                pygame.draw.rect(screen, self.colours[cell_value], cell_rect)
