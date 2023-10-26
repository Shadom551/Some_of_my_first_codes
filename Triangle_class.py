import math
class Triangle:
    
    def __init__(self,side_1,side_2,side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        
        
    def __str__(self):
        l = [self.side_1,self.side_2,self.side_3]
        m = []
        for k in range(3):
            i = max(l)
            m.append(i)
            l.pop(l.index(i))

        if m[0] >= m[1] + m[2]:
            return "It isn't a Triangle."
        elif self.side_1 == self.side_2 and self.side_2 == self.side_3:
            return "It's an Equilateral triangle"
        elif self.side_1 == self.side_2 or self.side_1 == self.side_3 or self.side_2 == self.side_3:
            return "It's an Isosceles triangle"
        return "It's a Scalene triangle"

    def area(self):            
        if Triangle.__str__(self) == "It isn't a Triangle.":
            return "It isn't a Triangle."
        else:    
            sp = (self.side_1 + self.side_2 + self.side_3)/2
            return math.sqrt(sp*(sp-self.side_1)*(sp-self.side_2)*(sp-self.side_3))

    def perimeter(self):
        if Triangle.__str__(self) == "It isn't a Triangle.":
            return "It isn't a Triangle."
        return self.side_1 + self.side_2 + self.side_3
