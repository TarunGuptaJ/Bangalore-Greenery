'''
Top left corner
N 13°16'20.1372"
E 77°05'10.6255"

Bottom right corner
N 12°40'26.6713"
E 78°11'30.4167"

Distance calculated by Haverine formula
left to right = 119.6km
top to bottom = 66.52km

202 x 113

Dimensions of each box:-
left to right = 0.592...km
top to bottom = 0.589...km
almost same

So let something be at tile x,y
distance of the top right corner of the box will be at
x * 0.592 km right and y * 0.589 km below
'''

import math

f = open("places.csv")
coords = open("coords.rtf", "w")
lat1 = 13 + (16 / 60) + (26.6713 / 3600)
lng1 = 77 + (5 / 60) + (10.6255 / 3600)
lat1 = math.radians(lat1)
lng1 = math.radians(lng1)
R = 6371        # radius of earth
for line in f:
    s = line.split(',')
    lngdist = (119.6 / 202) * (int(s[0]) - 0.5)
    latdist = (66.52 / 113) * (int(s[1]) - 0.5)
    # getting the lat2
    c = latdist / R
    a = math.pow(math.sin(c / 2), 2)
    lat2 = lat1 - 2 * math.asin(math.sqrt(a))
    # getting lng2
    c = lngdist / R
    a = math.pow(math.sin(c / 2), 2)
    lng2 = lng1 - 2 * math.sqrt(a) * math.pow(1 / math.cos(lat1), 2)
    # convert and store in degrees, minutes and seconds
    lat2 = math.degrees(lat2)
    lng2 = math.degrees(lng2)
    dlat = int(lat2)
    mlat = int((lat2 - dlat) * 60)
    slat = (lat2 - dlat - (mlat / 60)) * 3600
    dlng = int(lng2)
    mlng = int((lng2 - dlng) * 60)
    slng = (lng2 - dlng - (mlng / 60)) * 3600
    final_latitude = "N" + str(dlat) + chr(186) + str(mlat) + '\'' + str(slat) + '\"' + ','
    coords.write(final_latitude)
    final_longitude = "E" + str(dlng) + chr(186) + str(mlng) + '\'' + str(slng) + '\"' + '\n'
    coords.write(final_longitude)