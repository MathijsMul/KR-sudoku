def variable(r,c,v):
    return r * 81 + c * 9 + v

def uniqueness():
    print 'c row uniqueness'
    for r in range(0, 9):
        for v in range (1, 10):
            for c1 in range(0, 8):
                for c2 in range(c1+1, 9):
                    print str(-1 * variable(r,c1,v)),
                    print str(-1 * variable(r,c2,v)),
                    print '0'
