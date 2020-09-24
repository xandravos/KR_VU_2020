import sys
from sat_solver import SAT_Solver
import mxklabs.dimacs
from sat_solver import *
import statistics
from make_output_file import *

def main():
    global TOTAL_SPLITS
    global TOTAL_BACKTRACKS
    global NR_SOLVED
    global ZERO_SPLITS
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

        for i in range(1, NR_TESTING+1):
            full_filename = f"{filename}_{i}"
            filepath = f"dimacs_sudokus/{full_filename}"
            try:
                dimacs = mxklabs.dimacs.read(filepath)
                list_clauses = dimacs.clauses
            except Exception as e:
                print(e)
                sys.exit(1)

            # list_clauses = tautology_check(list_clauses)
            sat_solver = SAT_Solver()
            sudoku_solution = sat_solver.dp(list_clauses, set(), strategy)
            if sudoku_solution != "NSF":
                TOTAL_SPLITS.append(sat_solver.splits)
                TOTAL_BACKTRACKS.append(sat_solver.backtracks)
                NR_SOLVED += 1
                print(f"SUDOKU {i} SOLVED WITH {sat_solver.splits} SPLITS")
                # make_output_file(sudoku_solution, strategy, full_filename)
                if sat_solver.splits == 0:
                    ZERO_SPLITS += 1

    mean_splits = statistics.mean(TOTAL_SPLITS)
    std_splits = statistics.stdev(TOTAL_SPLITS)
    min_splits = min(TOTAL_SPLITS)
    max_splits = max(TOTAL_SPLITS)
    median_splits = statistics.median(TOTAL_SPLITS)
    mode_splits = statistics.mode(TOTAL_SPLITS)

    mean_backtracks = statistics.mean(TOTAL_BACKTRACKS)
    std_backtracks = statistics.stdev(TOTAL_BACKTRACKS)
    min_backtracks = min(TOTAL_BACKTRACKS)
    max_backtracks = max(TOTAL_BACKTRACKS)
    median_backtracks = statistics.median(TOTAL_BACKTRACKS)
    mode_backtracks = statistics.mode(TOTAL_BACKTRACKS)

    print(f"SUDOKUS SOLVED WITH FOLLOWING STATISTICS FOR THE SPLITS:\n"
    f"Mean: {mean_splits}\n"
    f"Std: {std_splits}\n"
    f"Min: {min_splits}\n"
    f"Max: {max_splits}\n"
    f"Median: {median_splits}\n"
    f"Mode: {mode_splits}")
    print(f"SUDOKUS SOLVED WITH FOLLOWING STATISTICS FOR THE BACKTRACKS:\n"
    f"Mean: {mean_backtracks}\n"
    f"Std: {std_backtracks}\n"
    f"Min: {min_backtracks}\n"
    f"Max: {max_backtracks}\n"
    f"Median: {median_backtracks}\n"
    f"Mode: {mode_backtracks}")
    print("Number of solved sudokus: ", NR_SOLVED)
    print("Number of solved without splits: ", ZERO_SPLITS)

if __name__ == "__main__":
    strategies = ["Random", "DLCS", "MOM", "JW_two_sided"]
    SUDOKUS_ORIGINAL = 1011
    SUDOKUS_X = 5
    TOTAL_SPLITS = []
    TOTAL_BACKTRACKS = []
    NR_TESTING = 500
    NR_SOLVED = 0
    ZERO_SPLITS = 0
    main()
