import matplotlib.pyplot as plt
import matplotlib.lines as mlines

nvertices=[1,2,3,5,7,10,15,20]



for n in nvertices:
    infile= open(f'graphs/_{n}_50', "r")
    nv= int(infile.readline())
    vertices= [[int(i) for i in infile.readline().split() ] for i in range(nv)]
    adjency_matrix=[[int(i) for i in infile.readline().split() ] for i in range(nv)]

    fig = plt.figure()
    ax = fig.add_subplot()

    ax.plot([v[0] for v in vertices ], [v[1] for v in vertices ],'ro')
    [ ax.text(v[0],v[1], str(v[2]) , fontsize=15) for v in vertices]

    [ax.add_line(mlines.Line2D([vertices[i][0], vertices[j][0]],[vertices[i][1],vertices[j][1]]  , lw=1,c="black" )) for i in range(nv) for j in range(nv) if adjency_matrix[i][j]!=0]
    plt.show()