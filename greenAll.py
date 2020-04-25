og = open("csv_files/green.csv","r")
new = open("csv_files/green_all.csv","w")
print("Area,Percentage,xval,yval",file = new)

for i in og.readlines():
    Val = i.split(",")[0][4:-4]
    Val = Val.replace('-',',')
    print(i[:-1],Val,sep = ",",file = new)

og.close()
new.close()