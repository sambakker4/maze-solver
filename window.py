from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.root_widget = Tk()
        self.root_widget.geometry = f"{width}x{height}"
        self.root_widget.title = "Title"
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update()
        self.root_widget.update_idletasks()

    def wait_for_close(self):
        self.running = True

        while self.running:
            self.redraw()

    def close(self):
        self.running = False
