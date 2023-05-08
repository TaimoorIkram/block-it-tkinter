from tkinter import Button, Canvas, Label,PhotoImage

from Ball import Ball
class MainMenuButton():
    def __init__(self,canvas,row,column,buttontext:str,icon:str,command,resolution='1280x720',sound="collisionSound.mp3") -> None:
        if resolution=='1280x720':
            icon=PhotoImage(file=icon).subsample(4,4)
            font=("Bahnschrift",12)
            ypadding=1
        elif resolution=='1920x1080':
            icon=PhotoImage(file=icon).subsample(3,3)
            font=("Bahnschrift",18)
            ypadding=5   

        self.canvas=canvas
        self.row=row
        self.column=column
        self.icon=icon

        self.button=Button(self.canvas,text=buttontext+"  ",font=("Bahnschrift",12,"bold"),fg='black',image=self.icon,compound='left',command=command,background='white',border=0).grid(row=self.row,column=self.column,sticky='w',padx=10,pady=ypadding)
class MainMenuTitle():
    def __init__(self,canvas,row=0,column=0,resolution='1280x720') -> None:
        
        self.canvas=canvas
        self.row=row
        self.column=column

        if resolution=='1280x720':
            self.button=Label(self.canvas,text="BLOCK IT!",bg="red",fg="white",width=20,font=("Bahnschrift Condensed",25),border=0).grid(row=self.row,column=self.column,sticky='n',padx=10,pady=10)
        if resolution=='1920x1080':
            self.button=Label(self.canvas,text="BLOCK IT!",bg="red",fg="white",width=20,font=("Bahnschrift Condensed",30),border=0).grid(row=self.row,column=self.column,sticky='n',padx=10,pady=10)

class Credit():
    def __init__(self,canvas,buttontype:str,) -> None:
        pass

    def header():
        pass
    def detail():
        pass

class ButtonResponsePopup():
    def __init__(self,window,headertext:str,detailtext:str,popupwidth=250,resolution='1280x720') -> None:
        self.window=window
        self.popupwidth=popupwidth
        self.resolution=resolution
        if self.resolution=="1920x1080":
            self.popupwidth=500
            ypadding=10
            fontheader=("Bahnschrift",24,"bold")
            fontdetail=("Bahnschrift",12)
        elif self.resolution=="1280x720":
            self.popupwidth=250
            ypadding=1
            fontheader=("Bahnschrift",12,"bold")
            fontdetail=("Bahnschrift",8)
        credcanv=Canvas(window,width=self.popupwidth,height=500,bg='black',border=0,borderwidth=0,highlightthickness=4,highlightbackground='yellow')
        headlab=Label(credcanv,text=headertext,font=fontheader,bg='yellow',fg='black')
        headlab.grid(row=0,column=0,sticky='w',padx=10,pady=10)
        detaillab=Label(credcanv,text=detailtext,font=fontdetail,bg='black',fg='white',justify='left')
        detaillab.grid(row=1,column=0,sticky='w',padx=10,pady=ypadding)
        credcanv.pack(pady=100)
        self.window.update()
        def understood():
            global isShowinghowto
            credcanv.destroy()
            isShowinghowto=False
        gotitbtn=Button(credcanv,text="UNDERSTOOD!",font=("Bahnschrift",8),fg='black',bg='yellow',border=0,command=understood)
        gotitbtn.grid(row=2,column=0,sticky='sw',padx=10,pady=10)
        pass