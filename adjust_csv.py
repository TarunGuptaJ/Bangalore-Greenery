'''
This code does the mapreduce on the existing heatmap created.
We create a new csv file from the old green_new.csv and set all
percentage values >= 75 as 100 and the others as 0.
When we generate the heatmap again we get the places
on the map with atleast 75% greenery
'''
f = open('csv_files/green400090255255.csv', 'r')
new_f = open('csv_files/green_above_75.csv', 'w') # change to green_all.csv
for line in f:
    # getting the positions of certain characters for extracting the percentage
    underscore = line.find('_')
    hyphen = line.find('-')
    dot = line.find('.')
    start = line.find(',')
    # extracting the number
    number = line[start + 1:]
    number = float(number)
    # we need the x and y values to output in the csv again
    xval = line[underscore + 1:hyphen]
    yval = line[hyphen + 1:dot]
    # manual mapreduce ; comment for green_all.csv
    if number >= 75:
        number = 100
        # printing the box coordinates for later use to find actual coords
        s = str(xval)+','+str(yval)
        print(s)
    else:
        number = 0
    newtext = line[:start] + ',' + str(number) + ',' + xval + ',' + yval +'\n'
    new_f.write(newtext)
    