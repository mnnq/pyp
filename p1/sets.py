#Inside a set you only can have unrepeated values

from statistics import mode


mylist = [1,1,1,1,2,2,2,2,3,3,3,3]

print(mylist)
print(set(mylist))

#with open i need to close the file 
myfile = open('myfile.txt')

print(myfile.read())

myfile.seek(0)

myfile.readlines()

myfile.close()

#if i select the mode=r is for reading , w writing and a for appending, r+ read and write, w+ write and read
with open('myfile.txt', mode='r') as my_new_file:
    contents=my_new_file.read()