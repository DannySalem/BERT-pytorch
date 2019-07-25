import pdb

f = open("text-test.txt", "r")

z = [x for x in f]


file1 = open("MyFile1.txt","w+") 

file1.writelines(set(z))
file1.close()