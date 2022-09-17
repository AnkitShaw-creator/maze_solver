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
    #for i in arr:
     #   print(i)
    
    return arr

def get_maze(file):
    print("opening file")
    f = open(file, 'r')
    reader = csv.reader(f)
    maze = []

    for line in reader:
        maze.append(f)

    return maze

def main():
    arr = get_array("tiny.png")
    #display_maze(arr)
    m = Maze(arr.tolist())
    graph = m.create_graph()
    solu = solver_bfs.solve(m.start, m.end, graph)
    print(solu)


    for i in graph.keys():
        print(i, graph[i])

if __name__ == "__main__":
    main()
