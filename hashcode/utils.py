def read_image_description(filename):
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