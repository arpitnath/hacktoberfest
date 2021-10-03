#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(1, n + 1):
        print((" " * (n - i)) + ("#" * i))

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)