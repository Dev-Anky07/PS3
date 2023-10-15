import json
import networkx as nx
import matplotlib.pyplot as plt

# Load the JSON data from the file
with open('response.json') as file:
    data = json.load(file)

# Create a directed graph
graph = nx.DiGraph()

# Set the maximum number of connections to visualize
max_connections = 20
connections_count = 0

# Iterate over the JSON data and add edges to the graph
for item in data['transfers']:
    if connections_count >= max_connections:
        break

    source = item['fromAddress']['address']
    target = item['toAddress']['address']
    graph.add_edge(source, target)
    connections_count += 1

# Draw the graph
pos = nx.spring_layout(graph, k=0.3)  # Increase the k value to increase the distance between nodes
nx.draw_networkx(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()
