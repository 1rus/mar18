import selenium.webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome import webdriver
from hrmsm.wrapconfig import Config
from hrmsm.webelement import WebElement
from hrmsm.base.FrameTest import FrameTestCase
import os
import os.path

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
'''if "OUTPUT_DIR" in os.environ.keys():
    print("length is not null, output dir is created")
    tc.take_numbered_screenshot()
    print(len(os.environ["SCREENSHOTS_DIR"]))
    tc.take_numbered_screenshot()
    print(tc.config)
else:
    raise Exception("configure error") '''

