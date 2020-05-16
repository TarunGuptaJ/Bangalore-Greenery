# Bangalore-Greenery
Places in Bangalore with lot of greenery according to Google map

---
> [Google Drive link](https://drive.google.com/drive/folders/1YK8cPM2ofDmusMXaA0jyx9KHpfJb79Rx?usp=sharing) for CCBD
---

## Project Description

1. The dataset was collected using [**SASGIS**](http://www.sasgis.org/) to generate satellite images of Bangalore. The dataset consists of [6840 satellite images](https://drive.google.com/drive/folders/1C-Uqv8cO7McPK_1byUVqoiHrNQAHc3he). The coordinates were obtained by visualizing a virtual rectangle around Bangalore City in Google Maps.

2. Then, the program *hsvtrack.py* was run on the satellite images to determine the hsv range for green values. The green values obtained had the lower bound of [40, 40, 0] and the upper bound was [120, 255, 255]. 

3. This range was used in *green_percent.py*. The code was run on each image to create the csv file with the green percentage of each image.

4. The coordinates of each image were extracted using the metadata of the geotiff files. This data is accessed using the [GDAL Package](https://gdal.org/) and these coordinates are stored in *coords_all.rtf*. The code to extract all coordinates is in *getCoordsAll.py*. Previously, the Haversine formula was used to get the coordinates and the code can be seen in *getCoordsDegreeDec.py*.

5. After generating the csv file with the green percentages, the Hadoop Map-reduce code is executed to obtain the places with >75% green cover.

6. This map reduce code is split into three files 
    1. Greater75-Driver
    2. Mapper
    3. Reducer 
 
7. This code is compiled into a .jar file and run on the Hadoop filesystem. It takes two command line arguments, one for the path of the input csv file and one for the output path.

8. The coordinates of these output images are extracted using *getCoords.py* and stored in *coords.rtf*.

9. The closest location names are extracted from these coordinates and are stored in *locationData.txt* using *getLocationName.py*. For this we used [Reverse Geocoder](https://pypi.org/project/reverse_geocoder/).

10. We have also written code to perform a visualisation of these data points using [Follium](https://pypi.org/project/folium/) to plot the locations onto a map. This map can be seen in *View_Map.ipynb*.

11. We have also written code to generate a heatmap of all the green percentages of the different blocks in *create_heatmap.py*.


