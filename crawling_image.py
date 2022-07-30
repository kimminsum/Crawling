from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import urllib.request
import tkinter as tk
import time
import os
"""
Get Text
"""
window = tk.Tk()
window.title("Download Image")
window.geometry("200x150+1500+100")

def getTextInput():
    global Research_text
    Research_text=textExample.get("1.0","end")
    window.quit()

textExample=tk.Text(window, height=5)
textExample.pack()
btnRead=tk.Button(window, height=1, width=15, text="Download Image", 
                    command=getTextInput)

btnRead.pack()
window.mainloop()
"""
Research Image
"""
driver = webdriver.Chrome("chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
driver.get("https://www.google.com/imghp?hl=ko&tab=8i")
### insert image name
RESEARCH_BOX = driver.find_element(By.CLASS_NAME, "gLFyf.gsfi")
RESEARCH_BOX.send_keys(Research_text)
"""
Get every Image
"""
SCROLL_PAUSE_SEC = 1

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, "input.mye4qd").click()
        except:
            break
    last_height = new_height
"""
Download Image
"""
images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")
index = 0
file_name = ""
for image in images:
    try:
        driver.implicitly_wait(2)
        image.click()
        image_link = str(driver.find_element(By.CSS_SELECTOR, "img.n3VNCb.KAlRDb").get_attribute("src"))
        if ".jpg" in image_link:
            file_name = f"img/{index}.jpg"
        elif ".jpeg" in image_link:
            file_name = f"img/{index}.jpeg"
        elif ".png" in image_link:
            file_name = f"img/{index}.png"
        else:
            print("!!!Out of style!!!")
            continue
        urllib.request.urlretrieve(str(image_link), str(file_name))
        index += 1
    except:
        print("!!!Image is blocked!!!")
os.system("cls")
driver.close()