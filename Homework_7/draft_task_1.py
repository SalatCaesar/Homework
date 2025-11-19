# Можно улучшить:
# 1. Добавить инпут
# 2. Добавить валидацию для ввода координат
# 3. Попробовать реализовать через график функции
# 4. Добавить
class Segment:
    def __init__(self, first_point, second_point):
        self.a = first_point
        self.b = second_point
    def len(self):
        c = ((self.b[0]-self.a[0])**2+(self.b[1]-self.a[1])**2)**(1/2)
        return round(c, 2)
    def abs(self):
        return self.a[0] * self.b[0] <= 0
    def ord(self):
        return self.a[1] * self.b[1] <= 0
d = Segment((-2, 3), (4, 0))
Segment.len(d)
Segment.abs(d)
Segment.ord(d)