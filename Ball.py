import winsound
class Ball:
    def __init__(self,canvas,x,y,diameter,xVelocity,yVelocity,texture,bgcolor,window=None,resolution="1920x1080",limitspd=10):
        self.window = window
        self.canvas = canvas
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.isHacked=False
        self.limitspeed=limitspd
        if resolution=='1920x1080':
            pass
        elif resolution=='1080x720':
            diameter=10
        
        self.image = canvas.create_oval(x,y,x+diameter,y+diameter,fill=texture,outline="Black",width=2)
        self.image2 = canvas.create_oval(x+x//2,y+y//2,x+x//2+(diameter-x),y+y//2+(diameter-y),fill="black")
        self.image3 = canvas.create_oval(x+x+x//8,y+y+y//8,(diameter-x//8),(diameter-y//8),fill=bgcolor)
    collisionSound='collisionSound.mp3'
    
    hasCollided=False
    hasDied=False    
    def moveBall(self):
        if self.isHacked==False:
            coordinates=self.canvas.coords(self.image)
            # print(coordinates)

            if(coordinates[0]<0 or coordinates[2]>=(self.canvas.winfo_width())):
                self.hasCollided=True
                if self.xVelocity>0:
                    if self.xVelocity<15:
                        self.xVelocity+=1
                    self.xVelocity=-self.xVelocity
                    
                else:
                    if self.xVelocity>-15:
                        self.xVelocity-=1
                    self.xVelocity=-self.xVelocity
                winsound.PlaySound("collisionSound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            
            if (coordinates[1]<0) or (coordinates[3]>=(self.canvas.winfo_height())):
                self.hasCollided=True
                if self.yVelocity>0:
                    if self.yVelocity<(self.limitspeed):
                        self.yVelocity+=0.5
                    self.yVelocity=-self.yVelocity
                else:
                    if self.yVelocity>-(self.limitspeed):
                        self.yVelocity-=0.5
                    self.yVelocity=-self.yVelocity
                winsound.PlaySound("collisionSound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            elif coordinates[3]>=(self.canvas.winfo_height()-5):
                self.hasDied=True
            self.canvas.move(self.image,self.xVelocity,self.yVelocity)
            self.canvas.move(self.image2,self.xVelocity,self.yVelocity)
            self.canvas.move(self.image3,self.xVelocity,self.yVelocity)
        
        elif self.isHacked==True:
            coordinates=self.canvas.coords(self.image)
            # print(coordinates)

            if(coordinates[0]<0 or coordinates[2]>=(self.canvas.winfo_width())):
                self.hasCollided=True
                if self.xVelocity>0:
                    if self.xVelocity<3:
                        self.xVelocity+=0.05
                    self.xVelocity=-self.xVelocity
                    
                else:
                    if self.xVelocity>-3:
                        self.xVelocity-=0.05
                    self.xVelocity=-self.xVelocity
                winsound.PlaySound("collisionSound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            
            if (coordinates[1]<0) or (coordinates[3]>=(self.window.winfo_height())):
                self.hasCollided=True
                if self.yVelocity>0:
                    if self.yVelocity<3:
                        self.yVelocity+=0.05
                    self.yVelocity=-self.yVelocity
                else:
                    if self.yVelocity>-3:
                        self.yVelocity-=0.05
                    self.yVelocity=-self.yVelocity
                winsound.PlaySound("collisionSound.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            elif coordinates[3]>=(self.canvas.winfo_height()-5):
                self.hasDied=True
            self.canvas.move(self.image,self.xVelocity,self.yVelocity)
            self.canvas.move(self.image2,self.xVelocity,self.yVelocity)
            self.canvas.move(self.image3,self.xVelocity,self.yVelocity)

    def restart():
        if Ball.hasDied==True:
            Ball.hasDied=False
            Ball.moveBall()

    