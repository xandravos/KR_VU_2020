def DLCS(clause_list):
    # Finding all possible literals
    literals = findliterals(clause_list)
    literals.sort()
    cp_list, cn_list, cp_cn_list = counter(clause_list, literals)
    maximum = max(cp_cn_list)
    index = cp_cn_list.index(maximum)
    CPv = cp_list[index]
    CNv = cn_list[index]
    if CPv > CNv:
        return literals[index]
    else:
        return 0 - literals[index]


def DLIS(clause_list):
    # Finding all possible literals
    literals = findliterals(clause_list)
    literals.sort()
    cp_list, cn_list, cp_cn_list = counter(clause_list, literals)

    if max(cp_list) > max(cn_list):
        index = cp_list.index(max(cp_list))
    else:
        index = cn_list.index(max(cn_list))
    cp = cp_list[index]
    cn = cn_list[index]
    if cp > cn:
        return literals[index]
    else:
        return 0 - literals[index]


def JW_onesided(clause_list):
    literals = findliterals(clause_list)
    literals.sort()

    all_J = []

    for literal in literals:
        j = 0
        for clause in clause_list:
            if literal in clause:
                j = j + (2**(0 - len(clause)))
        all_J.append(j)

    max_j = max(all_J)

    index = all_J.index(max_j)

    return literals[index]


def JW_twosided(clause_list):
    literals = findliterals(clause_list)
    literals.sort()

    all_J = []
    all_J_positief = []
    all_J_negatief = []

    for literal in literals:
        j_pos = 0
        j_neg = 0
        for clause in clause_list:
            if literal in clause:
                j_pos = j_pos + (2**(0 - len(clause)))
            elif 0 - literal in clause:
                j_neg = j_neg + (2**(0 - len(clause)))
        all_J.append(j_pos + j_neg)
        all_J_positief.append(j_pos)
        all_J_negatief.append(j_neg)

    max_j = max(all_J)

    index = all_J.index(max_j)
    if all_J_positief[index] >= all_J_negatief[index]:
        return literals[index]
    else:
        return 0 - literals[index]

def MOM(clause_list):
    lengths = []
    for clause in clause_list:
        lengths.append(len(clause))
    minimum = min(lengths)

    small_clauses = []
    for clause in clause_list:
        if len(clause) == minimum:
            small_clauses.append(clause)

    literals = findliterals(small_clauses)
    literals.sort()
    MOMs = []
    for literal in literals:
        fx = 0
        f_x = 0
        for clause in small_clauses:
            if literal in clause:
                fx = fx + 1
            if 0 - literal in clause:
                f_x = f_x + 1
        mom = (fx + f_x) * 2**2 + fx + f_x
        MOMs.append(mom)
    maximum = max(MOMs)
    index = MOMs.index(maximum)
    return literals[index]
