import os

import time
import random
#除了点击就是滑动，没啥可记得
while 1:
    time.sleep(0.5)
    os.popen('adb shell  input swipe 600 1314 600 600')
    time.sleep(1)
    os.popen('adb shell  input tap 120 1690')
    time.sleep(1)
    os.popen('adb shell  input tap 50 141')
    time.sleep(1)
    m = random.randint(10, 30)
    print(m)
    for i in range(random.randint(1, m)):
        # time.sleep(1)
        os.popen('adb shell  input swipe 600 600 600 1314')
        time.sleep(0.5)
        os.popen('adb shell  input swipe 600 2000 600 600')
        time.sleep(0.1)

    os.popen('adb shell  input swipe 600 1314 600 600')
    time.sleep(0.5)


