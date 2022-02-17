
name= "Mati"
print(f"Hello, his name is {name}")

print("This is a string {}".format("SARASA"))

print("This is a string {2} {0} {1}".format("SARASA","sarasa1","Sarasa2"))

print("This is a string {f} {b} {c}".format(f="asd",b="sarasa1",c="Sarasa2"))

#pep8 vars in lower case
print(50 ** 10)

a = "abcdefghij"

#until te position 3 but not included
print(a[:3])

print(a[2:])

print(a[3:6])

print(a[1:3])

print(a[::2]) #jumping in step size of 2

print(a[::-1])


''''
name = "Sam"
name[0] = 'P' This wont work because strings are imutable that means that i cant change the word
you can't use indexing to change individual elements of a string

'''

g = "gf dfg"
print(g.upper())
print(g.split())