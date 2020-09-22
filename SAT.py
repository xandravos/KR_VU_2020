import sys
from dp import dp
from dp import test
from dimacs_reader import dimacs_reader
from sat_solver import SAT_Solver
import mxklabs.dimacs
from sat_solver import *

def main():
    global TOTAL_SPLITS
    global TOTAL_BACKTRACKS
    ARGV_LEN = len(sys.argv)
    if ARGV_LEN != 3:
        print("Usage error, please use the following command: python SAT.py S<n> <file>.")
    else:
        strategy = int(sys.argv[1][1])
        if not strategy in range(1,5):
            print("Please use a strategy in the following range:")
            print("1. Random\n2. DLCS\n3. MOM\n4. Jeroslow-Wang two-sided")
            sys.exit(1)
        strategy = strategies[strategy - 1]
        filename = sys.argv[2]
        print(f"SAT Solver using the {strategy} heuristic started...")

        for i in range(1,NR_TESTING + 1):
            filepath = f"dimacs_sudokus/{filename}_{i}"
            try:
                dimacs = mxklabs.dimacs.read(filepath)
                list_clauses = dimacs.clauses
            except Exception as e:# Report error.
                print(e)
                sys.exit(1)

            # print(f"SAT Solver using the {strategy} heuristic started...")
            sat_solver = SAT_Solver()
            sudoku_solution = sat_solver.dp(list_clauses, set(), strategy)
            # print(sudoku_solution)
            print(f"SUDOKU {i} SOLVED WITH {sat_solver.splits} SPLITS")
            # print(f"SUDOKU {i} SOLVED WITH {sat_solver.backtracks} CONFLICTS")
            TOTAL_SPLITS += sat_solver.splits
            TOTAL_BACKTRACKS += sat_solver.backtracks
    print(f"ORIGINAL SUDOKUS SOLVED WITH {TOTAL_SPLITS/NR_TESTING} SPLITS ON AVERAGE")
    print(f"ORIGINAL SUDOKUS SOLVED WITH {TOTAL_BACKTRACKS/NR_TESTING} SPLITS ON AVERAGE")

if __name__ == "__main__":
    strategies = ["Random", "DLCS", "MOM", "JW_two_sided"]
    SUDOKUS_ORIGINAL = 1011
    SUDOKUS_X = 5
    TOTAL_SPLITS = 0
    TOTAL_BACKTRACKS = 0
    NR_TESTING = 500
    main()
