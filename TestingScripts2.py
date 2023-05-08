from tkinter import *

window=Tk()
window.geometry("1920x1080")

imagecanv=Canvas(window,width=1920,height=1080)
bgimage=PhotoImage(file="D:\\NUST\\Assignments\\Fundamentals of Programming\\End Semester Project\\GameAssets\\launcherBG.png")
bgimage.subsample(200,200)

imagecanv.create_image(0,0,image=bgimage,anchor='nw')
imagecanv.place(relwidth=1,relheight=1)
window.mainloop()



# class MainWindow(Frame):
#     def __init__(self):
#         super().__init__()
#         self.pack(expand=Y,fill=BOTH)

#         outercanvas = Canvas(self, width=200, height=100, bg='#00ffff')
#         outercanvas.pack(expand=Y,fill=BOTH)

#         innercanvas = Canvas(outercanvas, width=100, height=50)
#         outercanvas.create_window(50, 25, anchor=W, window=innercanvas)

        

#         innercanvas.create_text(10, 10, anchor=NW, text="Hello")

# root = MainWindow()
# root.mainloop()









# from ctypes import WINFUNCTYPE
# from time import sleep
# from tkinter import *
# from turtle import update
# from tkinter import *
# import winsound
# from playsound import playsound
# from PIL import ImageTk,Image
# class Ball:
#     def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,texture):
#         self.canvas = canvas
#         self.xVelocity = xVelocity
#         self.yVelocity = yVelocity
        
#         self.image = canvas.create_oval(x,y,diameter,diameter,fill=texture,outline="")

    
#     collisionSound='collisionSound.mp3'

#     hasCollided=False
#     hasDied=False    
#     def moveBall(self):
#         coordinates=self.canvas.coords(self.image)
#         print(coordinates)

#         if(coordinates[0]<0 or coordinates[2]>=(self.canvas.winfo_width())):
#             Ball.hasCollided=True
#             if self.xVelocity>0:
#                 self.xVelocity+=1
#                 self.xVelocity=-self.xVelocity
#             else:
#                 self.xVelocity-=1
#                 self.xVelocity=-self.xVelocity
            
        
#         if (coordinates[1]<ysize) or (coordinates[3]>=(self.canvas.winfo_height())):
#             Ball.hasCollided=True
#             if self.yVelocity>0:
#                 self.yVelocity+=1
#                 self.yVelocity=-self.yVelocity
#                 winsound.PlaySound("D:\\msys2\\usr\\share\\mintty\\sounds\\BOING.WAV", winsound.SND_ASYNC | winsound.SND_ALIAS )
#             else:
#                 self.yVelocity-=1
#                 self.yVelocity=-self.yVelocity
            
#         # elif coordinates[2]>=(self.canvas.winfo_width()):
#         #     Ball.hasDied=True
#         #     print("HASDIED!",coordinates)
#         self.canvas.move(self.image,self.xVelocity,self.yVelocity)

#     def restart():
#         if Ball.hasDied==True:
#             Ball.hasDied=False
#             Ball.moveBall()






# window=Tk()
# canvas=Canvas(window,width=1920,height=1080)
# canvas.pack()
# ball=Ball(canvas,1,1,25,1,1,"blue")
# xsize=25
# ysize=xsize

# rect=canvas.create_rectangle(0,0,xsize,ysize**2,fill="white",outline="",tags="bounce")
# rect2=canvas.create_rectangle(0,0,xsize*10,ysize,fill="white",outline="",tags="bounce")
# rect3=canvas.create_rectangle(xsize*10,0,xsize*10+xsize,ysize**2,fill="white",outline="",tags="bounce")
# rect4=canvas.create_rectangle(xsize,ysize**2-ysize,xsize*10,ysize**2,fill="white",outline="",tags="bounce")
# while True:
#     Ball.moveBall(ball)
#     window.update()
#     sleep(0.01)
# window.mainloop()