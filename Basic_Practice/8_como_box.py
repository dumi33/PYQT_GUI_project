from tkinter import *
import tkinter.ttk as ttk # 콤보박스 사용을 위해 

from numpy import var
from sklearn.model_selection import validation_curve

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") # 가로 * 세로

values = [str(i) + "일" for i in range(1,32)] # 1~31 까지의 숫자 
combobox = ttk.Combobox(root,height=5, values= values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정


# 목록값 임의로 변경 불가 
readonly_combobox = ttk.Combobox(root,height=10, values= values,state = "readonly")
readonly_combobox.current(0) # 0번째 인덱스 값 선택 
readonly_combobox.pack()


def btncmd() :
    print(combobox.get()) # 햄버거 중 선택된 라디오 항목의 값 출력 
    print(readonly_combobox.get()) 
    pass

btn = Button(root, text = "주문", command=btncmd)
btn.pack()

root.mainloop()