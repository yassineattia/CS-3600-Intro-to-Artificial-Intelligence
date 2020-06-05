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

testCarData()

def q5Test():
    print "Question Test starting\n"
    print "Pen Data is testing\n"
    
    iteration = 0
    penDataList = []
    while iteration < 5:
        penNet, testAccuracy = testPenData()
        penDataList.append(testAccuracy)
        iteration += 1

    print "Pen Data's average is:", average(penDataList)
    print "Pen Data's max is:", max(penDataList) 
    print "Pen Data's stad dev is:", stDeviation(penDataList)
    print "\n"

    print "Car Data is testing\n"
    iteration = 0
    carDataList = []
    while iteration < 5:
        carNet, testAccuracy = testCarData()
        carDataList.append(testAccuracy)
        iteration += 1

    print "Car Data's average is:", average(carDataList)
    print "Car Data's max is:", max(carDataList)   
    print "Car Data's stad dev is:", stDeviation(carDataList)
    print "\n"

q5Test()