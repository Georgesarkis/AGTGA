import os
from TestSuite.Test import Test
import subprocess


def PrintStart():
    print("*****************************************************************************************************************")
    print("*   FILENAME    *    PRIORITY    *  TEST-CASE LENGTH  *  NUMBER OF ACTIONS  *    BUG PRODUCED  *  EXCEPTION")
    print("*****************************************************************************************************************")

def PrintEnd(avg,actionavg):
    print("*   Average Test-Case Length               =                         " + avg)
    print("*   Average Action per Test-case           =                         " + actionavg)
    print("*****************************************************************************************************************")

def PrepareTheList(l, path):
    TestList = []
    for f in l:
        File = open(path + "/" + f)
        lineList = File.readlines()
        FileLength = len(lineList)
        File.close()

        File = open(path + "/" + f, "a")
        NumberOfActions = 0
        for l in lineList:
            if ".click()" in l or ".back()" in l:
                NumberOfActions = NumberOfActions + 1
        LastLine = lineList[len(lineList) - 1]
        if LastLine == "print('TestCase finished successfully')":
            File.close()
        else:
            File.write("print('TestCase finished successfully')")
            File.close()

        t = Test(f, None, False, FileLength, NumberOfActions)
        TestList.append(t)

    return TestList


def Run(TestList):
    for f in TestList:
        try:
            print("executing the " + f.TestID)
            path = "py " + str(f.TestID)
            myCmd = subprocess.run(path, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if "TestCase finished successfully" in str(myCmd.stdout):
                f.Reproduced = False
                f.ExceptionMSG = "None"
            elif "Error: socket hang up" in  str(myCmd.stderr):
                f.Reproduced = False
                f.ExceptionMSG = "Server-side error occurred. Please rerun this test-case"
            else:
                f.Reproduced = True
                f.ExceptionMSG = "test-case failed to execute with following message: " + str(myCmd.stderr)

        except Exception as e:
            f.Reproduced = True
            f.ExceptionMSG = str(e)
    return TestList


def PrintTheResaults(TestList):
    avgLength = 0
    avgAction = 0
    numberOfTestList = 0

    PrintStart()
    for l in TestList:
        Reproduced = "True" if l.Reproduced else "False"
        priority = " LOW  "
        if l.Reproduced:
            priority = "HIGH"
        else:
            if l.Length > 100:
                priority = " HIGH "
            elif l.Length > 50:
                priority = "MEDIUM"
            else:
                priority = " LOW"

        print("* " + l.TestID + "  *      " + priority + "      *         " + str(l.Length) + "         *       " + str(l.NumberOfActions) + "         *       " + Reproduced + "     *  " + l.ExceptionMSG)
        print("_________________________________________________________________________________________________________________")

        if l.Length > 18:
            avgLength = avgLength + l.Length
            avgAction = avgAction + l.NumberOfActions
            numberOfTestList = numberOfTestList + 1

    PrintEnd(str(avgLength / numberOfTestList), str(avgAction / numberOfTestList))


if __name__ == "__main__":
    currentPath = os.getcwd()
    path = currentPath + '/TestSuite/TestSuite'
    os.chdir(path)

    FileList = os.listdir()
    TestList = PrepareTheList(FileList, path)
    TestList = Run(TestList)

    PrintTheResaults(TestList)
