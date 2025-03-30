class car:
    def __init__(make, model, year, color):
        make.model = model
        make.year = year
        make.color = color
    def describe(make):
        print("This car is a " + make.model + " from " + make.year + " and is " + make.color + " in color.")

car1 = car("Toyota Corolla", "2020", "Black")
car1.describe()