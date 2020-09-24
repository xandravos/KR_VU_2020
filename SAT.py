import sys
from sat_solver import SAT_solver
import mxklabs.dimacs
from sat_solver import *
from make_output_file import *

def main():
    global TOTAL_SPLITS
    global TOTAL_BACKTRACKS
    global NR_SOLVED
    global ZERO_SPLITS
    ARGV_LEN = len(sys.argv)
    ARGV_LEN_STRAT = len(sys.argv[1])
    if ARGV_LEN != 3:
        print("Usage error, please use the following command: python SAT.py S<n> <file>.")
        sys.exit(1)
    elif ARGV_LEN_STRAT != 2:
        print("Please use a strategy in the following range:")
        print("1. Random\n2. DLCS\n3. MOM\n4. Jeroslow-Wang two-sided")
        sys.exit(1)
    else:
        strategy = int(sys.argv[1][1])
        if not strategy in range(1,5):
            print("Please use a strategy in the following range:")
            print("1. Random\n2. DLCS\n3. MOM\n4. Jeroslow-Wang two-sided")
            sys.exit(1)
        strategy = strategies[strategy - 1]
        filename = sys.argv[2]
        print(f"SAT solver using the {strategy} heuristic started...")

        filepath = f"dimacs_sudokus/{filename}"
        try:
            dimacs = mxklabs.dimacs.read(filepath)
            list_clauses = dimacs.clauses
        except Exception as e:
            print(e)
            sys.exit(1)

        sat_solver = SAT_Solver()
        sudoku_solution = sat_solver.dp(list_clauses, set(), strategy)
        if sudoku_solution != "NSF":
            print(f"Sudoku solved with {sat_solver.splits} splits")
            print(f"Sudoku solved with {sat_solver.backtracks} backtracks")
            make_output_file(sudoku_solution, strategy, filename)

if __name__ == "__main__":
    strategies = ["Random", "DLCS", "MOM", "JW_two_sided"]
    main()
