class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree:
    def __init__(self):
        self._root = None
        self._num = 0

    def _create(self):
        x = int(input())
        if x == -1:
            return None
        root = Node(x)
        self._num += 1
        root.left = self._create()
        root.right = self._create()
        return root

    def create(self):
        self._root = self._create()

    def _pre_order(self, root):
        if root is None:
            return
        print(root.data)
        self._pre_order(root.left)
        self._pre_order(root.right)

    def pre_order(self):
        self._pre_order(self._root)

    def _in_order(self, root):
        if root is None:
            return
        self._in_order(root.left)
        print(root.data)
        self._in_order(root.right)

    def in_order(self):
        self._in_order(self._root)

    def _post_order(self, root):
        if root is None:
            return
        self._post_order(root.left)
        self._post_order(root.right)
        print(root.data)

    def _height(self, root):
        if root is None:
            return 0
        return max(self._height(root.left) + 1, self._height(root.right) + 1)

    def height(self):
        return self._height(self._root)

    def ger_num(self):
        return self._num

    def bfs(self):
        Q = list()
        Q.append(self._root)
        while len(Q) != 0:
            t = Q.pop(0)
            print(t.data)
            if t.left is not None:
                Q.append(t.left)
            if t.right is not None:
                Q.append(t.right)


tree = BTree()
print("input node:")
tree.create()
print("pre_order:")
tree.pre_order()
print("height:")
print(tree.height())
print("node number:")
print(tree.ger_num())
