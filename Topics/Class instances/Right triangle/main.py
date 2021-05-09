class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2

    @property
    def is_right(self):
        return self.a ** 2 + self.b ** 2 == self.c ** 2

    @property
    def area(self):
        return self.a * self.b / 2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(hyp=input_c, leg_1=input_a, leg_2=input_b)
print(triangle.area if triangle.is_right else "Not right")
