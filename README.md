# Sudoku Solver

A command line based sudoku solver. I have made a few of these in different languages, but none as neat as this one.
Test cases and error handling come from http://sudopedia.enjoysudoku.com/Test_Cases.html

## Getting Started

To get started make sure you have python 3 and numpy installed on your machine. The test cases in test_cases.json, and the main code in solver.py give examples of how boards can be submitted to the Sudoku class, either as a 2d list or numpy array, or a string of 81 characters where blanks are represented by any character other then 1-9, most commonly either '0' or '.'.

```
...6.2.....1.9.2..3..5.4..76.97.35.12.......6...........4...6...1.2.6.8..62...93.
- or -
000010080302607000070000003080070500004000600003050010200000050000705108060040000
- or -
[[0,0,0,0,6,0,0,0,0],
  [0,0,1,0,2,0,8,0,0],
  [0,7,8,0,0,0,3,5,0],
  [0,0,5,7,0,8,9,0,0],
  [7,0,0,4,0,1,0,0,5],
  [0,0,0,0,0,0,0,0,0],
  [9,0,0,3,0,5,0,0,7],
  [0,6,0,0,0,0,0,9,0],
  [0,4,0,0,0,0,0,3,0]]
```
You can fill test_cases.json with your own puzzles boards, the existing code with loop through the array of json objects in that file and solve every one. Or define you board in solver.py and solve it on its own - example below.

```
board = "...6.2.....1.9.2..3..5.4..76.97.35.12.......6...........4...6...1.2.6.8..62...93."
s = Sudoku(board) # initializes solver
s.display() # displays the init board
s.solve() # solves the puzzle
s.display() # displays the solved board
```

## Future Development

Per sudopedia, boards with multiple solutions are invalid puzzles. Currently my solver will solve every square that has a clear value, but has to pick one of the mutliple solutions to continue. I'd like to implement a method to simply pick one of the multiple solutions and display a completed board. The solver class has a 2d numpy array of lists holding possible values for each square. You can print this at anytime after initalizing the class, and it could be used to view the mutliple solutions in those cases.

```
> board = ".39...12....9.7...8..4.1..6.42...79...........91...54.5..1.9..3...8.5....14...87."
> s = Sudoku(board)
> s.solve()
Invalid Puzzle (“no unique solution”)
> s.display() # displays the solved board
4 3 9 | 6 5 8 | 1 2 7
1 5 6 | 9 2 7 | 3 8 4
8 2 7 | 4 3 1 | 9 5 6
- - - + - - - + - - -
. 4 2 | 5 1 . | 7 9 8
7 8 5 | 2 9 4 | 6 3 1
. 9 1 | 7 8 . | 5 4 2
- - - + - - - + - - -
5 7 8 | 1 4 9 | 2 6 3
2 6 3 | 8 7 5 | 4 1 9
9 1 4 | 3 6 2 | 8 7 5
> print(s.possibles(3, 0)) # row, column
[3,6]
> print(s.possibles(5, 0))
[3,6]
> print(s.possibles(3, 5))
[3,6]
> print(s.possibles(5, 5))
[3,6]
```

## Contributing

Feel free to fork or submit issues/suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

