import re
from .utils import *


class LinearSolver:
    multiple_cell_expression = '#{1,}'

    def __init__(self, image):
        self.image = image

    def print_by_row(self):
        op_list = []
        for index, row in enumerate(self.image):
            op_list = op_list + self.__print_row(row, index)
        return op_list

    def print_by_column(self):
        op_list = []
        for col_index in range(1,len(self.image[0])):
            col = []
            for row in self.image:
                for c,e in enumerate(row):
                    if c == col_index:
                        col.append(e)
            op_list = op_list + self.__print_row(col, col_index)
        return op_list

    def __print_row(self, row, index):
        op_list = []
        string_line = ''.join(row)

        for m in re.finditer(self.multiple_cell_expression, string_line):
            op_list.append(line_instruction(index, m.start(), index, m.end() - 1))

        return op_list

    def __print_column(self, col, index):
        op_list = []
        string_line = ''.join(col)

        for m in re.finditer(self.multiple_cell_expression, string_line):
            op_list.append(line_instruction(m.start(), index, m.end() - 1, index))

        return op_list
