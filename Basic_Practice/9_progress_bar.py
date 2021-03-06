from tkinter import *
import time
import tkinter.ttk as ttk
from click import progressbar # 콤보박스 사용을 위해 

from numpy import var
from sklearn.model_selection import validation_curve

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

# indeterminate (언제 끝날지 모름)
# progressbar = ttk.Progressbar(root,maximum=100, mode = "indeterminate")
# progressbar = ttk.Progressbar(root,maximum=100, mode = "determinate")
# progressbar.start(10) # 10ms 마다 움직임 
# progressbar.pack()


# def btncmd() :
#     progressbar.stop() # 작동 중지 # 사라져버림 

# btn = Button(root, text = "중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar() # double (실수를 반영하기위해)
progressbar2 = ttk.Progressbar(root,maximum=100, length=150,variable=p_var2)
progressbar2.pack()

def btncmd2() :
    for i in range(1, 101) : # 1부터 100 
        time.sleep(0.01) # 0.01초 대기 


        p_var2.set(i) # progress bar의 값 설정 
        progressbar2.update() # for문 동작할 때마다 GUI가 동작 
        print(p_var2.get())


btn = Button(root, text = "시작", command = btncmd2)
btn.pack()


root.mainloop()