#!/usr/bin/env python3

import sys
import hashcode

col =0
row=0

if __name__ == '__main__':
    data = hashcode.read_image_description(sys.argv[1])
    nr_command = 0
    list_command = ''
    for line in data:
        col = 0
        while col < (len(line)-1):
            if line[col]=='#':
                starter_col = col
                while col < (len(line)) and line[col]=='#' :
                    col = col +1
                if(starter_col==(col-1)):
                    nr_command = nr_command +1
                    list_command = list_command +'PAINT_SQUARE '+str(row)+' '+str(col-1)+' 0\n'
                else:
                    nr_command = nr_command +1
                    list_command = list_command +'PAINT_LINE '+str(row)+' '+str(starter_col)+' '+str(row)+' '+str(col-1)+'\n'

            else:
                col =col+1
        row =row+1
    print(str(nr_command))
    print(list_command)