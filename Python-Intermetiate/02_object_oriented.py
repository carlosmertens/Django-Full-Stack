# OBJECT ORIENTED PROGRAMMING - OOP

# *** Create a Class Sample ***
print("\n***Sample Class")


class Sample():

    def __init__(self):  # Create a method of the class __init__(attributes)
        pass


x = Sample()
print(type(x))

# *** Create a Class Dog ***
print("\n***My dog Class")


class Dog():

    # Class Object Attributes
    species = "Mammal"  # General attributes for all object created

    def __init__(self, breed, name):

        self.breed = breed  # Create attribute for the method of the class
        self.name = name


my_dog = Dog(breed="Boxer", name="Caligula")
print("My dog's breed is", my_dog.breed)

# Create another dog
her_dog = Dog("Huskie", "Macarena")
print("Her dog's name is", her_dog.name)
print("Her dog's belongs to the {} species".format(her_dog.species))

# *** Create a Class Circle ***
print("\n***Circle Class")


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):  # Creat an executable method
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new):
        self.radius = new  # Change radius in place without returning anything


my_circle = Circle(3)
print("My area is", my_circle.area())

# Call method to change radius
my_circle.set_radius(100)
print("My new area is", my_circle.area())

# *** Inheritance ***
print("\n***Inheritance")

# Create a Class Animal


class Animal():

    def __init__(self):
        print("Animal created!")

    def who_am_I(self):
        print("I am an animal")

    def eat(self):
        print("Eating")


my_animal = Animal()
my_animal.who_am_I()
my_animal.eat()

# Create a Class Cat


class Cat(Animal):  # Cat inherit all attributes, methods from Animal Class

    def __init__(self):
        Animal.__init__(self)
        print("Cat created!")

    def meaw(self):
        print("Meaaaawwww!")

    def eat(self):  # Overwrite the Animal Class method
        print("Cat is eating")


print("\n(Create a Cat)")

my_cat = Cat()
my_cat.who_am_I()
my_cat.eat()
my_cat.meaw()

# *** Specail Methods ***
print("\n***Special Methods")

# Create a Book Class


class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """
        String Representation Speacial Method.

        To return a string desire when the method print() is called.
        """

        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        """
        Lenght Special Method

        To return the lenght of the class
        """

        return self.pages

    def __del__(self):
        """Delete Object Speciall Method."""
        print("The book has been destryed!")


my_book = Book("Python", "Carlos Mertens", 120)
# Without the String Representation method in the class, it would print an object location
print(my_book)
print(len(my_book))

del my_book  # Call "del" special method in the class
