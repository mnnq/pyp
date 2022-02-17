#Both are the same functions

from msilib import sequence


def add(x,y):
    return x+y

add2 = lambda x, y: x+y

print(add(2,2))    

#execute the function
(lambda x, y: x+y)(5,7)

#For example
def double(x):
    return x*2

sequencd = [1,3,4,7]

doubled = [double() for x in sequencd]
doubled = [(lambda x: x * 2)(x) for x in sequencd]
doubled = map(double,sequencd)
doubled = list(map(lambda x: x*2,sequencd))