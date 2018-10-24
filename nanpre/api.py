from nanpre.board import Board
from nanpre.grid_format import cells_from_grid, grid_from_cells
from nanpre.solver import solve


def solve_from_file(path):
    with open(path) as f:
        text = f.read()
    result = solve(Board(cells_from_grid(text)))
    return grid_from_cells(result)
