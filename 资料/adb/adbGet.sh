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

    获取序列号：

 adb get-serialno
查看连接计算机的设备：

 adb devices
重启机器：

 adb reboot
重启到bootloader，即刷机模式：

 adb reboot bootloader
重启到recovery，即恢复模式：

 adb reboot recovery
查看log：

 adb logcat
终止adb服务进程：

 adb kill-server
重启adb服务进程：

 adb start-server
获取机器MAC地址：

 adb shell  cat /sys/class/net/wlan0/address
获取CPU序列号：

adb shell cat /proc/cpuinfo
安装APK：

adb install <apkfile> //比如：adb install baidu.apk
保留数据和缓存文件，重新安装apk：

adb install -r <apkfile> //比如：adb install -r baidu.apk
安装apk到sd卡：

adb install -s <apkfile> // 比如：adb install -s baidu.apk
卸载APK：

adb uninstall <package> //比如：adb uninstall com.baidu.search
卸载app但保留数据和缓存文件：

adb uninstall -k <package> //比如：adb uninstall -k com.baidu.search
启动应用：

adb shell am start -n <package_name>/.<activity_class_name>
查看设备cpu和内存占用情况：

adb shell top
查看占用内存前6的app：

adb shell top -m 6
刷新一次内存信息，然后返回：

adb shell top -n 1
查询各进程内存使用情况：

adb shell procrank
杀死一个进程：

adb shell kill [pid]
查看进程列表：

adb shell ps
查看指定进程状态：

adb shell ps -x [PID]
查看后台services信息：

adb shell service list
查看当前内存占用：

adb shell cat /proc/meminfo
查看IO内存分区：

adb shell cat /proc/iomem
将system分区重新挂载为可读写分区：

adb remount
从本地复制文件到设备：

adb push <local> <remote>
从设备复制文件到本地：

adb pull <remote>  <local>
列出目录下的文件和文件夹，等同于dos中的dir命令：

adb shell ls
进入文件夹，等同于dos中的cd 命令：

adb shell cd <folder>
重命名文件：

adb shell rename path/oldfilename path/newfilename
删除system/avi.apk：

adb shell rm /system/avi.apk
删除文件夹及其下面所有文件：

adb shell rm -r <folder>
移动文件：

adb shell mv path/file newpath/file
设置文件权限：

adb shell chmod 777 /system/fonts/DroidSansFallback.ttf
新建文件夹：

adb shell mkdir path/foldelname
查看文件内容：

adb shell cat <file>
查看wifi密码：

adb shell cat /data/misc/wifi/*.conf
清除log缓存：

adb logcat -c
查看bug报告：

adb bugreport
获取设备名称：

adb shell cat /system/build.prop
查看ADB帮助：

adb help
跑monkey：

adb shell monkey -v -p your.package.name 500