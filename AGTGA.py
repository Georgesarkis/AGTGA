# Copyright (c) 2020-present, George Sarkisian. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#
#     * The names of the contributors may not be used to endorse or
#       promote products derived from this software without specific
#       prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
usage: py AGTGA.py F:/AGTGA/APKS/****.apk "Moto G (5)" LeakDetection 3 --Username=demo@demo.com --Password=********* --TestServer --Verbose
"""
import argparse
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


def main(pathToApk="F:/AGTGA/APKS/posifon.apk", deviceName="Moto G (5)", algo='LeakDetection', durationToWait=3, userName=None,password=None, TestServer=False, Verbose=False):
    desired_caps["app"] = pathToApk
    desired_caps["deviceName"] = deviceName
    if userName is None or password is None:
        userName = ""
        password = ""
    Main.run(desired_caps, userName, password, algo, durationToWait, TestServer,Verbose)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("APKPath", help="Path to the location of the apk you want to test")
    parser.add_argument("DeviceName", help="Name of the device that is connected to your computer and you want to test on")
    # TODO Leak detection is disabled because it returns alot of false positives.
    # parser.add_argument("Algo", help="Algorithm you want to use to generate the test case, available options: ActionCoverage, LeakDetection")
    parser.add_argument("Duration", help="Duration to wait in seconds after every single action")

    parser.add_argument("--Username", help="Username of the login if app requires login")
    parser.add_argument("--Password", help="Password of the login if app requires login")
    parser.add_argument("--TestServer", help="If exist will connect to test server", action="store_true")
    parser.add_argument("--Verbose", help="If exist verbose will be enabled", action="store_true")

    args = parser.parse_args()

    # TODO Leak detection is disabled because it returns alot of false positives.
    # main(args.APKPath, args.DeviceName,  args.Algo, int(args.Duration), args.Username, args.Password, args.TestServer)
    main(args.APKPath, args.DeviceName,  "ActionCoverage", int(args.Duration), args.Username, args.Password, args.TestServer, args.Verbose)
