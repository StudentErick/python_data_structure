from heapq import *

ls = [[1, 4], [3, 3], [5, 2], [4, 1]]
heapify(ls)
while len(ls) > 0:
    print(heappop(ls))
