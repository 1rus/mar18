from framework.pages.pim_page import PIM_Page
from framework.pages.login_page import LoginPage
from framework.base.FrameTest import FrameTestCase
import pytest


name = "Smith"
title = "QA Engineer"
employee = ['Amanda', 'Black', 'P1234567890', 'Female', 'Single']
empid = "0781"


@pytest.mark.incremental
class Test_PIM(FrameTestCase):

    def test_search_employee_by_id(self):
        self.page = PIM_Page(self.driver)
        self.page.open()
        employee = self.page.find_employee_by_id(empid)
        self.take_numbered_screenshot()

    def test_search_employee_by_title(self):
        self.page = PIM_Page(self.driver)
        self.page.open()
        employees, num_of_employees = self.page.find_employee_by_title(title)
        self.take_numbered_screenshot()

    def test_add_employee(self):
        self.page = PIM_Page(self.driver)
        self.page.open()
        emp_id, emp_username = self.page.add_employee(employee)
        self.assertions.verify_true(emp_id is not None)
        self.assertions.verify_true(len(emp_username) == 0)
        self.take_numbered_screenshot()

