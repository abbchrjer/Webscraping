import osmnx as ox
import networkx as nx
from django.shortcuts import render
from django.http import HttpResponse

ox.config(use_cache=True, log_console=True)

loc = (59.663822, 16.591977)
dest = (59.638996, 16.588524)

G = ox.graph_from_point(loc, dist=10000, network_type='drive')

G = ox.speed.add_edge_speeds(G)
G = ox.speed.add_edge_travel_times(G)

orig = ox.get_nearest_node(G, loc)
dest = ox.get_nearest_node(G, dest)
route = nx.shortest_path(G, orig, dest, 'travel_time')

route_map = ox.plot_route_folium(G, route)

route_map.save('templates/route.html')

def path(request):
    return render(request,'route.html')