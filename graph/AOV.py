def aov(my_graph):
    que = list()  # store node that has only one in edge
    graph = my_graph.get_graph_list()
    node_num = graph.get_node_num()
    in_edge = [0] * node_num  # store the number of in edge for every node
    for i in range(node_num):
        for node in graph[i]:
            in_edge[node.v] += 1
    for i in range(node_num):
        if in_edge[i] == 1:
            que.append(i)
    n = 0
    while len(que) > 0:
        u = que.pop(0)
        print(u, end=' ')
        n += 1
        for node in graph[u]:
            in_edge[node.v] -= 1  # number of in edge -1
            if in_edge[node.v] == 1:
                que.append(node.v)
    if n < node_num:
        print("loop in graph")
