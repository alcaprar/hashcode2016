import re
from .utils import *

class LinearSolver:
    single_cell_expression = '(\.#\.){1,1}'
    multiple_cell_expression = '(\.[#]{2,}\.)'

    def __init__(self, image):
        self.image = image

    def print_by_row(self):
        op_list = []
        for index, row in enumerate(self.image):
            op_list = op_list + self.__print_row(row, index)
        return op_list

    def print_by_column(self):
        pass
        # for index, col in enumerate(self.image.transpose()):
        #     op_list = []
        #     op_list = op_list + self.__print_row(col, index)
        # return op_list

    def __print_row(self, row, index):
        op_list = []
        string_line = ''.join(row)

        for m in re.finditer(self.single_cell_expression, string_line):
            op_list.append(square_instruction(index, m.start() + 1, 0))
        for m in re.finditer(self.multiple_cell_expression, string_line):
            op_list.append(line_instruction(index, m.start() + 1, index, m.end() - 1))

        return op_list

    def __print_column(self, col, index):
        op_list = []
        string_line = ''.join(col)

        for m in re.finditer(self.single_cell_expression, string_line):
            op_list.append(square_instruction(m.start() + 1, index, 0))
        for m in re.finditer(self.multiple_cell_expression, string_line):
            op_list.append(line_instruction(m.start() + 1, index, m.end() - 1, index))

        return op_list