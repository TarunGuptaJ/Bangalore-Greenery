f = open('green_new.csv', 'r')
new_f = open('green_above_75.csv', 'w')
for line in f:
    underscore = line.find('_')
    hyphen = line.find('-')
    dot = line.find('.')
    start = line.find(',')
    end = start + 1 + line[start + 1:].find(',')
    number = line[start + 1:end]
    number = float(number)
    xval = line[underscore + 1:hyphen]
    yval = line[hyphen+1:dot]
    if number >= 75:
        number = 100
        s = str(xval)+','+str(yval)
        print(s)
    else:
        number = 0
    newtext = line[:start] + ',' + str(number) + ',' + xval + ',' + yval +'\n'
    new_f.write(newtext)
    