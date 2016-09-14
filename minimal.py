#!/usr/bin/python
import sys
from lib.utils import *
from lib import cells, rows, columns, blocks

def count_clauses(givens):
    givens = filter(lambda x: x != '.', givens)
    cellD = 81
    rowU = 9 * 9 * 36
    colU = rowU
    blockU = rowU
    return len(givens) + cellD + rowU + colU + blockU

def main():
    if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" 'sudoku_instance_string'"
        print "Example: '....8.5....3.1.86.16.....7.....79.8..3.4..9.......6....5......44..1......72.3..1.'"
        sys.exit(2)
    givens = list(sys.argv[1])

    if len(givens) < 81:
        print "Error: String too short"
        sys.exit(2)
    if len(givens) > 81:
        print "Error: String too long"
        sys.exit(2)

    print_prelude(count_clauses(givens))

    cells.definedness()
    rows.uniqueness()
    columns.uniqueness()
    blocks.uniqueness()

    # redundant extensions
    cells.uniqueness()
    rows.definedness()
    columns.definedness()
    blocks.definedness()

    print_givens(givens)
    print '0'

if __name__ == "__main__":
    main()
