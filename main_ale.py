#!/usr/bin/env python3

import sys
import hashcode

row =0
col = 0
def check_row():
    global row
    global col

    starter_col = col

    col =+1
    while col=='#':
        col=+1

    if(starter_col==(col-1)):
        print('PAINT_SQUARE '+str(row)+' '+str(starter_col)+' 0')
    else:
        last_col = col-1
        print('PAINT_LINE '+str(row)+' '+str(starter_col)+' '+str(row)+' '+str(last_col))
    return

if __name__ == '__main__':
    data = hashcode.read_image_description(sys.argv[1])
    global col
    global row
    for line in data:
        for char in line:
            if char=='#':
                check_row()
            else:
                col +=1
        row +=1