import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        vec1 = [self.x, self.y, self.z]
        vec2 = [no.x, no.y, no.z]
        return Points(*[x1 - x2 for x1, x2 in zip(vec1, vec2)])

    def dot(self, no):
        vec1 = [self.x, self.y, self.z]
        vec2 = [no.x, no.y, no.z]
        return sum(x1 * x2 for x1, x2 in zip(vec1, vec2))

    def cross(self, no):
        vec1 = [self.x, self.y, self.z]
        vec2 = [no.x, no.y, no.z]
        x = (vec1[1] * vec2[2]) - (vec1[2] * vec2[1])
        y = (vec1[2] * vec2[0]) - (vec1[0] * vec2[2])
        z = (vec1[0] * vec2[1]) - (vec1[1] * vec2[0])
        return Points(x, y, z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))