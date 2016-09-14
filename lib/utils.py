def variable(r,c,v):
    return r * 81 + c * 9 + v


def print_givens(givens):
    for i, v in enumerate(givens):
        if v == '.':
            continue

        row = i / 9
        col = i % 9
        print str(variable(row, col, int(v))), 0

def print_prelude(clauses_num):
    print 'p cnf 729 ' + str(clauses_num)
