class Car:
    def __init__(self, b, ms, speed):
        self.brand = b
        self.max_speed = ms
        self.max_speed = speed


class Truck(Car):
    def __init__(self, b, ms, speed, nt, ml):
        super().__init__(b, ms, speed)
        self.num_trailers = nt
        self.max_load = ml

    def get_CAR(self):
            return self.brand,self.max_speed,self.max_speed,self.num_trailers,self.max_load
p = Truck(30, 40, 30, 20, 20)
print(p.get_CAR())
