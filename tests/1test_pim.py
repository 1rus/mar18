from hrmsm.base.FrameTest import FrameTestCase
from hrmsm.pages.pim_page import PIM_Page
import pytest

name = "Smith"
title = "QA Engineer"
employee = ['Amanda', 'Black', 'P1234567890', 'Female', 'Single']
empid = "0781"


class Test_PIM(FrameTestCase):

    def test_search_employee_by_id(self):
        page.open()
        employee = page.find_employee_by_id(empid)
        print(employee, '  =  ', empid)

    def test_search_employee_by_name(self):
        page.open()
        employees, num_of_employees = page.find_employee_by_name(name)
        print('our employees with name - ', name, ' total count - ', num_of_employees)
        print(employees, num_of_employees)

    def test_search_employee_by_title(self):
        page.open()
        employees, num_of_employees = page.find_employee_by_title(title)
        print('our employees with title - ', title, ' total count - ', num_of_employees)
        print(employees, num_of_employees)

    def test_add_employee(self):
        page.open()
        emp_id, emp_username = page.add_employee(employee)
        print(emp_id, emp_username)
        self.assertions.verify_true(emp_id is not None)
        self.assertions.verify_true(len(emp_username) > 0)

    def test_delete_employee_by_name(self):
        page.open()
        page.delete_employee_by_name(name)
        employees, num_of_employees = page.find_employee_by_name(name)
        self.assertions.verify_true(employees is None)
        self.assertions.verify_true(num_of_employees == 0)
