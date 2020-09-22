import copy
import random
import sys

sys.setrecursionlimit(10000)

class SAT_Solver():
    def __init__(self):
        self.splits = 0
        self.backtracks = 0
# Davis Putnam algorithm based on certain heuristic that determines how to split

    def dp(self, list_clauses, variable_values, strategy):
        # print("Splits:", self.splits)
        if self.splits < 1000:
            variable_values = copy.deepcopy(variable_values)
            # print(variable_values)

            if list_clauses == -1:
                # print("wanneer gebeurt dit dan")
                return [None, None, self.splits, self.backtracks]
                return None
            elif len(list_clauses) == 0:
                # print("en wanneer dit")
                answer_all = list(variable_values)
                answer_pos = [var for var in answer_all if var > 0]
                answer = [answer_pos, answer_all, self.splits, self.backtracks]
                return answer

            advance = True
            while advance == True:
                advance = False
                units = find_unit_clauses(list_clauses)
                pure_literals = find_pure_literals(list_clauses)
                literals = units + pure_literals
                for literal in literals:
                    advance = True
                    list_clauses = update_clause_list(list_clauses, literal)
                    variable_values.add(literal)
                    if list_clauses == -1:
                        variable_values.remove(literal)
                        return [None, None, self.splits, self.backtracks]
                        return None
                    elif len(list_clauses) == 0:
                        answer_all = list(variable_values)
                        answer_pos = [var for var in answer_all if var > 0]
                        answer = [answer_pos, answer_all, self.splits, self.backtracks]
                        return answer

            split_value = split(list_clauses, strategy)
            self.splits += 1

            variable_values.add(split_value)
            solution = self.dp(update_clause_list(list_clauses, split_value), variable_values, strategy)

            if not solution[0]:
                self.backtracks += 1
                variable_values.remove(split_value)
                variable_values.add(-split_value)
                solution = self.dp(update_clause_list(list_clauses, -split_value), variable_values, strategy)
            return solution

        else:
            print("NO SOLUTION FOUND")
            print("Splits:", self.splits)
            print("Backtracks:", self.backtracks)
            return "NSF"

def update_clause_list(list_clauses, value):
    if value is None or value == 0:
        return list_clauses
    list_clauses = [clause for clause in list_clauses if value not in clause]
    for i, clause in enumerate([*list_clauses]):
        clause = [literal for literal in clause if -value != literal]
        list_clauses[i] = clause
    if [] in list_clauses:
        return -1
    return list_clauses

def find_pure_literals(list_clauses):
    if list_clauses == -1:
        return []
    all_literals = []
    for clause in list_clauses:
        all_literals += clause
    pure_literals = set([literal for literal in all_literals if -literal not in all_literals])
    return list(pure_literals)


def find_unit_clauses(list_clauses):
    if list_clauses == -1:
        return []
    units = [clause[0] for clause in list_clauses if len(clause) == 1]
    return units

def make_list_literals(list_clauses):
    literals = []
    for clause in list_clauses:
        for literal in clause:
            if abs(literal) not in literals:
                literals.append(abs(literal))
    return literals

def minimum_size_clauses(list_clauses):
    min_len_clauses = []
    size = 0
    for clause in list_clauses:
        c_size = len(clause)
        if size == 0 or c_size < size:
            min_len_clauses = [clause]
            size = c_size
        elif c_size == size:
            min_len_clauses.append(clause)
    return(min_len_clauses)

def counter_pos_neg(list_clauses, list_literals):
    pos_list = []
    neg_list = []
    pos_neg_list = []
    for literal in list_literals:
        pos = 0
        neg = 0
        for clause in list_clauses:
            for literal_clause in clause:
                if literal_clause == literal:
                    pos += 1
                if literal_clause == -literal:
                    neg += 1
        pos_list.append(pos)
        neg_list.append(neg)
        pos_neg = pos + neg
        pos_neg_list.append(pos_neg)

    return pos_list, neg_list, pos_neg_list

def split(list_clauses, strategy):
    if strategy == "Random":
        return random_strategy(list_clauses)
    if strategy == "DLCS":
        return DLCS(list_clauses)
    if strategy == "MOM":
        return MOM(list_clauses)
    if strategy == "JW_two_sided":
        return JW_two_sided(list_clauses)

def random_strategy(list_clauses):
    len_clauses_list = len(list_clauses)
    random_int = random.randint(0, len_clauses_list - 1)
    random_clause = list_clauses[random_int]
    len_random_clause = len(random_clause)
    random_int = random.randits(0, len_random_clause - 1)
    random_lit = random_clause[random_int]
    return random_lit

def DLCS(list_clauses):
    list_literals = make_list_literals(list_clauses)
    list_literals.sort()
    pos_list, neg_list, pos_neg_list = counter_pos_neg(list_clauses, list_literals)
    max_value = max(pos_neg_list)
    max_index = pos_neg_list.index(max_value)
    pos = pos_list[max_index]
    neg = neg_list[max_index]
    if pos > neg:
        return list_literals[max_index]
    else:
        return -(list_literals[max_index])

def MOM(list_clauses):
    min_len_clauses = minimum_size_clauses(list_clauses)
    mom = []
    k = 2
    literals = make_list_literals(min_len_clauses)
    for literal in literals:
        f = 0
        fn = 0
        # number of occurences of literal in the smallest non-satisfiable clauses
        for clause in min_len_clauses:
            if literal in clause:
                f = f + 1
            elif -literal in clause:
                fn = fn + 1
        mom_f = (f + fn)*2**k + f + fn
        mom.append(mom_f)
    return literals[mom.index(max(mom))]

def JW_two_sided(list_clauses):
    list_literals = make_list_literals(list_clauses)
    list_literals.sort()
    j_pl_list = []
    j_nl_list = []
    j_sum_list = []

    for literal in list_literals:
        j_pl = 0
        j_nl = 0
        for clause in list_clauses:
            if literal in clause:
                j_pl = j_pl + 2**(0-len(clause))
            elif (literal * -1) in clause:
                j_nl = j_nl + 2** (0-len(clause))
        j_pl_list.append(j_pl)
        j_nl_list.append(j_nl)
        j_sum = j_pl+j_nl
        j_sum_list.append(j_sum)

    max_j = max(j_sum_list)
    index = j_sum_list.index(max_j)

    if j_pl_list[index] >= j_nl_list[index]:
        return list_literals[index]
    else:
        return list_literals[index] *-1
