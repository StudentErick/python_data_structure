# naive_matching algorithm
def naive_matching(t, p):
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if p[i] == t[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1
    if i == m:
        return j - i
    return -1


print("input main string:")
t = input()
print("input substring:")
p = input()
flag = naive_matching(t, p)
if flag != -1:
    print("yes, location is {}", flag + 1)
else:
    print("no")
