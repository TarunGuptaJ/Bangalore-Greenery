# Bangalore-Greenery
Places in Bangalore with lot of greenery according to Google map

[Dataset](https://drive.google.com/drive/folders/1a3UcbFKUPF9maoQxqVPGs6ERIv-N77TD?usp=sharing)


The dataset was collected using SASGIS to generate satellite images of bangalore. The dataset consists of 5016 satellite images.


First hsvtrack.py was used on the satellite images to determine the hsv range for green values. After this range was obtained green_percent.py is used to read all the images and create the csv file with the green percentage of each image.


After generating the csv file with the green percentages, the hadoop map-reduce code is executed to obtain the places with >75% green cover.

This map reduce code is split into three files Greater75-Driver, Mapper and Reducer. This code is compiled into a jar file and run on the hadoop filesystem. It takes two command line arguments, one for the path of the input csv file and one for the output path.

After this output is generated the indices of the locations are extracted using createPlaces.py and stored in places.csv.

Based on these indices we have used Haversine's formula to obtain the latitude and longitude of these locations which are stored in coords.rtf. This code is in getCoordsDegreeDec.py.

The closest location names are extracted from these coordinates and are stored in locationData.txt.

We have also written code to perform a visualisation of these data points using follium to plot the locations onto a map. This map can be seen in View_Map.ipynb

We have also written code to generate a heatmap of all the green percentages of the different blocks in create_heatmap.py
