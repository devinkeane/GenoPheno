# last rev: 02-18-21


# Import libraries
import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt
import networkx as nx
from string import ascii_lowercase
# ------------------------------------------------------------------------------------------------------
# Parse command line input and options
parser = argparse.ArgumentParser(description="	ʕっ•ᴥ•ʔっ  * Apply graph theory to your network table! * ")
parser.add_argument('-i', '--input', type=str, help='<INPUT_FILENAME.txt>  (list of MIM reference numbers, no headers, each MIM separated by a new line)')
parser.add_argument('-o', '--output', type=str, help='<OUTPUT_FILENAME.png>')
args = parser.parse_args()

# Assign parsed arguments into local variables
input = args.input
output = args.output

# ---------------------------------------------------------------------------
# GRAPHING THE DATA |
# ------------------+

gpn = pd.read_csv(input)
print(gpn)

# Create a NetworkX object called "G" where 'Superphenotype' is the source node
# and 'Node_name' is the target node.
G = nx.from_pandas_edgelist(gpn,source = 'Superphenotype', target = 'Node_name')

lst_overlap = gpn[gpn['Node_type'] == 'associated_and_overlapping_genes']['Node_name'].reset_index(drop=True)
lst_neighbors = gpn[gpn['Node_type'] == 'Intact_first_neighbors']['Node_name'].reset_index(drop=True)
lst_new = []
lst_overlap_2 = []
lst_neighbors_2 = []
for i in range(len(lst_overlap)):
    lst_new += [lst_overlap[i]]
    lst_overlap_2 += [lst_overlap[i]]
    lst_new += [lst_neighbors[i]]
    lst_neighbors_2 += [lst_neighbors[i]]

# Draw a graph with G using a color map that distinguishes between genes and phenotypes
plt.figure(figsize=(50,50))

color_map = []
for node in G:
    if node in lst_overlap_2:
        color_map.append('red')
    elif node in lst_neighbors_2:
        color_map.append('blue')
    else:
        color_map.append('green')
pos= nx.spring_layout(G)
nx.draw(G, node_color=color_map, node_size=300, pos=pos,with_labels=False)
superphenotype_labels = {}
neighbor_labels = {}
gene_labels = {}

for idx, node in enumerate(G.nodes()):
    if node in gpn['Superphenotype'].unique():
        superphenotype_labels[node] = node

bbox = dict(fc="blue", ec="black", boxstyle="square", lw=2)
nx.draw_networkx_labels(G, pos, labels=superphenotype_labels, font_size=14, font_color='white', font_family='copperplate',bbox=bbox)

for idx, node in enumerate(G.nodes()):
    if node in lst_overlap_2:
        gene_labels[node] = node

bbox2 = dict(fc="yellow", ec="black", boxstyle="circle", lw=2)
nx.draw_networkx_labels(G, pos, labels=gene_labels, font_size=14, font_color='black', font_family='copperplate',bbox=bbox2)


for idx, node in enumerate(G.nodes()):
    if node in lst_neighbors_2:
        neighbor_labels[node] = node

bbox3 = dict(fc="red", ec="black", boxstyle="sawtooth", lw=2)
nx.draw_networkx_labels(G, pos, labels=neighbor_labels, font_size=14, font_color='black', font_family='copperplate',bbox=bbox3)



# ---------------------------------------------------------------------------
# Save output to files |
# ---------------------+

# Name the graph output file based on the input argument for the file name.
# Append '.png' to the filename and save the figure as that filename.
graph_output_name = output.split('.')[0]
graph_output_name += '.png'
plt.savefig(graph_output_name)

# ---------------------------------------------------------------------------
# Print logo and output message |
# ------------------------------+
logo = """

O---o    ___|                       _ \   |
O---o   |       _ \  __ \    _ \   |   |  __ \    _ \  __ \    _ \   |
 O-o    |   |   __/  |   |  (   |  ___/   | | |   __/  |   |  (   |  |
  O    \____| \___| _|  _| \___/  _|     _| |_| \___| _|  _| \___/   |
 o-O   ______________________________________________________________|---------+
o---O   High Performance Computing Genomic Network Analysis    |  Version 1.4  |    ✧ - ･ﾟ*
O---o                               +------------------------------------------+ 
 O-o                     (✿◠‿◠)     |  (c) 2022-01-27 Devin Keane              |
  O                                 |  Feltus Lab                              |◉‿◉)つ
 o-O                                |  Department of Genetics and Biochemistry |
o---O                               |  Clemson University                      | 
O---o                        'ﾟ✧    |                                          |
                                    |  Last rev: 2022-02-21                    |
                                    +------------------------------------------+
                         , ⌒ *: ﾟ･✧* ･ﾟ✧ - *                      ─=≡Σ((( つ◕ل͜◕)つ
    ╰( ͡° ͜ʖ ͡° )つ──☆*:・^'
"""
print()
print('Thank you for using...')
print(logo)
print('--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+')
print()
print('                 ...Your network graph was saved as \"',output,'\" with ',len(gpn),' total nodes.')
print()
print('--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+')
print()