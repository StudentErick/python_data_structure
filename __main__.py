from my_code.graph.kruskal import kruskal
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

t = kruskal(G)
print("The MST is: %d" % t)
# 0 1 2
# 0 2 2
# 1 2 6
# 1 4 1
# 1 2 6
# 2 3 1
# -1 -1 -1
