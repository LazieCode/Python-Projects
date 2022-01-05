# Generating interactive web maps with python
# we are going to be building the web map using the folium library of python

import folium

map = folium.Map(location=[30,50], zoom_start=4, tiles= "Stamen Terrain")

# To add a marker to the map what we are doing is basically adding a child so we will use the add_child method
# map.add_child(folium.Marker(location=[20,70],popup="Hey there")) 

map.add_child(folium.Marker(location=[20,70],popup="Hey there")) # one way of doing it

# By using a feature group what we can do is basically keep the map clean and stack up the whole data in a feature group and then later add that feature group to the map.
# So we can have different feature groups for different layers and this is how we can have different layers in a map.
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[30,80], popup="Using fg", icon=folium.Icon(color="Red")))

map.add_child(fg)

map.save("Map.html")
