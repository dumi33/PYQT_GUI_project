import keyboard
import time 
from PIL import ImageGrab

def screenshot() :
    # _20220308_011330 
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time)) # ex) image __20220308_011330.png

keyboard.add_hotkey("F9",screenshot) # f9 키를 누르면 스크린 샷 저장 

keyboard.wait("esc") # 사용자가 esc를 누를때까지 프로그램 수행 
