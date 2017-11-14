def SPFA(Graph, start=0):
    num_node = Graph.get_node_num()
    graph = Graph.get_graph_list()
    INF = 1000000
    dist = [INF] * num_node  # store the minimize distance to start
    path = [-1] * num_node  # store the previous node in path
    inq = [0] * num_node  # sign of whether node is in queue
    for node in graph(start):
        dist[node.v] = node.w
        path[node.v] = start
    dist[start] = 0
    path[start] = start
    inq[start] += 1
    Q = [start]
    while len(Q) > 0:
        u = Q.pop(0)
        inq[u] -= 1
        for node in graph[u]:
            v = node.v
            w = node.w
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
                if inq[v] == 0:
                    inq[v] += 1
                    Q.append(v)
    return path


# output all path
def print_path(Graph, start=0):
    path = SPFA(Graph, start)
    num_node = Graph.get_node_num()
    for i in range(num_node):
        if i == start:
            continue
        k = 0
        shortest = [start] * num_node
        shortest[k] = i
        while path[shortest[k]] != start:
            shortest[k + 1] = path[shortest[k]]
            k += 1
        shortest[k + 1] = start
        for j in range(k + 1, 0, -1):
            print(shortest[j], end=' ')
        print(shortest[0])
