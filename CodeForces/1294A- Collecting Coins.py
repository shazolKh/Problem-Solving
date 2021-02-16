import sys
import bisect as bi
import math
from collections import defaultdict as dd
import heapq
import itertools

input = sys.stdin.readline
from random import randint

## import numpy as np
sys.setrecursionlimit(10 ** 7)
mo = 10 ** 9 + 7


def cin():
    return map(int, sin().split())


def ain():
    return list(map(int, sin().split()))


def sin():
    return input()


def inin():
    return int(input())


for _ in range(inin()):
    a, b, c, n = cin()
    if (a + b + c + n) % 3 == 0:
        if (a + b + c + n) // 3 >= max(a, b, c):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
