"""The Rectangle-exercises 9.1-9.3."""

class Rectangle:
    """A class that represents a Rectangle."""

    def __init__(self, width, height, cx, cy):
        self.width = width
        self.height = height
        self.x_c = cx
        self.y_c = cy

    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*self.width+2*self.height
    
    def get_corners(self):
        corners = [
                    [
                        self.x_c-self.width/2,
                        self.x_c-self.width/2,
                        self.x_c+self.width/2,
                        self.x_c+self.width/2
                    ],
                    [
                        self.y_c-self.height/2,
                        self.y_c+self.height/2,
                        self.y_c+self.height/2,
                        self.y_c-self.height/2                        
                    ]
        ]
        return corners
    
    def translate(self, r):
        self.x_c += r.x
        self.y_c += r.y
    