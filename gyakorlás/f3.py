import turtle

def rajzolj_oszlopot(t, magassag):
    if (100 > magassag):
        t.color("green")
    elif (200 > magassag):
        t.color("yellow")
    elif (200 <= magassag):
        t.color("red")
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    t.write(" "+ str(magassag))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.penup()
    t.end_fill()
    t.forward(10)
    t.pendown()

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.color("blue", "red")
Eszti.pensize(3)

xs = [48,117,200,240,160,260,220]

for m in xs:
    rajzolj_oszlopot(Eszti, m)


ablak.mainloop()