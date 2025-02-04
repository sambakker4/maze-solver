from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            random.seed(seed)


        self._create_cells()


    def _create_cells(self):
        self._cells = []

        for i in range(self.num_cols):
            self._cells.append([Cell(self._win) for j in range(self.num_rows)])

        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._draw_cell(i, j)
        
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        x1 = self._x1 + (i * self.cell_size_x)
        y1 = self._y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(len(self._cells) -1, len(self._cells[0]) -1) 
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []

            if i > 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((self._cells[i - 1][j], "left"))

            if i < self.num_cols - 1:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((self._cells[i + 1][j], "right"))


            if j > 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((self._cells[i][j - 1], "up"))

            if j < self.num_rows - 1:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((self._cells[i][j + 1], "down"))


            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            random_num = random.randrange(len(to_visit))
            random_cell, direction = to_visit[random_num][0], to_visit[random_num][1]

            if direction == "left":
                self._cells[i][j].has_left_wall = False
                random_cell.has_right_wall = False
                self._break_walls_r(i - 1, j)

            elif direction == "right":
                self._cells[i][j].has_right_wall = False
                random_cell.has_left_wall = False
                self._break_walls_r(i + 1, j)

            elif direction == "down":
                self._cells[i][j].has_bottom_wall = False
                random_cell.has_top_wall = False
                self._break_walls_r(i, j + 1)

            else:
                self._cells[i][j].has_top_wall = False
                random_cell.has_bottom_wall = False
                self._break_walls_r(i, j - 1)
    
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if self._cells[i][j] == self._cells[-1][-1]:
            return True

        directions = []

        if i > 0:
            directions.append((i - 1, j, "left"))
 
        if i < len(self._cells) - 1:
            directions.append((i + 1, j, "right"))

        if j > 0:
            directions.append((i, j - 1, "up"))

        if j < len(self._cells[0]) - 1:
            directions.append((i, j + 1, "down"))

        for i2, j2, direction in directions:
            if direction == "left":
                if ((not self._cells[i][j].has_left_wall)
                    and (not self._cells[i2][j2].has_right_wall)
                    and (not self._cells[i2][j2].visited)):
                    self._cells[i][j].draw_move(self._cells[i2][j2])

                    if self._solve_r(i2, j2):
                        return True
                    
                    self._cells[i][j].draw_move(self._cells[i2][j2], undo=True)

            if direction == "right":
                if ((not self._cells[i][j].has_right_wall)
                    and (not self._cells[i2][j2].has_left_wall) 
                    and (not self._cells[i2][j2].visited)):
                    self._cells[i][j].draw_move(self._cells[i2][j2])

                    if self._solve_r(i2, j2):
                        return True
                    
                    self._cells[i][j].draw_move(self._cells[i2][j2], undo=True)

            if direction == "up":
                if ((not self._cells[i][j].has_top_wall)
                    and (not self._cells[i2][j2].has_bottom_wall)
                    and (not self._cells[i2][j2].visited)):
                    self._cells[i][j].draw_move(self._cells[i2][j2])

                    if self._solve_r(i2, j2):
                        return True
                    
                    self._cells[i][j].draw_move(self._cells[i2][j2], undo=True)

            if direction == "down":
                if ((not self._cells[i][j].has_bottom_wall)
                    and (not self._cells[i2][j2].has_top_wall)
                    and (not self._cells[i2][j2].visited)):
                    self._cells[i][j].draw_move(self._cells[i2][j2])

                    if self._solve_r(i2, j2):
                        return True
                    
                    self._cells[i][j].draw_move(self._cells[i2][j2], undo=True)
        return False
