output = open("output","r")
places = open("../csv_files/places.csv","w")
data = output.readlines()
for i in data:
    fileName = i.split()[0][4:-4]
    fileName = fileName.replace('-',',')
    print(fileName,file = places)

