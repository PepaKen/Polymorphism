from trueRectangle import Rectangle, Square, Circle

rectangle_1 = Rectangle(3, 4)
rectangle_2 = Rectangle(12, 5)

square_1 = Square(4)
square_2 = Square(14)

circle_1 = Circle(3)
circle_2 = Circle(16)

figures = [rectangle_1, rectangle_2, square_1, square_2, circle_1, circle_2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.getAreaSquare())
    elif isinstance(figure, Circle):
        print(figure.getAreaCircle())
    else:
        print(figure.getArea())
