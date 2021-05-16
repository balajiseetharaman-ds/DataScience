##### Basic class definition

class testrun:   # Class definition
    __name='Balaji'    # Variable Intialization
    def __init__(self,name,account):   #self carries the id value in execution space from the object called
        print('calling init method with id value as below')
        print(id(self))  # Print the id value for each object call
        self.__name=name

#Object Creation
a=testrun('balaji',100)
print('calling object a with id value as below')
print(id(a))
b=testrun('bala',200)
print('calling object b with id value as below')
print(id(b))

# left blank test sample1


# Result of the above code
#calling init method with id value as below
#4474940752  # Object a
#calling object a with id value as below
#4474940752  # Object a
#calling init method with id value as below
#4474940880  # Object b
#calling object b with id value as below
#4474940880   # Object b


####### Assigning variable in init

class demo:   # Class definition
    __name='Balaji'    # Variable Intialization
    def __init__(self,name,account):   #self carries the id value in execution space from the object called
        self.name=name
        self.acct=account
        print(self.name,'|',self.acct)

z=demo('balaji',122)
y=demo('kkr',333)

#### Multiple Methods

class demo:   # Class definition
    __name='Balaji'    # Variable Intialization
    def __init__(self,name,account):   #self carries the id value in execution space from the object called
        self.name=name
        self.acct=account
        print(self.name,'|',self.acct)
    def offer(self,balance,n):
        self.balance=balance
        self.n=n
        self.balance+=self.n
        print('Balance after offer applied for :',self.name,'=',self.balance)   # the variable value pass to other method through self

z=demo('balaji',122)
z.offer(1000,33)
y=demo('kkr',333)
y.offer(1000,0)

# Inheritance

class Apple:
    manufacturer = 'Apple Inc'
    contact_website = 'www.apple.com/contact'
    name = 'Apple'
    year_of_manufac=2019

    def contact_details(self):
        print('Contact us at ', self.contact_website)
        print('apple class id :',id(self))


class MacBook(Apple): # child class inherits the parent class
    "This is a Macbook Class - docstring text "
    def __init__(self):
        self.year_of_manufacture = 2018
        print('macbook id init method:',id(self))


    def manufacture_details(self):
        self.created=20201210
        print('macbook id manufacture details:',id(self))
        print('This MacBook was manufactured in {0}, by {1}.'
              .format(self.year_of_manufacture, self.manufacturer))  # manufactured is through the parent class

    def extract_methods(self):
        method_list = [num for num in list(dir(MacBook)) if num.startswith('__') is True]
        print(method_list)

brand=Apple()
print('brand object id',id(brand))
print(type(brand))
brand.contact_details()
macbook = MacBook()
macbook.manufacture_details()
macbook.extract_methods()
print(macbook.__doc__)   # printing docstring
print(macbook.__class__)
print(macbook.__dict__)
print(macbook.__format__)
print(macbook.__getattribute__)
print(macbook.__delattr__)
print(macbook.__dir__)
print(macbook.__hash__)
