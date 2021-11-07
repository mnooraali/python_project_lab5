from person import Person
from car import Car

class Employee(Person):

    # moods = ("Happy", "Lazy", "Tired")

    def __init__(self, name, id, car, email=" ", salary= 0, distancetowork = 0):
        super().__init__(name)
        self.id = id
        self.car = Car(car)
        self.email = email
        self.salary = salary
        self.distancetowork = distancetowork
        # self.workhours = workhours
        # self.gasamount = gasamount

    def work(self, workhours):
        if workhours == 8:
            self.mood = f"Your mood is {Person.moods[0]}"
        elif workhours < 8:
            self.mood = f"Your mood is {Person.moods[1]}"
        else:
            self.mood = f"Your mood is {Person.moods[2]}"
        print(self.mood)

    def drive(self):
        pass

    def refuel(self, gasamount = 100):
        gasamount = gasamount - 10
        return gasamount

    def sendmail(self):
        pass

# name, id = 0, car = "", email =" ", salary = 0, distancetowork = 0, workhours = 0):

e = Employee("Toyota", 10,  Car.__init__(50, 50), "ahmed@gmail.com",1000, 50)

# e.work(10)
