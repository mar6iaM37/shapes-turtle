ask=input("The shape is -->")
color=input("Enter the color   ")
background=input("Enter background color   ")
def circle ():
    import turtle 
    r=int(input("The redius -->  "))    
    g=turtle.getscreen()
    c=turtle.Turtle()
    turtle.bgcolor(background)
    c.color(color)
    c.begin_fill()
    c.circle(r)
    c.dot(10)
    c.end_fill()
    turtle.done()
#star    
def star ():
    import turtle
    side=int(input("Enter side"))
    ge=turtle.getscreen()
    s=turtle.Turtle()
    turtle.bgcolor(background)
    s.color(color)
    s.begin_fill()
    for l in range (5):
        s.forward(side)
        s.right(144)
    s.end_fill()
    turtle.done()    
    s.hideturtle()
#heart    
def hr():
    import turtle
    h=turtle.Turtle()
    h.speed(-10)
    def curve ():
        for k in range (200):
            h.right(1)
            h.forward(1)            
    def heart ():
        h.color("red")
        h.begin_fill()
        h.left(140)
        h.forward(113)
        curve()
        h.left(120)
        curve()
        h.forward(112)
        h.end_fill()
    heart()        
    turtle.done()        
if ask=="circle":
    


