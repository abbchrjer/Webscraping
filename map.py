# importing neccessary libraries, json to load data, folium for mapping, geopy to find locations and webbrowser show html-file
from geopy.exc import GeocoderTimedOut 
from geopy.geocoders import Nominatim
import json
import folium
from folium import plugins
from folium.plugins import MarkerCluster
import webbrowser

# loading json-data and storing in the list properties
with open('data.json','r', encoding="utf-8") as f:
    properties = json.loads(f.read())
    
print(f'amount of properties: {len(properties)}')

# declaring city name, finding coordinates of the city and centering map on it
cityname = 'Västerås kommun'
geolocator = Nominatim(user_agent='chrome')
city = geolocator.geocode(cityname,timeout=10)
cityloc = city.latitude , city.longitude

# creating folium-map-object
map = folium.Map(cityloc, zoom_start=11, min_zoom = 5, control_scale=True)

# adding map settings/features
minimap = plugins.MiniMap(toggle_display=True)
fullscreen = plugins.Fullscreen(toggle_display=True)
map.add_child(fullscreen)
map.add_child(minimap)
# folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
# folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
# folium.raster_layers.TileLayer('CartoDB Positron').add_to(map)
# folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(map)
# folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
# folium.LayerControl().add_to(map)

# adding featurgroups for layercontrol and markerclusters for every property type
types =  ['Villa', 'Lägenhet', 'Radhus', 'Tomt', 'Fritidshus', 'Övrigt']
colors = ['blue', 'purple', 'orange', 'green', 'red', 'black']
for type, color in zip(types, colors):
    exec(f'''{type} = folium.FeatureGroup(name='<span style=\\"color: {color};\\">{type.title()}</span>')\n{type}_marker_cluster = MarkerCluster()''')

# adding property-type dictionaries with corresponding icons and colors for markers
icons = ['home', 'building', 'users', 'tree', 'bookmark', 'question']
icons = dict(zip(types, icons))
colors = dict(zip(types, colors))

# looping through properties and creating/adding markerdata to corresponding markercluster
for property in properties:
    
    # only using the first part (address) if the name is comma seperated with type in name or contains property type
    if ',' in property['location']: 
        property['location'] = property['location'].split(',')[0]
    for type in ['tomt', 'lgh']:
        if type in property['location'].lower():
            property['location'] = property['location'][:property['location'].lower().find(type)-1]
    
    # using geocode to convert address and cityname to coordinates, skipping past the location if location is not found
    location = geolocator.geocode(f'{property["location"]}, {cityname}',timeout=10)
    if location:
        property['coordinates'] = location.latitude , location.longitude
        
        # popup for displaying property-attributes
        html = f'''<b>Bostadstyp:&nbsp;&nbsp;</b>{property['type']}<br>
                   <b>Pris:&nbsp;&nbsp;</b>{property['price']}<br>
                   <b>Storlek:&nbsp;&nbsp;</b>{property['size']}<br>
                   <b>Rum:&nbsp;&nbsp;</b> {property['rooms']}<br>
                   <a href='{property['link']}' target="_blank">Länk till bostad</a>'''
        iframe = folium.IFrame(html, width=170, height=130)
        popup = folium.Popup(iframe, max_width=170)
        
        # creating marker with attributes from its json-data and adding to its corresponding markercluster
        folium.Marker(property['coordinates'],
                      popup=popup,
                      tooltip=property['location'].title(),
                      icon=folium.Icon(color=colors[property['type']], icon = icons[property['type']], prefix='fa')
                     ).add_to(eval(f'{property["type"]}_marker_cluster'))
    # else: print(property['location'])

# add layercontrol (by adding markerclusters for every type to their corresponding featuregroup and then adding everything to the folium map)
for type in types:
    exec(f'{type}.add_child({type}_marker_cluster)\nmap.add_child({type})')
folium.map.LayerControl('topright', collapsed=False).add_to(map)

# saving map to html file and opening the file in a browser
map.save("map.html")
webbrowser.open("map.html")