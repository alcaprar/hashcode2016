#!/usr/bin/env python3

import sys
import hashcode

if __name__ == '__main__':
    data = hashcode.read_image_description(sys.argv[1])
    [print(line) for line in data]