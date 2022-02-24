from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root,text = "버튼1")
btn1.pack()  # 프로그램에 포함

btn2 = Button(root,padx = 5, pady = 10 ,text = "버튼2") # 공간을 확보 (여백) 
btn2.pack() # 프로그램에 포함

btn3 = Button(root,padx = 10, pady = 5 ,text = "버튼3")
btn3.pack() # 프로그램에 포함

btn4 = Button(root,width = 10,height = 3 ,text = "버튼4") # 고정 크기 
btn4.pack() # 프로그램에 포함

btn5 = Button(root, fg = "red", bg = "yellow", text = "버튼5") #   노랑색 배경에 빨간색 글자 
btn5.pack() # 프로그램에 포함

photo = PhotoImage(file = "gui_basic/img.png")
btn6 = Button(root,image = photo)
btn6.pack() # 프로그램에 포함

def btncmd() :
    print("버튼이 클릭되었습니다.")
    
btn7 = Button(root,text = "동작하는 버튼", command = btncmd)
btn7.pack() # 프로그램에 포함


root.mainloop()