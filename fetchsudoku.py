#!/usr/bin/python
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print "Usage: "+sys.argv[0]+" difficulty_level"
        sys.exit(2)

    r = requests.get('http://www.thonky.com/sandbox/new-sudoku/ThonkySudokuJavascript.js?puzzle_id=&difficulty='+sys.argv[1])
    if r.status_code != requests.codes.ok:
        print "ERROR"
        exit(2)
    print r.text.split()[3][1:-2]

if __name__ == "__main__":
    main()
