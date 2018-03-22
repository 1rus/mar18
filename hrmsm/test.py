import selenium.webdriver
from selenium.webdriver.chrome import options
import selenium.webdriver.chrome
from hrmsm.wrapconfig import Config
import os


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




cwd = os.path.join(os.getcwd())
print(cwd)

upper = os.path.dirname(cwd)
print('upper = %s' % upper)

upper2 = os.path.join("..", cwd)
print('upper2 = %s' % upper2)
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
cf = Config()
cf.prepare()
print(os.environ["OUTPUT_DIR"])
