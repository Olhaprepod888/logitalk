from customtkinter import*
from PIL import Image

#---------- create client connection -----
from socket import*
import threading

client = socket(AF_INET , SOCK_STREAM)
client.connect(("localhost" , 12345))




   
# -------------------------------------------
#------------------ create window -------------------------

window = CTk()
window.geometry("400x550")
window.configure(fg_color = "orange")

#----- FRAME1 -----------
fr1 = CTkFrame(window, height= 400 , width= 350)                # 
fr1.pack_propagate(False)                                       # 
fr1.pack(pady= 10)
                                                                # 
message_box = CTkTextbox(fr1 ,height= 380 , width= 320)
message_box.configure(state="disabled")
message_box.pack(pady = 10)

#----- FRAME2 -----------
fr2 = CTkFrame(window, height= 80, width= 350)
fr2.pack_propagate(False)
fr2.pack(pady= 10)

entry = CTkEntry( fr2, placeholder_text="Введіть повідомлення...",
                 height= 60 ,width= 230)
entry.pack(pady= 20 , side = "left" , padx = 10)

#--- image for send-button --- 
img_load = Image.open("assets/send.png")
ready_image = CTkImage( light_image= img_load , size=(20 , 20))


def click_send():
    a = entry.get()
    entry.delete(0, END)
    
    
    
    message_box.configure(state="normal")
    message_box.insert(END, a + "\n")
    message_box.configure(state="disabled")
    
    client.send(a.encode())
    
def recieve():
    while True:
        try:
            message = client.recv(1024).decode()
            message_box.configure(state="normal")
            message_box.insert(END,message  + "\n")
            message_box.configure(state="disabled")

            print(message)
            
        except:
            pass

threading.Thread(target=recieve).start()



# def send_message():
#    while True:
#        client_message = input("__>")
#        client.send(client_message.encode())

# threading.Thread(target=send_message).start()




btn_send = CTkButton(fr2, text="SEND" , image = ready_image, compound="right", 
                     width= 90 ,height= 38,
                     command= click_send )
btn_send.pack(pady = 20)


window.mainloop()


