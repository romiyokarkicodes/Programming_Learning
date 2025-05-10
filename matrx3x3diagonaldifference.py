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
    leng = len(arr)
    count =len(arr)-1
    sum1 =0
    sum2 =0
    for i in range(0,leng):
        
        for j in range(0,len(arr[i])):
            if(j ==i):
                sum1 += arr[i][j]
                print(sum1)
            if (count ==j):
                sum2 += arr[i][j]
                print(sum2)
        count = count -1 
    return abs(sum1-sum2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
