# we usually use list to represent tree in python. Remember that !!!
class BTree:
    def __init__(self):
        self._root = None
        self._num = 0  # number of nodes

    def _create(self):  # create a binary tree
        x = input()
        if x == "-1":
            return None
        root = list()  # create an empty  list
        root.append(x)  # we need to use append here
        self._num += 1  # number +1
        root.append(self._create())
        root.append(self._create())
        # can not use index in a empty list
        return root

    def create(self):
        self._root = self._create()

    def _pre_order(self, root):
        if root is None:
            return
        print(root[0])
        self._pre_order(root[1])
        self._pre_order(root[2])

    def pre_order(self):
        self._pre_order(self._root)

    def _in_order(self, root):
        if root is None:
            return
        self._in_order(root[1])
        print(root[0])
        self._in_order(root[2])

    def in_order(self):
        self._in_order(self._root)

    def _post_order(self, root):
        if root is None:
            return
        self._post_order(root[1])
        self._post_order(root[2])
        print(root[0])

    def post_order(self):
        self._post_order(self._root)

    def _high(self, root):
        if root is None:
            return 0
        else:
            l_high = self._high(root[1]) + 1
            r_high = self._high(root[2]) + 1
            return max(l_high, r_high)

    def high(self):
        return self._high(self._root)

    def get_nodes(self):
        return self._num

    def bfs(self):
        Q = list()
        Q.append(self._root)
        while len(Q) != 0:
            t = Q.pop(0)
            print(t[0])
            if t[1] is not None:
                Q.append(t[1])
            if t[2] is not None:
                Q.append(t[2])


tree = BTree()
print("input node:")
tree.create()
print("first order")
tree.pre_order()
print("in order")
tree.in_order()
print("post")
tree.post_order()
print("height:")
print(tree.high())
print("number of nodes:")
print(tree.get_nodes())
print("level order")
tree.bfs()
