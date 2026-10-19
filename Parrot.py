class parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

woo = parrot("Woo",15)
Blu = parrot("Blu",10) 


print("Blu is a ",Blu.species)
print("Woo is also a ",woo.species)

print("{} is {} years old".format(Blu.name,Blu.age))
print("{} is {} years old".format(woo.name,woo.age))