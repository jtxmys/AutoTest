# appium -a 127.0.0.1 -p 4723 -U 90a2a822  --no-reset
from appium import webdriver
# import win32com.client
import os
def openApp(apppackage='com.android.bbkcalculator',appActivity='com.android.bbkcalculator.Calculator'):
    devn = os.popen('adb devices').read()#获取设备id
    pfv = os.popen('adb shell getprop ro.build.version.release').read()#获取当前系统版本号
    apppackage =  apppackage
    appActivity = appActivity

    devicename = devn[25:33]
    print(devicename)

    desired_caps = {'platformName' :'Android',
                    'platformVersion':pfv,
                    'deviceName':devicename,
                    'appPackage':apppackage,
                    'appActivity':appActivity
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


if __name__ == '__main__':

    openApp()