from set_values import set_literal_truth_values
from collections import Counter

def check_for_pure_literals(clause_list, variable_list):
    print("1")
    all_literals = []
    variables_changed = []
    for clause in clause_list:
        new_literals = [literal.value for literal in clause.list]
        all_literals += new_literals
    pures = [literal for literal in all_literals if (0 - literal) not in all_literals]
    print("2")
    print(len(all_literals))
    print("pures:", len(pures))
    for literal in pures:
        if literal < 0:
            for variable in variable_list:
                if abs(literal) == variable.literal:
                    variable.truth_value = False
                    variables_changed.append(variable)
                    continue
        else:
            for variable in variable_list:
                if literal == variable.literal:
                    variable.truth_value = True
                    variables_changed.append(variable)
                    continue
    set_literal_truth_values(clause_list, variables_changed)
    if len(pures) > 0:
        return 1
    else:
        return 0
