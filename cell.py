from point import Point, Line

class Cell:
    def __init__(
        self,
        x1,
        y1,
        x2,
        y2,
        win,
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


    def draw(self):
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
