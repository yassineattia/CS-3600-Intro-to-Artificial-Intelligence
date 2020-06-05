from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)

def printResults(results):
    print("average: {}".format(average(results)))
    print("maximum:     {}".format(max(results)))
    print("standard deviation:     {}".format(stDeviation(results)))

testCarData()

def q5():
    print("Question 5 Pen Data starting")
    print("-----------------------------------------------------------")
    pen_results = []
    for i in range(5):
        pen_results.append(testPenData()[1])
    printResults(pen_results)


    print("Question 5 car Data starting")
    print("-----------------------------------------------------------")
    car_results = []
    for i in range(5):
        car_results.append(testCarData()[1])
    printResults(car_results)

def q6():
    # print("")

    # print("Question 6 Pen Data starting")
    # print("-----------------------------------------------------------")
    # for i in range(0, 41, 5):
    #     pen_results = []
    #     for _ in range(5):
    #         pen_results.append(testPenData([i])[1])
    #     print("pen data perceptrons: {}".format(i))
    #     printResults(pen_results)

    
    print("Question 6 Car Data starting")
    print("-----------------------------------------------------------")

    for i in range(0, 41, 5):
        car_results = []
        for _ in range(5):
            car_results.append(testCarData([i])[1])
        print("car data perceptrons: {}".format(i))
        printResults(car_results)


q6()
