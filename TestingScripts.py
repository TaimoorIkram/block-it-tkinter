scores=[["Aslam","Ali","Sara"],[4,12,5]]
print(scores.sort(key=int))

# from time import sleep
# import pyttsx3
# friend=pyttsx3.init()
# friend.say("Hello and welcome to the game!")
# sleep(1)
# friend.say("Before we begin the game, it is important to start with the basics.")
# sleep(1)
# friend.say("Press the W key to move forward. Release to stop the character.")
# sleep(1)
# friend.say("Press the S key to move backward, A key to move left and D to move right.")
# sleep(3)
# friend.say("Alright then, you're good to go.")

# friend.runAndWait()

def validateInt(intValue):
   """
   Check whether entered data type is an integer or not.
   Takes a string and returns a bool.
   """
   try:
      intValue = int(intValue)
      return True
   except:
      return False

def convertToInt(intValue):
   """
   Takes a value and returns a list with 0th term being the truth value and the 1th being the number itself.
   """
   try:
      intValue = int(intValue)
      return intValue
   except:
      return intValue










# import tkinter as Tkinter
# import queue as Queue

# class Flash(Tkinter.Toplevel):
#     def __init__(self, root, **options):
#         Tkinter.Toplevel.__init__(self, root, width=100, height=20, **options)

#         self.overrideredirect(True) # remove header from toplevel
#         self.root = root

#         self.attributes("-alpha", 0.0) # set transparency to 100%

#         self.queue = Queue.Queue()
#         self.update_me()

#     def write(self, message):
#         self.queue.put(message) # insert message into the queue

#     def update_me(self):
#         #This makes our tkinter widget threadsafe
#         # http://effbot.org/zone/tkinter-threads.htm
#         try:
#             while 1:
#                 message = self.queue.get_nowait() # get message from the queue

#                 # if a message is received code will execute from here otherwise exception
#                 # http://stackoverflow.com/questions/11156766/placing-child-window-relative-to-parent-in-tkinter-pythons
#                 x = root.winfo_rootx() # set x coordinate of root
#                 y = root.winfo_rooty() # set y coordinate of root
#                 width = root.winfo_width() # get the width of root
#                 self.geometry("+%d+%d" % (x+width-self.winfo_width() ,y)) # place in the top right cornder of root

#                 self.fade_in() # fade in when a message is received
#                 label_flash = Tkinter.Label(self, text=message, bg='black', fg='white', padx=5, pady=5)
#                 label_flash.pack(anchor='e')
#                 self.lift(self.root)

#                 def callback():
#                     label_flash.after(2000, label_flash.destroy) # destroy the label after 5 seconds
#                     self.fade_away() # fade away after 3 seconds
#                 label_flash.after(3000, callback)

#         except Queue.Empty:
#             pass
#         self.after(100, self.update_me) # check queue every 100th of a second

#     # http://stackoverflow.com/questions/3399882/having-trouble-with-tkinter-transparency
#     def fade_in(self):
#         alpha = self.attributes("-alpha")
#         alpha = min(alpha + .01, 1.0)
#         self.attributes("-alpha", alpha)
#         if alpha < 1.0:
#             self.after(10, self.fade_in)

#     # http://stackoverflow.com/questions/22491488/how-to-create-a-fade-out-effect-in-tkinter-my-code-crashes
#     def fade_away(self):
#         alpha = self.attributes("-alpha")
#         if alpha > 0:
#             alpha -= .1
#             self.attributes("-alpha", alpha)
#             self.after(10, self.fade_away)

# if __name__ == '__main__':
#     root = Tkinter.Tk()
#     root.minsize(700, 300)
#     root.geometry("700x500")

#     flash = Flash(root) # create toplevel instance

#     def callback():
#         # put a delay between each message so we can check the behaviour depending on the lenght of the delay between messages
#         import time
#         flash.write('Hello World')
#         time.sleep(1)
#         flash.write('Ready!')
#         time.sleep(2)
#         flash.write('Steady!')
#         time.sleep(4)
#         flash.write('Go!')

#     # create a thread to prevent the delays from blocking our GUI
#     import threading
#     t = threading.Thread(target=callback)
#     t.daemon = True
#     t.start()
#     root.mainloop()
#     exit()