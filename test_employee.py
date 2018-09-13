import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        """SetUp method, invoked at the beginning of every test"""
        self.emp_1 = Employee('Corey', 'Schafer',50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def test_email(self):
        """Tests whether the correct email is returned"""
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
        # introduce new variables
        self.emp_1.fname = 'John'
        self.emp_2.fname = 'Jane'
        """check if the second variables are correctly used
        to return correct fullnames"""
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        """Tests whether the correct fullname is returned"""
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        # introduce new variables
        self.emp_1.fname = 'John'
        self.emp_2.fname = 'Jane'
        """check if the second variables are correctly used
        to return correct fullnames"""
        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        """Test whether an employee who has applied for a raise
        can receive correct amount"""
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        """Tests the monthly schedule using Mock class and patch.
        This enables the mocking of the site we are accessing regardless of its availability"""
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.emp_1.monthly_schedule('May')
            # Check that the mock was called with the specified arguments
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')
            mocked_get.return_value.ok = False
            # Use different arguments
            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Schafer/June')
            self.assertEqual(schedule, 'Bad Response!')

    def tearDown(self):
        """method invoked after the every test"""
        pass


if __name__ == '__main__':
    unittest.main()


