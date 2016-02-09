#!/usr/bin/env python3

import sys
import hashcode

if __name__ == '__main__':
    data = hashcode.read_image_description(sys.argv[1])
    solver = hashcode.LinearSolver(data)

    row_op = solver.print_by_row()
    col_op = solver.print_by_column()
    if len(row_op) < len(col_op):
        ops = row_op
    else:
        ops = col_op

    print(len(ops))
    [print(op) for op in ops]