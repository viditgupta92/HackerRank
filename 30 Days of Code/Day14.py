class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = 0
        length = len(self.__elements)
        for i in range(length):
            for j in range(length):
                diff = (self.__elements[i] - self.__elements[j])
                if diff > self.maximumDifference:
                    self.maximumDifference = diff


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)