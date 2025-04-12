from customtkinter import *

window = CTk()

window.geometry("600x400")

window.title("CLICKER")

window.configure(fg_color = "pink")
def points():
    global point
    point = point + 1
    label.configure(text = str(point))
    
btn = CTkButton(window , corner_radius= 30 ,
                text= "CLICK",
                font = ('Arial', 30 , 'bold'),
                command= points)

label = CTkLabel(window , text = "0",  
                 width = 150 , height=150,
                 font=('Arial' , 30, 'bold'))

point = 0


btn.pack()
label.pack()

window.mainloop()