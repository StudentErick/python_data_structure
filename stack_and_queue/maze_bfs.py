import random

# 4 directions
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# size of maze is 10*10, and 0 is ok to pass while 1 cannot, generate in random
maze = [[random.randint(-1, 0) for i in range(10)] for i in range(10)]

# if a block is visited, its flag will be 1
visited = [[0 for i in range(10)] for i in range(10)]


class Node:
    def __init__(self, x_=0, y_=0):
        self.x = x_
        self.y = y_


def bfs(my_maze, start, end):
    my_maze[start.x][start.y] = 0
    my_maze[end.x][end.y] = 0
    Q = []
    tmp = start
    Q.append(start)
    visited[start.x][start.y] = 1
    while len(Q) != 0:
        tmp = Q.pop(0)
        for i in range(4):
            x = tmp.x + dirs[i][0]
            y = tmp.y + dirs[i][1]
            if 0 <= x < 10 and 0 <= y < 10 and my_maze[x][y] == 0 and visited[x][y] == 0:
                visited[x][y] = 1
                t = Node(x, y)
                Q.append(t)
                my_maze[x][y] = my_maze[tmp.x][tmp.y] + 1
                if x == end.x and y == end.y:
                    print("find")
                    return True, my_maze
    print("No way")
    return False, my_maze


def path(maze, start, end):
    x = end.x
    y = end.y
    dis = maze[x][y]
    print(x, y)
    while x != start.x or y != start.y:
        for i in range(4):
            x1 = x + dirs[i][0]
            y1 = y + dirs[i][1]
            if 0 <= x1 < 10 and 0 <= y < 10 and maze[x1][y1] == dis - 1 and maze[x1][y1] > 0:
                dis -= 1
                print(x1, y1)
                x = x1
                y = y1
                break


start = Node(0, 0)
end = Node(3, 3)
flag, maze = bfs(maze, start, end)
for i in range(10):
    print(maze[i])
if flag:
    path(maze, start, end)
