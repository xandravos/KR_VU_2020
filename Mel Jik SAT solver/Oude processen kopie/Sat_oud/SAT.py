import sys
import random

from helpers.read_dimacs import read_dimacs
from pure_literal import check_for_pure_literals
from tautology import check_for_tautology

def main():
     ARGV_LEN = len(sys.argv)
     if ARGV_LEN == 2:
         filename = sys.argv[1]
         filename = f"sodoku's_dimac/{filename}"
         input = read_dimacs(filename)
         clause_list = input[0]
         variable_list = input[1]
         check_for_tautology(clause_list)
         sat_solver(clause_list, variable_list)
         for variable in variable_list:
             if variable.truth_value == True:
                print(variable)

     else:
       if ARGV_LEN > 0:
         print("usage error: {} <file>".format(sys.argv[0]))
       else:
         print("usage error")

def sat_solver(clause_list, variable_list):
    print("Start\n")
    changes_made_unit = 1
    changes_made_pures = 1
    while changes_made_unit > 0 or changes_made_pures > 0:
        print("unit")
        changes_made_unit = check_for_unit_clauses(clause_list, variable_list)
        print("pure")
        print("clauses",len(clause_list))
        changes_made_pures = check_for_pure_literals(clause_list, variable_list)
        print("clauses", len(clause_list))
    if len(clause_list) > 0:
        print("split")
        make_split(clause_list, variable_list)

    if len(clause_list) == 0:
        return
    elif [] in clause_list:
        print("WOW")
        return
    else:
        sat_solver(clause_list, variable_list)



def make_split(clause_list, variable_list):
    if len(clause_list[0].list) > 0:
        variable_value = abs(clause_list[0].list[0].value)
        random_number = random.randint(0,1)
        for variable in variable_list:
            if variable.literal == variable_value:
                if random_number == 0:
                    variable.truth_value = False
                else:
                    variable.truth_value = True
                set_literal_truth_values(clause_list, [variable])



def check_for_unit_clauses(clause_list, variable_list):
    clauses_to_remove = []
    variables_changed = []
    changes_made = 0
    for clause in clause_list:
        if len(clause.list) == 1:
            literal = clause.list[0].value
            if literal < 0:
                for variable in variable_list:
                    if abs(literal) == variable.literal:
                        variable.truth_value = False
                        variables_changed.append(variable)
            else:
                for variable in variable_list:
                    if literal == variable.literal:
                        variable.truth_value = True
                        variables_changed.append(variable)
            clauses_to_remove.append(clause)
            changes_made = 1

    for clause in clauses_to_remove:
        clause_list.remove(clause)
    set_literal_truth_values(clause_list, variables_changed)
    return changes_made



def set_literal_truth_values(clause_list, variable_list):
    print("set start")
    clauses_to_remove = []
    for variable in variable_list:
        if variable.truth_value == False:
            clauses_to_remove += [clause for clause in clause_list if clause.check_if_remove(0 - variable.literal)]
            # literals_to_remove = []
            for clause in clause_list:
                literals_to_remove = [literal for literal in clause.list if abs(literal.value) == variable.literal and literal.value > 0]
                # for literal in clause.list:
                #     if abs(literal.value) == variable.literal:
                #         if literal.value < 0:
                #             if clause in clauses_to_remove:
                #                 continue
                #             clauses_to_remove.append(clause)
                #         else:
                #             literals_to_remove.append(literal)
                for literal in literals_to_remove:
                    clause.list.remove(literal)

        elif variable.truth_value == True:
            clauses_to_remove += [clause for clause in clause_list if clause.check_if_remove(variable.literal)]
            # literals_to_remove = []
            for clause in clause_list:
                literals_to_remove = [literal for literal in clause.list if literal.value == variable.literal and literal.value < 0]

            # for clause in clause_list:
            #     literals_to_remove = []
            #     for literal in clause.list:
            #         if abs(literal.value) == variable.literal:
            #             if literal.value < 0:
            #                 literals_to_remove.append(literal)
            #             else:
            #                 if clause in clauses_to_remove:
            #                     continue
            #                 clauses_to_remove.append(clause)
                for literal in literals_to_remove:
                    clause.list.remove(literal)

    for clause in clauses_to_remove:
        clause_list.remove(clause)


if __name__ == "__main__":
    main()
