#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    
    primary_diag_sum = 0
    secondary_diag_sum = 0
    
    for i in range(n):
        primary_diag_sum += arr[i][i]
        secondary_diag_sum += arr[i][n - 1 - i]
    
    dif = abs(primary_diag_sum - secondary_diag_sum)
    
    return dif
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()