def make_output_file(sudoku_solution, strategy, filename):
    filename_out = f"output_sudokus/{filename}_{strategy}.out"
    solution_pos = sudoku_solution[0]
    if solution_pos == None:
        solution_pos = []
    all_values = sudoku_solution[1]
    if all_values == None:
        all_values = []
    len_set_values = len(set(all_values))
    len_values = len(all_values)
    solution_splits = sudoku_solution[2]
    solution_backtracks = sudoku_solution[3]
    with open(filename_out, "w") as f:
        f.write(f"p cnf {len_values} {len_values}\n")
        for variable in all_values:
            f.write(f"{variable} 0\n")
    f.close()
