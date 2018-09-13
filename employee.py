class Employee:
    """A sample Employee class"""

    raise_amnt = 1.05

    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.fname,self.lname)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)