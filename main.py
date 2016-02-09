#!/usr/bin/env python3

import sys
import hashcode

if __name__ == '__main__':
    data = hashcode.read_image_description(sys.argv[1])
    solver = hashcode.LinearSolver(data)

    op_list = solver.print_by_row()
    [print(op) for op in op_list]
    print('''Eseguite %d operazioni''' % len(op_list))


    # op_list = solver.print_by_column()
    # [print(op) for op in op_list]
    # print('''Eseguite %d operazioni''' % len(op_list))