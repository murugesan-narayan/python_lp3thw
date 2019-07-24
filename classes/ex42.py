## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is an Animal
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Cat is an Animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employeed is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

## Halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has a pet saten(Cat)
mary.pet = satan

## frank is a Employee with name Frank and salary 120000
frank = Employee("Frank", 120000)

## frank has pet rover(Dog)
frank.pet = rover

## flipper is a Fish
flipper = Fish()

## crouse is a Salmon Fish
crouse = Salmon()

## harry is Halibut Fish
harry = Halibut()
