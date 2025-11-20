class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed



class Bus(PublicTransport):



class Tram(PublicTransport):













# transport = PublicTransport('Автомобиль', 500, 2040, 'Фиолетовый', 300)
# first_bus = Bus('ЛиАЗ', 210, 2015, 'Зеленый', 100, 70, 1232, 32)
# second_bus = Bus('VOLGABUS', 320, 2019, 'Желтый', 110, 39, 1111, 32)
# first_tram = Tram('71-931M', 125, 2010, 'Красный', 75, 5, 15, 32)
# second_tram = Tram('71-409-1', 240, 2018, 'Белый', 85, 7, 17, 32)