import time

from PIL import ImageGrab # python image library

time.sleep(5) # 5초 대기 

for i in range(1,11) : # 2초 간격으로 10 개 이미지 저장 
    img = ImageGrab.grab() # 현재 스크린 이미지를 갖고옴 
    img.save("image{}.png".format(i)) # 파일 저장 
    time.sleep(2) # 2초 단위 
