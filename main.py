from graph_generator import GraphGenerator
from exaustive_search import ExaustiveSearch

nvertices=[1,2,3,5,7,10,15,20]

"""
for n in nvertices:
    g= GraphGenerator(n)
    g.generate_graph("graphs/")
"""
stat_file=open("stats", "w")
for n in nvertices:
    s= ExaustiveSearch(f'graphs/_{n}_75')
    weight, clique, time = s.search()
    stat_file.write(f'{n} {75} {weight} {clique} {time}\n')
    print(time)
    s= ExaustiveSearch(f'graphs/_{n}_25')
    weight, clique, time = s.search()
    stat_file.write(f'{n} {25} {weight} {clique} {time}\n')
    print(time)
    s= ExaustiveSearch(f'graphs/_{n}_50')
    weight, clique, time = s.search()
    stat_file.write(f'{n} {55} {weight} {clique} {time}\n')
    print(time)
stat_file.close()