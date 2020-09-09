def set_literal_truth_values(clause_list, variable_list):
    print("set start")
    print("clauses",len(clause_list))
    clauses_to_remove = []
    for variable in variable_list:
        if variable.truth_value == False:
            for clause in clause_list:
                literals_to_remove = []
                for literal in clause.list:
                    if abs(literal.value) == variable.literal:
                        if literal.value < 0:
                            if clause in clauses_to_remove:
                                continue
                            clauses_to_remove.append(clause)
                        else:
                            literals_to_remove.append(literal)
                for literal in literals_to_remove:
                    clause.list.remove(literal)

        elif variable.truth_value == True:
            for clause in clause_list:
                literals_to_remove = []
                for literal in clause.list:
                    if abs(literal.value) == variable.literal:
                        if literal.value < 0:
                            literals_to_remove.append(literal)
                        else:
                            if clause in clauses_to_remove:
                                continue
                            clauses_to_remove.append(clause)
                for literal in literals_to_remove:
                    clause.list.remove(literal)

    for clause in clauses_to_remove:
        clause_list.remove(clause)
    print("clauses:", len(clause_list))
    print("end of setting:::")
