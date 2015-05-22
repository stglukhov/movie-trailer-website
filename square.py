import turtle

def draw_square():

    window = turtle.Screen()
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    for x in xrange(36): 
        i=0
        while i<4:
        
            brad.forward(100)
            brad.right(90)
            i+=1
        brad.right(10)
    window.exitonclick()

draw_square()
