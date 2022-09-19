# implementation of Breadth First Search algorithm for solving the maze

from collections import deque


def solve(s, e, maze):
    start = s
    end = e

    queue = deque([start])
    visited = [start]
    prev = [start]

    count = 0
    solved = False

    while queue:
        count += 1

        current  = queue.pop()

        if current == end:
            solved = True
            break

        for n in maze[current]:
            if n != None:
                if n not in visited:
                    queue.append(n)
                    visited.append(n)
                    prev.append(current)

    path = []
    
    for i in prev:
        if i not in path:
            path.append(i)
    path.append(end)
        


    return path
    




    


    