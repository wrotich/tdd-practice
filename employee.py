import requests

class Employee:
    """A sample Employee class"""

    raise_amnt = 1.05

    def __init__(self,fname,lname,pay):
        """Constructor method"""
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @property
    def email(self):
        """Method for setting up email(email combination"""
        return '{}.{}@email.com'.format(self.fname,self.lname)
    
    @property
    def fullname(self):
        """Method for setting up the fullname"""
        return '{} {}'.format(self.fname,self.lname)
    
    def apply_raise(self):
        """A method for calculating an employee's raise"""
        self.pay = int(self.pay * self.raise_amnt)

    def monthly_schedule(self,month):
        """A method that eneables the fetching of an individual's raise in a given month"""
        response = requests.get(f'http://company.com/{self.lname}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'
        