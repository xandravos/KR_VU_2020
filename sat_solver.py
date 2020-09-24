import copy
import random
import sys

sys.setrecursionlimit(10000)

class SAT_solver():
    def __init__(self):
        self.splits = 0
        self.backtracks = 0

    def dp(self, list_clauses, good_values, heuristic):
        if self.splits < 1000:
            good_values = copy.deepcopy(good_values)
            if list_clauses == -1:
                return [None, None, self.splits, self.backtracks]
            elif len(list_clauses) == 0:
                all_values = list(good_values)
                pos_values = []
                for variable in all_values:
                    if variable > 0:
                        pos_values.append(variable)
                return [pos_values, all_values, self.splits, self.backtracks]

            continuing = True
            while continuing == True:
                continuing = False
                units = find_units(list_clauses)
                pures = find_pures(list_clauses)
                literals = units + pures
                for literal in literals:
                    continuing = True
                    list_clauses = new_list_clauses(list_clauses, literal)
                    good_values.add(literal)
                    if list_clauses == -1:
                        good_values.remove(literal)
                        return [None, None, self.splits, self.backtracks]
                    elif len(list_clauses) == 0:
                        all_values = list(good_values)
                        pos_values = []
                        for variable in all_values:
                            if variable > 0:
                                pos_values.append(variable)
                        return [pos_values, all_values, self.splits, self.backtracks]

            split_value = split(list_clauses, heuristic)
            self.splits += 1
            good_values.add(split_value)

            solution = self.dp(new_list_clauses(list_clauses, split_value), good_values, heuristic)
            if not solution[0]:
                self.backtracks += 1
                good_values.remove(split_value)
                good_values.add(-split_value)
                solution = self.dp(new_list_clauses(list_clauses, -split_value), good_values, heuristic)
            return solution

        else:
            print("The maximum number of splits is reached. The sudoku is not solved.")
            print("Splits: ", self.splits, "\nBacktracks: ", self.backtracks)
            return "NSF"

def new_list_clauses(list_clauses, update_value):
    if update_value == 0 or update_value == None:
        return list_clauses
    for clause in list_clauses:
        if update_value in clause:
            list_clauses.remove(clause)
    for i, clause in enumerate([*list_clauses]):
        clause_list = [literal for literal in clause if -update_value != literal]
        list_clauses[i] = clause_list
    if [] in list_clauses:
        return -1
    return list_clauses

def find_pures(list_clauses):
    if list_clauses == -1:
        return []
    all_literals = []
    for clause in list_clauses:
        all_literals += clause
    pure_literals = []
    for literal in all_literals:
        if not -literal in all_literals:
            pure_literals.append(literal)
    return list(pure_literals)

def find_units(list_clauses):
    units = []
    if list_clauses == -1:
        return []
    for clause in list_clauses:
        if len(clause) == 1:
            units.append(clause[0])
    return units

def make_list_literals(list_clauses):
    all_lit = []
    for clause in list_clauses:
        for lit in clause:
            abs_lit = abs(lit)
            if abs_lit not in all_lit:
                all_lit.append(abs_lit)
    return all_lit

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

def split(list_clauses, heuristic):
    if heuristic == "Random":
        return random_heuristic(list_clauses)
    if heuristic == "DLCS":
        return DLCS(list_clauses)
    if heuristic == "MOM":
        return MOM(list_clauses)
    if heuristic == "JW_two_sided":
        return JW_two_sided(list_clauses)

def random_heuristic(list_clauses):
    len_clauses_list = len(list_clauses)
    random_int = random.randint(0, len_clauses_list - 1)
    random_clause = list_clauses[random_int]
    len_random_clause = len(random_clause)
    random_int = random.randint(0, len_random_clause - 1)
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
