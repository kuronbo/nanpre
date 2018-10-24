from itertools import product

from nanpre.exceptions import BoardError


class Board(object):
    """ナンプレの盤面

    よくある9x9のナンプレの盤面。
    実は、このクラスにルールを判定する仕組みは無い。ユーザーの使い方に委ねるのみ
    である。しかし、ヒントとなる最初の数字がルールを無視しているのなら、例外が
    発生する。
    座標の範囲はx, yともに最小0, 最大8である。
    また、設定できる数字の範囲は、最小1, 最大9である。

    Notes:
        ピア: ピアとは数字が競合するセルのことである。ピアと同じ数字を設定する
            ことはできない。
            一つのセルに対して、ピアは最大20個存在する。
    """
    def __init__(self, first_cells):
        """
        Args:
             first_cells (dict): ナンプレの最初のヒント。
                keyがxy座標、valueが数字となっている。
        """
        self._area = {}
        for position, number in first_cells.items():
            if number not in self.possible_numbers(position):
                raise BoardError('初期設定がルールに反しています。')
            self.set(position, number)

    def now(self):
        return self._area

    def get(self, position):
        if not (0, 0) <= position <= (8, 8):
            raise BoardError('x, y値の範囲は0-8であるべきです。')
        return self._area[position]

    def set(self, position, number):
        if not (0, 0) <= position <= (8, 8):
            raise BoardError('x, y値の範囲は0-8であるべきです。')
        if number not in range(1, 10):
            raise BoardError('numberの値は1-9であるべきです。')
        self._area[position] = number

    def rm(self, position):
        if not (0, 0) <= position <= (8, 8):
            raise BoardError('x, y値の範囲は0-8であるべきです。')
        if self._area.get(position):
            del self._area[position]

    def free_cell_positions(self):
        """値未設定のセルの位置を返す

        Returns:
            list: xとyのタプル(`position`)を要素としたリスト
        """
        positions = []
        for position in product(range(9), range(9)):
            if position not in self._area:
                positions.append(position)
        return positions

    def possible_numbers(self, position):
        """指定のセルに設定可能な数字群を返す

        ナンプレのルールに則り、指定のセルに設定可能な数字群を返す。
        もっと詳しく言えば、ピアに設定されていない数字を返す。

        Parameters:
            position (tuple): セルの位置。xy座標。

        Returns:
            set: 設定可能な数字の集合
        """
        already_nums = set()
        for peer_position in self._peer_positions(position):
            already_nums.add(self._area.get(peer_position, None))
        already_nums = already_nums - {None}
        return {*range(1, 10)} - already_nums

    def _peer_positions(self, position):
        x, y = position
        positions = []
        for yj in range(9):
            positions.append((x, yj))
        for xi in range(9):
            positions.append((xi, y))
        block_no = x//3 + y//3*3
        xs = [i + (block_no % 3) * 3 for i in range(3)]
        ys = [j + (block_no // 3) * 3 for j in range(3)]
        for xi, yj in product(xs, ys):
            positions.append((xi, yj))
        return set(positions) - {(x, y)}
