import argparse
import sys, getopt
from Algo import Main

desired_caps = {  # UiAutomator2 UiAutomator1 Espresso
    "automationName": "UiAutomator2",
    "deviceName": "",
    "platformName": "Android",
    "app": '',
    "autoGrantPermissions": "true",
    "appWaitActivity": "*.*",
    "fullreset": "false",
    "noReset": "true"
    # "appActivity" : ".*"
}


def main(pathToApk="F:/AGTGA/APKS/posifon.apk", deviceName="Moto G (5)", durationToWait=4, userName='demo4@konto.se',
         password='Sommar2018', algo='LeakDetection', TestServer=False):
    desired_caps["app"] = pathToApk
    desired_caps["deviceName"] = deviceName
    if userName is None or password is None:
        userName = ""
        password = ""
    Main.run(desired_caps, userName, password, algo, durationToWait, TestServer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("APKPath", help="Path to the location of the apk you want to test")
    parser.add_argument("DeviceName", help="Name of the device that is connected to your computer and you want to test on")
    parser.add_argument("Duration", help="Duration to wait in seconds after every single action")
    parser.add_argument("Algo", help="Algorithm you want to use to generate the test case, available options: ActionCoverage, LeakDetection")

    parser.add_argument("--Username", help="Username of the login if app requires login")
    parser.add_argument("--Password", help="Password of the login if app requires login")
    parser.add_argument("--TestServer", help="If exist will connect to test server", action="store_true")

    args = parser.parse_args()

    main(args.APKPath, args.DeviceName, args.Duration, args.userName, args.Password, args.TestServer)
