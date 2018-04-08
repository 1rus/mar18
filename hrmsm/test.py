import selenium.webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome import webdriver
from hrmsm.wrapconfig import Config
from hrmsm.webelement import WebElement
from hrmsm.base.FrameTest import FrameTestCase
import os
import os.path
import numpy
from math import factorial

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap_map = {
    "firefox": DesiredCapabilities.FIREFOX.copy(),
    "internet explorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "internetexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "iexplorer": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "ie": DesiredCapabilities.INTERNETEXPLORER.copy(),
    "chrome": DesiredCapabilities.CHROME.copy(),
    "opera": DesiredCapabilities.OPERA.copy(),
    "phantomjs": DesiredCapabilities.PHANTOMJS.copy(),
    "htmlunitjs": DesiredCapabilities.HTMLUNITWITHJS.copy(),
    "htmlunit": DesiredCapabilities.HTMLUNIT.copy(),
    "iphone": DesiredCapabilities.IPHONE.copy(),
    "ipad": DesiredCapabilities.IPAD.copy(),
    "android": DesiredCapabilities.ANDROID.copy(),
    "edge": DesiredCapabilities.EDGE.copy(),
    "safari": DesiredCapabilities.SAFARI.copy()
}

c=[]
c = Config()
c.prepare()
print(c.__dict__["_data"])
print(os.environ.items())
if "OUTPUT_DIR" in os.environ.keys():
    print("output dir already exists", str(os.environ["OUTPUT_DIR"])[-19:])

if isinstance(c, Config) and hasattr(c, "_data"):
    print("c has data")
    print(len(c.__dict__['_data']))
else:
    print("config not prepared")
'''
array_size = 10
number = 10
a = numpy.random.randint(10, size=array_size)
#a=[1,3,6,2,0,4,5,6,1,7]
print(a)
for i in range(array_size-1):
    if a[i]+a[i+1] == number:
        print(a[i], '\t', a[i+1], '\t', "summ equals %s\n" % number)

y = 1
print("y = %s" % y)
def fibR(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibR(n-1)+fibR(n-2)
print("fibo of %s with recursion = " % y, fibR(y))

fibo_array=[]
def fibY(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        yield a
for x in fibY(y):
    fibo_array.append(x)
print("fibo array of %s with generator = " % y, fibo_array)

def fibN(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
print("fibo of %s easy = " % y, fibN(y))

def factorial1(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def factorial2(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

print(factorial1(y), factorial2(y), factorial(y))
#browser = selenium.webdriver.Remote(command_executor='http://10.0.0.3:5555/wd/hub', desired_capabilities=caps, browser_profile=None)
'''
caps = cap_map['chrome']
browser = selenium.webdriver.Chrome()
browser.get('http://hrm.seleniumminutes.com')

browser.find_element_by_id('txtUsername').send_keys('admin')
browser.find_element_by_id('txtPassword').send_keys('Password')
browser.find_element_by_id('btnLogin').click()

browser.quit()
'''

#tc.setup_class()
#tc.setup_method(classmethod)
#print("len is - ", len(os.environ["OUTPUT_DIR"]))
if "OUTPUT_DIR" in os.environ.keys():
    print("length is not null, output dir is created")
    tc.take_numbered_screenshot()
    print(len(os.environ["SCREENSHOTS_DIR"]))
    tc.take_numbered_screenshot()
    print(tc.config)
else:
    raise Exception("configure error") '''

