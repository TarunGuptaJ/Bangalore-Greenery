'''
Top left corner
13.151955, 77.370003

Bottom right corner
12.803351,  77.777871

Distance calculated by Haverine formula
left to right = 44.16km
top to bottom = 38.76km

76x66

So let something be at tile x,y
distance of the top right corner of the box will be at
x * (44.16/76) km right and y * (38.76/66) km below
'''

import math

f = open("csv_files/places.csv")
coords = open("coords.rtf", "w")
lat1 = 13.151955
lng1 = 77.370003
lat1 = math.radians(lat1)
lng1 = math.radians(lng1)
R = 6371        # radius of earth
for line in f:
    s = line.split(',')
    lngdist = (44.16/76) * (int(s[0]) - 0.5)
    latdist = (38.76/66) * (int(s[1]) - 0.5)
    # getting the lat2
    c = latdist / R
    a = math.pow(math.sin(c / 2), 2)
    lat2 = lat1 - 2 * math.asin(math.sqrt(a))
    # getting lng2
    c = lngdist / R
    a = math.pow(math.sin(c / 2), 2)
    lng2 = lng1 - 2 * math.sqrt(a) * math.pow(1 / math.cos(lat1), 2)
    lat2 = math.degrees(lat2)
    lng2 = math.degrees(lng2)
    final_latitude = str(lat2) + ','
    coords.write(final_latitude)
    final_longitude = str(lng2) + '\n'
    coords.write(final_longitude)