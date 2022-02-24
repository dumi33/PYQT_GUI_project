from tkinter import *

from click import CommandCollection

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

label1 = Label(root, text= "안녕하세요")
label1.pack()

photo = PhotoImage(file = "gui_basic/img.png")
label2 = Label(root,image = photo)
label2.pack()

def Change() :
    label1. config(text = "또 만나요") # 레이블 변경 
    global photo2 # 전역변수로 실행해야 함수가 끝나도 사라지지않음
    photo2 = PhotoImage(file = "gui_basic/img2.png")
    label2.config(image=photo2)

btn = Button(root,text = "클릭",command=Change)
btn.pack()

root.mainloop()