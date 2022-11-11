class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(selft):
        return (2 * selft.width) + (2 * selft.height)

    def get_diagonal(self):
        return ((self.width**2) + (self.height**2))**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            pic = ""
            for i in range(self.height):
                for j in range(self.width):
                    pic += "*"
                pic += "\n"
            return pic

    def get_amount_inside(self, polygon):
        if polygon.width > self.width or polygon.height > self.height:
            return 0
        else:
            row = int(self.height/polygon.height)
            col = int(self.width/polygon.width)
            return row * col

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_height(height)
        super().set_width(height)

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
