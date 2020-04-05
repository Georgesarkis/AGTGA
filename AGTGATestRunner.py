import os

currentPath = os.getcwd()

os.chdir(currentPath + '/TestSuite/TestSuite')

list = os.listdir()

for f in list:
    try:
        print("executing the " + f)
        path = "py " + str(f)
        print(path)
        os.system(path)
    except Exception as e:
        print("test-case " + f + " has detected bug")
        print("with exception: " + str(e))

