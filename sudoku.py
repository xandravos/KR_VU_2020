import numpy as np

options = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def find_region(l):
    r_region = np.floor(l[0]/3)
    c_region = np.floor(l[1]/3)
    region = r_region * c_region

def region_vals(r, s):
    v = []
    for r in len(s):
        for c in len(s):
            if find_region([r, c]) == r:
                v.append(s[c][r])

    return v

def find_val(l, s, p=0):
    l_region = find_region(l)

    row_vals = s[l[0]]
    column_vals = s[:,l[1]]
    region_vals = region_vals(l_region, s)

    for i in options:
        if i not in row_vals and i not in column_vals and i not in region_vals and i != p:
            return i
        else:
            return 0

def solve(s, l=None, p=None, edited=[]):
    if not edited and p == 9:
        return False

    if l and p:
        x = find_val(l, s, p)
        if x != 0:
            s[l[1]][l[0]] = s
            return s
        else:
            return solve(s, edited[-1])

    for r in range(len(s)):
        for c in range(len(s)):
            if s[c][r] in options:
                continue
            else:
                x = find_val([r, c], s)
                if x != 0:
                    s[c][r] = x
                else:
