import sys
import math

def main():
    argv_len = len(sys.argv)
    if argv_len == 2:
        filename = sys.argv[1]
        # print(filename)
        file = "raw_sudokus/" + filename
        read_sudoku(file)
    else:
        if argv_len > 0:
            print("usage error: {} <file>".format(sys.argv[0]))
        else:
            print("usage error")

def read_sudoku(file):
    with open(file, "r") as f:
        sudokus = f.readlines()
        # print(sudokus)
        sudoku_nr = 0
        for sudoku in sudokus:
            # print("new")
            # print(sudoku)
            sudoku = sudoku.strip()
            sudoku_size = int(math.sqrt(len(sudoku)))
            dimacs_list = []
            row = 1
            column = 1
            for character in sudoku:
                if character != ".":
                    clause = str(row) + str(column) + character
                    dimacs_list.append(clause)
                # print(dimacs_list)
                column += 1
                if column > sudoku_size:
                    column %= sudoku_size
                    row += 1
            sudoku_nr += 1
            # sudoku_to_dimacs(sudoku_nr, sudoku_size, dimacs_list)
    f.close()
#
# def sudoku_to_dimacs(sudoku_nr, sudoku_size, dimacs_list):
#     file_write = f"dimacs_sudokus/sudoku{sudoku_size}x{sudoku_size}_{sudoku_nr}"
#     file_read = f"raw_sudokus/sudoku_rules{sudoku_size}x{sudoku_size}.txt"
#     with open(file_read, "r") as f:
#         clauses_rules = f.readlines()
#     with open(file_write, "w") as f:
#         f.write(f"p cnf {sudoku_size}{sudoku_size}{sudoku_size} {len(clauses_rules) + len(dimacs_list)}\n")
#         for clause in dimacs_list:
#             f.write(f"{clause} 0\n")
#         for clause in clauses_rules:
#             f.write(clause)
#     f.close()


if __name__ == "__main__":
    main()
