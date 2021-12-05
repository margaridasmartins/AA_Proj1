"""

Project 1 Advanced Algorithmts
Margarida Martins

"""

from itertools import combinations
import time
import math

class GreedySearch:

    def __init__(self, infile):
        infile= open(infile,"r")

        self.nvertices= int(infile.readline())
        self.vertices= [[i] + [int(i) for i in infile.readline().split() ] for i in range(self.nvertices)]
        self.adjency_matrix=[[int(i) for i in infile.readline().split() ] for i in range(self.nvertices)]

        infile.close()



    def search(self, heuristic=0):
        time_start= time.time()
        #generate all possible cliques      
        max_weight=0
        max_clique=set()
        solutions=0
        operations=0

        #two different heuristics the default one gets better results
        if heuristic==0:
            possible= sorted(self.vertices,key= lambda p : p[3])
        elif heuristic==1:
            possible= sorted(self.vertices,key=self.heuristic)

        operations+=self.nvertices*math.ceil(math.log(self.nvertices))

        while possible:
            p = possible.pop()
            solutions+=1

            if self.is_clique(max_clique,p):
                max_clique.add(p[0])
                max_weight+= p[3]
                operations+=2
            
            operations+=len(max_clique)
    
        return max_weight, max_clique, time.time()- time_start, operations, solutions

    def is_clique(self,max_clique, p):
        for v in max_clique:
            if self.adjency_matrix[p[0]][v]==0:
                return False
        return True

    def heuristic(self,p):
        return sum(self.adjency_matrix[p[0]])*(sum([v[3] for v in self.vertices])/self.nvertices) + p[3]