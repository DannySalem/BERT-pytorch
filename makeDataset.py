''' The Purpose of this script is to read a data corpus 
of SMILES strings and create two new datasets from it: Train and Test '''

import pdb
import random
import numpy


def makeDataset():
    #load corpus

    with open('data/aromatase_corpus.txt', "r") as f:
        #pdb.set_trace()
        datapoints = 0
        for i, line in enumerate(f):
            datapoints+=1
        trainset_ids = list(range(datapoints))
        testset_size = int(datapoints*0.15)
        testset_ids = random.sample(range(datapoints),  testset_size)
        for i in testset_ids:
            trainset_ids.remove(i)

    return datapoints, trainset_ids, testset_ids

datapoints, trainset_ids, testset_ids = makeDataset()
print(len(testset_ids))
print(len(trainset_ids))
print(datapoints)
test = numpy.array(testset_ids+trainset_ids)
print(len(numpy.unique(test)))


with open('data/aromatase_corpus.txt', "r") as f:
    trainfile = open('data/aromatase_traincorpus.txt', "w")
    testfile = open('data/aromatase_testcorpus.txt', "w")
    for i, line in enumerate(f):
        if i in testset_ids:
            testfile.write(line)
        else:
            trainfile.write(line)