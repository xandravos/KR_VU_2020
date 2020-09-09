class Clause_list():
    def __init__(self, clause_list):
        self.clause_list = clause_list

    def find_tautologies(self):
        tautologies = [clause for clause in self.clause_list if clause.is_tautology() == True]
        return tautologies

    def find_unit_clauses(self):
        unit_classes = [clause for clause in self.clause_list if clause.is_unit() == True]
        return unit_classes

    def find_pure_literals(self):
        all_literals = []
        for clause in self.clause_list:
            all_literals += clause.list
        pure_literals = [lit for lit in all_literals if (0 - lit) not in all_literals]
        pure_literals = list(set(pure_literals))
        return pure_literals


    def remove(self, clauses_to_remove):
        self.clause_list = [clause for clause in self.clause_list if clause not in clauses_to_remove]

    def remove_clauses_from_values(self, values):
        self.clause_list = [clause for clause in self.clause_list if (set(clause.list) & set(values)) == set()]

    def remove_literals_from_clauses(self, literals):
        for clause in self.clause_list:
            clause.list = [lit for lit in clause.list if lit not in literals and 0 - lit not in literals]

    def contains_empty_clause(self):
        for clause in self.clause_list:
            if len(clause.list) == 0:
                return True
        return False


    def __str__(self):
        s = ""
        for clause in self.clause_list:
            s += "\n"
            for literal in clause.list:
                s = s + str(literal) + " "
        return s
