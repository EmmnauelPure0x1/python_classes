# # Classes, objects and instantiation
#
# # How to create a class
# # Syntax: class name_of_class starting with capital letters
# # good naming convention is required.
#
# # Classes are a way top bring data functionality together
#
# class Dog:
#
#     animal_kind = "canin"
#
# # defining 'class variable'
#     def bark(self):
#         # self refers to current class - self says that this func belongs to dog class
#         return "woof"
#
# # to call we need to instantiate/initialise
# # In order to execute a class we have to create an object of this class
#
# # creating object of Dog
# # Objects and instances are the same
# # creating and instance of the dog class named batman
#
# batman = Dog()
#
# # prints memory location of instance
# print(batman)
#
# # prints the batman instance with the class attribute
# print(batman.animal_kind)
#
# # prints the class instance along with the class method/function
# print(batman.bark())
#
# DMX = Dog()
# print("DMX Barks:", DMX.bark())
# print(DMX.animal_kind)
#
# # any changes made to one object (not super class) will not have any impact to parent class.
#
# # This is account of the DMX obj
# DMX.animal_kind = "Rapper"
# print(DMX.animal_kind)
#
# # difference
# print("batman is:", batman.animal_kind)

class Dog:

    def __init__(self, name, colour): # initialising Dog Class
        self.name = name
        self.colour = colour
        self.animal_kind = "canin"

    def bark(self):
        return "woof"

fido = Dog("fido", "brown") # creating an object of Dog Class

print(fido.name)
print(fido.colour)
print(fido.animal_kind)
print(fido.bark()) #() after bark represents the fact that this is a method in the class.