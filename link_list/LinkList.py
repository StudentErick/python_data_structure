# 定义结点类型
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


# 定义链表结构
class LList:
    def __init__(self):  # 初始化
        self._head = None

    def is_empty(self):  # 是否为空
        return self._head is None

    def prepend(self, elem):  # 从表头插入元素
        self._head = LNode(elem, self._head)

    def pop(self):  # 删除表头元素
        if self.is_empty():
            print("no elements in list")
            return
        e = self._head.elem
        self._head = self._head.next

    def append(self, elem):  # 表尾添加元素
        if self.is_empty():
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):  # 删除表尾元素
        if self.is_empty():
            print("No element in list")
        p = self._head
        while p.next is not None:
            p = p.next
        e = p.elem
        p = None
        return e

    def print_all(self):  # 输出所有元素
        p = self._head
        while p is not None:
            print(p.elem, end='')
            p = p.next
        print('')

    def elements(self):  # 迭代器
        p = self._head
        while p is not None:
            yield p.elem  # 注意yield的使用
            p = p.next

    def find(self, pred):  # 查找指定元素
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next


mylist = LList()  # 注意，定义类后边需要增加括号
for i in range(10):
    mylist.prepend(i)

print("list elements are:")
for elem in mylist.elements():
    print(elem, end=' ')
print('')
