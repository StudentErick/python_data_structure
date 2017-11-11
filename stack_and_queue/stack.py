class StackUnderflow(ValueError):
    pass


class SStack:  # implement a stack based on sequence list
    def __init__(self):
        self._elem = []  # store elements in list object

    def is_empty(self):
        return self._elem is []

    def top(self):
        if self._elem is []:
            raise StackUnderflow
        return self._elem[-1]

    def push(self, elem):
        self._elem.append(elem)

    def pop(self):
        if self._elem is []:
            raise StackUnderflow
        return self._elem.pop()

    def size(self):
        return len(self._elem)


def check_patterns(text):
    patterns = "()[]{}"
    open_patterns = "([{"
    opposite = {")": "(", "]": "[", "}": "{"}

    def parentheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in patterns:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_patterns:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print("Can not match is found at", i, "for", pr)
            return False
    if st.is_empty() is False:
        print("No")
    else:
        print("Match")
    return True


print("input text")
text = input()
check_patterns(text)
