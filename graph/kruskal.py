class UnionSet:
    def __init__(self, num=0):
        self._num = num
        self._par = [-1 for i in range(num)]

    def find(self, x):  # find root and compress path
        s = x
        while self._par[s] >= 0:
            s = self._par[s]
        while s != x:
            tmp = self._par[x]
            self._par[x] = s
            x = tmp
        return s

    def union(self, x, y):
        r1 = self.find(x)
        r2 = self.find(y)
        if r1 == r2:  # r1 r2 are in same set, cannot uniioin
            return
        n = self._par[r1] + self._par[r2]
        if self._par[r1] < self._par[r2]:
            self._par[r2] = r1
            self._par[r1] = n
        else:
            self._par[r1] = r2
            self._par[r2] = n


def kruskal(Graph):
    node_num = Graph.get_node_num()
    # edge_num = Graph.get_edge_num()
    graph = Graph.get_graph_list()
    edges = []
    for i in range(node_num):
        for node in graph[i]:
            edges.append([i, node.v, node.w])
    edges.sort(key=lambda p: p[2])  # sorted by weight of edges
    union = UnionSet(node_num)
    w = 0
    n = 0
    k = 0
    for edge in edges:
        if union.find(edge[0]) != union.find(edge[1]):
            w += edge[2]
            union.union(edge[0], edge[1])
            k += 1
        if k == node_num - 1:  # there node_num-1 edges in MST
            break
    return w
