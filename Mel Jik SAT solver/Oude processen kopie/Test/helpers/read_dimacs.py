import mxklabs.dimacs
from classes.literal import Literal
from classes.clause import Clause
from classes.variable import Variable
from classes.variable_dict import Variable_dict
from classes.clause_list import Clause_list

def read_dimacs(filename):
    try:
        # Read the DIMACS file
        dimacs = mxklabs.dimacs.read(filename)
        # Iterate over clauses.
        clause_list = []
        variable_dict = {}
        literal_values_list = []
        for clause in dimacs.clauses:
            new_clause = Clause()
            for literal in clause:
                new_clause.list.append(literal)
                if abs(literal) not in literal_values_list:
                     literal_values_list.append(abs(literal))
                     # new_variable = Variable(abs(literal))
                     variable_dict[abs(literal)] = None

            clause_list.append(new_clause)
        return_list = [Clause_list(clause_list), Variable_dict(variable_dict)]
        return return_list

    except Exception as e:
      # Report error.
      print(e)
