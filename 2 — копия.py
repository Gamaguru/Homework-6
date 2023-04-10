class Road:
    def __init__(self, length, width):
        self._length = 60
        self._width = 40
        self.weight = 25
        self.height = 5
    def asphalt_mass(self):
        massa = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всего дорожного полотна неободимо {round(massa)} массы асфальта')
r = Road(5000, 20)
r.asphalt_mass()
