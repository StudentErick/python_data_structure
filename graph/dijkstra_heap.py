from heapq import *


def dijkstra(Graph, start=0):
    num_node = Graph.get_node_num()
    graph = Graph.get_graph_list()
    INF = 1000000
    dist = [INF] * num_node
    path = [-1] * num_node
    S = [0] * num_node
    vis = [False] * num_node
    S[start] = 1
    for node in graph[start]:
        dist[node.v] = node.w
        path[node.v] = start
    dist[start] = 0
    path[start] = start
    Q = [(dist[start], start, 0)]
    heapify(Q)
    while len(Q) > 0:
        tmp = heappop(Q)
        u = tmp[1]
        if vis[u] is True:
            continue
        vis[u] = True
        for node in graph[u]:
            v = node.v
            w = node.w
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                path[v] = u
                heappush((dist[v], v, w))
    return path
