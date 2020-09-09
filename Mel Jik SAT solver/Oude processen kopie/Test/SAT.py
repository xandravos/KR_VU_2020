import sys
from helpers.read_dimacs import read_dimacs

from classes.solver import Solver
from algorithms.dp import dp

def main():
     ARGV_LEN = len(sys.argv)
     if ARGV_LEN == 2:
         filename = sys.argv[1]
         filename = f"sodoku's_dimac/{filename}"
         input = read_dimacs(filename)
         clause_list = input[0]
         variable_list = input[1]
         solver = Solver(clause_list, variable_list)

         solved = solver.solve()
         # print(solved)

         # for variable in variable_list:
         #     if variable.truth_value == True:
         #        print(variable)

     else:
       if ARGV_LEN > 0:
         print("usage error: {} <file>".format(sys.argv[0]))
       else:
         print("usage error")

if __name__ == "__main__":
    main()
