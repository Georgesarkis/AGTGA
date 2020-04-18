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
            if "TestCase finished successfully" in str(myCmd.stdout):
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
    print("********************************************************************************************")
    print("*   FILENAME    *    PRIORITY    *  TEST-CASE LENGTH  *   BUG PRODUCED  *  EXCEPTION")
    print("********************************************************************************************")
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
                priority = " LOW  "

        print("* " + l.TestID +"  *      "   + priority + "      *         " + str(l.Length) + "         *       " + Reproduced + "     *  " + l.ExceptionMSG)
        print("____________________________________________________________________________________________")

        if l.Length > 18:
            avgLength = avgLength + l.Length
            numberOfTestList = numberOfTestList + 1
    print("*   Average Test-Case Length               =                         " + str(avgLength/numberOfTestList))
    print("********************************************************************************************")


if __name__ == "__main__":
    currentPath = os.getcwd()
    path = currentPath + '/TestSuite/TestSuite'
    os.chdir(path)

    FileList = os.listdir()
    TestList = PrepareTheList(FileList, path)
    TestList = Run(TestList)

    PrintTheResaults(TestList)
