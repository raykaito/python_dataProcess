import os
import csv
import numpy as np

rootFolder = "H:/2021-09-13_Lily_3D_tracerTest/rootFolder/"

directories = os.listdir(rootFolder)
header = ["folder name : data count", "sum", "1stMoment", "2ndMoment", "3rdMoment", "4thMoment"]
data = []

for directory in directories:
    print("working on direcotry [" + directory + "]")
    csvDirectory = rootFolder + directory + "/imageJ/step4_AnalyzeConcentration/"
    xcsvDir = csvDirectory + "Concentration_X-Axis.csv"
    zcsvDir = csvDirectory + "Concentration_Z-Axis.csv"

    #Check if subDirectory Exists
    if not os.path.isfile(xcsvDir):
        print("the x-axis.csv file does not exist.")
        print("skipping to next direcotry.")
        continue
    if not os.path.isfile(zcsvDir):
        print("the z-axis.csv file does not exist.")
        print("skipping to next direcotry.")
        continue

    a = np.loadtxt(zcsvDir, skiprows = 1,delimiter=",")
    dataCount = np.shape(a)[1]
    for dataIndex in range(dataCount)[1:]:
        title = directory + "_data-" + str(dataIndex)
        slice = a[:,dataIndex]
        sum = np.sum(slice)
        firstMoment  = np.dot(a[:,0], slice) / sum
        indexOffset  = a[:,0] - firstMoment
        secondMoment = np.dot(indexOffset**2, slice) / sum
        thirdMoment  = np.dot(indexOffset**3, slice) / sum
        forthMoment  = np.dot(indexOffset**4, slice) / sum
        data.append([title, sum, firstMoment, secondMoment, thirdMoment, forthMoment])
    print(type(a))
    print("Data Count is " + str(dataCount))
    print(data)


with open(rootFolder + "data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in data:
        writer.writerow(row)