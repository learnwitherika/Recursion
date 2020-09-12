# import csv
# empfile = open("test.csv")
# reader = csv.reader(empfile)

class Person():
    firstname = ""
    lastname = ""
    gender = ""
    id = 0
    personid = 0

    def __init__(self, fn, ln, g):
        self.firstname = fn
        self.lastname = ln
        self.gender = g
        Person.id = Person.id + 1
        self.personid = Person.id

    def get_name(self):
        return self.firstname + " " + self.lastname
#
# print(Person.id)
# m = Person("ES", "Sujatha", "F")
# print(m.firstname)
# print(m.lastname)
# print(m.gender)
# print(m.get_name())
# print(m.__dict__)
#
# print(Person.id)
# s = Person("Sarang", "P", "M")
# print(s.firstname)
# print(s.lastname)
# print(s.gender)
# print(s.get_name())
# print(s.__dict__)
class Salary():
    pay=12000
    def __init__(self,pay):
        self.pay=pay

    def annual_salary(self):
        return self.pay*12

import datetime
class Employee(Person):
    doj = 12-11-2019
    dept = ""
    empid = ""
    salary = None
    def __init__(self,fn,ln,g,doj=datetime.date.today(),dept="OTH",pay=120000):
        Person.__init__(self,fn,ln,g)
        self.doj=doj
        self.dept=dept
        self.empid=dept+"-"+str(self.personid)
        self.salary=Salary(pay)


# p = Employee("AJ", "Parameswaran", "M")
# m = Employee("AP", "Sujatha", "F")
s = Employee("P", "Sarang", "M")
# print(p.__dict__)
# print(p.get_name())
# print(p.firstname, s.lastname)
#
# print(m.__dict__)
# print(m.get_name())
# print(m.firstname, s.lastname)

print(s.__dict__)
print(s.get_name())
print(s.firstname, s.lastname)
print("Pay = ",s.salary.pay)
print("Annual Salary",s.salary.annual_salary())

class Email():
    email = ""
    def __init__(self,email):
        self.email=email

class Phone():
    phone = ""
    def __init__(self,phone):
        self.phone=phone

class Address():
    city = ""
    state = ""
    def __init__(self,city,state):
        self.city=city
        self.state=state

class ContactDetails():
    address = None
    phone = None
    email = None
    def __init__(self,add=None,ph=None,em=None):
        self.address = add
        self.phone = ph
        self.email = em

add1 = Address("Mumbai","MH")
ph1 = Phone(8451033120)
em1 = Email("sarangparameswaran@gmail.com")
c = ContactDetails(add1,ph1,em1)

print(c.__dict__)
print(c.address.city)
print(c.address.state)
print(c.email.email)
print(c.phone.phone)