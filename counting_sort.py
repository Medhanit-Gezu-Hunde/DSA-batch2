import math
import os
import random
import re
import sys

def countingSort(arr):
    # Initialize frequency array with zeros
    frequency = [0] * 100  # Since 0 ≤ arr[i] < 100

    # Count the frequency of each number in the input array
    for num in arr:
        frequency[num] += 1

    return frequency

if name == 'main':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().strip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)) + '\n')
    fptr.close()
