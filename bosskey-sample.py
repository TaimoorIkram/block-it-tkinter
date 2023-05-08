scrtest=[["JUMMY","JACK","PEPE","DUCK","LOLXD"],[57,48,99,35,102]]
    
thisdict ={}
for index, names in enumerate(scrtest[0]):
    thisdict[names] = scrtest[1][index]
arrangeddict = {}
for i in range(len(thisdict)):
    max_num = max(i for i in thisdict.values())
    
    max_word = list(thisdict.keys())[list(thisdict.values()).index(max_num)]
    arrangeddict[max_word] = max_num

    del thisdict[max_word]
final_list =[[],[]]
for names, marks in arrangeddict.items():
    final_list[0].append(names)
    final_list[1].append(marks)

print(final_list)

# list1 = [['xd','xd1','xd2','xd3'],[23,54,23,76]]

# thisdict ={}
# for index, names in enumerate(list1[0]):
#     thisdict[names] = list1[1][index]
# arrangeddict = {}
# for i in range(len(thisdict)):
#     max_num = max(i for i in thisdict.values())
#     value_list =list(thisdict.values())
#     item_list =list(thisdict.keys())

#     item_list[value_list.index(max_num)]

#     max_word = list(thisdict.keys())[list(thisdict.values()).index(max_num)]
#     arrangeddict[max_word] = max_num

#     del thisdict[max_word]

# from tkinter import *      
# window = Tk()
# canvas = Canvas(window, width = 2000, height = 800)      
# canvas.pack()

# bk=False
# img = PhotoImage(file="work_image.png")
# def bauss(event):
#     global bk
#     if bk==False:
#         bk=True
#         image=canvas.create_image(700,400, image=img)
#     elif bk==True:
#         bk=False
#         canvas.delete("all")
#         window.destroy()

# window.bind("<b>", bauss)




# mainloop()   
