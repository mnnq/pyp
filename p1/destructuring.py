people = [("BOb",42,"mech"),("BObfew",33,"gfdfg"),("Basdadsb",11,"echa")]

dd = ("bob", 42,"mec")
name, _, prof = dd

#with _ i tell python that i dont want to use that value
print(name, prof)

for name, age, profession in people:
    print(f"name: {name} name: {profession} name: {age}")


    head, *tail = [1,2,3,4,5]
    print(head, tail)