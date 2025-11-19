class Segment:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point
    def sum(self):
        print(self.first_point + self.second_point)
a = Segment (1, 2)
Segment.sum(a)