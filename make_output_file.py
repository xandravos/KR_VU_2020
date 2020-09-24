def make_output_file(sudoku_solution, strategy, filename):
    filename_out = f"output_sudokus/{filename}_{strategy}.out"
    if sudoku_solution == None:
        sudoku_solution = []
    len_set_solution = len(set(sudoku_solution))
    len_solution = len(sudoku_solution)
    with open(filename_out, "w") as f:
        f.write(f"p cnf {len_set_solution} {len_solution}\n")
        for variable in sudoku_solution:
            f.write(f"{variable} 0\n")
    f.close()
