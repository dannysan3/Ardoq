import csv
import matplotlib.pyplot as plt
import numpy as np
import calendar
import datetime

def makeGraph(file):

    filname = file

    fields = []
    rows = []

    with open(filname, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)



        print("Rows in total: %d"%(csvreader.line_num))

    rows.append(["2020-10-32","2020-10-32","0000"]) #to mark the end of the input lines



    duration = rows[0][2]


    date = rows[0][0][:11]


    count = 1
    average = int(duration)


    dicts = {}
    for row in rows[1:]:

        duration = row[2]



        if row[0][:11] == date:
            average += int(duration)
            count +=1
        else:
            dicts[date] = average/count
            date = row[0][:11]
            count = 1
            average = int(duration)




    keys = []
    values = []

    for key in dicts:
        keys.append(key[8:])
        values.append(dicts[key])



    maxValue = max(values)
    index = values.index(maxValue)
    minValue = min(values)
    indexMin = values.index(minValue)

    keys_list = list(dicts)


    minDate = keys_list[indexMin]
    maxDate = keys_list[index]


    minDay = findDay(minDate)
    maxDay = findDay(maxDate)




    fig = plt.figure()
    graph = fig.subplots()

    graph.annotate("Max: " + str(maxValue) + " Day: " + maxDay, xy =(index,maxValue),
    xytext =(index+1, maxValue+1 ),arrowprops=dict(facecolor='black', shrink=0.05),)

    graph.annotate("Min: " + str(minValue) + " Day: " + minDay, xy =(indexMin,minValue),
    xytext =(indexMin+1, minValue+1 ),arrowprops=dict(facecolor='black', shrink=0.05),)



    plt.xlabel("Dates")
    plt.ylabel("Average duration")
    plt.plot(keys,values)
    month = str(file[:-4])

    plt.title(month + " Oslo bysykkel")
    plt.show()

def findDay(date):
    daySplit = date.split("-")
    ans = datetime.date(int(daySplit[0]),int(daySplit[1]),int(daySplit[2]))
    day = calendar.day_name[ans.weekday()]
    return day




inp = input("Filename: ")

try:
    makeGraph(inp)
except FileNotFoundError:
    print("File not found, please use a valid csv file")
