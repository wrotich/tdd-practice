import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self, emp_1, emp_2):
        
        self.emp_1 = Employee('Corey', 'Schafer',50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)


    def test_email(self):
        
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.fname = 'John'
        self.emp_2.lname = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.fname = 'John'
        self.emp_2.lname = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


