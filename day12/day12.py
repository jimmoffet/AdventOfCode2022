import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import numpy as np
import sys

# f = 'day12_test.txt'
f = 'day12.txt'

steps = [
    nx.shortest_path_length(G, source=start_coords, target=end_coords) 
    for start_coords, end_coords, G in 
    ([
        [
            (
                start_coords, 
                end_coords, 
                next(
                    G.remove_edges_from([
                        (a,b)[:2] for a, b in G.edges() 
                        if 
                        (array2D[a[0]][a[1]]) - (array2D[b[0]][b[1]]) < -1
                    ]) or G for G in 
                    (nx.grid_2d_graph(*array2D.shape).to_directed(),) # one item tuple
                )
            ) 
            for start_coords, end_coords, array2D in 
            ((
                lambda start_coord_pairs, end_coord_pairs, array2D : ( 
                    tuple(map(sum, zip(*start_coord_pairs))), 
                    tuple(map(sum, zip(*end_coord_pairs))), 
                    np.array(array2D) 
                )
            )(
                *map(list, zip(*[
                    ( 
                        ((i, line.index('S')) if 'S' in line else (0,0)),
                        ((i, line.index('E')) if 'E' in line else (0,0)),
                        [1 if char=='S' else 26 if char=='E' else ord(char) - 96 for char in line]
                    )
                    for i, line in enumerate(open(f,'r').read().splitlines())
                ]))
            ),) # one item tuple
        ]
    ][0][0],) # one item tuple
][0]

print(f'shortest path length: {steps}')