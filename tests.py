import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_large(self):
        num_cols = 20
        num_rows = 20
        maze = Maze(0, 0, num_rows, num_cols, 50, 50)

        self.assertEqual(num_cols, len(maze._cells))
        self.assertEqual(num_rows, len(maze._cells[0]))

    def test_reset_cells_visited(self):
        num_cols = 20
        num_rows = 20
        maze = Maze(0, 0, num_rows, num_cols, 30, 30)
        
        for col in maze._cells:
            for cell in col:
                self.assertEqual(cell.visited, False)

if __name__ == "__main__":
    unittest.main()
