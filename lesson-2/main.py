# <------------------------------> Task one <------------------------------>
class MyClass:
    variable1 = 1
    variable2 = 2

    def foo(self): # We'll explain self parameter later
        return "Hello from function foo"


my_object = MyClass()
another_object = MyClass()

my_object.variable2 = 3

print(my_object.variable2)
print(another_object.variable2)

#Print variable1 from my_object
???

# Print call method foo() of object my_object
???
# <---------------------------> End of task one <--------------------------->



# <------------------------------> Task two <------------------------------>
class Car:
    color = ""

    def description(self):  # we'll explain the self parameter later
        description_string = f"This is a {self.color} car."
        return description_string


car1 = Car()
car2 = ???

car1.color = "blue"
car2.color = ???

# Print description() method of car1
???

# Print description() method of car2
???
# <---------------------------> End of task two <--------------------------->