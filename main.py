import math


class Tetrahedron:
    def __init__(self, side: int):
        self.side = side
        self.area = self.side**2 * math.sqrt(3)
        self.volume = math.sqrt(3)/18 * self.side ** 4

    def __str__(self):
        return f'площадь правильного тетраэдра = {self.area:.2f}\n' \
               f'объём правильного тетраэдра = {self.volume:.2f}'


tr1 = Tetrahedron(5)
print(tr1)

# площадь правильного тетраэдра = 43.30
# объём правильного тетраэдра = 60.14
#
# Process finished with exit code 0

