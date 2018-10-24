import re


REGEX_SIMLE_GRID = \
    r'(([\d\.]\s){8}[\d\.]\n){9}'


def cells_from_grid(text):
    result = {}
    r = re.match(REGEX_SIMLE_GRID, text)
    lines = text.strip().split('\n')
    for y, line in enumerate(lines):
        for x, v in enumerate(line.strip().split(' ')):
            if v == '0' or v == '.':
                continue
            result[(x, y)] = int(v)
    return result


def grid_from_cells(cells):
    result = []
    for y in range(9):
        line = []
        for x in range(9):
            line.append(str(cells.get((x, y), '.')))
        line = ' '.join(line)
        result.append(line)
    return '\n'.join(result)
