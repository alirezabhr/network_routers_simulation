# Network Routers Simulation

This project was developed for network course in university.
Its purpose is to simulate a network of routers and determine the shortest path between a designated starting router and all other routers in the network.
It will calculate the shortest path using Dijkstra Algorithm.

The configuration of all routers and the distance between them can be specified in the `routers.json` file, including the designation of the starting router with the `start` attribute.


## Getting Started

Before you can use this project, you must install the `matplotlib` and `networkx` packages using `pip`.
This can be done by executing the following command:

```pip install -r requirements.txt```

Once the packages have been installed, you can configure the information for your routers in the `routers.json` file and then run the program.



## Results

Routers and cost of each edge between them before finding shortest paths:
![Routers Before Finding Shortest Path](https://i.imgur.com/GAT7Y0x.png)


Routers and their shortest path after running Dijkstra algorithm on the network:
![Routers After Finding Shortest Path](https://i.imgur.com/7ybVF9o.png)
