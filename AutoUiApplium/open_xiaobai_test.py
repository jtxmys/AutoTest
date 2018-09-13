# appium -a 127.0.0.1 -p 4723 -U 90a2a822  --no-reset
import time

from appium import webdriver
# import win32com.client
import os
def openApp(apppackage='com.jinchenshenghui.xbzd',appActivity='com.jinchenshenghui.xbzd.view.activity.home.WelcomeActivity'):
    # desired_caps['appActivity'] = 'com.jinchenshenghui.xbzd.view.activity.home.WelcomeActivity'
    devn = os.popen('adb devices').read()#获取设备id
    pfv = os.popen('adb shell getprop ro.build.version.release').read()#获取当前系统版本号例如android5.1 ：，（5.1）
    apppackage =  apppackage
    appActivity = appActivity

    devicename = str(devn).split('\n')[1]
    devicename = devicename.split('\t')[0]
    print(devicename)
    print(devn,type(devn),pfv,devicename)
    desired_caps = {'platformName' :'Android',
                    'platformVersion':pfv,
                    # 'deviceName':'OPPO R9M',
                    'deviceName':'vivo X21UD A',

                    'appPackage':apppackage,
                    'appActivity':appActivity,
                    'NoReset': True

                    # 'unicodeKeyboard' : True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return driver


# 获得机器屏幕大小x,y
def getSize(dr):
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    return (x, y)


# 屏幕向上滑动
def swipeUp(dr,t=100):
    l = getSize(dr)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起始y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    dr.swipe(x1, y1, x1, y2,t)


# 屏幕向下滑动
def swipeDown(dr,t=100):
    l = getSize(dr)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.25)  # 起始y坐标
    y2 = int(l[1] * 0.75)  # 终点y坐标
    dr.swipe(x1, y1, x1, y2,t)


# 屏幕向左滑动
def swipLeft(dr,t=100):
    l = getSize(dr)
    x1 = int(l[0] * 0.75)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.05)
    dr.swipe(x1, y1, x2, y1,t)


# 屏幕向右滑动
def swipRight(dr,t=100):
    l = getSize(dr)
    x1 = int(l[0] * 0.05)
    y1 = int(l[1] * 0.5)
    x2 = int(l[0] * 0.75)
    dr.swipe(x1, y1, x2, y1,t)
if __name__ == '__main__':

    driver = openApp()
    driver.implicitly_wait(30)
    time.sleep(10)
    for i in range(5):
        swipLeft(driver,1000)
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print(driver.get_window_size())
    # driver.tap([(567,1657)])
    time.sleep(2)
    #点击立即体验
    driver.find_element_by_id('com.jinchenshenghui.xbzd:id/tv_lead_next').click()
    # 点击x
    print('点击x')
    driver.find_element_by_id('com.jinchenshenghui.xbzd:id/iv_ad_close').click()
    # 点击我的
    print('点击我的')
    driver.find_elements_by_id('com.jinchenshenghui.xbzd:id/iv_tab_icon')[4].click()
    # 点击立即登录
    print()
    driver.find_element_by_id('com.jinchenshenghui.xbzd:id/tv_user_name').click()
    # driver.tap([(567,1542)])
    #点击密码登录com.jinchenshenghui.xbzd:id/tv_login_with_code_use_psw
    print()
    driver.find_element_by_id('com.jinchenshenghui.xbzd:id/tv_login_with_code_use_psw').click()

    #输入手机号com.jinchenshenghui.xbzd:id/et_login_with_psw_phone
    print('输入手机号')

    driver.find_element_by_id('com.jinchenshenghui.xbzd:id/et_login_with_psw_phone').send_keys('18713567520')
    # driver.hide_keyboard()
    #输入密码：com.jinchenshenghui.xbzd:id/et_login_with_psw_psw

    # driver.find_element_by_id('com.jinchenshenghui.xbzd:id/et_login_with_psw_psw').click()
    print('输入密码')
    driver.find_element_by_id('com.jinchenshenghui.xbzd:id/et_login_with_psw_psw').send_keys('qwer1234')
    # driver.hide_keyboard()
    print('输入密码')
    #点击登录com.jinchenshenghui.xbzd:id/tv_login_with_psw_login
    driver.find_element_by_id('com.jinchenshenghui.xbzd:id/tv_login_with_psw_login').click()
    phone = driver.find_element_by_id('com.jinchenshenghui.xbzd:id/tv_user_phone').text
    print(phone)
    assert(phone=='187****7520')
    time.sleep(2)
    print(x,y,'HELLO')
    print('hello world')
    driver.quit()
