from django.shortcuts import render
from django.http import HttpResponse
import geocoder
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser


userloc = geocoder.ip('me').latlng
print(userloc)

def map(request):
    
    m = folium.Map(userloc, zoom_start=13)    

    
    
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
    
    loc = [userloc,
      (userloc[0],userloc[1]+1)]

    folium.PolyLine(loc,
                color='red',
                weight=15,
                opacity=0.8).add_to(m)
    
    m = m._repr_html_()
    context = {
        'geomap': m,
    }
    return render(request, 'map.html', context)