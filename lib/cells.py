def variable(r,c,v):
    return r * 81 + c * 9 + v

def definedness():
    print 'c cell definedness'
    for row in range(0, 9):
        for col in range(0, 9):
            for value in range (1, 10):
                print str(variable(row,col,value)),
            print '0'
