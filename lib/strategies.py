def variable(r,c,v):
    return r * 81 + c * 9 + v

def row_to_column():
    print 'c row_to_column'
    for r1 in range(0,9):
        for c in range(0,9):
            for v in range(1,10):
                for r2 in filter(lambda x: x != r1, range(0,9)):
                    print str(-1 * variable(r2,c,v)),
                    print str(-1 * variable(r1,c,v)),
                    print '0'

def column_to_row():
    print 'c column_to_row'
    for c1 in range(0,9):
        for r in range(0,9):
            for v in range(1,10):
                for c2 in filter(lambda x: x != c1, range(0,9)):
                    print str(-1 * variable(r,c1,v)),
                    print str(-1 * variable(r,c2,v)),
                    print '0'

 
