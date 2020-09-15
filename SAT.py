import sys
from dp import dp
from dp import test
from dimacs_reader import dimacs_reader
from sat_solver import Solver
import mxklabs.dimacs
from sat_solver import *

# python SAT.py sudoku9x9_1


def main():
    ARGV_LEN = len(sys.argv)
    if ARGV_LEN == 2:
        # TO DO: implement the strategy choice
        filename = sys.argv[1]
        filepath = f"dimacs_sudokus/{filename}"
        try:
            dimacs = mxklabs.dimacs.read(filepath)
            list_clauses = dimacs.clauses
        except Exception as e:# Report error.
            print(e)
            sys.exit(1)

        sudoku_solution = dpll(list_clauses)
        print("NEW SUDOKU\n")
        print(sudoku_solution)

    else:
        if ARGV_LEN > 0:
            print("Usage error, please use the following command: python {} S<n> <file>, where n is the chosen heuristic.".format(sys.argv[0]))
            # print("usage error: {} <file>".format(sys.argv[0]))
        else:
            print("huh")
            # print("Please use the following command: python {} S<n> <file>, where n is the chosen heuristic.".format(sys.argv[0]))

def dpll(list_clauses):
    print("jahallo")
    sat_solver = Solver()
    strategy = "Random"
    sudoku_solution = sat_solver.dp(update_clause_list(list_clauses, None), set(), strategy)
    return sudoku_solution
    # print(list_clauses)

if __name__ == "__main__":
    main()
