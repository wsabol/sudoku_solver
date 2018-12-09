import json
from sudoku import Sudoku

if __name__ == '__main__':
    # get test puzzles
    with open('test_cases.json') as f:
        puzzles = json.load(f)

    for p in puzzles:
        print(p['title'])
        print(p['result'])
        print('---')
        s = Sudoku(p['board'])
        s.solve()
        s.display()
        print()

    # board formats
    board = "...6.2.....1.9.2..3..5.4..76.97.35.12.......6...........4...6...1.2.6.8..62...93."
    s = Sudoku(board)
    s.solve()
    s.display()
    print()

    board = "000010080302607000070000003080070500004000600003050010200000050000705108060040000"
    s = Sudoku(board)
    s.solve()
    s.display()
    print()

    board = [
      [0,0,0,0,6,0,0,0,0],
      [0,0,1,0,2,0,8,0,0],
      [0,7,8,0,0,0,3,5,0],
      [0,0,5,7,0,8,9,0,0],
      [7,0,0,4,0,1,0,0,5],
      [0,0,0,0,0,0,0,0,0],
      [9,0,0,3,0,5,0,0,7],
      [0,6,0,0,0,0,0,9,0],
      [0,4,0,0,0,0,0,3,0]
    ]
    s = Sudoku(board)
    s.solve()
    s.display()
