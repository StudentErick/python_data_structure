def bellman_ford(Graph, start=0):
    node_num = Graph.get_node_num()
    graph = Graph.get_graph_list()
    INF = 1000000
    dist = [INF] * node_num  # store the minimize distance to start
    path = [-1] * node_num  # store the previous node in path
    for v, w in graph[start]:
        dist[v] = w
        path[v] = start
    dist[start] = 0
    for k in range(node_num):
        for v, w in graph[k]:
            if dist[k] != INF and dist[v] < dist[k] + w:
                dist[v] = dist[k] + w
                path[v] = k
    return path  # return all path


# output all path
def print_path(Graph, start=0):
    path = bellman_ford(Graph, start)
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
        for j in range(k - 1, 0, -1):
            print(shortest[j], end=' ')
        print(shortest[0])
