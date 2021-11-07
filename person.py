class Person:

    moods = ("Happy", "Lazy", "Tired")

    def __init__(self, name , money = 0, mood = None, healthrate = None):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthrate
        # self.sleephours = sleephours
        # self.meals = meals

    def sleep(self, sleephours):
        if sleephours == 7:
            # self.mood = "Happy"
            self.mood = f"Your mood is {Person.moods[0]}"
        elif sleephours < 7:
            # self.mood = "Tired"
            self.mood = f"Your mood is {Person.moods[2]}"
        else:
            # self.mood = "Lazy"
            self.mood = f"Your mood is {Person.moods[1]}"

        print(self.mood)


    def eat(self, meals):
        if meals == 3:
            self.healthrate = "100%"
        elif meals == 2:
            self.healthrate = "75%"
        elif meals == 1:
            self.healthrate = "50"

        print(f"Your Health is {self.healthrate} based on your meals")

    def buy(self, items):
        if items.isdigit():
            self.money = self.money - (10 * items)
        else:
            print("Wrong items")

    @property
    def money(self):
        return self.__salary

    @money.setter
    def money(self, salary):
        self.__salary = abs(salary)
        if self.__salary < 1000:
            # raise ValueError("Wrong Salary,, The Salary should be > 1000 ")
            print("Wrong salary,, The Salary should be > 1000 ")
        else:
            print("Good Salary")

# name, money, mood, healthrate, workhours, sleephours, meals):


p = Person("Ahmed", 100, 10, 1)
# print(p)
p.sleep(10)
p.eat(3)

