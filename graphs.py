import networkx as nx 
import matplotlib.pyplot as plt

graphedges = [['Dubna', 'Moscow', 3], ['Dubna', 'Rome', 4],
			['Moscow', 'NewYork', 20], ['Moscow', 'Dubna', 3],
			['Rome', 'NewYork', 5], ['Rome', 'Dubna', 4],
			['NewYork', 'Paris', 4], ['NewYork', 'London', 7], 
			['NewYork', 'Berlin', 11], ['NewYork', 'Moscow', 20], 
			['NewYork', 'Rome', 5], ['Paris', 'London', 3], 
			['Paris', 'Amsterdam', 6], ['Paris', 'NewYork', 4],
			['London', 'Paris', 3], ['London', 'Amsterdam', 9], 
			['London', 'NewYork', 7], ['Berlin', 'Amsterdam', 2], 
			['Berlin', 'NewYork', 11], ['Amsterdam', 'Paris', 6], 
			['Amsterdam', 'London', 9], ['Amsterdam', 'Berlin', 2]]

mygraph = nx.Graph()
for edge in graphedges:
	mygraph.add_edge(edge[0], edge[1], weight = edge[2])

start = 'Amsterdam'
end = 'Dubna'

print(nx.shortest_path(mygraph, start, end, weight = 'weight'))
print(nx.shortest_path_length(mygraph, start, end, weight = 'weight'))

pos = nx.spring_layout(mygraph, seed=3068) 
nx.draw(mygraph, pos=pos, with_labels=True)
edge_labels = nx.get_edge_attributes(mygraph, "weight")
nx.draw_networkx_edge_labels(mygraph, pos, edge_labels)
plt.show()

#nx.draw_networkx(nx.minimum_spanning_tree(mygraph))
#plt.show()
