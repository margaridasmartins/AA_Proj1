"""

Project 1 Advanced Algorithmts
Margarida Martins

"""

import random


class GraphGenerator:

    def __init__(self, nvertices):
        self.nvertices=nvertices
        
        random.seed(93169)


    def generate_graph(self, outfile):

        axis_values= [[i, j] for i in range(1,10) for j in range(1,10)]
        vertices=[]

        for i in range(self.nvertices):
            coord=random.choice(axis_values)
            axis_values.remove(coord)
            vertices.append(coord+[random.randint(1,100)])

        

