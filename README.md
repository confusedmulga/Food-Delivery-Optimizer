# Optimizing Food Delivery Routes with Real-Time Traffic Data

This project helps find the fastest delivery route in a city by using map data and shortest path algorithms. It's designed for services like Uber Eats or DoorDash to improve delivery time and reduce fuel costs.

Right now, it works for Bangalore, India using open-source street data.

## What It Does

- Downloads real-world road network using OSMNX
- Calculates the shortest path between pickup and drop locations using Dijkstra’s algorithm
- Visualizes the route on an interactive map
- (Optional) Can integrate real-time traffic data using Google Maps API

## Project Structure

project\_root/
│
├── config.py              # API key config
├── main.py                # Run the full workflow
├── requirements.txt       # Python dependencies
├── README.md              # You're reading it!
│
├── data/                  # Saved street graph
│   └── bangalore.graphml
│
├── notebooks/
│   └── get\_map\_data.ipynb # Download map data
│
└── src/
├── fetch\_traffic.py   # (Optional) Google Maps API integration
├── optimize\_route.py  # Dijkstra path finder
├── visualize.py       # Route plotting
└── utils.py           # Placeholder for helper functions

````

## How To Use

1. Clone this repository
2. (Optional) Create a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
````

4. Download map data for your city (example provided for Bangalore):

```bash
jupyter notebook notebooks/get_map_data.ipynb
```

5. Run the project:

```bash
python main.py
```

This will calculate the shortest route and generate an `optimized_route.html` map.

## Google Maps API Key

This project includes optional support for real-time traffic data using the Google Maps Directions API. If you'd like to use this feature:

1. Create a Google Cloud account
2. Enable the **Directions API**
3. Generate an API key
4. Add your key to `config.py`:

```python
GOOGLE_API_KEY = "your_api_key_here"
```

If no key is provided, the project wont run.

## Future Improvements

* Add weather-based routing logic
* Optimize for multiple deliveries (TSP)
* Add a simple dashboard

---

Feel free to fork or contribute.

