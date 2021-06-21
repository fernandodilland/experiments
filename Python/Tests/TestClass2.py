# Experiment programmed for practice by: Fernando Dilland Mireles Cisneros

class Test:
    def __init__(self, name, age): 
        self.name = name
        self.age = age

firstHuman = Test("John", 36) # The first piece of data "John" is managed
                                # with "name" of the class and "36" with "age"
                                # of the class.

print(firstHuman.name)
print(firstHuman.age)