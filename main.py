from window import Window
from point import Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    cell = Cell(10, 50, 500, 500, win)
    cell.draw()
    win.wait_for_close()


main()
