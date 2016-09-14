def variable(r,c,v):
    return r * 81 + c * 9 + v

def uniqueness():
    print 'c column uniqueness'
    for c in range(0, 9):
        for v in range (1, 10):
            for r1 in range(0, 8):
                for r2 in range(r1+1, 9):
                    print str(-1 * variable(r1,c,v)),
                    print str(-1 * variable(r2,c,v)),
                    print '0'

def definedness():
    print 'c column definedness'
    for col in range(0, 9):
        for value in range(1,10):
            for row in range(0,9):
                print str(variable(row,col,value)),
            print '0'
