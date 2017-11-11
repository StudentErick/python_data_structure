class GraphError(ValueError):
    pass


class Node:
    def __init__(self, v_=0, w_=0):
        self.v = v_
        self.w = w_


class GraphList:
    def __init__(self, vnum=0):  # vnum is the number of vertex
        self._vnum = vnum
        self._enum = 0
        self._list = [[] for i in range(self._vnum)]
        self._vis = [False for i in range(vnum)]

    def get_graph_list(self):
        return self._list

    def get_node_num(self):
        return self._vnum

    def get_edge_num(self):
        return self._enum

    def add_edge(self, vi, vj, w):
        if vi < 0 or vi > self._vnum or vj < 0 or vj > self._vnum:
            raise GraphError("wrong node" + str(vi) + "or" + str(vj))
        self._list[vi].append(Node(vj, w))
        self._enum += 1

    def print_all(self):  # output all info in graph
        for i in range(self._vnum):
            print("node=%d: " % i)
            for node in self._list[i]:
                print("(v=%d,w=%d) " % (node.v, node.w))
            print('')

    def dfs(self, start):
        if self._vis[start] is True:
            return
        print(start)
        self._vis[start] = True
        for node in self._list[start]:
            if self._vis[node.v] is False:  # this node has not been visited
                self.dfs(node.v)

    def bfs(self, start):
        Q = list()
        Q.append(start)
        self._vis[start] = True
        while len(Q) > 0:
            front = Q.pop(0)
            print(front)
            for node in self._list[front]:
                if self._vis[node.v] is False:
                    Q.append(node.v)
                    self._vis[node.v] = True


# G = GraphList(5)
# while True:
#     u, v, w = input().split(' ')
#     if int(u) < 0 or int(v) < 0:
#         break
#     G.add_edge(int(u), int(v), int(w))
# # G.print_all()
# G.bfs(0)
