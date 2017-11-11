from heapq import heappush, heappop, heapify
from collections import defaultdict


# In this code, we use list to represent a huffman tree. We usually use list to represent tree in python
def encode(symb2freq):
    # in [sym, ""], "" represents an empty list
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        # [lo[0] + hi[0]] + lo[1:] + hi[1:] becomes a new huffman tree
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


txt = input("please input your txt:")
symb2freq = defaultdict(int)
for ch in txt:
    symb2freq[ch] += 1
huff = encode(symb2freq)
print("Symbol\tWeight\tHuffman Code")
for p in huff:
    print("%s\t\t%s\t\t%s" % (p[0], symb2freq[p[0]], p[1]))
