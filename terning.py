class Electrobike():
    def __init__ (self,name, speed, battery):
        self.name = name
        self.speed = speed
        self.battery = battery

    def drive (self):
        print(f"{self.name} едет в горы")




    def overclocking(self, max_speeed):
        if max_speeed >= 45:
            print(f"Скорость велосипеда {self.name} слишком большая")
            self.battery -= 40
        elif max_speeed == 15 or max_speeed <= 45:
            print(f"Крутите педали быстрее.")
            self.battery -= 5
        else:
            print(f"{self.name} стоит на месте")



    def info(self):
         print(f"{self.name}")
         print(f"{self.speed}")
         print(f"{self.battery}")




bike_1 = Electrobike("Шенди", 50, 100)

bike_1.info()
bike_1.drive()
bike_1.info()
bike_1.overclocking(37)
bike_1.info()
bike_1.overclocking(50)
bike_1.info()

