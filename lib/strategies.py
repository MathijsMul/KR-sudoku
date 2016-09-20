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
                    
