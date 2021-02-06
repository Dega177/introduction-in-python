from time import sleep
from itertools import cycle


class TrafficLight:

    __colors = cycle(['Красный', 'Желтый', 'Зеленый', 'Желтый'])

    def running(self):
        while True:
            color = next(self.__colors)
            if color != 'Желтый':
                print(f'\33[31m{color}\033[0m') if color == 'Красный' else print(f'\33[32m{color}\033[0m')
                for x in range(7, 0, -1):
                    print(x)
                    sleep(1)
            else:
                print(f'\33[33m{color}\033[0m')
                for x in range(2, 0, -1):
                    print(x)
                    sleep(1)


TrafficLight().running()
