import reverse_geocoder as rg
data = open("coords.rtf","r")
loc = open("locationData.txt","w")
coordinates = data.readlines()
for i in coordinates:
    coord = i.split(",")
    coord[0] = float(coord[0])
    coord[1] = float(coord[1])
    print(rg.search(coord),file = loc)
loc.close()
data.close()