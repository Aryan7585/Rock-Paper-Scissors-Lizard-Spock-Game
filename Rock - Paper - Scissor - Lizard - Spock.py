from re import match
from tkinter import *
import random
from typing import Match


root = Tk()


root.geometry("710x575")



root.title("Rock Paper Scissor Lizard Spock Game ")

# Assigning Values 

computer_value = {
	"0":"Rock",
	"1":"Paper",
	"2":"Scissor",
    "3":"Lizard",
    "4":"Spock"
}

c_v = 0
 
# Reset Button 

def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	b4["state"] = "active"
	b5["state"] = "active"
	l1.config(text = "Player")
	l2.config(text = "Computer")
	l4.config(text = "")








# Quit Game 

def quit_game():
	root.destroy()


# Disabling Button 

def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"
	b4["state"] = "disable"
	b5["state"] = "disable"

# Selecting Rock 

def isrock():
	c_v = computer_value[str(random.randint(0,4))]
	if c_v == "Rock":
		match_result1 = "Match Draw"
		l2.config(text="Rock")
	elif c_v == "Paper":
		match_result1 = "Computer Win"
		l2.config(text="Paper")		
	elif c_v=="Scissor":
		match_result1 = "Player Win"
		l2.config(text="Scissor")
	elif c_v=="Lizard":
		match_result1 = "Player Win "
		l2.config(text="Lizard")	
	elif c_v == "Spock":
		match_result1 = "Computer Win "
		l2.config(text = "Spock")	
	l4.config(text = match_result1)
	l1.config(text = "Rock")

	button_disable()

# Selecting Paper 

def ispaper():
	c_v = computer_value[str(random.randint(0,4))]
	if c_v == "Paper":
		match_result2 = "Match Draw"
		l2.config(text="Paper")
	elif c_v == "Scissor":
		match_result2 = "Computer Win "
		l2.config(text="Scissor")	
	elif c_v == "Rock":
		match_result2 = "Player Win "
		l2.config(text="Rock")
	elif c_v == "Lizard":
		match_result2 = "Computer Win"
		l2.config(text="Lizard")
	elif c_v == "Spock":
		match_result2 = "Player Win"
		l2.config(text="Spock")			

	l4.config(text = match_result2)
	l1.config(text = "Paper")

	button_disable()

# Selecting Scissor 

def isscissor():
	c_v = computer_value[str(random.randint(0,4))]
	if c_v == "Scissor":
		match_result3 = "Match Draw"
		l2.config(text="Scissor")
	elif c_v == "Rock":
		match_result3 = "Computer Win"
		l2.config(text="Rock")	
	elif c_v == "Paper":
		match_result3 = "Player Win "
		l2.config(text="Paper")
	elif c_v == "Lizard":
		match_result3 = "Player Win"
		l2.config(text="Lizard")
	elif c_v == "Spock":
		match_result3 = "Computer Win "
		l2.config(text="Spock")			

	l4.config(text = match_result3)
	l1.config(text = "Scissor")

# Selecting Lizard

def islizard():
	c_v = computer_value[str(random.randint(0,4))]
	if c_v == "Lizard":
		match_result4 = "Match Draw"
		l2.config(text="Lizard")
	elif c_v == "Rock":
		match_result4 = "Computer Win "
		l2.config(text="Rock")
	elif c_v == "Paper":
		match_result4 = "Player Win"
		l2.config(text="Paper")
	elif c_v == "Scissor":
		match_result4 = "Computer Win"
		l2.config(text="Scissor")
	elif c_v == "Spock":
		match_result4 = "Player Win"
		l2.config(text="Spock")


	l4.config(text = match_result4)
	l1.config(text = "Lizard")

	button_disable()

# Selecting Spock 

def isspock():
	c_v = computer_value[str(random.randint(0,4))]
	
	if c_v == "Paper":
		match_result5 = "Computer Win"
		l2.config(text = "Paper" )
	elif c_v == "Rock":
		match_result5 = "Player Win"
		l2.config(text = "Rock" )
	elif c_v == "Scissor":
		match_result5 = "Player Win"
		l2.config(text = "Scissor" )
	elif c_v == "Lizard":
		match_result5 = "Computer Win"
		l2.config(text = "Lizard" )
	elif c_v == "Spock":
		match_result5 = "Match Draw"
		l2.config(text = "Spock" )

	l4.config(text = match_result5)
	l1.config(text = "Spock")

	button_disable()

# Code for output  

l = Label(root,
	text = "Rock - Paper - Scissors - Lizard - Spock",
	font = "normal 20 bold",
	fg = "blue")

l.pack(pady = 10)

l_1 =Label(root,
	text = " Player    vs  Computer ",
	font = "normal 17 bold" ,	
	fg = "white",
	bg = "black"
	)

l_1.pack(pady = 10)
frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text = "Player",
		font = 10)

lv = Label(frame,text="vs",font=10)


comp = "Computer"


l2 = Label(frame,
		text = comp,
		font = 10)
		


l1.pack(side = LEFT)
l2.pack(side=RIGHT)
lv.pack()


l4 = Label(root,
		text = "",
		font = "normal 20 bold",
		bg = "white",
		width = 15 ,
		borderwidth = 2,
		relief = "solid")
l4.pack(pady = 20)

# Making frame 

frame1 = Frame(root)
frame1.pack()

# Making Buttons

b1 = Button(frame1, text = "Rock",
			font = 10, width = 7,
			command = isrock)

b2 = Button(frame1, text = "Paper ",
			font = 10, width = 7,
			command = ispaper 
			)

b3 = Button(frame1, text = "Scissor",
			font = 10, width = 7,
			command=isscissor
			)

b4 = Button(frame1, text = "Lizard",
			font = 10, width = 7
			,command = islizard)

b5 = Button(frame1, text = "Spock",
			font = 10, width = 7
			,command = isspock)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(side = LEFT,padx = 10)
b4.pack(side = LEFT,padx = 10)
b5.pack(side = LEFT,padx = 10)

# Making Reset Button 

reset_button = Button(root, text = "Reset Game",
	font = 10, fg = "White",
	bg = "black", command = reset_game)
reset_button.pack(pady = 15)

# Making Quit Game button 

quit_game = Button(root, text = "Quit Game ",
	font = 10, fg = "Red",
	bg = "black", command = quit_game)

quit_game.pack()
  
root.mainloop()
