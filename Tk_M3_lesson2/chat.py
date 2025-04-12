from customtkinter import *
from PIL import Image

window = CTk()

window.geometry("400x500")

window.title("CHAT")

window.configure(fg_color="blue")

#--- load image for send ---- 
load_image = Image.open("assets/send2.png")
ready_image = CTkImage(light_image=load_image, size=(20,20))
#-----------------------------------


frame1 = CTkFrame(window, width=370, height=400)
frame1.pack_propagate(False)

box_msg = CTkTextbox(frame1 , width = 350 , height=350)
box_msg.pack(pady = 25)


frame1.pack(pady = 10)

frame2 = CTkFrame(window , width=370, height=50 )
frame2.pack_propagate(False)

button = CTkButton(frame2, text="Відправити" , 
                   width = 70 , height=30,
                   corner_radius = 50,
                   image = ready_image,
                   compound='right'
                    )

entry =CTkEntry(frame2, width = 250)
entry.pack(side = "left")
button.pack(side = 'right')
frame2.pack(pady = 10)
window.mainloop()