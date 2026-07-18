#class to perform operation on rectangle



class Rectangle:
    #member variables
    length = 0
    breadth = 0
    #method to initialize the data
    def initialize(self, l, b):
        self.length = l
        self.breadth = b
        #method to display the data
    def display (self):
        print("===== Rectangle =====")
        print("Length of rectangle is: ", self.length,"cm")
        print("Breadth of rectangle is: ", self.breadth,"cm")
        #method to calculate area
    
        rect=Rectangle()
        rect.initialize(20,50)
        rect.display()
        