#implementation of Depth-Frist Search algorithm for solving the maze

from collections import deque


def solve(s, e,maze):
    start = s
    end = e

    stack = deque([start])
    visited = []
    prev = []
    count = 0

    while stack:
        count += 1
        current =  stack.pop()

        if current == end:
            break
        
        visited.append(current)

        for n in maze[current]:
            if n != None:
                if n not in visited:
                    stack.append(n)
                    prev.append(current)


    path = []
    
    for i in prev:
        if i not in path:
            path.append(i)

    path.append(end)


    return path


