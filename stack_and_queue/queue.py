class SQueue:
    def __init__(self):
        self._elem = []

    def is_empty(self):
        return len(self._elem) == 0

    def push(self, elem):
        self._elem.append(elem)

    def pop(self, elem):
        if self.is_empty():
            print("No elements")
        else:
            self._elem.pop(0)

    def print_all(self):
        for i in self._elem:
            print(i, end=' ')
        print('')

    def elements(self):
        for i in self._elem:
            yield i


Q = SQueue()
for i in range(10):
    Q.push(i)
print("iterator:")
for i in Q.elements():
    print(i, end=' ')
print('')
