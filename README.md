# AGTGA TOOL
This tool is used to automatically generated android GUI test cases using android Appium testing tool.
This tool can generate test-suite from apk, regardless if the apk is created using native android, cross-platform or hybrid application.


## Pre-requirements
To run this tool you need to have following tools/frameworks installed:
* python 3.*
* Appium Server
* Appium Client
* JDK

Moreover, you need to connect your android phone to your computer and confirm:
* Developer options is enabled on the android phone
* USB debugging in enabled on the android phone
* Android phone is recognized by the computer (should also worked with emulator. For how to setup with emulator, check: https://appium.io/)


## constrains
This tool will perform the best if:
* User already logged in to the app and accepted the permissions (user configurations should be save on the device)
* Andorid application should not have dependencies on external applications.
* Android application should not have inbuild video 


## How to install and start using
To run this tool:
* Start the appium server.
* Import the master branch and from terminal run following command:
```bash
py AGTGA.py -app = "PATH TO THE LOCATION OF THE APP YOU WANT TO TEST" 
            -wait = "DURCATION YOU WANT TO WAIT AFTER EVERY SINGLE CLICK"
            -deviceName = "NAME OF THE DEVICE YOU WANT TO TEST ON"
            -userName = "IF THE APPLICAITON  REQUIRES LOGIN PROCESS"       #(demo, default is "")             options: "" , username
            -password = "IF THE APPLICAITON  REQUIRES LOGIN PROCESS"       #(demo, default is "")             options: "" , password
            -testServer = "IF THE IS EXTRA STEP TO LOGIN TO TEST SERVER"   #(demo, default is false)          options: True, False
            -algo = "ALGARITHEM YOU WANT TO USE TO GENERATE THE TEST CASE" #(demo, default is ActionCoverage) options: ActionCoverage, LeakDetection
```

## Generated logs and screenshots
The AGTGA will generate a screenshot after every single actions it takes to invoke the GUI of the android app. Moreover, it will generate intensive log on which element was clicked, where was the location of the element and what was the current view on the screen.
Those logs and screenshots will automatically generate for every single test-case and with a goal to give the developer ability to better understand reason the bug accrued and how to regenerate it manually.
logs and screenshots can be found in "ScreenShots" folder. 

log and screenshots generated from the first test-case will have be "log0.txt" and the screenshots will be in folder "0" 

log and screenshots generated from the second test-case will have be "log1.txt" and the screenshots will be in folder "1"  and so on...


## Generated test-suite
Generated test-cases can be found in  "TestSuite/TestSuite" folder. 

### Pre-requirements
Same Pre-requirements to run the AGTGA tool and more:
* The phone the is used to generate the test-cases on should be the same as the found the test-case will run on.


### Generated test-case format
Generated test-cases will be python code that was generated on Appium format, for more info please check: https://appium.io


### How to run generated test-cases
To run the generated test-cases:
* Connect your android phone to the computer.
* Run Appium server.
* Run generated test cases using following commend:
```bash
    py TestCase0.py # to run the test-case 1
    py TestCase1.py # to run the test-case 2 .....
```


# Additional information
for more information please check: https://docs.google.com/document/d/1ifs-jdqyqSSAA2qixPVZZLl9UEur3YlRK174owTBOa0/edit?usp=sharing

The main algorithm can be found in https://drive.google.com/file/d/1vgK-Ent6BYPK_YaqoVxQvajgsGAtHjGI/view