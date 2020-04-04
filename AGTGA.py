import sys, getopt
from Algo import Main

desired_caps = {# UiAutomator2 UiAutomator1 Espresso
    "automationName" : "UiAutomator2",
    "deviceName": "",
    "platformName": "Android",
    "app": '',
    "autoGrantPermissions" : "true",
    "appWaitActivity" : "*.*",
    "fullreset" : "false",
    "noReset" : "true"
    #"appActivity" : ".*"
}


def main(argv):
    pathToApk = ''
    deviceName = ''
    durationToWait = None
    userName = ''
    password = ''

    try:
        opts, args = getopt.getopt(argv, "hp:d", ["p=", "d="])
    except getopt.GetoptError:
        print("error accured")
        print('test.py -p <apk path> -d <device name> -w <duraition to wait in milliseconds> -u <username> -p <password>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -p  <apk path> -d <device name> -w <duraition to wait in milliseconds> -u <username> -p <password>')
            sys.exit()
        elif opt in ("-p", "--app"):
            pathToApk = arg
        elif opt in ("-d", "--deviceName"):
            deviceName = arg
        elif opt in ("-w", "--durationToWait"):
            durationToWait = arg
            durationToWait = int(float(durationToWait))
        elif opt in ("-u", "--username"):
            userName = arg
        elif opt in ("-p", "--password"):
            password = arg

    print('pathToApk file is "', pathToApk)
    print('deviceName is "', deviceName)
    print('duration To Wait after every action is "', durationToWait)
    print('userName is "', userName)
    print('Password is "', password)

    desired_caps["app"] = pathToApk
    desired_caps["deviceName"] = deviceName


def main1():
    #-primary= 'NULLPOINTEXCEPTION' -secondary= 'TESTLENGTH'
    #FOR TESTING
    pathToApk = 'F:/AGTGA/APKS/posifon.apk'
    deviceName =  'Moto G (5)'##'Moto Z3 Play'
    desired_caps["app"] = pathToApk
    desired_caps["deviceName"] = deviceName
    durationToWait = 4
    userName = ""#'demo4@konto.se'
    password = ""#'Sommar2018'
    algo = 'ActionCoverage'
    TestServer = False
    Main.run(desired_caps, userName, password, algo, durationToWait , TestServer)


if __name__ == "__main__":
    #main(sys.argv[1:])
    main1()
