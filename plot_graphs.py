"""

Project 1 Advanced Algorithmts
Margarida Martins

"""

import matplotlib.pyplot as plt
import matplotlib.lines as mlines

nvertices=[2,3,4,5,7,9,11,13,15,17,20]



for n in nvertices:
    infile= open(f'graphs/_{n}_75', "r")
    nv= int(infile.readline())
    vertices= [[int(i) for i in infile.readline().split() ] for i in range(nv)]
    adjency_matrix=[[int(i) for i in infile.readline().split() ] for i in range(nv)]
    infile.close()
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot([v[0] for v in vertices ], [v[1] for v in vertices ],'bo', ms=15)
    t=[ ax.text(v[0],v[1], str(v[2]) , fontsize=10, color="white") for v in vertices]
    [ti.set_bbox(dict(facecolor='red', alpha=0.5, edgecolor='red')) for ti in t]

    [ax.add_line(mlines.Line2D([vertices[i][0], vertices[j][0]],[vertices[i][1],vertices[j][1]]  , lw=1,c="black" )) for i in range(nv) for j in range(nv) if adjency_matrix[i][j]!=0]
    plt.savefig(f'images/_{n}_75.png')

    infile= open(f'graphs/_{n}_50', "r")
    nv= int(infile.readline())
    vertices= [[int(i) for i in infile.readline().split() ] for i in range(nv)]
    adjency_matrix=[[int(i) for i in infile.readline().split() ] for i in range(nv)]
    infile.close()
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot([v[0] for v in vertices ], [v[1] for v in vertices ],'bo', ms=15)
    t=[ ax.text(v[0],v[1], str(v[2]) , fontsize=10, color="white") for v in vertices]
    [ti.set_bbox(dict(facecolor='red', alpha=0.5, edgecolor='red')) for ti in t]

    [ax.add_line(mlines.Line2D([vertices[i][0], vertices[j][0]],[vertices[i][1],vertices[j][1]]  , lw=1,c="black" )) for i in range(nv) for j in range(nv) if adjency_matrix[i][j]!=0]
    plt.savefig(f'images/_{n}_50.png')

    infile= open(f'graphs/_{n}_25', "r")
    nv= int(infile.readline())
    vertices= [[int(i) for i in infile.readline().split() ] for i in range(nv)]
    adjency_matrix=[[int(i) for i in infile.readline().split() ] for i in range(nv)]
    infile.close()
    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot([v[0] for v in vertices ], [v[1] for v in vertices ],'bo', ms=15)
    t=[ ax.text(v[0],v[1], str(v[2]) , fontsize=10, color="white") for v in vertices]
    [ti.set_bbox(dict(facecolor='red', alpha=0.5, edgecolor='red')) for ti in t]

    [ax.add_line(mlines.Line2D([vertices[i][0], vertices[j][0]],[vertices[i][1],vertices[j][1]]  , lw=1,c="black" )) for i in range(nv) for j in range(nv) if adjency_matrix[i][j]!=0]
    plt.savefig(f'images/_{n}_25.png')
