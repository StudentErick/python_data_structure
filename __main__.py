from my_code.graph.bellman_ford import print_path
from my_code.graph.graph_list import GraphList

n = input("please input the number of node: ")
n = int(n)
G = GraphList(n)
print("input the adjacent node and weight,input -1 -1 -1 as end:")
while True:
    u, v, w = input().split(' ')
    if int(u) < 0 or int(v) < 0:
        break
    G.add_edge(int(u), int(v), int(w))

print_path(G)
# 0 1 1
# 0 2 2
# 0 6 -3
# 1 3 -1
# 2 3 3
# 3 4 2
# 3 5 4
# 4 7 -3
# 5 7 1
# 6 7 2