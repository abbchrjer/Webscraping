from django.shortcuts import render
from django.http import HttpResponse

import geocoder
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser


userloc = geocoder.ip('me').latlng
print(userloc)

m = folium.Map(userloc, zoom_start=15)    

folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)

folium.TileLayer('cartodbdark_matter').add_to(m)
    
folium.LayerControl().add_to(m)

folium.Marker(userloc,
                      popup='your location',
                      tooltip='hello there!',
                     ).add_to(m)  

m.save("templates/maps.html")

def maps(request):
    return render(request, 'maps.html')