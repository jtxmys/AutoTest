import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def element():
    id = "id"
    xpath = "xpath"
    link_text = "link text"
    partial_link_text = "partial link text"
    name = "name"
    tag_name = "tag name"
    class_name = "class name"
    css_selector = "css selector"
def suppers(argess):
    return argess.upper()
def lowers(argess):
    return argess.lower()
def get(url):
    driver.get(url)
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
def deco(func):
    def wrapper(id):
        start = time.time()
        while True:
            try:
                func(id)
                break
            except :
                time.sleep(.5)
                end = time.time()
                print(end-start)
                if (end-start)>30:
                    raise TimeoutError("实在是找不到{}啊".format(id))
                    break
            # print(time.time())
    return wrapper

@deco
def ids(ID):
    return driver.find_element_by_id(ID)
@deco
def calsss(ID):
    return driver.find_element_by_class_name(ID)
@deco
def csss(ID):
    return driver.find_element_by_class_name(ID)
@deco
def xpaths(ID):
    return driver.find_element_by_class_name(ID)
@deco
def tagnames(ID):
    return driver.find_element_by_class_name(ID)

'''------------------以下是取elements方法'''
@deco
def elements_ids(ID):
    return driver.find_element_by_id(ID)
@deco
def elements_calsss(ID):
    return driver.find_element_by_class_name(ID)
@deco
def elements_csss(ID):
    return driver.find_element_by_class_name(ID)
@deco
def elements_xpaths(ID):
    return driver.find_element_by_class_name(ID)
@deco
def elements_tagnames(ID):
    return driver.find_element_by_class_name(ID)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    get('http://www.baidu.com')

    start = time.time()
    ids('kww')
    end = time.time()
    print(end-start)
    # element = WebDriverWait(driver,10).until(
    # EC.presence_of_element_located((By.ID, "kw111"))
