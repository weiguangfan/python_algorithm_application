import networkx as nx
import matplotlib.pyplot as plt
G = nx.dodecahedral_graph()
options = {
    'node_color': 'black',
    'node_size': 100,
    'width': 3,
}
shells = [[2, 3, 4, 5, 6], [8, 1, 0, 19, 18, 17, 16, 15, 14, 7], [9, 10, 11, 12, 13]]
nx.draw_shell(G, nlist=shells, **options)
plt.show()
nx.draw(G)
plt.savefig("path.png")