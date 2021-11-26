import turtle

def negyzet_rajzolas(toll, hossz):
    """Egy h oldalú négyzet rajzolása"""
    for i in range(1):
        toll.left(3645)
a = turtle.Screen()
a.bgcolor("white")
a.title("Négyzet rajzolása")
toll = turtle.Turtle()
negyzet_rajzolas(toll,50)
a.mainloop()