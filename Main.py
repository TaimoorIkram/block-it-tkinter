from ast import Try
from random import choice,randint
from mainMenu import *
from threading import Thread
from time import sleep
from tkinter import N, NE, messagebox
import winsound
from Ball import *
from tkinter import PhotoImage,Tk,Button,Label,Canvas,LEFT,RIGHT,TOP,BOTTOM,NW,Entry,Radiobutton,StringVar
# scores=[["ALBERTO","IMAHACKER666","DRAGUNOV","LIBRA","ZION","NOOB","WHYAMIHERE091","NTTV"],[13,45,63,12,1,23,47,999]]
scores=[[],[]]
scoresfinal=[[],[]]

speedx=1
speedy=1
master = Tk()
master.geometry("275x100")
 
# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")

# Dictionary to create multiple buttons
values = {"720p" : "1",
          "1080p" : "2"}
def checkvalue(btn):
    global launcherresolution
    if v.get()=='2':
        launcherresolution='1920x1080'
    else:
        launcherresolution='1280x720'
    master.destroy()

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
label=Label(master,text="Select a Resolution",font=("Bahnscrift",20,"bold")).pack()
b1=Radiobutton(master, text = "720p", variable = v,value = '1', indicator = True,font=("Bahnscrift",12,"bold"),fg='white',background = "black",command=lambda:checkvalue(b1),activebackground='black',activeforeground='white').pack(fill = 'both', ipady = 5)
b2=Radiobutton(master, text = "1080p", variable = v,value = '2', indicator = True,font=("Bahnscrift",12,"bold"),fg='white',background = "black",command=lambda:checkvalue(b1),activebackground='black',activeforeground='white').pack(fill = 'both', ipady = 5)


master.mainloop()

#A thread to play sound on mouse click.
def onRightMouseButtonClick():
    userwallsound="userWallCollisionSound.wav"
    winsound.PlaySound(userwallsound, winsound.SND_ASYNC | winsound.SND_ALIAS)

hadcheated=False

isblocked=False
def ClickSound(event):
    """
    Blocks the ball.
    """
    global canvas,isblocked,ball,rectangle,automate
    isblocked=True
    click=Thread(target=onRightMouseButtonClick)
    def killblock():
        canvas.delete("rect")
        pass
        isblocked=False
    xoff=0
    if launcherresolution=='1280x720':
        rectangle=canvas.create_rectangle(xoff,gamewindow.winfo_height()-90,canvas.winfo_width()-xoff,gamewindow.winfo_height()-50,fill="white",outline='',tags="rect")
    elif launcherresolution=='1920x1080':
        rectangle=canvas.create_rectangle(xoff,gamewindow.winfo_height()-50,canvas.winfo_width()-xoff,gamewindow.winfo_height()-10,fill="white",outline='',tags="rect")
    click.start()
    canvas.after(1,checkcoll)
    canvas.after(100,killblock)
    isblocked=False
 



hascollided=False
def checkcoll():
    """Checks collision."""
    global counter,boxCollider,ballCollider
    boxCollider=canvas.bbox(rectangle)
    ballCollider=canvas.bbox(ball.image)
    if ball.isHacked==False:
        if ballCollider[3]>boxCollider[1] and ball.hasCollided==False:
            counter+=1
            if ball.yVelocity>0:
                if ball.yVelocity<5:
                    ball.yVelocity+=0.5
                ball.yVelocity=-ball.yVelocity
            else:
                if ball.yVelocity>-5:
                    ball.yVelocity-=0.5
                ball.yVelocity=-ball.yVelocity
            ball.hasCollided=True
    elif ball.isHacked==True:
        if ballCollider[3]>boxCollider[1] and ball.hasCollided==False:
            counter+=2
            ball.hasCollided=True
            if ball.yVelocity>0:
                if ball.yVelocity<5:
                    ball.yVelocity+=0.5
                ball.yVelocity=-ball.yVelocity
            else:
                if ball.yVelocity>-5:
                    ball.yVelocity-=0.5
                ball.yVelocity=-ball.yVelocity
    else:
        return

def theStart():
    startSound='startSound.wav'
    winsound.PlaySound(startSound,winsound.SND_ASYNC | winsound.SND_ALIAS)

def SplashScreen():
    hasClickedtoStart=False
    global window

    #Creates the main menu window.
    window=Tk()
    global launcherresolution
    window.title("Block It Launcher")
    window.geometry("540x540")
    window.iconbitmap('gameIcon60x60.ico')
    window.configure(bg="black")
    
    window.state("zoomed")
    
    #Creates a canvas for the buttons and game title.
    initialscreen=Canvas(window,bg="black",borderwidth=0,highlightthickness=4,highlightbackground='red')
    

    # Creates an image to show as BG in the main menu.
    bgimage=PhotoImage(file='launcherBG_notitle.png').subsample(1,1)
    initialscreen.create_image(0,0,image=bgimage,anchor='n')

    #Creates a canvas for the game version, located at the bottom of main menu window.
    gamevercanvas=Canvas(window,width=1920,height=500,bg='green')
    startgamelabel0=Label(gamevercanvas,text="Copyright 2022 NTTV Studios. Block It v0.0.1 Beta",bg="black",fg="white",font=("Bahnschrift",10))
    startgamelabel0.pack(side=BOTTOM)
    gamevercanvas.pack(side=BOTTOM)

    #GAME TITLE
    startgamelabel1=MainMenuTitle(initialscreen,resolution=launcherresolution)
    # startgamelabel1.pack(side=TOP)    

    #BUTTONS
    #PLAY
    playbtn=MainMenuButton(initialscreen,1,0,"PLAY","playIcon.png",runGame,resolution=launcherresolution)

    #LEADERBOARD
    leaderboardbtn=MainMenuButton(initialscreen,2,0,"LEADERBOARD","leaderboardIcon.png",showLeaderBoard,resolution=launcherresolution)

    #HOW TO PLAY
    howtoplaybtn=MainMenuButton(initialscreen,3,0,"HOW TO PLAY","helpIcon.png",howtoplay,resolution=launcherresolution)
    
    #CREDITS
    creditsbtn=MainMenuButton(initialscreen,4,0,"CREDITS","credIcon.png",creditScreen,resolution=launcherresolution)
    
    #EXIT
    exitbtn=MainMenuButton(initialscreen,5,0,"EXIT","quitIcon.png",endGame,resolution=launcherresolution)
    
    #Dev team icon on the top of the window.
    devico=PhotoImage(file="devLogo.png")
    disub=devico.subsample(10,10)
    devlogo=Label(window,image=disub,background='black')
    devlogo.pack(side=TOP)
    initialscreen.pack(side=LEFT,padx=10)

    global sessionstatus,status
    status="There aren't any sessions going on currently. Try playing a game or two!"
    sessionstatus=Label(initialscreen,text=status,font=("Bahnscrift",12),fg="white",bg="black")
    sessionstatus.grid(row=10,column=0,sticky='nw',padx=10,pady=10)
    endsession=MainMenuButton(initialscreen,9,0,"END CURRENT SESSION","end_sessionIcon.png",endSession,resolution=launcherresolution)
    window.mainloop()

noSessions=True
def endSession():
    """
    Ends a running game session.
    """
    global noSessions,sessionstatus,status
    if noSessions==True:
        messagebox.showerror("End Session","No current sessions. Play something and try again.")
    else:
        global inSession
        try:
            gamewindow.destroy()
        except:
            pass
        inSession=False
        noSessions=True
        sessionstatus.config(text=status)

def endGame():
    """
    Ends the game.
    """
    if inSession==True:
        try:   
            gamewindow.destroy()
        except:
            pass
    window.destroy()

inSession=False
def runGame():
    """
    Starts the game.
    """
    global inSession
    if inSession==False:
        inSession=True
        startScreen()
    elif inSession==True:
        messagebox.showerror("Start Game","The game is already in session. Close recent session and try again.")

counter = 0
def counter_label(label,cheat=False):
    """
    Counter incrementer.
    """
    global counter
    def cheatcount():
        global counter 
        counter+=100
        canvas.itemconfig(label,text=str(counter))
    def count():
        global counter
        canvas.itemconfig(label,text=str(counter))
        canvas.after(1,count)
    if cheat==True:
        cheatcount()
    else:
        count()

isPaused=False
def pause():
    """
    Pause menu.
    """
    global gamewindow,isPaused
    def pausemenu():
        if isPaused==True:
            global pmcanvas,quitgame,canvas
            pmcanvas=Canvas(gamewindow,background="black",highlightbackground='red',highlightthickness=4)
            pmheader=Label(pmcanvas,text="GAME PAUSED",font=("Bahnschrift",24),fg="white",bg="red")
            unpausebutton=Button(pmcanvas,command=pause,text="UNPAUSE",font=("Bahnscrift",12),bg="black",fg="white",border=0)
            quitgame=Button(pmcanvas,text="EXIT",font=("Bahnschrift",12),fg='white',command=endSession,background='black',border=0)
            restrtbtn=Button(pmcanvas,text="RESTART",font=("Bahnschrift",12),fg='white',command=restart,background='black',border=0)
            cheatcodesbtn=Button(pmcanvas,command=cheat,text="CHEATS",font=("Bahnscrift",12),bg="black",fg="white",border=0)
            
            quitgame.pack(side=BOTTOM,pady=10,padx=10)
            pmcanvas.grid(row=0,column=0,sticky='ew',padx=50)
            pmheader.pack(side=TOP,padx=10,pady=10)
            unpausebutton.pack(pady=10,padx=10)
            restrtbtn.pack(padx=10,pady=10)
            cheatcodesbtn.pack(padx=10,pady=10)
            pmcanvas.tkraise()
    if isPaused==False:
        isPaused=True
        pausemenu()
    else:
        global buttoncanvas,canvas
        seconds=2
        isPaused=False
        timer=Label(buttoncanvas,text="Starting in "+str(seconds),font=("Bahnscrift",24),bg="black",fg="white")
        timer.pack()
        pmcanvas.destroy()
        for i in range(3,0,-1):
            timer.config(text="Starting in "+str(i))
            timer.update()
            sleep(1)
        canvas.config(bg=backgroundcol)
        timer.destroy()
        pausegame.config(text="■")


def startScreen():
    """
    The main menu constructor.
    """
    global isPaused
    global inSession,noSessions,counter,backgroundcol,canvas,score,gamewindow,buttoncanvas
    backgroundcol=choice(["OrangeRed","DeepPink","Gold"])
    counter=0
    inSession=True
    noSessions=False
    thread1=Thread(target=theStart)
    thread1.start()
    gamewindow=Tk()
    gamewindow.title("Block It!")
    gamewindow.iconbitmap('gameIcon60x60.ico')
    gamewindow.configure(bg="black")
    if launcherresolution=='1280x720':
        gamewindow.state('normal')
    else:
        gamewindow.state('zoomed')
    isPaused=False
    
    respara=launcherresolution.split('x')
    global width,height
    width=int(respara[0])
    height=int(respara[1])
    
    # buttoncanvas.grid(row=0,column=1,sticky='w')

    canvas=Canvas(gamewindow,width=540,height=height+20,bg=backgroundcol)
    buttoncanvas=Canvas(canvas,width=540,height=540,bg='white')
    buttoncanvas.place(anchor=NW)
    if launcherresolution=='1280x720':
        guide=canvas.create_rectangle(0,height-60,550,height-40,fill="black",outline='')
    elif launcherresolution=='1920x1080':
        guide=canvas.create_rectangle(0,height-330,550,height-310,fill="black",outline='')

    global label,scorecard
    scorecard=canvas.create_text(250,500,fill='white',text="USER_SCORE",font="Bahnschrift 50",anchor=NW)
    
    canvas.grid(row=0,column=0,sticky="news")
    gamewindow.update()
    if launcherresolution=='1280x720':
        window_width = gamewindow.winfo_width()
        window_height = gamewindow.winfo_height()
        screen_width = gamewindow.winfo_screenwidth()
        screen_height = gamewindow.winfo_height()
        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2))
        gamewindow.geometry(f"{window_width}x{window_height}+{x}+{y}")
    # canvas.grid(row=0,column=0,sticky='n')
    global pausegame
    pausegame=Button(buttoncanvas,text="■",font=("Arial Black",24),fg='white',command=pause,background='black',border=0)
    pausegame.pack(side=TOP)
    counter_label(scorecard)
    createBall(launcherresolution)

bosskey=False
bosskeyscr=None
def bossKey(event):
    """
    Bosskey.
    """
    global bosskey,gamewindow,window,bosskeyscr,istakingname
    if bosskey==False and istakingname==False:
        bosskeyscr=Tk()
        bosskeyscr.state('zoomed')
        bosskeyscr.configure(bg='blue')
        canvas=Canvas(bosskeyscr,width=1920,height=1080,bg='#0723DB')
        winsound.PlaySound("bosskeySound.wav",winsound.SND_ASYNC | winsound.SND_ALIAS)
        canvas.create_text(250,150,text=":(",fill='white',font=("Bahnschrift",150),anchor='nw')
        canvas.create_text(250,450,text="Your PC ran into a problem that it couldn't handle,\nand now it needs to restart.",font=("Bahnschrift",20),fill='white',anchor='nw')
        canvas.create_text(250,550,text="You can try looking up the error for more info at microsoft.com/windows\nCRITICAL_PROCESS_DIED",font=("Bahnschrift",11),fill='white',anchor='nw')
        canvas.pack()
        # bosskeyscr.withdraw()
        pause()
        bosskey=True
        # bosskeyscr.deiconify()

    elif bosskey==True:
        bosskeyscr.destroy()
        pause()
        bosskey=False

hasStarted=False
def touchtostart():
    """
    Assigns start state after the game starts.
    """
    global gamewindow,hasStarted,scorecard,canvas
    if hasStarted==False:
        hasStarted=True
    else:
        canvas.itemconfig(scorecard,text="TOUCH")
        canvas.update()

def gethigh():
    """
    Gets the all-time highscore."""
    highscore=open("highscore.txt","rt")
    highest=highscore.read()
    highscore.close()
    print(highest)
    return highest

breaktime=0
def createBall(res):
    """
    The heart of the game. Creates, moves and check for death of the ball.
    """
    global gamewindow,canvas,ball,hasStarted,breaktime

    def hotkeypause(event):
        pause()

    ballTexture='White'
    ball=Ball(canvas,15,15,50,choice([0.5,-0.5]),5,ballTexture,backgroundcol,window=gamewindow,resolution=res,limitspd=20)
    gamewindow.bind("b",bossKey)
    gamewindow.bind("p",hotkeypause)

    def savescore():
        if name.get()=="":
            messagebox.showinfo("Save Score","Name cannot be empty.")
            return
        global istakingname
        scores[0].append(name.get())
        scores[1].append(counter)
        savebtn.config(text="Saved!",state='disabled')
        name.config(state='disabled')
        istakingname=False
    #LOSE
    lose=Canvas(gamewindow,highlightbackground="red",highlightthickness=4,bg='black')
    losetext=Label(lose,font=("Bahnschrift",36),text="OOPS, MISSED IT!",fg='white',bg='red')
    losetext.grid(row=0,column=0,pady=10,padx=10)
    losetext=Label(lose,font=("Bahnschrift",24),text="ENTER YOUR NAME",fg='white',bg='black')
    losetext.grid(row=1,column=0,pady=10,padx=10)
    _name=""
    name=Entry(lose,textvariable=_name,font=("Bahnschrift",32))
    savebtn=Button(gamewindow,border=0,bg="black",fg="white",text="SAVE",font=("Bahnschrift",32),command=savescore)
    global istakingname
    istakingname=False

    while True:
        global automate
        
        global pausegame
        if isblocked==False and ball.hasDied==False:
            canvas.bind("<Button-1>",ClickSound)
        else:
            pass
        global breaktime
        ballcoords=canvas.bbox(ball.image)
        breaktime+=1
        height_check_for_automate=(height-20) if launcherresolution=='1280x720' else height-300
        if automate==True and ballcoords[3]>=height_check_for_automate:
            ClickSound(None)
            
        gamewindow.update()

        if isPaused==True:
            pausegame.config(text="▶")
            canvas.config(bg='black')
            continue
        
        if hasStarted==True:
            ball.moveBall()
        elif hasStarted==False:
            touchtostart()
        global sessionstatus    
        status="A game is currently running. Go block it!"
        sessionstatus.config(text=status)



        if ball.hasCollided==True and isblocked==False:
            ball.hasCollided=False
        
        if ball.hasDied==True:
            global scores
            
            lose.grid(row=0,column=0,sticky='n',pady=50)
            
            name.grid(row=2,column=0,sticky='n',pady=50,padx=10)
            savebtn.grid(row=0,column=0,sticky="s",pady=300)
            istakingname=True
            # label.grid(row=0,column=0,sticky="news")
            winsound.PlaySound("endSound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
            return
        sleep(float(1/100))

isshowingLB=False
def showLeaderBoard():
    """
    Shoes the leaderboard.
    """
    global isshowingLB,isShowinghowto,isShowingCred
    if isShowingCred==True or isShowinghowto==True or isshowingLB==True:
        messagebox.showerror("Credits","Such window is already open!")
        return
    else:
        pass
    b=gethigh()
    isshowingLB=True
    credcanv=Canvas(window,width=500,height=500,bg='black',border=0,borderwidth=0,highlightthickness=3,highlightbackground='yellow')
    LBcanv=Canvas(credcanv,width=50,height=50,bg='black',highlightthickness=0)

    # player names and their marks will be stored in this list
    scrtest=[["JUMMY","JACK","PEPE","DUCK","LOLXD"],[57,48,99,35,102]]

    
    global scoresfinal
    
    thisdict ={}
    for index, names in enumerate(scores[0]):
        thisdict[names] = scores[1][index]
    arrangeddict = {}
    # arranges dictionary in descending order wrt scores.
    for i in range(len(thisdict)):
        max_num = max(i for i in thisdict.values())
        
        max_word = list(thisdict.keys())[list(thisdict.values()).index(max_num)]
        arrangeddict[max_word] = max_num

        del thisdict[max_word]
    
    # the final names and scores will be stored in an empty list named scoresfinal.
    scoresfinal =[[],[]]
    for names, marks in arrangeddict.items():
        scoresfinal[0].append(names)
        scoresfinal[1].append(marks)


    def makeLB(name,score,row):
        """
        Creates Leaderboard.
        """
        playername=Label(LBcanv,text=name,bg='khaki1',fg='black',width=20,font=("Bahnschrift",12,"bold"))
        playername.grid(row=row,column=0,padx=10,pady=5,sticky='e')
        playerscore=Label(LBcanv,text=score,bg='khaki1',fg='black',width=10,font=("Bahnschrift",12,"bold"))
        playerscore.grid(row=row,column=1,padx=10,pady=5,sticky='w')
        if row==0:
            playername.config(bg='gold')
            playerscore.config(bg='gold')
        elif row==1:
            playername.config(bg='silver')
            playerscore.config(bg='silver')
        elif row==2:
            playername.config(bg='brown')
            playerscore.config(bg='brown')
        


    print (len(scoresfinal[1]))
    try:
        if len(scoresfinal[1])!=0:
            if scoresfinal[1][0]>int(b):
                messagebox.showinfo("Block It!",f'Congratulations {scoresfinal[0][0]}, you\'ve reached a current all time high score!')
                highscorenew=open('highscore.txt','w')
                highscorenew.write(str(scoresfinal[1][0]))
                highscorenew.close()
    except:
        pass
    
    headlab=Label(credcanv,text="THE LEADERBOARD",font=("Bahnschrift",24,"bold"),bg='yellow',fg='black')
    headlab.grid(row=0,column=0,sticky='n',pady=10,padx=10)
    hs=open('highscore.txt','r')
    detaillab=Label(credcanv,text="ALL-TIME HIGHSCORE: "+hs.read(),font=("Bahnschrift",12),bg='black',fg='white')
    hs.close()
    detaillab.grid(row=1,column=0,sticky='n',pady=10,padx=10)

    if len(scoresfinal[0])==0:
        detaillab.config(text="Hmm... sure is quiet in here isnt it?")
        skul=PhotoImage(file="skull.png")
        sademo=Label(credcanv,image=skul,bg='black')
        sademo.grid(row=2,column=0,sticky='s',pady=10)
    else:
        for indx,i in enumerate(scoresfinal[0]):
            makeLB(i,scoresfinal[1][indx],indx)

    LBcanv.grid(row=3,column=0,sticky='n',pady=10,padx=10)
    window.update()
    
    def understood():
        global isshowingLB
        credcanv.destroy()
        isshowingLB=False
    
    gotitbtn=Button(credcanv,text="ALRGIHT THEN",font=("Bahnschrift",8),fg='black',bg='yellow',border=0,command=understood)
    gotitbtn.grid(row=4,column=0,sticky='s',padx=10,pady=10)
    credcanv.pack(pady=10)

    window.mainloop()

isShowingCred=False
def creditScreen():
    """
    Displays the devteam, the libraries used.
    """
    global isShowingCred,isShowinghowto,isshowingLB
    if isShowingCred==True or isShowinghowto==True or isshowingLB==True:
        messagebox.showerror("Credits","Such window is already open!")
        return
    else:
        pass
    isShowingCred=True
    credcanv=Canvas(window,width=500,height=500,bg='black',border=0,borderwidth=0,highlightthickness=3,highlightbackground='yellow')
    head=["MADE BY","THE DEV TEAM","LIBRARIES"]
    headlab=Label(credcanv,text="HEADER_HEAD",font=("Bahnschrift",24,"bold"),bg='yellow',fg='black',width=30)
    headlab.grid(row=0,column=0,sticky='n',pady=10,padx=10)
    detail=["NTTV STUDIOS LLC\nNUST ISLAMABAD","TAIMOOR IKRAM\nTAYYIB-UL-HASSAN\nVISHAL SAGAR\nNIDA NAVEED","TKINTER\nRANDOM\nTHREADING\nTIME\nWINSOUND\nPLAYSOUND\nBALL SCRIPT\nMAIN MENU SCRIPT"]
    detaillab=Label(credcanv,text="DETAIL_DET",font=("Bahnschrift",12),bg='black',fg='white')
    detaillab.grid(row=1,column=0,sticky='n',pady=10,padx=10)
    credcanv.pack(pady=100)
    for i in range(len(head)):
        headlab.config(text=head[i])
        detaillab.config(text=detail[i])
        window.update()
        sleep(2)
    headlab.config(text="THANKS FOR PLAYING!")
    detaillab.config(text="(C) 2022 - NTTV")
    window.update()
    sleep(3)
    credcanv.destroy()
    isShowingCred=False

    window.mainloop()
    pass

isShowinghowto=False
def howtoplay():
    """
    Displays instructions about how to play game.
    """
    global isShowinghowto,isShowingCred,isshowingLB
    if isShowingCred==True or isShowinghowto==True or isshowingLB==True:
        messagebox.showerror("How to play","Such window is already open!")
        return
    else:
        pass
    isShowinghowto=True
    credcanv=Canvas(window,width=500,height=500,bg='black',border=0,borderwidth=0,highlightthickness=4,highlightbackground='yellow')
    headlab=Label(credcanv,text="HOW TO PLAY",font=("Bahnschrift",24,"bold"),bg='yellow',fg='black')
    headlab.grid(row=0,column=0,sticky='w',padx=10,pady=10)
    detail="Don't let the ball get away!\nBlock it features a reflex-based gameplay. Block the path of the ball by your vivid mouse clicks.\nIf the ball excapes, you're out. Good luck!\n\nKEYBINDS\nPause\t\tP\nBlock\t\tLEFT-CLICK\nBosskey\t\tB\n"
    detaillab=Label(credcanv,text=detail,font=("Bahnschrift",12),bg='black',fg='white',justify='left')
    detaillab.grid(row=1,column=0,sticky='w',padx=10)
    credcanv.pack(pady=100)
    window.update()
    def understood():
        global isShowinghowto
        credcanv.destroy()
        isShowinghowto=False
    gotitbtn=Button(credcanv,text="UNDERSTOOD!",font=("Bahnschrift",8),fg='black',bg='yellow',border=0,command=understood)
    gotitbtn.grid(row=2,column=0,sticky='sw',padx=10,pady=10)

    window.mainloop()
    pass

automate=False
def cheat():
    """
    Cheatcodes.
    """
    cheatcodes=["m3n4c3".upper(),"Aut0mat3".upper()]
    cheatcanv=Canvas(gamewindow,highlightbackground="red",highlightthickness=4,bg='black')
    
    cheattext=Label(cheatcanv,font=("Bahnschrift",36),text="CHEAT CODES",fg='white',bg='red')
    cheattext.grid(row=0,column=0,pady=10,padx=10)
    
    cheattext=Label(cheatcanv,font=("Bahnschrift",24),text="ENTER CHEAT CODE",fg='white',bg='black')
    cheattext.grid(row=1,column=0,pady=10,padx=10)
    cheatcanv.grid(row=0,column=0,sticky='n',pady=50)
    _cheatcode=""
    cheatcodefinal=Entry(cheatcanv,textvariable=_cheatcode,font=("Bahnschrift",32))
    cheatcodefinal.grid(row=2,column=0,sticky='n',pady=50,padx=10)
    
    def checkcheat():
        """
        Tallies the cheatcodes
        """
        global automate
        if cheatcodefinal.get().upper() not in cheatcodes:
            messagebox.showerror("Cheat Code","Oops, seems like this cheat doesnt exist.")
        elif cheatcodefinal.get().upper()=='M3N4C3':
            messagebox.showinfo("Hack0912sjiowsxklaslA{PSLKOP","HACK_GAME_098767521709-e090is1o-aso0c-i9a=0sda-sdaxxxxxxxxxx")
            pause()
            ball.isHacked=True
            for i in range(100):
                counter_label(scorecard,cheat=True)
        elif cheatcodefinal.get().upper()=='AUT0MAT3':
            if automate==False:
                automate=True
                pause()
            else:
                automate=False
                ball.hasDied=True
                messagebox.showinfo("Automate.bis","Cheat deactivated, but your score will not be saved! Unpause to continue.")
        cheatcanv.destroy()
        savebtn.destroy()
    savebtn=Button(gamewindow,border=0,bg="black",fg="white",text="APPLY",font=("Bahnschrift",32),command=checkcheat)
    if height==720:
        savebtn.grid(row=0,column=0,sticky="s",pady=100)
    elif height==1080:
        savebtn.grid(row=0,column=0,sticky="s",pady=300)

def restart():
    endSession()
    runGame()

def main():
    SplashScreen()

main()
