"""
class point:      # point is the class
    def move(self):     # move is the method of the class point
        print("move")

    def draw(self):
        print("draw")


our_class = point()
our_class.draw()
our_class.move()
"""


# attribute
class point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


our_class = point()
our_class.x = 10  # x is an attribute of ourclass
our_class.y = 20  # y is an attribute of ourclass
print(our_class.x)
our_class.draw()
our_class.move()


his_class = point()
his_class.x = 30
his_class.y = 50

print(his_class.y)



