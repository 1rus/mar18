from framework.base.base_page import BasePage
from framework.pages.login_page import LoginPage
from selenium.webdriver.common.keys import Keys
from framework.pages.elements.attribute import Attribute
from framework.pages.elements.checkbox import CheckBox
from framework.pages.elements.select import Select
from framework.pages.elements.input_textarea import Input
import random
import string
import array
import time
from selenium.common.exceptions import StaleElementReferenceException

locators = {
            'menu_pim': 'id=menu_pim_viewPimModule',
            'btn_add': 'id=btnAdd',
            'search_name': 'id=empsearch_employee_name_empName',
            'search_btn': 'id=searchBtn',
            'reset_btn': 'id=resetBtn',
            'add_btn': 'id=addBtn',
            'save_btn': 'id=btnSave',
            'delete_btn': 'id=btnDelete',
            'sidenav': 'id=sidenav',
            'search_css': 'css=.input.empsearch_employee_name_empName',
            'loaded': 'class=panel_resizable panel-preview',
            'search_id': 'id=empsearch_id',
            'search_title': 'id=empsearch_job_title',
            'result_table': 'css=table.hover',
            'num_of_columns': 'css=th.header',
            'num_of_records': 'css=td.left',
            'add_first_name': 'id=firstName',
            'add_last_name': 'id=lastName',
            'id_number': 'id=employeeId',
            'radio_gender': 'id=personal_optGender_',
            'select_martial_status': 'id=personal_cmbMarital',
            'check_login': 'id=chkLogin',
            'id_username': 'id=user_name',
            'id_password1': 'id=user_password',
            'id_password2': 'id=re_password',
            'login_sect': 'class=loginSection',
            'check_all': 'id=ohrmList_chkSelectAll',
            'confirm_modal': 'id=deleteConfModal',
            'conf_del_btn': 'id=dialogDeleteBtn',
}
base_url = 'http://hrm.seleniumminutes.com'
pim_url = '/symfony/web/index.php/pim/viewPimModule'
chars = string.ascii_uppercase + string.digits


class PIM_Page(BasePage):


    def __init__(self, driver):
        self.driver = driver
        page = LoginPage(self.driver)
        page.open()
        page.login_with("admin", "Password")

    def open(self):
        self.driver.get(base_url+pim_url)

    def delete_employee_by_name(self, name):
        self.find_employee_by_name(name)
        CheckBox(self.driver, locators['check_all']).__set__('')
        self.driver.find_element_by_locator(locators['delete_btn']).click()
        for handle in self.driver.window_handles:
            self.driver.switch_to_window(handle)
            if self.driver.is_visible(locators['confirm_modal']):
                self.driver.find_element_by_locator(locators['conf_del_btn']).click()

    def find_employee_by_id(self, emp_id):
        self.driver.find_element_by_locator(locators['reset_btn']).click()
        Input(self.driver, locators['search_id']).__set__(emp_id)
        self.driver.find_element_by_locator(locators['search_btn']).click()
        return self.wrap_results()

    def find_employee_by_title(self, title):
        self.driver.find_element_by_locator(locators['reset_btn']).click()
        Select(self.driver, locators['search_title']).__set__('text='+title)
        self.driver.find_element_by_locator(locators['search_btn']).click()
        return self.wrap_results()

    def find_employee_by_name(self, _name):
        self.driver.find_element_by_locator(locators['reset_btn']).click()
        self.wait_for_value_change(Attribute(locators['search_name'], 'class'), 'loading')
        Input(self.driver, locators['search_name']).__set__(_name + Keys.SPACE + Keys.ESCAPE)
        self.driver.find_element_by_locator(locators['search_btn']).click()
        return self.wrap_results()

    def add_employee(self, _employee):
        self.driver.find_element_by_locator(locators['btn_add']).click()
        emp_first_name, emp_last_name, emp_pass, gender, martial_status = _employee
        Input(self.driver, locators['add_first_name']).__set__(emp_first_name)
        Input(self.driver, locators['add_last_name']).__set__(emp_last_name)
        if self.driver.is_visible(locators['login_sect']) is False:
            CheckBox(self.driver, locators['check_login']).__set__('3')
        login_name = emp_first_name+'_'+''.join(random.choices(chars, k=6))
        Input(self.driver, locators['id_username']).__set__(login_name)
        Input(self.driver, locators['id_password1']).__set__(emp_pass)
        Input(self.driver, locators['id_password2']).__set__(emp_pass)
        emp_id = int(Attribute(locators['id_number'], 'value').__get__(self.driver))
        self.driver.find_element_by_locator(locators['save_btn']).click()
        self.wait_for_available(locators['sidenav'])
        self.driver.find_element_by_locator(locators['save_btn']).click()
        if gender == 'Male':
            CheckBox(self.driver, locators['radio_gender']+'1').__set__(gender)
        else:
            CheckBox(self.driver, locators['radio_gender']+'2').__set__(gender)
        Select(self.driver, locators['select_martial_status']).__set__('text='+martial_status)
        self.driver.find_element_by_locator(locators['save_btn'])
        return emp_id, login_name

    def wrap_results(self):
        employees = [[]]
        self.driver.find_element_by_locator(locators['result_table'])
        num_of_columns = len(self.driver.find_elements_by_locator(locators['num_of_columns']))
        records = self.driver.find_elements_by_locator(locators['num_of_records'])
        num_of_emp = 0
        iterator = 1
        for e in records:
            if iterator != num_of_columns:
                employees[num_of_emp].append(e.text)
                iterator = iterator + 1
            elif iterator * (num_of_emp+1) == len(records):
                break
            else:
                employees.append([])
                iterator = 1
                num_of_emp = num_of_emp+1
        if not employees[0]:
            return None, 0
        else:
            return employees, num_of_emp+1



