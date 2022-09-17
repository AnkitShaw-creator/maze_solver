"""
Here we need to create a graph out of the 2D array or the maze(depends)
Key notes:
1. starting and ending of a corrodor should be treated as a node
2. if a path is connect to other paths in more than 2 direction then it should be treated as node
3. start and end should be also treated as nodes
4. Graph could be created using dictionary with key being it s coordinates and value being a list of nodes it is connected to
5. There wont be any weights on the edges, so each node will have only 1 as its weight
"""

from collections import defaultdict
from turtle import width


class Maze:
    """class node:

        def __init__(self, position):
            self.position = position
            self.neighbour = [None, None, None, None]"""
    
    def __init__(self, arr):
        self.width = len(arr[0])
        self.height = len(arr)
        self.start = (0,arr[0].index(1))
        self.end = (len(arr)-1, arr[-1].index(1))
        self._maze = arr

    def create_graph(self):
        count = 1 # count the no of nodes created (can be used to increase the efficiency), 1 as the first node is the starting node
        a = self._maze
        graph = defaultdict()
        graph[self.start] = [None, None, None,(1, self.start[1])]
        
        upnode = [None]*self.width # buffer for connecting to nodes at the top
        upnode[self.start[1]] = self.start
        for i in range(1,self.height-1):
            prev = False
            cur = False
            next = a[i][1]>0
            leftnode = None
            
            for j in range(1,self.width-1):
                prev = cur
                cur = next
                next = a[i][j+1] > 0
                
                if cur == False:
                    # hit the wall
                    continue
 
                # create nodes  only if:
                # path path path
                # wall path path
                # path path wall
                # wall path wall (only if its a dead end, or has wall in three sides)

                if prev == True:
                    if next == True:
                        # if path path path, then create node only if up and down are path as well
                        if a[i-1][j] == 1 or a[i+1][j] == 1:
                            graph[(i,j)]=[None, None, None, None] # [left, right, up , down]
                            count += 1
                            if leftnode != None:
                                graph[(i,j)][0] = leftnode # add the last node in leftnode as the neighbour of the node
                                graph[leftnode][1] = (i,j) # add the new node as the neighbour of the last node in lastnode
                                leftnode = (i,j)
                            """if upnode[j] != None:
                                graph[(i,j)][2] = upnode[j] # add the latest upnode as the neighbour of the node
                                graph[upnode[j]][3] = (i,j) # add the new node as the neighbour of the latest upnode
                                upnode[j] = None
                            if a[i+1][j] >0:
                                upnode[j] = (i,j)"""
                            
                            
                    else:
                        # if path path wall, then create a node1 as it the end of the corridor
                        graph[(i,j)]=[None, None, None, None] # [left, right, up , down]
                        count+=1
                        if leftnode != None:
                            graph[(i,j)][0] = leftnode # add the last node in leftnode as the neighbour of the node
                            graph[leftnode][1] = (i,j) # add the new node as the neighbour of the last node in lastnode
                            leftnode = None
                            
                        """if upnode[j] != None:
                            graph[(i,j)][2] = upnode[j] # add the latest upnode as the neighbour of the node
                            graph[upnode[j]][3] = (i,j) # add the new node as the neighbour of the latest upnode
                            if a[i-1][j] == a[i+1][j] != 0:
                                upnode[j] = (i,j)
                            else:
                                upnode[j] = None"""
                            
                else:
                    if next == True:
                        # wall path path
                        graph[(i,j)] = [None, None, None, None]
                        leftnode = (i,j)
                        count += 1
                        
                        

                    else:
                        # wall path wall
                        
                        if a[i-1][j] != 1 or a[i+1][j] != 1: # 1 for path, 0 for wall
                            # create node only if there is path up or down
                            graph[(i,j)] = [None, None, None, None]
                            count += 1
                            

                """if (i,j) in graph.keys():
                    # if the immediate top cell, is in dictionary, then that would suggest any kind of turning or stop.
                    if a[i-1][j] == 1 :
                        if (i-1,j) in graph.keys():
                            graph[(i,j)][2] = (i-1,j)
                            graph[(i-1,j)][3] = (i,j)"""
                    
                if (i,j) in graph.keys():
                    if a[i-1][j] ==1:
                        if upnode[j] != None:
                            graph[(i,j)][2] = upnode[j]
                            graph[upnode[j]][3] = (i,j)
                            
                    if a[i+1][j] == 1:
                        upnode[j] = (i,j)
                    else:
                        upnode[j] = None
                        
                                                  
        graph[self.end] = [None, None, (self.end[0]-1, self.end[1]), None]
        graph[(self.end[0]-1, self.end[1])][3]= self.end 
        count += 1

        print(f'{count} number of nodes created')
        return graph

