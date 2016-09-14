def variable(r,c,v):
    return r * 81 + c * 9 + v

def definedness():
    print 'c cell definedness'
    for row in range(0, 9):
        for col in range(0, 9):
            for value in range (1, 10):
                print str(variable(row,col,value)),
            print '0'

def uniqueness():
    print 'c cell uniqueness'
    for row in range(0, 9):
        for col in range(0, 9):
            for value_1 in range(1,9):
                for value_2 in range(value_1 + 1, 10):
                    print str(-1 * variable(row,col,value_1)),
                    print str(-1 * variable(row,col,value_2)),
                    print '0'
