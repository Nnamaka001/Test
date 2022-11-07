'''def greet_user(item):
    print('I am learning ' + item)
greet_user('python')'''

#John is from Ghana and is learning python

'''def john_details(country, item):
    print('John is from ' + country + ' and is learning ' + item)
john_details('Ghana', 'python')'''

'''def john_details(item, country = 'Ghana'):
    """this code just describes a user"""
    print('John is from ' + country + ' and is learning ' + item)
john_details('python')'''

'''def user_details(fname, age, country):
    print('My name is ' + fname + ' and I am ' + str(age) + ' years old.')
    print(fname + ' is from ' + country)
    if age > 18:
        print(fname + ' can vote')
    else:
        print(fname + ' is not eligible to vote.')
user_details('Zubby', 16, 'Nigeria')
#user_details('Chuka', 'coding', 'USA')'''

'''def make_shirt(size, text):
    print('The size of the proposed shirt is ' + size + ' and the message on the shirt should be ' + text)
make_shirt('XXL', 'KINGING KING')
make_shirt(size = 'L', text = 'Toby is 4!')'''

'''def make_shirt(size, text = 'I love Python!'):
    print('I want to get a size ' + size + '. Print ' + text + ' on the back of the shirt.')
make_shirt('L')
make_shirt('M')
make_shirt('XXL', 'LOOK AHEAD!')'''

'''def describe_city(city, country):
    x = (city + 'is in ' + country)
    return x
describe_city('Reykjavik', 'Iceland')'''

'''def describe_city(name, surname):
    describe_city = name + ' ' + surname
    return describe_city
print(describe_city('Chris', 'Chuks'))'''

'''def myfunc(x):
    return 5*x
print(myfunc(7))'''

'''def Insurance(age):
    if age >= 45:
        insurance = 500
    else:
        insurance = 300
    return insurance
age = int(input('Enter your age in years: '))
print('insurance', (Insurance(age)))'''

'''def hello_func():
    return 'Hello Function!'
print(hello_func())'''

'''def hello_func(greeting):
    return '{} Funtion.'.format(greeting)
print(hello_func('Hi'))'''

'''def hello_func(greeting, name = 'You'):
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi', name = 'Corey))'''

'''def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Mathematics', 'Art']
info = {'name': 'John', 'age':22}

student_info(courses, info)'''

'''courses = ['Mathematics', 'Art']
info = {'name': 'John', 'age':22}

student_info(*courses, **info)'''

'''#Number of days in a month. First placeholder for indexing purposes only.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years"""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Returns number of days in that month in that year"""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

#print(is_leap(2024))
print(days_in_month(201, 1))'''

def myfunc(counter):
    i = 2
    while i < counter:
        print('Loop')
        i = i+1
    else:
        return 'End of Loop'

print(myfunc(6))