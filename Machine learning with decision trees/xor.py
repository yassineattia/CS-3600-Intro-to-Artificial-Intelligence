
import NeuralNet
import Testing
import random

possibleExamples = [([0, 0], [0]), ([0, 1], [1]), ([1, 0], [1]), ([1, 1], [0])]


def createExamples(size):
    numTrain = size * 4 / 5
    numTest = size / 5
    training = []
    testing = []
    for i in range(numTrain):
        training.append(random.choice(possibleExamples))
    for i in range(numTest):
        testing.append(random.choice(possibleExamples))

    #print "Generated " + str(size) + " Examples \n"
    return training, testing


def xor():
    examples = createExamples(1000)
    result = []
    # no hidden layer
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[])[1])
    print "Layer 0 -> \n"
    print "Maximum: " + str(max(result)) + "\n Average: " + str(Testing.average(result)) +\
          " \nStandard Deviatio: " + str(Testing.stDeviation(result)) + "\n"

    # 1 in hidden layer
    result = []
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[1])[1])
    print " Layer 1 -> \n"
    print " Maximum: " + str(max(result)) + "\n Average: " + str(Testing.average(result)) +\
          "\n Standard Deviatio: " + str(Testing.stDeviation(result)) + "\n"

    # 2 in hidden layer
    result = []
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[2])[1])
    print "Layer 2 -> \n"
    print "Maximum: " + str(max(result)) + " \nAverage: " + str(Testing.average(result)) +\
          " \nStandard Deviatio: " + str(Testing.stDeviation(result)) + "\n"

    # 3 in hidden layer
    result = []
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[3])[1])
    print "Layer 3 -> \n"
    print "Maximum: " + str(max(result)) + " \nAverage: " + str(Testing.average(result)) +\
          " \nStandard Deviatio: " + str(Testing.stDeviation(result)) + "\n"


    result = []
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[4])[1])
    print " Layer 4 -> \n"
    print "Maximum: " + str(max(result)) + "\n Average: " + str(Testing.average(result)) +\
          "\n Standard Deviation: " + str(Testing.stDeviation(result)) + "\n"


    result = []
    for i in range(5):
        result.append(NeuralNet.buildNeuralNet(examples, maxItr=400, hiddenLayerList=[5])[1])
    print " Layer 5 -> \n"
    print "Maximum: " + str(max(result))  + " \n Average: " + str(Testing.average(result)) +\
          " \n Standardd Dev: " + str(Testing.stDeviation(result)) + "\n"

xor()