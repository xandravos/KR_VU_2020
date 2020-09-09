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
