# Cat class creation

# one function that returns meow

# create 2 class level variables
# create 3 objects
# display all information with each obj
# change class variable
# change the class variable values in each object and display
# sudo code each block of code


class Cat:

    animal_type = "feline"
    happy_cat = "purrrrr"

    def cry(self):
    # if cry funtion is called, call will "Meow"
        return "MEOWWWW"

    def hungry(self):
    # hungry mathod call it will return below string
        return "the cat seems hungry..."

    def tired(self):
    # cat is tired so value is true
        return True

# instance of cat created
bip = Cat()

# The type of animal is printed
print(bip.animal_type)

# animal's mood is printed
print(bip.happy_cat)

# cat cry function called
print(bip.cry())

#cat is hungry
print(bip.hungry())

#cat is tired which equates to true
print(bip.tired())






