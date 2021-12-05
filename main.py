"""

Project 1 Advanced Algorithmts
Margarida Martins

"""


from graph_generator import GraphGenerator
from exaustive_search import ExaustiveSearch
from greedy_search import GreedySearch
import matplotlib.pyplot as plt
import math

nvertices=[2,3,4,5,7,9,11,13,15,17,20]

"""
for n in nvertices:
    g= GraphGenerator(n)
    g.generate_graph("graphs/")
"""
stat_file=open("stats", "w")

data_es=[]
data_gd=[]

time_stats_es_25=[]
time_stats_gd_25=[]

time_stats_es_75=[]
time_stats_gd_75=[]

time_stats_es_50=[]
time_stats_gd_50=[]

op_stats_es_25=[]
op_stats_gd_25=[]

op_stats_es_75=[]
op_stats_gd_75=[]

op_stats_es_50=[]
op_stats_gd_50=[]

sol_stats_es_25=[]
sol_stats_gd_25=[]

sol_stats_es_75=[]
sol_stats_gd_75=[]

sol_stats_es_50=[]
sol_stats_gd_50=[]


for n in nvertices:
    stat_file.write("\n\n{:^150} Vertices\n".format(n))
    stat_file.write("| {:10} | {:10} | {:10} | {:40} | {:20} | {:20} | {:20} |\n".format("Search", "Edges %", "Max Weight", "Clique", "Number of Operations", "Solutions Tested", "Execution Time"))

    s= ExaustiveSearch(f'graphs/_{n}_75')
    weight, clique, time, operations, solutions = s.search()
    stat_file.write("| {:10} | {:10} | {:10} | {:40} | {:20} | {:20} | {:20.3} |\n".format( 'Exaustive', 75, weight,'{}'.format(clique),operations,solutions,time))

    time_stats_es_75.append(math.log(time))
    op_stats_es_75.append(math.log(operations))
    sol_stats_es_75.append(math.log(solutions))

    g= GreedySearch(f'graphs/_{n}_75')
    weight, clique, time, operations, solutions = g.search()
    stat_file.write("| {:10} | {:10} | {:10} | {:40} | {:20} | {:20} | {:20.3} |\n".format( 'Greedy', 75, weight,'{}'.format(clique),operations,solutions,time))

    time_stats_gd_75.append(math.log(time))
    op_stats_gd_75.append(math.log(operations))
    sol_stats_gd_75.append(math.log(solutions))

    s= ExaustiveSearch(f'graphs/_{n}_50')
    weight, clique, time, operations, solutions = s.search()
    stat_file.write("| {:10} | {:10} | {:10} | {:40} | {:20} | {:20} | {:20.3} |\n".format( 'Exaustive', 50, weight,'{}'.format(clique),operations,solutions,time))

    time_stats_es_50.append(math.log(time))
    op_stats_es_50.append(math.log(operations))
    sol_stats_es_50.append(math.log(solutions))

    g= GreedySearch(f'graphs/_{n}_50')
    weight, clique, time, operations, solutions = g.search()
    stat_file.write("| {:10} | {:10} | {:10} | {:40} | {:20} | {:20} | {:20.3} |\n".format( 'Greedy', 50, weight,'{}'.format(clique),operations,solutions,time))

    time_stats_gd_50.append(math.log(time))
    op_stats_gd_50.append(math.log(operations))
    sol_stats_gd_50.append(math.log(solutions))

    s= ExaustiveSearch(f'graphs/_{n}_25')
    weight, clique, time, operations, solutions = s.search()
    stat_file.write("| {:10} | {:10} | {:10} | {:40} | {:20} | {:20} | {:20.3} |\n".format( 'Exaustive', 25, weight,'{}'.format(clique),operations,solutions,time))

    time_stats_es_25.append(math.log(time))
    op_stats_es_25.append(math.log(operations))
    sol_stats_es_25.append(math.log(solutions))

    g= GreedySearch(f'graphs/_{n}_25')
    weight, clique, time, operations, solutions = g.search()
    stat_file.write("| {:10} | {:10} | {:10} | {:40} | {:20} | {:20} | {:20.3} |\n".format( 'Greedy', 25, weight,'{}'.format(clique),operations,solutions,time))

    time_stats_gd_25.append(math.log(time))
    op_stats_gd_25.append(math.log(operations))
    sol_stats_gd_25.append(math.log(solutions))

    data_es.append(math.log(math.pow(2,n)*n))
    data_gd.append(math.log(math.log(n)*n))

    
stat_file.close()

plt.figure(1)
plt.plot(nvertices, data_es, 'o-')
plt.plot(nvertices, data_gd, 'o-')
plt.plot(nvertices, time_stats_es_25, 'o-')
plt.plot(nvertices, time_stats_gd_25, 'o-')
plt.plot(nvertices, time_stats_es_50, 'o-')
plt.plot(nvertices, time_stats_gd_50, 'o-')
plt.plot(nvertices, time_stats_es_75, 'o-')
plt.plot(nvertices, time_stats_gd_75, 'o-')
plt.legend(['n * 2^n', 'n log n','Exaustive Search 25%', 'Greedy Search 25%','Exaustive Search 50%', 'Greedy Search 50%','Exaustive Search 75%', 'Greedy Search 75%'])
plt.xlabel("Number of vertices")
plt.ylabel("Execution time")
plt.savefig(f'images/time_stats.png')

plt.figure(2)
plt.plot(nvertices, data_es, 'o-')
plt.plot(nvertices, data_gd, 'o-')
plt.plot(nvertices, op_stats_es_25, 'o-')
plt.plot(nvertices, op_stats_gd_25, 'o-')
plt.plot(nvertices, op_stats_es_50, 'o-')
plt.plot(nvertices, op_stats_gd_50, 'o-')
plt.plot(nvertices, op_stats_es_75, 'o-')
plt.plot(nvertices, op_stats_gd_75, 'o-')
plt.legend(['n * 2^n', 'n log n','Exaustive Search 25%', 'Greedy Search 25%','Exaustive Search 50%', 'Greedy Search 50%','Exaustive Search 75%', 'Greedy Search 75%'])
plt.xlabel("Number of vertices")
plt.ylabel("Number of basic operations")
plt.savefig(f'images/operation_stats.png')


plt.figure(3)
plt.plot(nvertices, data_es, 'o-')
plt.plot(nvertices, data_gd, 'o-')
plt.plot(nvertices, sol_stats_es_25, 'o-')
plt.plot(nvertices, sol_stats_gd_25, 'o-')
plt.plot(nvertices, sol_stats_es_50, 'o-')
plt.plot(nvertices, sol_stats_gd_50, 'o-')
plt.plot(nvertices, sol_stats_es_75, 'o-')
plt.plot(nvertices, sol_stats_gd_75, 'o-')
plt.legend(['n * 2^n', 'n log n','Exaustive Search 25%', 'Greedy Search 25%','Exaustive Search 50%', 'Greedy Search 50%','Exaustive Search 75%', 'Greedy Search 75%'])
plt.xlabel("Number of vertices")
plt.ylabel("Number of solutions tested")
plt.savefig(f'images/solutions_stats.png')
