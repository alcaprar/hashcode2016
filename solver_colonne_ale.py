#!/usr/bin/env python3

import sys
import hashcode

col =0
row=0

if __name__ == '__main__':
    data = hashcode.read_image_description(sys.argv[1])
    nr_command = 0
    list_command = ''
    max_row = len(data)
    max_col = len(data[0])
    while col < max_col:
        row = 0
        while row < max_row:
            if data[row][col]=='#':
                starter_row= row
                while row < max_row and data[row][col]=='#':
                    row = row +1
                if(starter_row==(row-1)):
                    nr_command = nr_command +1
                    list_command = list_command +'PAINT_SQUARE '+str(row-1)+' '+str(col)+' 0\n'
                else:
                    nr_command = nr_command +1
                    list_command = list_command +'PAINT_LINE '+str(starter_row)+' '+str(col)+' '+str(row-1)+' '+str(col)+'\n'
            else:
                row = row+1
        col = col +1
    print(str(nr_command))
    print(list_command)