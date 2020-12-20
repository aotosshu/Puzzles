import pprint
import time

from sudoku.simple_linear_dfs_solver.board import Board


def dfs(board: Board, res: list):
    coordinate = board.find_empty_coordinate_first()
    if coordinate is None:
        res.append(board.get_copy())
        return

    x, y = coordinate
    can_use = board.find_choices(x, y)
    for val in can_use:
        board.put(x, y, val)
        dfs(board, res)
        board.reset(x, y)


def main():
    with open('../problems/001.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    field = [list(line) for line in lines]

    start = time.time()

    board = Board(field)
    print('Problem:')
    pprint.pprint(board.field)
    results = []
    dfs(board, results)

    end = time.time()
    elapsed_time = end - start
    print("elapsed_time: {0:.3f}".format(elapsed_time) + "[sec]")

    if not results:
        print('No solutions.')
    elif len(results) > 1:
        print('More than one solutions.')
    else:
        print('Found one solution:')
        board = results[0]
        pprint.pprint(board.field)


if __name__ == '__main__':
    main()
