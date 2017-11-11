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

def kruskal(Graph):
    node_num = Graph.get_node_num()
    edge_num = Graph.get_edge_num()
    graph = Graph.get_graph_list()
    edges = []
    for i in range(node_num):
        for node in graph[i]:
            edges.append([i, node.v, node.w])

