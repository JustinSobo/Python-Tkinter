from tkinter import *

#Was not able to get Pillow (forked from PIL) imported...
from PIL import ImageTk,Image

root = Tk()
root.title('I am learning Tkinter Fundamentals!')
root.iconbitmap('C:/Users/Justin/Downloads/iconfinder_Pacman_Ghost_381615.ico')

my_img = ImageTk.PhotoImage(Image.open("C:/Users/Justin/Downloads/github_profile.jpg"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()
