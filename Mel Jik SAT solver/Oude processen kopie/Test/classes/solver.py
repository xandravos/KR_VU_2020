from algorithms.dp import dp
import random
import sys
from classes.clause_list import Clause_list
from classes.variable_dict import Variable_dict


class Solver():
    def __init__(self, clause_list, variable_dict):
        self.clause_list = clause_list
        self.variable_dict = variable_dict
        self.solved = False
        self.depth = 0

    def solve(self):
        tautologies = self.clause_list.find_tautologies()
        if tautologies != []:
            self.clause_list.remove(tautologies)
        return self.dp()

    def dp(self):
        print("start")
        if len(self.clause_list.clause_list) == 0:
            print("yest")
            return True
        # if self.clause_list.contains_empty_clause():
        #     print("kut")
        #     # print(self.clause_list)
        #     return None

        self.depth += 1
        print("\n\nclause_list_begin", self.depth, self.clause_list)

        o1 = Clause_list(self.clause_list.clause_list)
        o2 = Variable_dict(self.variable_dict.variable_dict)

        advance = True
        while advance == True:
            advance = False
            unit_clauses = self.clause_list.find_unit_clauses()
            variable_values_units = [clause.list[0] for clause in unit_clauses]
            if variable_values_units != []:
                advance = True
                for variable_value in variable_values_units:
                    self.make_choice([variable_value])
                # self.variable_dict.set_values(variable_values_units)
                # self.clause_list.remove_clauses_from_values(variable_values_units)
                # self.clause_list.remove_literals_from_clauses(variable_values_units)
                print("\n\nclause_list_afer unit", self.depth, self.clause_list)


            pure_literals = self.clause_list.find_pure_literals()
            if pure_literals != []:
                advance = True
                for pure_literal in pure_literals:
                    self.make_choice([pure_literal])
                # self.variable_dict.set_values(pure_literals)
                # self.clause_list.remove_clauses_from_values(pure_literals)
                # self.clause_list.remove_literals_from_clauses(pure_literals)
                print("\n\nclause_list_after pure", self.depth, self.clause_list)

        print("\n\nclause_list_after dp", self.depth, self.clause_list)


        if len(self.clause_list.clause_list) == 0:
            print("yessss")
            return True
        if self.clause_list.contains_empty_clause():
            print("kut")
            return None

        print("\n\nclause_list_before_split", self.depth, self.clause_list)

        length_list = len(self.clause_list.clause_list)
        random_number = random.randint(1,length_list) - 1
        variable_value = abs(self.clause_list.clause_list[random_number].list[0])
        self.make_choice([variable_value])

        # self.variable_dict.set_values([variable_value])
        # self.clause_list.remove_clauses_from_values([variable_value])
        # self.clause_list.remove_literals_from_clauses([variable_value])
        print(variable_value)
        print("\n\nclause_list_after_split", self.depth, self.clause_list)

        if not self.dp():
            self.clause_list = Clause_list(o1.clause_list)
            self.variable_dict = Variable_dict(o2.variable_dict)

            print("\n\nclause list reset", self.depth, self.clause_list)

            self.make_choice([variable_value])

            # self.variable_dict.set_values([0 - variable_value])
            # self.clause_list.remove_clauses_from_values([0 - variable_value])
            # self.clause_list.remove_literals_from_clauses([0 - variable_value])

            print("\n\nclause list other choice", self.depth, self.clause_list)

            return self.dp()

    def make_choice(self, choice):
        self.variable_dict.set_values(choice)
        self.clause_list.remove_clauses_from_values(choice)
        self.clause_list.remove_literals_from_clauses(choice)
