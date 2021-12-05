"""

Project 1 Advanced Algorithmts
Margarida Martins

"""

from itertools import combinations
import time

class ExaustiveSearch:

    def __init__(self, infile):
        infile= open(infile,"r")

        self.nvertices= int(infile.readline())
        self.vertices= [[int(i) for i in infile.readline().split() ] for i in range(self.nvertices)]
        self.adjency_matrix=[[int(i) for i in infile.readline().split() ] for i in range(self.nvertices)]

        infile.close()



    def search(self):
        time_start= time.time()
        #generate all possible cliques      
        max_weight=0
        max_clique=set()
        operations=0
        solutions=0
        #while there is still possible cliques
        for i in range(1,self.nvertices+1):
            possible=[ p for p in combinations(range(self.nvertices),i)]

            while possible:
                p = possible.pop()
                solutions+=1

                if sum([1 for v in range(i) for j in range(i) if self.adjency_matrix[p[v]][p[j]]==0 and v!=j])==0:
                    w=sum([self.vertices[p[k]][2] for k in range(i)])
                    operations+=i
                
                if w>max_weight:
                    max_clique=set(p)
                    max_weight=w
                    operations+=2
                
                operations+=i*i +1

        return max_weight, max_clique, time.time()- time_start, operations, solutions

        
