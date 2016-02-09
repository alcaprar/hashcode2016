def read_image_description(filename):
    """
    :param filename:
    :return:
    """
    f = open(filename, 'r')
    header = f.readline()
    (rows, cols) = header.strip('\n').split(' ')
    content = f.readlines()
    data = []
    for row, line in enumerate(content):
        data.append([])
        for char in line.strip('\n'):
            data[row].append(char)
    return data

def square_instruction(r, c, s):
    return ('''PAINT_SQUARE %d %d %d''' % (r, c, s))

def line_instruction(r1, c1, r2, c2):
    return ('''PAINT_LINE %d %d %d %d''' % (r1, c1, r2, c2))