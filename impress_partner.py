import turtle
import turtle as trt 
from turtle import *
import time
win=Screen()
win.setup(1250,650)
win.title('My Cute Baby')
time.sleep(1)
win.bgcolor('white')
time.sleep(1)
a=trt.Turtle()
a.color('blue','red')
a.shape('arrow')
a.penup()
time.sleep(1)
a.goto(-600,250)
a.width(8)


#B
a.left(90)
a.penup()
a.left(180)
a.pendown()
a.circle(150/4)
a.forward(150/2)
a.circle(150/4)

#A
a.penup()
a.forward(150/4)
a.left(90)
a.forward(150/4+75)
a.left(90)
win.bgcolor('#75a3a3')
a.pendown()
a.forward(150)
a.right(90)
a.forward(70)
a.right(90)
a.forward(150/2)
a.right(90)
a.forward(70)
a.bk(70)
a.left(90)
a.forward(150/2)
a.left(90)

#B
a.penup()
a.forward(150/4)
a.left(90)
a.forward(112.5)
a.left(180)
a.pendown()
a.circle(150/4)
a.forward(150/2)
a.circle(150/4)
win.bgcolor('#bfff80')
#y
a.penup()
a.forward(150/4)
a.left(90)
a.forward(3*(150/4))



#Y
a.pendown()
a.forward(70)
a.left(90)
a.forward(150)
a.bk(150/2)
a.left(90)
a.forward(70)
a.right(90)
a.forward(150/2)


a.penup()
a.backward(150)
a.right(90)



def curve(): 
	for i in range(200): 
		a.right(1) 
		a.forward(1) 


def heart(): 
	a.fillcolor('red')  
	a.begin_fill() 
	a.left(140) 
	a.forward(113)
	win.bgcolor('#ffcccc')
	curve() 
	a.left(120) 
	curve() 
	a.forward(112) 
	a.end_fill() 
 
a.penup()
a.setpos(0,-100) 
a.pendown()
a.width(4)
a.shape('turtle')
a.color('white','yellow')
heart()

a.penup()
a.setpos(120,-100)
a.left(50)
win.bgcolor('#80dfff')
a.pendown()
a.width(8)
a.forward(150)
a.left(90)
a.forward(80)

a.left(90)
a.forward(150)
a.penup()
a.setpos(400,245)

#Rose Flower

a.pendown ()
a.width(2)
a.color('black','red')
a.shape('circle')
a.right (90)

# flower base
a.fillcolor ("red")
a.begin_fill ()
a.circle (10,180)
a.circle (25,110)
a.left (50)
a.circle (60,45)
a.circle (20,170)
a.right (24)
a.fd (30)
a.left (10)
a.circle (30,110)
a.fd (20)
a.left (40)
a.circle (90,70)
a.circle (30,150)
a.right (30)
a.fd (15)
a.circle (80,90)
a.left (15)
a.fd (45)
a.right (165)
a.fd (20)
a.left (155)
a.circle (150,80)
a.left (50)
a.circle (150,90)
a.end_fill ()

# Petal 1
a.left (150)
a.circle (-90,70)
a.left (20)
a.circle (75,105)
a.setheading (60)
a.circle (80,98)
a.circle (-90,40)

# Petal 2
a.left (180)
a.circle (90,40)
a.circle (-80,98)
a.setheading (-83)

# Leaves 1
a.fd (30)
a.left (90)
a.fd (25)
a.left (45)
a.fillcolor ("green")
a.begin_fill ()
a.circle (-80,90)
a.right (90)
a.circle (-80,90)
a.end_fill ()
a.right (135)
a.fd (60)
a.left (180)
a.fd (85)
a.left (90)
a.fd (80)

# Leaves 2
a.right (90)
a.right (45)
a.fillcolor ("green")
a.begin_fill ()
a.circle (80,90)
a.left (90)
a.circle (80,90)
a.end_fill ()
a.left (135)
a.fd (60)
a.left (180)
a.fd (60)
a.right (90)
a.circle (200,60)

pen=trt.Turtle('classic')
def txt():
	pen.up()
	pen.setpos(-600,95)
	pen.down()
	pen.color('deep pink')
	pen.write('\u2764\ufe0f \u2764\ufe0f \u2764\ufe0f My Angel Baby \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f', font=("Courier",15,"italic"))
	time.sleep(1.5)
	pen.up()
	pen.setpos(-600,55)
	pen.down()
	pen.color('red')
	pen.write("My Sweet Heart \u2764\ufe0f \u2764\ufe0f \u2764\ufe0f",font=("Courier",15,"italic"))
	time.sleep(1.5)
	pen.up()
	pen.setpos(-600,10)
	pen.down()
	pen.color('red')
	pen.write(" \u2764\ufe0f \u2764\ufe0f My Lovely Cutiee \u2764\ufe0f \u2764\ufe0f ",font=("Courier",15,"italic"))
	time.sleep(2)
	pen.up()
	pen.setpos(-600,-40)
	pen.down()
	pen.color('#992600')
	pen.write("You are mine BABY",font=("Courier",20,"italic"))
	time.sleep(2.5)
	pen.up() 
	pen.setpos(-600,-125) 
	pen.down()
	pen.color('deep pink') 
	pen.write("I love you Baby \u2764\ufe0f ...", font=("Courier", 15, "italic"))
	time.sleep(2)
	pen.up() 
	pen.setpos(-600,-155) 
	pen.down() 
	pen.color('deep pink') 
	pen.write("U are the most liked Person\u2764\ufe0f in my life Baby...", font=("Courier", 15, "italic"))
	time.sleep(2)
	pen.up() 
	pen.setpos(-600,-185) 
	pen.down() 
	pen.color('deep pink') 
	pen.write("I will never forget our memories...", font=("Courier", 15, "italic"))
	time.sleep(3)
	pen.up() 
	pen.setpos(-600,-215) 
	pen.down() 
	pen.color('deep pink') 
	pen.write("Your smile is my favorite thing in the world.", font=("Courier", 15, "italic"))
	time.sleep(2)
	pen.up() 
	pen.setpos(-600,-245) 
	pen.down() 
	pen.color('deep pink') 
	pen.write("The way you understand and support me means more than words can express", font=("Courier", 15, "italic"))
	time.sleep(2)
	pen.up() 
	pen.setpos(-600,-275) 
	pen.down() 
	pen.color('deep pink') 
	pen.write("I am missing 🙁🙁 you every moment Dear", font=("Courier", 15, "italic"))
	time.sleep(2)
	pen.up() 
	pen.setpos(-600,-305) 
	pen.down() 
	pen.color('red') 
	pen.write("I Love you Baby \u2764\ufe0f...You are MINE... HAPPY VALENTINES DAY DEAR", font=("Courier", 15, "italic"))



win.title('My Cute Baby -  I \u2764\ufe0f U ')

win.bgcolor('#ecb3ff')
txt()

win.mainloop()












