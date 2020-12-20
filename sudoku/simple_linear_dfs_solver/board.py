import copy


class Board:
    def __init__(self, field: list):
        self.__field = [[int(s) if s.isdigit() else 0 for s in line]
                        for line in field]

    @property
    def field(self):
        return self.__field

    def get_copy(self):
        return copy.deepcopy(self)

    def find_empty_coordinate_first(self):
        for x in range(0, len(self.__field)):
            for y in range(0, len(self.__field[0])):
                if self.__field[x][y] == 0:
                    return x, y
        return None

    def find_choices(self, x: int, y: int):
        can_use = list(range(1, 10))
        # 同じ行に同じ数字を入れることはできない
        for i in range(0, 9):
            can_use = [v for v in can_use if v != self.__field[x][i]]
        # 同じ列に同じ数字を入れることはできない
        for i in range(0, 9):
            can_use = [v for v in can_use if v != self.__field[i][y]]
        # 同じブロックに同じ数字を入れることはできない
        # マス (cx, cy) はマス (x, y) を含むブロックの中央マスを表す
        cx = int(x / 3) * 3 + 1
        cy = int(y / 3) * 3 + 1
        for i in range(cx - 1, cx + 1):
            for j in range(cy - 1, cy + 1):
                can_use = [v for v in can_use if v != self.__field[i][j]]
        return can_use

    def put(self, x: int, y: int, val: int):
        self.__field[x][y] = val

    def reset(self, x: int, y: int):
        self.__field[x][y] = 0
