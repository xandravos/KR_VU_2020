# KR_VU_2020 SAT solver
This is the repository for the SAT solver for the 2020 course Knowledge
Representation at the Vrije Universiteit Amsterdam. The SAT solver is built by
Laura Brongers, Ravi Meijer, Adrian Nichici, and Xandra Vos (Group 5).

## Our research
Our research included comparing the performance of four heuristics within the
DPLL algorithm when used as a SAT solver for Sudoku puzzles. We also compared
the performance on a different type of Sudoku, namely SudokuX. The code that is
present in this repository is not the same as the code used for the experiments.
More information about the experiments can be found in our paper.

## Files
The main file is SAT.py. The files that are used by SAT.py are sat_solver.py
and make_output_file.py. The first one runs the whole DPLL algorithm and the
latter writes the output file when a solution is found.
The dimacs_sudokus folder contains all the SudokuX and regular Sudoku files in
DIMACS format. The corresponding rules are also included in the files.

The script to write the raw Sudoku files to DIMACS files are not in the
repository because they are not used when running the final code.

## Running the code

To run the SAT solver for a regular Sudoku, type the following command in your
terminal of choice:

<pre><code>python SAT.py Sn sudoku9x9_1</code></pre>

With this command, regular Sudoku 1 is used as input. There are 985 regular
Sudokus so the number that says 1 in the command above can vary from
1 to 985.
<br>
If you want to run a SudokuX file, use:

<pre><code>python SAT.py Sn sudokux9x9_1</code></pre>

Since there are 15 SudokuX files, the number can vary from 1 to 15.
The "n" should be a number from 1 to 4, which corresponds with the following
heuristics used for the split in the DPLL algorithm:
1. Random
2. DLCS
3. MOM
4. JW two-sided
