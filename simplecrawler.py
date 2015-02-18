__author__ = 'Tim Carlson (dotcarls@indiana.edu)'
from random import *

small_www = [   (1,  [2]),
                (2,  [3,12]),
                (3,  [4, 8, 12]),
                (4,  [8]),
                (5,  [1]),
                (6,  [1, 2]),
                (7,  [2, 12]),
                (8,  [9, 12, 13, 14, 15]),
                (9,  [16]),
                (10, [5, 6, 7]),
                (11, [10]),
                (12, [16]),
                (13, [16]),
                (14, [16]),
                (15, [16]),
                (16, [11]) ]

def collect_statistics (www,prob,k) :
    result = [0]*len(www)
    current = randrange(1,len(www)+1)
    while k > 0 :
        result[current-1] += 1
        if random() * 100 < prob :
            current = randrange(1,len(www)+1)
        else :
            neighbors = www[current-1][1]
            current = choice(neighbors)
        k -=1
    return zip(range(1,len(www)+1),result)


def top (www) :
    d = collect_statistics(www,15,1000000)
    d.sort(key = lambda x : x[1], reverse = True)
    return d[:3]

print top(small_www)