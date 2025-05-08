import folium
import osmnx as ox

def plot_route(graph_path, route):
    G = ox.load_graphml(graph_path)
    m = ox.plot_route_folium(G, route)
    m.save("optimized_route.html")
