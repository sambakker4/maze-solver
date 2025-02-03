from point import Point, Line

class Cell:
    def __init__(
        self,
        win,
        x1=None,
        y1=None,
        x2=None,
        y2=None,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True
    ):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall


    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            point1 = Point(self._x1, self._y1)
            point2 = Point(self._x1, self._y2)

            line = Line(point1, point2)

            self._win.draw_line(line)
        
        if self.has_right_wall:
            point1 = Point(self._x2, self._y1)
            point2 = Point(self._x2, self._y2)

            line = Line(point1, point2)

            self._win.draw_line(line)
        
        if self.has_top_wall:
            point1 = Point(self._x1, self._y1)
            point2 = Point(self._x2, self._y1)

            line = Line(point1, point2)

            self._win.draw_line(line)
        
        if self.has_bottom_wall:
            point1 = Point(self._x1, self._y2)
            point2 = Point(self._x2, self._y2)

            line = Line(point1, point2)

            self._win.draw_line(line)
        
    def draw_move(self, to_cell, undo=False):
        if undo:
            colour = "grey"
        else:
            colour = "red"

        point1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        point2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)

        line = Line(point1, point2)
        
        self._win.draw_line(line, colour)
