from nanpre.exceptions import SolverError


def solve(board):
    result = Solver(board).solve()
    if result:
        return result.now()
    else:
        raise SolverError('問題を解けませんでした。')


class Solver(object):
    def __init__(self, board):
        self.board = board
        self.free_positions = self.board.free_cell_positions()

    def solve(self):
        def _solve(idx):
            if idx == len(self.free_positions):
                return True
            position = self.free_positions[idx]
            for n in self.board.possible_numbers(position):
                self.board.set(position, n)
                is_ok = _solve(idx + 1)
                if is_ok:
                    return True
                else:
                    self.board.rm(position)
            return False
        if _solve(0):
            return self.board
        else:
            return None
