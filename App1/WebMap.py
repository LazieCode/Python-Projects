import folium
import pandas as pd

vol = pd.read_csv("App1\Volcanoes.txt")
df = vol.copy()
df = df[1:]
df.columns = ["VOLCANX020","NUMBER","NAME","LOCATION","STATUS","ELEV","TYPE","TIMEFRAME","LAT","LON"]

lat = [float(i) for i in df.LAT]
lon = [float(i) for i in df.LON]
name = [i for i in df.NAME]
height = [i for i in df.ELEV]
map = folium.Map(location=[30,50], zoom_start=4, tiles= "Stamen Terrain")
fg = folium.FeatureGroup(name="Volcanoes")
fg1 = folium.FeatureGroup(name="Polygon")

def elev_to_color(elev):
    if(elev<= 1600):
        return "green"
    elif(elev> 1600 and elev< 3000):
        return 'blue'
    else:
        return 'red'

for lt,ln,el, nm in zip(lat,lon,height,name): # we can use zip to loop through multiple elements at the same time.
    map.add_child(folium.Marker(location= [lt, ln], popup = nm, icon=folium.Icon(color=elev_to_color(el))))

fg1.add_child(folium.GeoJson(data=open('App1\world.json', encoding='utf-8-sig').read(), 
                            style_function= lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                            else 'red'}))

map.add_child(fg)
map.add_child(fg1)
map.add_child(folium.LayerControl())

map.save("WebMap.html")
