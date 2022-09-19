from PIL import Image # for image manipulation
import time # for getting the system time to check the efficiency of the algorithm
import os, sys #for controlling the input/output
import argparse # to parse the cli input
import csv  #as reader
import numpy as np # for generating np array for the csv
from mazes import Maze
import solver_bfs

def get_array(im_file):
    im = Image.open(im_file, 'r')
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

def main():
    
    arr = get_array("normal.png")
    #display_maze(arr)
    initial_time = time.time()
    m = Maze(arr.tolist())
    graph = m.create_graph()
    #print(m.start, m.end)
    solu = solver_bfs.solve(m.start, m.end, graph)
    time_final = time.time()
    
    if solu != None:
        print(f'\nSolution Found!. Length:{len(solu)}')
        print(solu)
    else:
        print("\nGiven maze cannot be solved with current algorithm")
        
    print("\nTime taken:", time_final-initial_time)

    # uncomment the below lines to check the graph nodes and their respective neighbours
    """for i in graph.keys():  
        print(i, graph[i])"""

if __name__ == "__main__":
    main()
