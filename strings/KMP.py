# find next array
def gen_pnext(p):
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m  # initialize array elements to -1
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext


# matching algorithm
def matching_KMP(t, p, pnext):
    i, j = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            i, j = i + 1, j + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    else:
        return -1


print("input main string:")
t = input()
print("input substring:")
p = input()
arr = gen_pnext(p)
flag = matching_KMP(t, p, arr)
if flag != -1:
    print("yes, location is {}", flag + 1)
else:
    print("no")
