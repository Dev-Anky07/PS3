import json
import networkx as nx
import matplotlib.pyplot as plt

# Load the JSON data from the file
with open('response.json') as file:
    data = json.load(file)

# Create a directed graph
graph = nx.DiGraph()

# Iterate over the JSON data and add edges to the graph
for item in data['transfers']:
    source = item['fromAddress']['address']
    target = item['toAddress']['address']
    graph.add_edge(source, target)

# Draw the graph
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
