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

def q6():
	print("")

    print("Question 6 Pen Data starting")
    print("-----------------------------------------------------------")
    for i in range(0, 41, 5):
        pen_results = []
        for _ in range(5):
            pen_results.append(testPenData([i])[1])
        print("pen data perceptrons: {}".format(i))
        printResults(pen_results)


q6()