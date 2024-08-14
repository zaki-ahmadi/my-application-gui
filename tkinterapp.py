import tkinter as tk
from tkinter import Toplevel, Text, Scrollbar
# from PIL import Image,ImageTk

def open_code_window(title, code_text):
    new_window = Toplevel(root)
    new_window.title(title)
    

    frame = tk.Frame(new_window)
    frame.pack(padx=10, pady=10, expand=True, fill="both")

    # new_window.configure(bg='black')

    text_widget = Text(frame, wrap="word", width=80, height=25,bg='black',foreground='#00e210',border=10)
    text_widget.insert("9.0", code_text)
    text_widget.config(state="disabled")
    text_widget.pack(side="left", expand=True, fill="both")



    scrollbar = Scrollbar(frame, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")
    text_widget.config(yscrollcommand=scrollbar.set)



root = tk.Tk()
root.title("Homework of Python ")
root.geometry('500x700')
root.configure(bg='black')
# image1 = Image.open('111.jpg')
# # b_i = ImageTk.PhotoImage(image1)
# label = tk.Label(root,text= '''⏩⏩⏩In the name of Allah⏪⏪⏪
# ''',font=('MRT_Nadine',12),fg='white',background='black',border=15,width=1000).pack()


label = tk.Label(root,text= '''This program is for homework of the <OOP>'''
                 ,font=('MRT_Nadine',12),fg='white',background='black',border=15,width=1000,
                 ).pack()

# label = tk.Label(root,text= '''⚕️⚕️⚕️ Python ⚕️⚕️⚕️'''
#                  ,font=('MRT_Nadine',12),fg='white',background='black',border=15,width=1000,
#                  ).pack()



stu_information = """Name : Mohammad Zaki Ahamdi
Fathre name : Mehrab Ali
Class : first class of OOP
HW : OOP + Biultin_Fuction
Teacher : Abdul_Roheed Khaliqeyar
Department : Information Tecnology
"""

code00 = '''
def factorial(n):
    if n == 0 :
        return 1
    else:
       return n * factorial(n-1)
    

print(factorial(5))
'''
code0 = """
# BUILT IN FUNCTIONS
# (1)
# PYTHON abs() 

num = float(input('Enter a number :'))
print(f'the abs value of num is : {num}')

# (2)
# python all()

list_all = [True,True,False,True]
result=all(list_all)
if result:
    print('all of the elemests of list is true.')
else:
    print('one of the elemests is false.')

# (3)
# python any()

list1 = [10,20,30,40]
result1 = any(list1)
if result1:
    print('at lest one of the elements is in the list. ')
else:
    print('the all of the elements are not in the list. ')

# (4)
# python ascii()

a = input('enter a string :')
asc_re = ascii(a)
print(f'asci {asc_re}')

# (5)
# python bin()

a1 = int(input('enter a number : '))
bainary = bin(a1)
print(f'the binari of {a1} is {bainary}.')

# (6)
# python bool()

a2 = input('enter a value')
u_b = bool(a2)
print(f'the bool value of {a2} is {u_b}.')

# (7)
# python bytearray

num1 = [1,2,3,4]
bbb = bytearray(num1)
print(f'bytearray is {bbb}')

# (8)
# python bytes()

num2 = [1,2,3,4]
by = bytes(num2)
print(f' is : {by}')

# (9)
# python callable()

def x():
  a_ca = 5

print(callable(x))

# (10)
# python chr()


num2 = int(input('enter a number : '))
print(chr(4))


# (11)
# python classmethod()





# (12)
# python compile()

x_c = compile('print(11)','abc', 'eval' )
exec(x_c)


# (13)
# python complex()
# creat a complex numbers

x_complex = int(input('enter a number : '))
x_complex1 = int(input('enter a number : '))
x_co = complex(x_complex,x_complex1)
print(f'the complex number is : {x_co}')



# (14)
# python delattr()
# delets attribute from the object

class Person:
    name = 'ali'
    age = 19
    country = 'Afghanistan'
delattr(Person,'age')


# (15)
# python dict()
# creats a dictionary.

x = dict(name = "John", age = 36, country = "Norway")

# (16)
# python dir()
# tries to return to attributrs of object
print(dir(str))

# (17)
# python divmod()
# return a tuple of quotient and reminder

print(divmod(55,22))

# (18)
# python enumerate()
# return a enumerate object

print(list(enumerate(['a','b','c'])))


# (19)
# python eval()
# runs python code within program

x_x = 'print(11)'
eval(x_x)



# (20)
# python exec()
# executes dynamically created program

n = name ='ali \nprint(name)'
exec(n)


# (21)
# python filter ()
# constructs iterator from elements which are true
list_filtre = [1,2,3,4,5,6.7]
x = list(filter(lambda x: x%2 == 0 , list_filtre))
print(x)


# (22)
# python float()
# returns Floating Point number from number,string
print(float(100))



# (23)
# python format()
# returns formatted repersentation of a value
x_f = format(1 , '%') 
print(x_f)

# (24)
# pyhton frozenset()
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)


# (25)
# python getattr()

class Person:
  name = "abbas"
  age = 21
  country = "Pakistan"

x = getattr(Person, 'age')


# (26)
# python globals()

x = globals(input('enter a value . :'))
print(x)

# (27)
# python hasattr()
class Animal:
  name = "max"
  age = 7
  animaal = "dog"

x = hasattr(Animal, 'age')


# (28)
# python hash()




# (29)
# python help()



# (30)
# python hex()
a_hex = int(input('enter a number ; '))
x_hex= hex(a_hex)

# (31)
# python id()

x_id= ('apple', 'banana', 'cherry')
y_id= id(x_id)



# (32)
# python input()

print('Enter your name:')
x_input = input('-->')
print('Hello, ' + x_input)


# (33)
# python int()

x_int_int = int(7878.78)
print(x_int_int)


# (34)
# python isinstance()

is_in = 6
print(isinstance(num,int))

# (35)
# python issubclass()

class Animal:
    pass
class Dog(Animal):
    pass
print(issubclass(Dog,Animal))

# (36)
# python iter()

iter_list = [11,22,33]
iter_list = iter(iter_list)
print(next(iter_list))

# (37)
# python len()

len_list = [9,6,5,3]
print(len(len_list))

# (38)
# python list()

string_l = str(input('enter a string'))
string_list = list(string_l)
print(string_list)

# (39)
# python locals()

def lo_func():
    a = 1000
    b = 2000
    print(locals())

lo_func()


# (40)
 # python map()

list_map = [8,7,6,5]
result_map = map(lambda x : x*2 ,list_map )
print(list(result_map))

# (41)
# puthon max()

list_max = [44,55,66,77]
print(max(list_max))

# (42)
# python memoryview()

zzz = bytearray(b'ABC')
mmm = memoryview(zzz)
print(list(mmm))

# (43)
# pyhton min()

list_min = [1000,999,888,777]
print(min(list))

# (44)
# python next()

list_next = iter([11,22,33,44,55])
print(next(list_next))
print(next(list_next))
print(next(list_next))


# (45)
# python object()





# (46)
# python oct()
o_oct = int(input('enter a num to change in octal : '))
x_oct = oct(o_oct)

# (47)
# python open()

f_open = open("abcfile.txt", "r")
print(f_open.read())


# (48)
# python ord()

x_ord = ord("h")
print(x_ord)


# (49)
# python pow()

x_pow = int(input('enter a number to the base of pow :'))
y_pow = int(input('enter a number to the power of the pow '))
z_pow = pow(x_pow,y_pow)
print(z_pow)

# (50)
# python print()

print("Hello World !!! Iam Mohammad Zaki Ahmadi .")


# (51)
# python property()




# (52)
# python range()

x = range(90)
for n in x:
  print(n)


# (53)
# python repr()





# (54)
# python reversed()
alph_rev = ["z", "a", "k", "i"]
ralph_rev= reversed(alph_rev)
for x in ralph_rev:
  print(x)



# (55)
# python round()

num_r = 53.669
print(round(num_r))


# (56)
# python set()

str_set = 'i am a boy'
print(set(str_set))

# (57)
# python setattr()

class People:
    name = 'zaki'
    age = 20
    country = 'USA'


setattr(People, 'age', 25)


# (58)
# python slice()

a_slice = ('a', 'b', 'c', 'z', 'x', 'f')
s_slice = slice(2,4)
print(a_slice[s_slice])



# (59)
# python sorted()

z_sorted = (1,5,6,3,9,0)
x_sorted = sorted(z_sorted)
print(x_sorted)

# (60)
# python staticmethod()

class A:
    def total(n_st1,n_st2):
        return n_st1+n_st2
A.total = staticmethod(A.total)
sum_st = A.total(50,70)
print(f'sum is : {sum_st}')


# (61)
# python str()

str_str = 5656
print(str(str_str))


# (62)
# pyhton super()

class A:
    def __init__(self, matn):
        self.pyam = matn

    def printpyam(self):
        print(self.pyam)

class B(A):
    def __init__(self,matn):
        super().__init__(matn)


x_super = B('hi how are you !!!')
x_super.printpyam()




# (63)
# python tuple()

list_t = [1,2,3,4]
list_tt = tuple(list_t)
print(list_tt)


# (64)
# python type()


n_type = 'zaki'
print(type(n_type))

# (65)
# python vars()

print(vars(int))


# (66)
# python zip()


person = ['ali', 'zaki', 'reza']
var = [11,18,20]
result_zip = zip(person,var)
print(list(zip(result_zip)))


# (67)
# python __import__()
a_import = __import__()

"""
code1 = """
from math import pi
# oop home work 

# (1)
class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age


ali = Person('ali', 20)

print('__________________________________________________________________)

# (2)
class Person1 :
  def __init__(self,name,age):
      self.name = name
      self.age = age
    

  def greet(self):
      print('Hello Wellcome Mr:' + self.name)

first_person1 = Person1('Ahsan', 14) 
first_person1.greet()

print('__________________________________________________________________)

# (3)
class Car:
    def __init__(self,model,made,year):
        self.model = model
        self.make = made
        self.year = year

car1 = Car('Benz','made by USA', 2020)

print(car1.make)
print(car1.model)
print(car1.year)

print('__________________________________________________________________)

# (4)
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        a_a = pi * (self.radius ** 2)
        print(a_a)

cri1 = Circle(5)
cri1.area()
    
print('__________________________________________________________________)

# (5)

class A_P:

    def __init__(self, tool, arz):
        self.tool = tool
        self.arz = arz

    def area(self):
        a_t = self.tool * self.arz
        print(a_t)

    def enviroment(self):
        p_t = (self.tool * 2) + (self.arz * 2)
        print(p_t)

ap1 = A_P(5, 4)
ap1.area()
ap1.enviroment()

"""
code2 = """print('The first question ')
# (1)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + 'SPEAK SPEAK SPEAK')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name + 'OW OW OW OW')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(self.name + 'MIOW MIOW MIOW')

animal1 = Animal('an animal speak\'s : ')
animal1.speak()

dog1 = Dog('dog name is max and speak like this : ')
dog1.speak()

cat1 = Cat('cat name is bilo and speak like this : ')
cat1.speak()

print('The second question ')

print('__________________________________________________________________)

# (2)

class Shapes:
    def __init__(self):
        pass

class Area_of_Square(Shapes):
    def __init__(self, tool , arz):
        self.tool = tool
        self.arz = arz

    def area(self):
        print(self.tool * self.arz)


class Area_of_Triangle(Shapes):
    def __init__(self,qaidah, ertifa):
        self.qaidah = qaidah
        self.ertifa = ertifa


    def area(self):
        print(0.5 * self.qaidah * self.ertifa)


squ = Area_of_Square(4 ,4)
squ.area()
tri = Area_of_Triangle(2 ,4)
tri.area()

print('The theard question ')

print('__________________________________________________________________)

# (3)

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department


manager1 = Manager('adulkhaliq', 10000 , 'information technologe')
print(manager1.name)
print(manager1.salary)
print(manager1.department)

print('The fuorth question ')

print('__________________________________________________________________)


# (4)

class Vehicle:
    def __init__(self,name):
        self.name = name

    def drive(self):
         print('vehicle drive drive !!! 🛞🛞🛞')

class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
         print(f'{self.name} ride ride !!! 🚲🚲🚲' )
    
class Truck(Vehicle):
    def __init__(self, name):
        super().__init__(name)

    def drive(self):
         print(f'{self.name} drive drive !!! 🚜🚜🚜' )
    
bike1 = Bike('ali\'s bike')
bike1.drive()
truck1 = Truck('ahmad\'s truck')
truck1.drive()

print('The fifth question ')

print('__________________________________________________________________)


# (5)

class Bird:
    def __init__(self,name_of_bird):
        self.name_of_bird = name_of_bird

    def fly(self):
        print(f'{self.name_of_bird} flying ')
class Eagle(Bird):
    def __init__(self, name_of_bird):
        super().__init__(name_of_bird)

    def fly(self):
        print(f'{self.name_of_bird} can fly !!! ')

class Penguin(Bird):
    def __init__(self, name_of_bird):
        super().__init__(name_of_bird)

    
    def fly(self):
        print(f'{self.name_of_bird} can not fly !!! ')

eagle1 = Eagle('Eagle🦅🦅🦅')
eagle1.fly()
Penguin1 = Penguin('Penguin🐧🐧🐧')
Penguin1.fly()
"""
code3 = """
# (1)
class Account:

    def __init__(self, in_money=0):
        self.__in_money = in_money

    def input_money(self, amount):
        if amount > 0:
            self.__in_money += amount
            print(f'{amount} money inputed in the Account ')

        else:
            print('an Error ❌❌❌')

    def output_money(self, amount):
        if 0 < amount <= self.__in_money:
            self.__in_money -= amount
            print(f'{amount} money outed from the Account ')
        else:
            print('an Erronr ❌❌❌')

    def allin_the_account_money(self):
        print(self.__in_money)

Account1 = Account(500)

Account1.input_money(500)

Account1.output_money(300)

Account1.allin_the_account_money()

print('__________________________________________________________________)

# (2)
class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_pages(self):
        return self.__pages

    def set_pages(self, pages):
        self.__pages = pages

book1 = Book('Programing', 'ali ahmadi', 678)
print(book1.get_title())

book1.set_pages(900)
print(book1.get_pages())

print(book1.get_author())

print('__________________________________________________________________)

# (3)
class Laptop:
    def __init__(self, model, brand, price) :
        self.__model = model
        self.__brand = brand
        self.__price = price

    def takhfif(self, takhfif_laptop):
        if 0 < takhfif_laptop < self.__price:
            self.__price -= takhfif_laptop
        else:
            print('an Error ')

    def show_model_brand_price(self):
        print(f'the laptop model is {self.__model}.')
        print()
        print(f'the laptop brand is {self.__brand}.')
        print()
        print(f'the laptop price is {self.__price}.')
        print()


Laptop1 = Laptop('dell_7400', 'Dell', 18000)

Laptop1.show_model_brand_price()

print('After of the takhfif ⬇️  ⬇️  ⬇️')
print()
Laptop1.takhfif(3000)

Laptop1.show_model_brand_price()

print('__________________________________________________________________)


# (4)
class BankAccount:
    def __init__(self, account_num, blance=0):
        self.__account_num = account_num
        self.__blance = blance

    def in_money(self,amount):
        if amount > 0 : 
            self.__blance += amount
            print(f'You {amount} (Afghni) inputed in your bank_account')
        else:
            print('an Error')

    def out_money(self,amount):
        if 0 < amount <= self.__blance:
            self.__blance -= amount
            print(f'You {amount} (Afghni) was outputed from your bank_account ')
        else:
            print('an Error')

    def show_blance(self):
        print(f'Your blancce is : {self.__blance} (Afghni)')

ali_acc = BankAccount(56565656,7800)

ali_acc.show_blance()

ali_acc.in_money(200)

ali_acc.out_money(3000)

ali_acc.show_blance()

print('__________________________________________________________________)


# (5)

class Student:
    def __init__(self,name,grade,age):
        self.__name = name
        self.__grade = grade
        self.__age = age

    def get_name(self):
        print(self.__name)
        
    def get_grade(self):
        print(self.__grade)

    def get_age(self):
        print(self.__age)

    def set_name_grade_age(self,name,grade,age):
        self.__name = name 
        self.__grade = grade
        self.__age = age

    def show_details_of_students(self):
        print(f'name : {self.__name} \ngrade : {self.__grade} \nage : {self.__age}')


ali = Student('ali' , 'first' , 20)
print('befor changing the details of student.\n⬇️')
ali.show_details_of_students()
ali.set_name_grade_age('ali' , 'second' , '21')
print('after changing the details of student.\n⬇️')
ali.show_details_of_students()
"""
code4 = """
# (1)
from typing import Any

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f'this book <<{book.title}>> added to library.')

    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f'this <<{book.title}>> removed from library.')
        else:
            print('this book is not here.')
    
    def show_all_books(self):
        if self.books:
            print('the all of books in library:')
            print()
            for book in self.books:
                print(f'name of book: {book.title}, author :{book.author}')
        else:
                print('library is empaty.')
                
Library1 = Library('Kabul University Library')
book1 = Book('Afghanistan', 'Mohammad')
book2 = Book('Kabul', 'Ali Mohammad')
Library1.add_book(book1)
Library1.add_book(book2)
print()
Library1.show_all_books()

print('____________________________________________________')

# (2)
class stu:
    def __init__(self,name):
        self.name = name
        
class School:
    def __init__(self,name):
        self.name = name
        self.students = []

    def add(self,student):
        self.students.append(student)
        print(f'{student.name} added to school.')
    
    def rem(self,student):
        if student in self.students:
            self.students.remove(student)
            print(f'{student.name} removed from scholl.')

        else:
            print(f'{student} is not in our school.')

sch = School('Abdul-rahim-e-shahid')
stu1 = stu('ali')
sch.add(stu1)
sch.rem(stu1)

print('____________________________________________________')

# (3)
class Members:
    def __init__(self, name_menber):
        self.name_menber = name_menber

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_mem(self, member):
        self.members.append(member)
        print(f'{member.name_menber} added to team')

    def remove_mem(self, member):
        if member in self.members:
            self.members.remove(member)
            print(f'{member.name_menber} removed from team')
        else:
            print(f'{member} is not in this team')

team_football = Team('ITF')
mem_1 = Members('jawid')
team_football.add_mem(mem_1)
mem_2 = Members('zaki')
team_football.add_mem(mem_2)
mem_3 = Members('ali')
team_football.add_mem(mem_3)
mem_4 = Members('ahmad')
team_football.add_mem(mem_4)
team_football.remove_mem(mem_3)

print('____________________________________________________')

# (4)

class Employee:
    def __init__(self,name_e):
        self.name_e = name_e


class Factori:
    def __init__(self,name):
        self.name = name
        self.employees = []

    def a_d(self,employee):
        self.employees.append(employee)
        print(f'{employee.name_e} added to factori ' )

    def r_m(self,employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f'{employee.name_e} removed from factori ' )
        else:
            print(f'he/she is not in this <<{self.name}>> Factori ')

fact_099 = Factori('Tesla')
emp_099 = Employee('zaki')
fact_099.a_d(emp_099)
fact_099.r_m(emp_099)

print('____________________________________________________')

# (5)


class Animal:
    def __init__(self,name_a):
        self.name_a = name_a


class Zoo:
    def __init__(self,name):
        self.name = name
        self.animals = []

    def a_a(self,animal):
        self.animals.append(animal)
        print(f'{animal.name_a} added to zoo ' )

    def r_a(self,animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f'{animal.name_a} removed from zoo ' )
        else:
            print(f'it is not in this <<{self.name}>> zoo ')

zoo = Zoo('international zoo of USA')
ani = Animal('dog')
zoo.a_a(ani)
"""
code5 = '''
# (1)
class FileManager:
    def __init__(self,name):
        self.name = name

    def open_file_read(self):
        print('file opened to read')
        o_r = open('abc.txt', "r")
        print(o_r.read())
        

    def open_file_write(self):
        print('file opened to write')

        o_w = open('abcd.txt', "w")
        print(o_w.write('hello world '))
        print(o_w.write('new line'))
        
        o_w.close
        

a = FileManager('file to read and write')
a.open_file_read()
a.open_file_write()


print('_________________________________________________________')
# (2)

class Log:
    def __init__(self ,file_t):
        self.file_t = file_t

    def write_error(self ,error_message):
        with open('error.txt', 'a') as file:
            file.write(f'Error : {error_message}\n')
            print('in the file error was sent!!!')


log = Log('error.txt')
log.write_error('this is an error masege')

print('_________________________________________________________')
# (3)


class Config:
    def read(self):
        with open("configuration setings.txt","r") as f:
            print(f.__dir__())

    def access_dir(self):
        with open("configuration setings.txt","r+") as f:
            print(f.__dir__())

label=Config()
label.access_dir()



print('_____________________________________________________________')


# (4)

list = ["ali","abbas","sara","aziz"]
class Database:
    global list

    def queries(self,name):
        try:
            for i in list:
                if i == n:
                    print(f"your name is{name}")

        except:
            print("connection fails")

jawad = Database()
jawad.queries("jawad")

print('___________________________________________________________________')
# (5)


class Report:
    try:
        def generate_data(self):
            with open("dat.txt","r") as f:
                print(f.readlines())


    except FileNotFoundError :
         print("file does not exist or can not read")

new=Report()
new.generate_data()

'''

code6 = '''# (1)
class Ticket:
    def __init__(self,movie_name,seat_num,price):
        self.movie_name = movie_name
        self.seat_num = seat_num
        self.price = price

    def show_details(self):
        print(f'movie_name : {self.movie_name} \nseat_num : {self.seat_num},\nprice : {self.price} ')
    def takhfif(self,amount):
        if 0 < amount < self.price:
            self.price -= amount
            print(f'{amount} afghani is you takhfif.')

        else:
            print('an error')


ahmad = Ticket('love' , 99 , 350)

ahmad.show_details()

ahmad.takhfif(50)

ahmad.show_details()
            
# (2)
print('____________________________________________')

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price
        print(f'{name} added to items ')

    def rem_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f'{name} is removed.')
        else:
            print(f'{name} is not in items ')

    def show_item(self):
        if not self.items:
            print('the items is emapaty .')
        else:
            for name, price in self.items.items():
                print(f'name : {name} , price : {price}')


sho = ShoppingCart()
sho.add_item('milk', 25)
sho.add_item('wather', 10)
sho.add_item('egg', 10)
sho.show_item()
print('after of the remove')
sho.rem_item('milk')
sho.show_item()

# (3)
print('____________________________________________')
class Reatsurant :
    def __init__(self,name):
        self.name = name
        self.menu = []

    def add_to_menu(self,name_food):
        self.menu.append(name_food)
        print(f'{name_food} added to the menu')

    def remove_from_menu(self,name_food):
        if name_food in self.menu:
            self.menu.remove(name_food)
            print(f'{name_food} removed from the menu')

    def display_menu(self):
        print('the menu of the Reatsurant')
        for food in self.menu:
            print(f'food : {food}')



abc = Reatsurant('Barg Continital')
abc.add_to_menu('Palaw')
abc.add_to_menu('Shorba')
abc.add_to_menu('Kabab')
abc.remove_from_menu('Palaw')
abc.display_menu()

print('____________________________________________')
# (4)

class Flight:
    def __init__(self,flight_num,destination,):
        self.flight_num = flight_num
        self.destination = destination
        self.passengers = []

    def add_passenger(self,person):
        self.passengers.append(person)
        print(f'{person} added to this Flight going to {self.destination}.')
        print()
    def remove_passengers(self,person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f'{person} removed from this Flight to the going {self.destination}')
            print()
    def show_all_passengers(self):
        for i in self.passengers:
            print(f'name of passengers : {i}')
        print()


flight404 = Flight( 404 , 'Kabul')
flight404.add_passenger('ali')
flight404.add_passenger('zaki')
flight404.add_passenger('abdullah')
flight404.add_passenger('haji')
flight404.show_all_passengers()
flight404.remove_passengers('haji')
flight404.show_all_passengers()



print('____________________________________________')

# (5)

class Hotel:
    def __int__(self, name, room_numbers):
        self.name = name
        self.room_numbers
        self.rooms = {num: False for num in room_numbers}

    def book(self, room_number):
        if not self.rooms[room_number]:
            self.rooms[room_number] = True
            return f'{room_number} is booked'
        return f'{room_number} before you was booked'

    def check_out(self,room_number):
        if self.rooms[room_number]:
            self.rooms[room_number] = False
            return f'{room_number} is check out'
        return f'{room_number} was check outed'

hotel1 = Hotel('kabul' , [1,2,3])
print(hotel1.book(1))
print(hotel1.check_out(3))
'''

code7 = '''

# سوالات پایتون از ۳۶ تا ۴۰  یا از ۳۱ تا ۳۵ 

# (1)
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("CounterApp")
window.geometry("400x400")
window.config(bg="light blue")
window.resizable(False,False)
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=2)
window.columnconfigure(2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
total_m= 1000000
label1 =ttk.Label(window,text="Your current account equal :",font="arial 12",background="gray")
label1.grid(row=1,column=1,sticky="e")
global_var =1000000
label2 =ttk.Label(window,text= global_var ,font="arial 12",background="green")
label2.grid(row=1,column=2,sticky="w")
entry_var =tk.StringVar(value='Entry your amount...?')
def d_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var - new_m
    label2['text']= global_var

def i_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var + new_m
    label2['text']= global_var

entry1 = ttk.Entry(window, font="arial 12", width=20,textvariable=entry_var)
entry1.grid(row=2, column=1, sticky="e", rowspan=2)
button1 =ttk.Button(window, text="Decrement button", width=22,command=d_button)
button1.grid(row=2,column=2,sticky="w")
button2 =ttk.Button(window, text="Increment button", width=22,command=i_button)
button2.grid(row=3,column=2,sticky="w")

window.mainloop()


print('__________________________________________________________________')

# (2)

window = tk.Tk()
window.title("ToDoApp")
window.geometry("700x400")
window.config(bg="orange")
window.resizable(False,False)
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=2)
window.columnconfigure(2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)

label1 =ttk.Label(window,text="Tasks : Teacher, Docter, ",font="arial 12",background="gray")
label1.grid(row=1,column=1,sticky="e")
list_task= ["Manager,","Officer,","Minister"]
label2 =ttk.Label(window,text= list_task ,font="arial 12",background="gray")
label2.grid(row=1,column=2,sticky="w")
entry_var =tk.StringVar(value='Entry your task...?')

def d_button():
    global list_task
    new_m =str( entry_var.get())
    for i in list_task:
        if i == new_m:
            list_task.remove(i)
    label2['text'] = list_task

def a_button():
    global list_task
    new_m =str( entry_var.get())
    list_task.append(new_m)
    label2['text']= list_task

entry1 = ttk.Entry(window, font="arial 12", width=20,textvariable=entry_var)
entry1.grid(row=2, column=1, sticky="e", rowspan=2)

button1 =ttk.Button(window, text="Delete button", width=22,command=d_button)
button1.grid(row=2,column=2,sticky="w")

button2 =ttk.Button(window, text="Add button", width=22,command=a_button)
button2.grid(row=3,column=2,sticky="w")

window.mainloop()




print('__________________________________________________________________')
# (3)


calculator = ""
def add_to_calculation(symbol):
    global calculator
    calculator += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculator)
def evaluate_calculation():
    global calculator
    try:
        calculator = str(eval(calculator))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculator)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculator
    calculator =""
    text_result.delete(1.0, "end")

window=tk.Tk()
window.title("calculator")
window.geometry("300x300")
window.resizable(False,False)
text_result = tk.Text(window,height=2, width = 16, font =("Arial", 24))
text_result.grid(columnspan = 5)
btn_1 = tk.Button(window, text ="1", command = lambda: add_to_calculation(1),width = 5, font = ("Arial",14))
btn_1.grid(row = 2, column = 1)
btn_2 = tk.Button(window, text ="2", command = lambda: add_to_calculation(2),width = 5, font = ("Arial",14))
btn_2.grid(row = 2, column = 2)
btn_3 = tk.Button(window, text ="3", command = lambda: add_to_calculation(3),width = 5, font = ("Arial",14))
btn_3.grid(row = 2, column = 3)
btn_4 = tk.Button(window, text ="4", command = lambda: add_to_calculation(4),width = 5, font = ("Arial",14))
btn_4.grid(row = 3, column = 1)
btn_5 = tk.Button(window, text ="5", command = lambda: add_to_calculation(5),width = 5, font = ("Arial",14))
btn_5.grid(row = 3, column = 2)
btn_6 = tk.Button(window, text ="6", command = lambda: add_to_calculation(6),width = 5, font = ("Arial",14))
btn_6.grid(row = 3, column = 3)
btn_7 = tk.Button(window, text ="7", command = lambda: add_to_calculation(7),width = 5, font = ("Arial",14))
btn_7.grid(row = 4, column = 1)
btn_8 = tk.Button(window, text ="8", command = lambda: add_to_calculation(8),width = 5, font = ("Arial",14))
btn_8.grid(row = 4, column = 2)
btn_9 = tk.Button(window, text ="9", command = lambda: add_to_calculation(9),width = 5, font = ("Arial",14))
btn_9.grid(row = 4, column = 3)
btn_0 = tk.Button(window, text ="0", command = lambda: add_to_calculation(0),width = 5, font = ("Arial",14))
btn_0.grid(row = 5, column = 2)
btn_plus = tk.Button(window, text ="+", command = lambda: add_to_calculation("+"),width = 5, font = ("Arial",14),bg ="gray")
btn_plus.grid(row = 2, column = 4)
btn_minus = tk.Button(window, text ="-", command = lambda: add_to_calculation("-"),width = 5, font = ("Arial",14),bg ="gray")
btn_minus.grid(row = 3, column = 4)
btn_mul = tk.Button(window, text ="*", command = lambda: add_to_calculation("*"),width = 5, font = ("Arial",14),bg="gray")
btn_mul.grid(row = 4, column = 4)
btn_dvi = tk.Button(window, text ="/", command = lambda: add_to_calculation("/"),width = 5, font = ("Arial",14),bg = "gray")
btn_dvi.grid(row = 5, column = 4)
btn_open = tk.Button(window, text ="(", command = lambda: add_to_calculation("("),width = 5, font = ("Arial",14))
btn_open.grid(row = 5, column = 1)
btn_close = tk.Button(window, text =")", command = lambda: add_to_calculation(")"),width = 5, font = ("Arial",14))
btn_close.grid(row = 5, column = 3)
btn_equals = tk.Button(window, text ="=", command = evaluate_calculation,width = 11, font = ("Arial",14),bg="light blue")
btn_equals.grid(row = 6, column = 3,columnspan=2)
btn_clear = tk.Button(window, text ="c", command = clear_field,width = 11, font = ("Arial",14),bg="light blue")
btn_clear.grid(row = 6, column = 1,columnspan=2)

window.mainloop()

print('__________________________________________________________________________________')

# (4)

window = tk.Tk()
window.title("loginApp")
window.geometry("400x400")
window.config(bg="light blue")
window.resizable(False,False)
window.columnconfigure(1,weight=2)
window.columnconfigure( 2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)


label1 =ttk.Label(window,text="User Name :",font="arial 20",background="light blue")
label1.grid(row=1,column=1,sticky="e")
entry_text=tk.StringVar()
entry1 = ttk.Entry(window,font="arial 12",width=15,textvariable=entry_text)
entry1.grid(row=1,column=2,sticky="w")
label2 =ttk.Label(window,text=" PassWord :",font="arial 20",background="light blue")
label2.grid(row=2,column=1,sticky="e")
entry_text1=tk.StringVar()
entry2 = ttk.Entry(window,font="arial 12",width=15,textvariable=entry_text1)
entry2.grid(row=2,column=2,sticky="w")
button =ttk.Button(window,text="Click For login",width=30)
button.place(relx=0.2,rely=0.5)

window.mainloop()
#___________________________________________________________________________________________________
#36. Create a class CounterApp that uses tkinter to create a simple counter GUI with increment and
#ecrement buttonds.

import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("CounterApp")
window.geometry("400x400")
window.config(bg="light blue")
window.resizable(False,False)
window.columnconfigure(0,weight=2)
window.columnconfigure(1,weight=2)
window.columnconfigure(2,weight=2)
window.columnconfigure(3,weight=2)
window.rowconfigure((0,1,2,3,4,5,6,7,8,9),weight=1)
total_m= 1000000
label1 =ttk.Label(window,text="Your current account equal :",font="arial 12",background="gray")
label1.grid(row=1,column=1,sticky="e")
global_var =1000000
label2 =ttk.Label(window,text= global_var ,font="arial 12",background="green")
label2.grid(row=1,column=2,sticky="w")
entry_var =tk.StringVar(value='Entry your amount...?')
def d_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var - new_m
    label2['text']= global_var

def i_button():
    global global_var
    new_m =int( entry_var.get())
    global_var = global_var + new_m
    label2['text']= global_var

entry1 = ttk.Entry(window, font="arial 12", width=20,textvariable=entry_var)
entry1.grid(row=2, column=1, sticky="e", rowspan=2)
button1 =ttk.Button(window, text="Decrement button", width=22,command=d_button)
button1.grid(row=2,column=2,sticky="w")
button2 =ttk.Button(window, text="Increment button", width=22,command=i_button)
button2.grid(row=3,column=2,sticky="w")

window.mainloop()



print('_____________________________________________________________________________')


# (5)


window = tk.Tk()
window.title("WeatherApp")
window.geometry("1100x600")
window.resizable(False,False)
window.columnconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),weight=1)
window.rowconfigure((0,1,2,3),weight=1)



label = ttk.Label(window,text="WEATHER APP",font=("arial 40 bold"),background="#4a4a4a",foreground="white")
label.place(relx = 0.3,rely=0.1)
label1 = ttk.Label(window,text=" Province :",font=("arial 25"))
label1.grid(row=2,column=4)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=1)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=6)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=7)
label1 = ttk.Label(window,font=("arial 25"))
label1.grid(row=2,column=9)
entry_text=tk.StringVar(value="Searching...?   ")
entry = ttk.Entry(window,textvariable=entry_text,font='arial 20 ', background="#111111",foreground="black")
entry.grid(row=2,column =6)

button1 = ttk.Button(window,text= "    Today   : Kabul ---> Suuny * \n"
                                  
                                  "\n Tomorrow : Kabul ---> Rainy  ")
button1.grid(row=1,column =4 ,columnspan=3,sticky="nsew",padx =2,pady=2)
button2 = ttk.Button(window,text="    Today    : Bamyan ---> Sunny * \n"
                                  
                                  "\n Tomorrow : Bamyan ---> Rainy  ")
button2.grid(row=1,column =0 ,columnspan=4,sticky="nsew",padx =2,pady=2)
button3 = ttk.Button(window,text="    Today    : Herat ---> Cloudy \n"
                                  
                                  "\n Tomorrow : Herat ---> Sunny * ")
button3.grid(row=1,column =7,columnspan=4,sticky="nsew",padx =2,pady=2)
button4 = ttk.Button(window,text="       Today    : Helmand ---> Sunny * \n"
                                  
                                "\n      Tomorrow : Helmand ---> Rainy  ")
button4.grid(row=1,column =12 ,columnspan=4,sticky="nsew",padx =2,pady=2)
window.mainloop()

print('_____________________________________________________________________________________________')
'''

stu = tk.Button(root,width=40,bd = 7,background='white',fg='black' ,text="INFORMATIO OF STUDENT", command=lambda: open_code_window("INFORMATIO OF STUDENT", stu_information))
button00 = tk.Button(root,width=40,bd = 7,background='white',fg='black' ,text="FACTORIAL", command=lambda: open_code_window("Factorial", code00))

button0 = tk.Button(root,width=40,bd = 7,background='white',fg='black' ,text="Builtin Functions in Python", command=lambda: open_code_window("Builtin Functions in Python", code0))
button1 = tk.Button(root,width=40,bd = 7,background='white',fg='black' ,text="QUESTION : 1_5", command=lambda: open_code_window("QUESTION : 1_5", code1))
button2 = tk.Button(root,width=40,bd = 7,background='white',fg='black' ,text="QUESTION : 5_10", command=lambda: open_code_window("QUESTION : 5_10", code2))
button3 = tk.Button(root,width=40,bd = 7,background='white',fg='black' ,text="QUESTION : 10_15", command=lambda: open_code_window("QUESTION : 10_15", code3))
button4 = tk.Button(root,width=40,bd = 7,background='white',fg='black' ,text="QUESTION : 15_20", command=lambda: open_code_window("QUESTION : 15_20", code4))
button5 = tk.Button(root,width=40,bd = 7,background='white',fg='black' ,text="QUESTION : 20_25", command=lambda: open_code_window("QUESTION : 20_25", code5))
button6 = tk.Button(root,width=40,bd = 7,background='white',fg='black' ,text="QUESTION : 25_30", command=lambda: open_code_window("QUESTION : 25_30", code6))
button7 = tk.Button(root,width=40,bd = 7,background='white',fg='black',text="QUESTION : 30_35", command=lambda: open_code_window("QUESTION : 30_35", code7))


stu.pack(pady=5)
button00.pack(pady=5)
button0.pack(pady=5)
button1.pack(pady=5)
button2.pack(pady=5)
button3.pack(pady=5)
button4.pack(pady=5)
button5.pack(pady=5)
button6.pack(pady=5)
button7.pack(pady=5)





label = tk.Label(root,text= ''''''
                 ,font=('MRT_Nadine',12),fg='white',background='black',border=15,width=1000).pack()

label = tk.Label(root,text= ''''''
                 ,font=('MRT_Nadine',12),fg='white',background='black',border=15,width=1000,
                 ).pack()

label = tk.Label(root,text= ''''''
                 ,font=('MRT_Nadine',12),fg='white',background='black',border=15,width=1000,
                 ).pack()

label = tk.Label(root,text= ''''''
                 ,font=('MRT_Nadine',12),fg='white',background='black',border=15,width=1000,
                 ).pack()



root.mainloop()
