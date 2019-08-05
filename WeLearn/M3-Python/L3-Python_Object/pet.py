class Pet(object):
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "Happy"

    def eat(self):
        print("> %s is eating" % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("< %s may have eaten too much." % self.name)
            self.mood = "Lethargic"

    def move(self):
        print("> %s is sitting still" % self.name)
        called = raw_input("Call %s (y/n?): " % self.name)
        if called is "y":
            if my_pet.is_hungry:
                print("%s is too hungry and won't move" % self.name)
            else:
                print("%s came to you!" % self.name)
        elif called is "n":
            print("%s stayed there..." % self.name)
        else:
            print("User input invalid, please enter y for yes or n for no")

my_pet = Pet("Fido", 3, "dog")

my_pet.is_hungry = True
print("is my pet hungry? %s" % my_pet.is_hungry)
my_pet.eat()
print("How about now? %s" % my_pet.is_hungry)
print("My pet is feeling %s" % my_pet.mood)

print("")

my_pet.move()
