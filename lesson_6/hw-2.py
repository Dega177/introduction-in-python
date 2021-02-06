class Road:

    _asphalt_weight_per_meter = 25
    _asphalt_thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_weight(self):
        return self._width * self._length * Road._asphalt_weight_per_meter * Road._asphalt_thickness / 1000


a310 = Road(5000, 20)
print(f'{a310.get_asphalt_weight():.2f} т.')
