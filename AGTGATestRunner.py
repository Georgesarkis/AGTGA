import os

currentPath = os.getcwd()

os.chdir(currentPath + '/TestSuite/TestSuite')

list = os.listdir()

for f in list:
    path = "py " + str(f)
    print(path)
    os.system(path)
