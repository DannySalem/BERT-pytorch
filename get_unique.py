import pdb

def get_unique():
    f = open("text-test.txt", "r")

    z = [x for x in f]


    file1 = open("MyFile1.txt","w+") 

    file1.writelines(set(z))
    file1.close()

def get_maxLength():

    with open('data/ChemBlDB.txt', "r") as f:
        maxLength=0
        for line in f:
            lineLength = len(line)
            if (lineLength > maxLength):
                maxLength = lineLength
            

    print(maxLength) #401


