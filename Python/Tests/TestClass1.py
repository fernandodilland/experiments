# Experiment programmed for practice by: Fernando Dilland Mireles Cisneros

class Human:
    """
    init is short for initialization. It is a constructor which gets called
    when you make an instance of the class and it is not necessary. But usually
    it our practice to write init method for setting default state of the object.
    If you are not willing to set any state of the object initially then you
    don't need to write this method.
    """
    def __init__(self, name, age): 
        """
        self represents the instance of the class. By using the “self” keyword
        we can access the attributes and methods of the class in python. It binds
        the attributes with the given arguments.
        The reason you need to use self. is because Python does not use the @
        syntax to refer to instance attributes. Python decided to do methods in
        a way that makes the instance to which the method belongs be passed
        automatically, but not received automatically: the first parameter of
        methods is the instance the method is called on.
        """
        self.name = name
        self.age = age

firstHuman = Human("John", 36) # The first piece of data "John" is managed
                                # with "name" of the class and "36" with "age"
                                # of the class.

print(firstHuman.name)
print(firstHuman.age)