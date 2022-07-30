from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import tkinter as tk
import time
import urllib.request

"""
Get Text
"""
window = tk.Tk()
window.title("Download Image")
window.geometry("200x150")

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
Download Image
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

images = driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")
for image in images:
    image.click()
    print(image.get_attribute("src"))
    urllib.request.urlretrieve(str(image.get_attribute("src")), "NASA.jpg")
    time.sleep(0.5)

driver.close()