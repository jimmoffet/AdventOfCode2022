import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import numpy as np
import sys

# f = 'day12_test.txt'
f = 'day12.txt'

steps = [nx.shortest_path_length(G, source=start_coords, target=end_coords) for start_coords, end_coords, G in ([[(start_coords, end_coords, [G.remove_edges_from(list(e[:2] for e in [(a,b,attrs) for a, b, attrs in G.edges(data=True) 
    if (
        ( 
            (ar[a[0]][a[1]]) - (ar[b[0]][b[1]]) < -1 
            and 
            ar[a[0]][a[1]] != 0 
            and 
            ar[b[0]][b[1]] != 27
        ) or (
            (ar[a[0]][a[1]]) - (ar[b[0]][b[1]]) < -2
            and 
            (ar[a[0]][a[1]] == 0 
            or 
            ar[b[0]][b[1]] == 27)
        )
    )
])) or G for G in (nx.grid_2d_graph(*ar.shape).to_directed(),)][0]) for start_coords, end_coords, ar in (( next(zip(*np.where(ar == 0))), next(zip(*np.where(ar == 27))), ar),) ] for ar in (np.array([[ord(char) - 96 if char.islower() else 0 if char=='S' else 27 for i, char in enumerate(line)] for i, line in enumerate(open(f,'r').read().splitlines())]),)][0][0],)][0]

print(f'shortest path length: {steps}')