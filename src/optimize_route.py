import networkx as nx
import osmnx as ox

def get_shortest_path(graph_path, source_coords, dest_coords):
    G = ox.load_graphml(graph_path)
    source_node = ox.distance.nearest_nodes(G, source_coords[1], source_coords[0])
    dest_node = ox.distance.nearest_nodes(G, dest_coords[1], dest_coords[0])
    route = nx.shortest_path(G, source=source_node, target=dest_node, weight='length')
    return route
