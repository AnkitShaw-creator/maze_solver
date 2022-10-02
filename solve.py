from PIL import Image # for image manipulation
import time # for getting the system time to check the efficiency of the algorithm
import os, sys #for controlling the input/output
import argparse # to parse the cli input
import numpy as np # for generating np array for the csv
from mazes import Maze
import solver_bfs, solver_dfs
from factory import SolverFactory

def get_array(im):
    arr = np.array(im)
    os.system('cls')
    """for i in arr:
        print(i)"""
    
    return arr

# function to create a maze out of a csv file, if required
"""def get_maze(file):
    print("opening file")
    f = open(file, 'r')
    reader = csv.reader(f)
    maze = []

    for line in reader:
        maze.append(f)

    print('\n')
    return maze"""


def solve(factory, method, maze):
    graph = maze.create_graph()
    # uncomment the below lines to check the graph nodes and their respective neighbours
    """for i in graph.keys():  
        print(i, graph[i])"""
    [title, solver] = factory.createsolver("DFS")
    solu = solver(maze.start, maze.end, graph)

    return [title,solu]


def draw_path(img, s, file_name):
    im = img.convert('RGB')
    path = s[1]
    impixel = im.load()
    img_file_name=f'solution_{s[0]}_{file_name[:-5]}.png'
    lenpath = len(path)

    for i in range(0,lenpath-1):
        a = path[i]
        b = path[i+1]

        r = int((i/lenpath)*255)
        px = (r,0,255-r)


        if a[0] == b[0]:
            # path is horizontal

            for x in range(min(a[1],b[1]), max(a[1],b[1])):
                impixel[x,a[0]] = px

        elif a[1]==b[1]:
            #path is vertical

            for y in range(min(a[0],b[0]), max(a[0],b[0])+1):
                impixel[a[1],y] = px

    
    im.save(img_file_name)


def main():
    str = input("Enter the image file name: ")
    print("\nLoading image ..........")
    img = Image.open(str)
    arr = get_array(img)
    #display_maze(arr)
    initial_time = time.time()
    maze= Maze(arr.tolist())
  
    sf = SolverFactory()
    solu = solve(sf, "DFS", maze)
    time_final = time.time()
    
    
    
    if solu != None:
        print(f'\nSolution Found!. Length:{len(solu[1])}')
        print(f'Method: {solu[0]}')
        print(f'Path found: {len(solu[1])}')
        print("Drawing path ..........")
        draw_path(img,solu,str)
    else:
        print("\nGiven maze cannot be solved with current algorithm")
        
    print("\nTime taken:", time_final-initial_time)

    

if __name__ == "__main__":
    main()
