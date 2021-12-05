"""

Project 1 Advanced Algorithmts
Margarida Martins

"""

import random
import math


class GraphGenerator:

    def __init__(self, nvertices):
        self.nvertices=nvertices
        self.densities=[0.25,0.50,0.75]
        random.seed(93169)


    def generate_graph(self, outfile):

        for d in self.densities:
            axis_values= [[i, j] for i in range(1,10) for j in range(1,10)]
            filename=f'{outfile}_{self.nvertices}_{int(d*100)}'
            outf = open(filename , "w")
            outf.write(f'{self.nvertices}\n')
            for i in range(self.nvertices):
                coord=random.choice(axis_values)
                axis_values.remove(coord)

                #don't allow verticies too close
                if [coord[0]-1, coord[1]] in axis_values:
                    axis_values.remove([coord[0]-1, coord[1]]) 

                if [coord[0]+1, coord[1]] in axis_values:
                    axis_values.remove([coord[0]+1, coord[1]]) 

                if [coord[0], coord[1]-1] in axis_values:
                    axis_values.remove([coord[0], coord[1]-1]) 

                if [coord[0], coord[1]+1] in axis_values:
                    axis_values.remove([coord[0], coord[1]+1]) 

                outf.write(f'{coord[0]} {coord[1]} {random.randint(1,100)}\n')

            # based on the density compute the number of edges
            nedges= math.ceil(d*(self.nvertices*(self.nvertices-1)/2))
            adjency_matrix= [[0 for i in range(self.nvertices)]  for j in range(self.nvertices) ]
            indices = [[i,j] for i in range(self.nvertices) for j in range(self.nvertices) if i!=j] 

            # randomly attribute edges
            for i in range(nedges):
                ind= random.choice(indices)
                adjency_matrix[ind[0]][ind[1]]=1
                adjency_matrix[ind[1]][ind[0]]=1
                indices.remove(ind)
                indices.remove([ind[1],ind[0]])

            [outf.write(f'{str(row).replace("[","").replace("]","").replace(","," ")}\n') for row in adjency_matrix]
        
