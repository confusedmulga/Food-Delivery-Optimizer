from src.fetch_traffic import get_traffic_data
from src.optimize_route import get_shortest_path
from src.visualize import plot_route

origin = "Jayanagar, Bangalore"
destination = "Indiranagar, Bangalore"

# getting traffic data
traffic_info = get_traffic_data(origin, destination)
print("Estimated travel time:", traffic_info['routes'][0]['legs'][0]['duration_in_traffic']['text'])

# getting shortest path using Dijkstra
route = get_shortest_path("data/bangalore.graphml", (12.925, 77.593), (12.9716, 77.6412))

# plot it
plot_route("data/bangalore.graphml", route)
