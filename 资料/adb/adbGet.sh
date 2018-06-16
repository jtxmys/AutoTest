#Android命令

    #获取手机名称

    GET_PHONE_NAME = 'adb shell getprop ro.product.model'

    #获取手机版本

    GET_PHONE_VERSION = 'adb shell getprop ro.build.version.release'

    #获取手机厂商

    GET_PHONE_PRODUCER = 'adb shell getprop ro.product.brand'

    #获取手机已安装的输入法

    GET_PHONE_HAD_IME = 'adb shell ime list -s'

    #获取手机当前输入法

    GET_PHONE_CURRENT_IME = 'adb shell settings get secure default_input_method'

    #设置手机输入法

    SET_PHONE_IME = 'adb shell settings put secure default_input_method' #此方法后面必须再加包名

    #获取手机分辨率

    GET_SCREEN_SIZE = 'adb shell wm size'

    #非中文输入

    INPUT_TEXT = 'adb shell input text'