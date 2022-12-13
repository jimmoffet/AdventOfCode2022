import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import numpy as np
import sys
import timeit

f = 'day12_test.txt'
# f = 'day12.txt'

steps = lambda f : (next(
    nx.shortest_path_length(G, source=start_coords, target=end_coords) 
    for start_coords, end_coords, G in 
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
        (( # lambda
            lambda start_coord_pairs, end_coord_pairs, array2D : ( 
                tuple(map(sum, zip(*start_coord_pairs))), 
                tuple(map(sum, zip(*end_coord_pairs))), 
                np.array(array2D) 
            )
        )( # lambda args
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
))

print(f'shortest path length: {steps(f)}')

###################################################################
# Check that we're within 50% of the expected time for O(n) runtime
###################################################################

scaling_factor = 4 # scaled input matrix in Y/height/rows direction
f = 'day12.txt'
input_scaled = 'day12_scaled.txt'
f1 = 'steps(f)'
f2 = 'steps(input_scaled)'

def get_variance(f1, f2, iter):
    input_time_n = timeit.timeit(f1, number=iter, globals=globals())
    input_time_n_scaled = timeit.timeit(f2, number=iter, globals=globals())
    input_time_n_expected = input_time_n_scaled / scaling_factor
    return (input_time_n / input_time_n_expected) - 1

variance = get_variance(f1, f2, 10)
result = "Yay!" if variance < 0.50 else "Boo!"
print(f'Variance is {variance:.2%} {result}')

