class Square():

    def __init__(self, w , l):

        self.length = l
        self.width = w
 

    def rectangle_area(self):

        return self.length*self.width
    

newRectangle = Square(12, 10)
print("Dimension of rectangle - Length:  %d Width: %d" % (newRectangle.length, newRectangle.width))
print("Area of rectangle: %d" % (newRectangle.rectangle_area()))
