import requests
class GetImg():
    '''会生成很多的png图片，如果想要删除，直接去目录下边执行cmd命令    del *.png   '''
    def get_img(info=True):
        n=1
        while True:
            a = requests.get('http://859j7.cn/index.php?m=Common&a=verify')
            print(a)
            with open("img_png{}.png".format(n),'wb') as f:
                f.write(a.content)
                print(n)
            n += 1
if __name__ == '__main__':
    GetImg.get_img()