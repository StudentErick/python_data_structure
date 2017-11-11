class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LCList:
    def __init__(self):
        self._head = None
        self._rear = None

    def is_empty(self):
        return self._head is None and self._rear is None

    def prepend(self, elem):  # insert from head
        if self.is_empty():
            self._head = LNode(elem)
            self._rear = self._head
        else:
            p = LNode(elem)
            p.next = self._head
            self._head = p
            self._rear.next = p

    def append(self, elem):  # insert from rear
        if self.is_empty():
            self._head = LNode(elem)
            self._rear = self._head
        else:
            p = LNode(elem)
            self._rear.next = p
            self._rear = p
            self._rear.next = self._head

    def pop(self):  # delete from head
        if self.is_empty():
            print("empty list")
        elif self._head.next is self._rear:  # only one element
            e = self._head.elem
            self._head = None
            self._rear = None
            return e
        else:
            e = self._head.elem
            self._head = self._head.next
            self._rear.next = self._head
            return e

    def pop_last(self):  # delete from rear
        if self.is_empty():
            print("empty list")
        elif self._head.next is self._rear:  # only one element
            e = self._head.elem
            self._head = None
            self._rear = None
            return e
        else:
            e = self._rear.elem
            p = self._head
            while p.next is not self._rear:
                p = p.next
            p.next = self._head
            self._rear = p

    def print_all(self):  # output all elements
        p = self._head
        print(p.elem, end=' ')
        p = p.next
        while p is not self._head:
            print(p.elem, end=' ')
            p = p.next
        print('')

    def elements(self):  # iterator
        if self.is_empty():
            return None
        p = self._head
        yield p.elem
        p = p.next
        while p is not self._head:
            yield p.elem
            p = p.next


lclist = LCList()  # 注意，定义类后边需要增加括号
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
