import os
from TestSuite.Test import Test
import subprocess


def PrepareTheList(l, path):
    TestList = []
    for f in l:
        File = open(path + "/" + f, "a")
        File.write("print('TestCase finished successfully') \n")
        File.close()
        File = open(path + "/" + f)
        FileLength = len(File.readlines())
        File.close()
        t = Test(f, None, False, FileLength)
        TestList.append(t)

    return TestList


def Run(TestList):
    for f in TestList:
        try:
            print("executing the " + f.TestID)
            path = "py " + str(f.TestID)
            myCmd = subprocess.run(path, stdout=subprocess.PIPE)
            if myCmd == "TestCase finished successfully":
                f.Reproduced = False
                f.ExceptionMSG = "None"
            else:
                f.Reproduced = True
                f.ExceptionMSG = str(myCmd.stdout)

        except Exception as e:
            f.Reproduced = True
            f.ExceptionMSG = str(e)
    return TestList


def PrintTheResaults(TestList):
    avgLength = 0
    numberOfTestList = 0
    print("************************************************************************")
    print("*   FILENAME    *   TEST-CASE LENGTH  *   BUG PRODUCED  *      EXCEPTION")
    print("************************************************************************")
    for l in TestList:
        Reproduced = "True" if l.Reproduced else "False"
        print("* " + l.TestID + "  *         " + str(l.Length) + "          *       " + Reproduced + "      *  " + l.ExceptionMSG)
        print("________________________________________________________________________")
        if l.Length > 18:
            avgLength = avgLength + l.Length
            numberOfTestList = numberOfTestList + 1
    print("*   Average Test-Case Length  =              " + str(avgLength/numberOfTestList) +"         *")
    print("************************************************************************")


if __name__ == "__main__":
    currentPath = os.getcwd()
    path = currentPath + '/TestSuite/TestSuite'
    os.chdir(path)

    FileList = os.listdir()
    TestList = PrepareTheList(FileList, path)
    TestList = Run(TestList)

    PrintTheResaults(TestList)
