from osgeo import gdal
output = open("output","r")
places = open("../coords.rtf","w")
data = output.readlines()
for i in data:
    fileName = "../images/" + i.split()[0]
    ds = gdal.Open(fileName)
    width = ds.RasterXSize
    height = ds.RasterYSize
    gt = ds.GetGeoTransform()
    minx = gt[0]
    miny = gt[3] + width*gt[4] + height*gt[5] 
    maxx = gt[0] + width*gt[1] + height*gt[2]
    maxy = gt[3] 
    cenx = (minx + maxx)/2
    ceny = (miny + maxy)/2
    print(ceny,cenx,sep = ",",file = places)
