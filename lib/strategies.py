import itertools

def variable(r,c,v):
    return r * 81 + c * 9 + v

def complete_row():
    print 'c complete_row'
    for r in range(0,9):
        for c1 in range(0,9):
            other_columns = filter(lambda x: x != c1, range(0,9))
            for v in range(1,10):
                other_values = filter(lambda x: x != v, range(1,10))
                perms = itertools.permutations(other_values)
                for permutation in perms:
                    #print(permutation)
                    count = 0
                    for value in permutation:
                        print str(-1 * variable(r,other_columns[count],value)),
                        count += 1
                    print str(variable(r,c1,v)),
                    print '0'

def naked_twins_by_row():
    print 'c naked twins by row'
    for r in range(0,9):
        for c1 in range(0, 8):
            for c2 in range(c1+1, 9):
                other_columns = filter(lambda x: x != c1 and x != c2, range(0,9))
                for v1 in range(1, 9):
                    for v2 in range(v1+1, 10):
                        other_values = filter(lambda x: x != v1 and x != v2, range(1,10))
                        for c3 in other_columns:
                            for v3 in other_values:
                                print str(variable(r,c1,v3)),
                                print str(variable(r,c2,v3)),
                            print str(-1* variable(r,c3,v1)),0

                            for v3 in other_values:
                                print str(variable(r,c1,v3)),
                                print str(variable(r,c2,v3)),
                            print str(-1* variable(r,c3,v2)),0

def naked_twins_by_col():
    print 'c naked twins by column'
    for c in range(0,9):
        for r1 in range(0, 8):
            for r2 in range(r1+1, 9):
                other_rows = filter(lambda x: x != r1 and x != r2, range(0,9))
                for v1 in range(1, 9):
                    for v2 in range(v1+1, 10):
                        other_values = filter(lambda x: x != v1 and x != v2, range(1,10))
                        for r3 in other_rows:
                            for v3 in other_values:
                                print str(variable(r1,c,v3)),
                                print str(variable(r2,c,v3)),
                            print str(-1* variable(r3,c,v1)),0

                            for v3 in other_values:
                                print str(variable(r1,c,v3)),
                                print str(variable(r2,c,v3)),
                            print str(-1* variable(r3,c,v2)),0
