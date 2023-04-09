#!/bin/python3
 
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
 
if n % 2 == 1:
    # n is odd
    print("Weird")
elif n in range(2,6):
    # n is even and in the range of 2 to 5 (inclusive)
    print("Not Weird")
elif n in range(6,21):
    # n is even and in the range of 6 to 20 (inclusive)
    print("Weird")
else:
    # n is even and greater than 20
    print("Not Weird")
