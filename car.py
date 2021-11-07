
class Car:

    def __init__(self, fuelrate = 0, velocity = 0):
        # super().__init__( distancetowork)
        # self.name = name
        self.fuelrate = fuelrate
        self.velocity = velocity

    @property
    def fuelrate(self):
        return self.__carrate

    @fuelrate.setter
    def fuelrate(self, carrate) -> None:
        self.__carrate = abs(carrate)
        if 0 < self.__carrate <= 100:
            print("Good Fuel Rate")
        else:
            # raise ValueError("Wrong fuel rate")
            print("Wrong fuel rate")

    @property
    def velocity(self):
        return self.__carvelocity

    @velocity.setter
    def velocity(self, carvelocity):
        self.__carvelocity = abs(carvelocity)
        if 0 < self.__carvelocity <= 200:
            print("Good velocity")
        else:
            # raise ValueError("Wrong fuel rate")
            print("Wrong Velocity rate")

    def run(self, velocity, distancetowork):
        self.velocity = velocity
        startfual = self.fuelrate
        self.fuelrate = self.fuelrate - distancetowork
        finalfuel = startfual - self.fuelrate

        if finalfuel == 0:
            if distancetowork == 0:
                print("You're Arrived")
            else:
                print("No more Fuel...")
        else:
            print("You're Arrived")

        self.stop(distancetowork)
        print("we are done.....")

    def stop(self, distancetowork):
        print("From Stop Method")
        self.velocity = 0
        print(f"Your left Distance is {distancetowork}")


#  name, distancetowork, fuelrate = 0, velocity = 0 ):
c = Car(100, 20)
# c.run(20, 100)
