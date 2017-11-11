# definition of double link node
class DLNode:
    def __init__(self, elem, pre_=None, next_=None):
        self.elem = elem
        self.pre = pre_
        self.next = next_


# definition of double link list
class DLList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):  # insert element from head
        if self.is_empty():
            self._head = DLNode(elem)
        else:
            p = DLNode(elem)
            p.next = self._head
            self._head.pre = p
            self._head = p

    def append(self, elem):  # insert element in rear
        if self.is_empty():
            self._head = DLNode(elem)
        else:
            p = self._head
            while p.next is not None:
                p = p.next
            t = DLNode(elem)
            p.next = t

    def pop_last(self):  # delete element from rear
        if self.is_empty():
            print("No elements in list")
        else:
            p = self._head
            while p.next is not None:
                p = p.next
            e = p.elem
            p = None
            return e

    def pop(self):  # delete element from head
        if self.is_empty():
            print("No elements in list")
        else:
            e = self._head.elem
            self._head = self._head.next

    def print_all(self):  # output all elements
        if self.is_empty():
            print("empty list!")
        else:
            p = self._head
            while p is not None:
                print(p.elem, end=' ')
                p = p.next
            print('')

    def elements(self):  # iterator
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next


lclist = DLList()  # 注意，定义类后边需要增加括号
for i in range(10):
    lclist.prepend(i)

print("iterator:")
for elem in lclist.elements():
    print(elem, end=' ')
print('')
print("print test")
lclist.print_all()
print("append rear")
lclist.append(-1)
lclist.print_all()
print("append head")
lclist.prepend(10)
lclist.print_all()
print("delete head")
lclist.pop()
lclist.print_all()
print("delete rear")
lclist.pop_last()
lclist.print_all()
print('')
