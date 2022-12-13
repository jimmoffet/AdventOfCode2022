import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import numpy as np
import sys


# steps = [nx.shortest_path_length(G, source=start_coords, target=end_coords) for start_coords, end_coords, G in ([[(start_coords, end_coords, [G.remove_edges_from(list(e[:2] for e in [(a,b,attrs) for a, b, attrs in G.edges(data=True) 
#     if (
#         ( 
#             (ar[a[0]][a[1]]) - (ar[b[0]][b[1]]) < -1 
#             and 
#             ar[a[0]][a[1]] != 0 
#             and 
#             ar[b[0]][b[1]] != 27
#         ) or (
#             (ar[a[0]][a[1]]) - (ar[b[0]][b[1]]) < -2
#             and 
#             (ar[a[0]][a[1]] == 0 
#             or 
#             ar[b[0]][b[1]] == 27)
#         )
#     )
# ])) or G for G in (nx.grid_2d_graph(*ar.shape).to_directed(),)][0]) for start_coords, end_coords, ar in (( next(zip(*np.where(ar == 0))), next(zip(*np.where(ar == 27))), ar),) ] for ar in (np.array([[ord(char) - 96 if char.islower() else 0 if char=='S' else 27 for i, char in enumerate(line)] for i, line in enumerate(open(f,'r').read().splitlines())]),)][0][0],)][0]

# print(f'shortest path length: {steps}')

# f = 'day12_test.txt'
f = 'day12.txt'
f = 'day12_test.txt'
# f = 'day12.txt'

# steps = [
#     nx.shortest_path_length(G, source=start_coords, target=end_coords) 
#     for start_coords, end_coords, G in 
#     (
#         [
#             [
#                 (
#                     start_coords, 
#                     end_coords, 
#                     [
#                         G.remove_edges_from(
#                             list(
#                                 e[:2] for e in [
#                                     (a,b,attrs) for a, b, attrs in G.edges(data=True) 
#                                     if (
#                                         ( 
#                                             (ar[a[0]][a[1]]) - (ar[b[0]][b[1]]) < -1 
#                                             and 
#                                             ar[a[0]][a[1]] != 0 
#                                             and 
#                                             ar[b[0]][b[1]] != 27
#                                         ) 
#                                         or 
#                                         (
#                                             (ar[a[0]][a[1]]) - (ar[b[0]][b[1]]) < -2
#                                             and 
#                                             (ar[a[0]][a[1]] == 0 
#                                             or 
#                                             ar[b[0]][b[1]] == 27)
#                                         )
#                                     )
#                                 ]
#                             )
#                         ) 
#                         or G for G in 
#                         (nx.grid_2d_graph(*ar.shape).to_directed(),) # one item tuple
#                     ][0]
#                 ) 
#                 for start_coords, end_coords, ar 
#                 in 
#                 (( 
#                     next(zip(*np.where(ar == 0))), 
#                     next(zip(*np.where(ar == 27))), 
#                     ar
#                 ),) # one item tuple
#             ] 
#             for ar in 
#             (
#                 np.array(
#                     [
#                         [ord(char) - 96 if char.islower() else 0 if char=='S' else 27 for i, char in enumerate(line)] 
#                         for i, line in enumerate(open(f,'r').read().splitlines())
#                     ]
#                 ),
#             )
#         ][0][0],
#     )
# ][0]

# print(f'shortest path length: {steps}')


# enumerated_lines = enumerate(open(f,'r').read().splitlines())

# mylines = [(( {'start': (i,line.index('S'))} if 'S' in line else {'start':(0,0)}, {'end': (i,line.index('E'))} if 'E' in line else {'end':(0,0)} ), [ord(char) - 96 if char.islower() else 1 if char=='S' else 26 for char in line]) for i, line in enumerated_lines]

# asdf = for 
# print(f'mylines: {mylines}')
# sys.exit()

mylines = [[ord(char) - 96 if char.islower() else 0 if char=='S' else 27 for i, char in enumerate(line)] for i, line in enumerate(open(f,'r').read().splitlines())]

ar = np.array(mylines)

inds = [(start_coords, end_coords, grid) for start_coords, end_coords, grid in (( next(zip(*np.where(ar == 0))), next(zip(*np.where(ar == 27))), ar),) ]

start_coords = inds[0][0]
end_coords = inds[0][1]


# np.put(ar, (2,5), -1, mode='raise')
# np.put(ar, next(zip(*np.where(ar == 27))), 26, mode='raise')
# print(f'ar adjusted: {ar}')



# define grid graph according to the shape of a
G = nx.grid_2d_graph(*ar.shape).to_directed()

# for a,b in G.edges():
#     a_val = ar[a[0]][a[1]]
#     b_val = ar[b[0]][b[1]]
#     dif = a_val - b_val
#     print(f'a,b is {a},{b}: {a_val},{b_val} with dif {dif}')




edge_pairs = [(a,b,attrs) for a, b, attrs in G.edges(data=True) 
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
]
le_ids = list(e[:2] for e in edge_pairs)
print(f'edge_pairs: {edge_pairs}')
G.remove_edges_from(le_ids)



# # remove those nodes where the corresponding value is != 0
# for val,node in zip(ar.ravel(), sorted(G.nodes())):
#     if val!=1:
#         G.remove_node(node)

plt.figure(figsize=(15,8))
# coordinate rotation
pos = {(x,y):(y,-x) for x,y in G.nodes()}
nx.draw(G, pos=pos, 
        node_color='blue',
        width = 1,
        node_size=10)
# plt.show()

# for node in G.nodes(data=True):
#     print(f'node: {node}')


steps = nx.shortest_path_length(G, source=start_coords, target=end_coords)
print(f'shortest path length: {steps}')

path = nx.shortest_path(G,source=start_coords,target=end_coords)
path_edges = list(zip(path,path[1:]))
nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=1)
plt.axis('equal')
plt.show()

sys.exit()
# construct edges from grid_graph?

asdf = 'abcaaaaaaccaaaaacccccccccaaaaccaaaaaaaaaacaaagggpppssssssswwwwwwrrqmmmmmccccccccc'
print(f'len(asdf): {len(asdf)}')

steps = nx.shortest_path_length([g.add_edges_from(edgeList) or g for g in (nx.Graph(),)][0], source=0, target=10)
print(f'shortest path length: {steps}')

# NOTE: dont need graph data
# NOTE: enumerate keeps being surprisingly useful for one line constructions
# NOTE: would be nice to be able to use something like np.loadtxt or genfromtxt
# NOTE: cheated by hardcoding line length

# pos = nx.planar_layout(g)

# nx.draw(g, pos, with_labels=True, node_color="#f86e00")

# bfs = nx.bfs_tree(g, source=edgeList[0][0])

# nx.draw(bfs, pos, with_labels=True, node_color="#f86e00", edge_color="#dd2222")

# plt.show()