# KR_VU_2020
## SAT Solver
This is the repository for the SAT solver for the 2020 course Knowledge
Representation at the Vrije Universiteit Amsterdam. The SAT solver is built by
Laura Brongers, Ravi Meijer, Adrian Nichici, and Xandra Vos (Group 5).

### Running the code

To run the SAT solver, type the following command in your terminal of choice:

<pre><code>python SAT.py S<n> sudoku9x9_1.txt</code></pre>

The "n" should be a number from 1 to 4, which corresponds with the following
heuristics used for the split in the DPLL algorithm:
1. Random
2. DLCS
3. MOM
4. JW two-sided
