from code.graph.graph_list import GraphList

n = input("please input the number of node: ")
n = int(n)
G = GraphList(n)
print("input the adjacent node and weight,input -1 -1 -1 as end:")
while True:
    u, v, w = input().split(' ')
    if int(u) < 0 or int(v) < 0:
        break
    G.add_edge(int(u), int(v), int(w))


def prim(Graph, start=0):
    node_num = Graph.get_node_num()
    edge_num = Graph.get_edge_num()
    graph = Graph.get_graph_list()
    sum = 0
    INF = 100000
    lowcost = [INF] * node_num
    MST = [False] * node_num
    MST[start] = True
    for node in graph[start]:
        lowcost[node.v] = node.w
    for k in range(node_num - 1):
        mini_node = -1
        mini_edge = INF
        for i in range(node_num):
            if MST[i] is False and mini_edge > lowcost[i]:
                mini_node = i
                mini_edge = lowcost[i]
        sum += mini_edge
        MST[mini_node] = True
        for node in graph[mini_node]:
            if MST[node.v] is False and lowcost[node.v] > node.w:
                lowcost[node.v] = node.w
    return sum


t = prim(G)
print("The MST is: %d" % t)
# 0 1 2
# 0 2 2
# 1 2 6
# 1 4 1
# 1 2 6
# 2 3 1
# -1 -1 -1
