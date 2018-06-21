# appium -a 127.0.0.1 -p 4723 -U 90a2a822  --no-reset
from appium import webdriver
# import win32com.client
import os
def openApp(apppackage='com.jinchenshenghui.xbzd',appActivity='.view.activity.home.MainActivity'):
    devn = os.popen('adb devices').read()#获取设备id
    pfv = os.popen('adb shell getprop ro.build.version.release').read()#获取当前系统版本号
    apppackage =  apppackage
    appActivity = appActivity

    devicename = str(devn).split('\n')[1]
    devicename = devicename.split('\t')[0]
    print(devicename)
    print(devn,type(devn))
    desired_caps = {'platformName' :'Android',
                    'platformVersion':pfv,
                    'deviceName':devicename,
                    'appPackage':apppackage,
                    'appActivity':appActivity
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


if __name__ == '__main__':

    openApp()