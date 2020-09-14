import sys
from dp import dp
from dp import test
from sudoku_reader import dimacs_reader

def main():
    ARGV_LEN = len(sys.argv)
    if ARGV_LEN == 2:
        filename = sys.argv[1]
        filename = f"dimacs_sudokus/{filename}"
        clause_list = dimacs_reader(filename)
        solution = dp(test(clause_list, None), set())
        for sol in solution:
            if sol > 0:
                print(sol)

    else:
        if ARGV_LEN > 0:
            print("usage error: {} <file>".format(sys.argv[0]))
        else:
            print("usage error")

if __name__ == "__main__":
    main()
