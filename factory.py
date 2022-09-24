



class SolverFactory:

    def __init__(self):
        self.default = "BFS"
        self.choices = ["BFS", "DFS", "dijkstra", "astar"]
        

    def createsolver(self, type):
        if type == None or type == "BFS":
            import solver_bfs
            return ["BFS", solver_bfs.solve]

        if type == "DFS":
            import solver_dfs
            return ["DFS", solver_dfs.solve]

