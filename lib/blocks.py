def get_var(r,c,v):
    return r * 81 + c * 9 + v

def calc_row(off, cell):
    row = off * 3 + cell / 3
    return row * 81

def calc_col(off, cell):
    col = off * 3 + cell % 3
    return col * 9

def definedness():
    print 'c block uniqueness'

    blocks_in_a_row = 3
    blocks_in_a_col = 3

    for r_off in range(0, blocks_in_a_row):
        for c_off in range(0, blocks_in_a_col):
            for v in range (1, 10):
                for cell in range(0, 9):
                    print str(calc_row(r_off,cell) + calc_col(c_off,cell) + v),
                print 0

def uniqueness():
    print 'c block uniqueness'

    blocks_in_a_row = 3
    blocks_in_a_col = 3

    for r_off in range(0, blocks_in_a_row):
        for c_off in range(0, blocks_in_a_col):
            for v in range (1, 10):
                for cell1 in range(0, 8):
                    for cell2 in range(cell1+1, 9):
                        print str(-1 * (calc_row(r_off,cell1) + calc_col(c_off,cell1) + v)),
                        print str(-1 * (calc_row(r_off,cell2) + calc_col(c_off,cell2) + v)),
                        print '0'
