# Food Delivery Optimizer

This project finds the shortest delivery route using real-time traffic and maps. You can run everything except traffic data without an API key.

Steps:
1. Use OSMNX to download a street graph.
2. Use Dijkstra's algorithm to find shortest route.
3. Plot the route on a map.
4. (Optional) Use Google Maps API for traffic data.

To run:
```bash
pip install -r requirements.txt
python main.py
```
