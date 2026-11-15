from tkinter import *


root=Tk()

root.title("PDE3413- Robot")
root.geometry("500x450+10+20")

## functions

def openDoor():
    msg_text="Opening door..."
    screen_msg.config(text=msg_text)

def checkBins():
    msg_text="Checking bins..."
    screen_msg.config(text=msg_text)


def cameraFeed():
    msg_text="Camera feed..."
    screen_msg.config(text=msg_text)


## buttons
open_door=Button(root, text="Open Door", command=openDoor)
open_door.place(x=20, y=80)


check_bins=Button(root, text="Check bins", command=checkBins)
check_bins.place(x=120, y=80)


camera_feed=Button(root, text="Camera feed", command=cameraFeed)
camera_feed.place(x=220, y=80)


## screen messages
screen_msg= Label(root,
                  text ='Raspberry Pi',
                  font = "90",fg="Navyblue",
                  borderwidth=1,
                  relief="solid")

screen_msg.place(x=20, y=200)









root.mainloop()



