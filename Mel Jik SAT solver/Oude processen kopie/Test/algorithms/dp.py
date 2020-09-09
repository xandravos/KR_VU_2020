import random
from classes.clause_list import Clause_list
from classes.variable_dict import Variable_dict

def dp(clause_list, variable_dict, last_len):

     # end condition
    length = len(clause_list.clause_list)
    print("start", length)
    if length is last_len or length is 0:
        if length == 0:
            print("JIPI")
        return
    else:
        last_len = length

    o1 = Clause_list(clause_list.clause_list)
    o2 = Variable_dict(variable_dict.variable_dict)
    # tautologies = clause_list.find_tautologies()
    # if tautologies != []:
    #     clause_list.remove(tautologies)
    advance = True
    while advance == True:
        advance = False
        unit_clauses = clause_list.find_unit_clauses()
        if unit_clauses != []:
            advance = True
            variable_values_units = [clause.list[0] for clause in unit_clauses]
            variable_dict.set_values(variable_values_units)
            clause_list.remove_clauses_from_values(variable_values_units)
            clause_list.remove_literals_from_clauses(variable_values_units)

        pure_literals = clause_list.find_pure_literals()
        if pure_literals != []:
            advance = True
            variable_dict.set_values(pure_literals)
            clause_list.remove_clauses_from_values(pure_literals)
            clause_list.remove_literals_from_clauses(pure_literals)

        # print(clause_list)
        # print(variable_dict.variable_dict)
    length_list = len(clause_list.clause_list)
    if clause_list.contains_empty_clause() == False and length_list > 0:
        random_number_1 = random.randint(0,1)
        random_number_2 = random.randint(1,length_list) - 1
        variable_value = abs(clause_list.clause_list[random_number_2].list[0])
        if random_number_1 == 0:
            variable_value = 0 - variable_value
        variable_dict.set_values([variable_value])
        clause_list.remove_clauses_from_values([variable_value])
        clause_list.remove_literals_from_clauses([variable_value])

    dp(clause_list, variable_dict, last_len)

    # clause_list = Clause_list(o1.clause_list)
    # variable_dict = Variable_dict(o2.variable_dict)

    print("back")
    print(length_list)
