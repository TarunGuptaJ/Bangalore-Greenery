# Bangalore-Greenery
Places in Bangalore with lot of greenery according to Google map

[CCBD](https://drive.google.com/drive/folders/1YK8cPM2ofDmusMXaA0jyx9KHpfJb79Rx?usp=sharing)


The dataset was collected using SASGIS to generate satellite images of bangalore. The dataset consists of 6840 satellite images.


First hsvtrack.py was used on the satellite images to determine the hsv range for green values. After this range was obtained green_percent.py is used to read all the images and create the csv file with the green percentage of each image.

The coordinates of each image are extracted using the metadata of the geotiff files. This data is accessed using the gdal package and these coordinates are stored in coords_all.rtf, the coordinate extraction code is getCoordsAll.py

After generating the csv file with the green percentages, the hadoop map-reduce code is executed to obtain the places with >75% green cover.

This map reduce code is split into three files Greater75-Driver, Mapper and Reducer. This code is compiled into a jar file and run on the hadoop filesystem. It takes two command line arguments, one for the path of the input csv file and one for the output path.

The coordinates of these output images are extracted using getCoords.py and stored in coords.rtf

The closest location names are extracted from these coordinates and are stored in locationData.txt using getLocationName.py.

We have also written code to perform a visualisation of these data points using follium to plot the locations onto a map. This map can be seen in View_Map.ipynb

We have also written code to generate a heatmap of all the green percentages of the different blocks in create_heatmap.py


