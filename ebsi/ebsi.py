from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


a_link = 0
subject = {'국어' : 1, '수학' : 2, '과학' : 6}
sub = input('국어, 수학, 과학 중 선택: ')
how_times = int(input("몇개?: "))
driver = webdriver.Chrome('/home/kar7mp5/바탕화면/Crawling/chromedriver')

driver.get("https://www.ebsi.co.kr/ebs/pot/potl/login.ebs?alertYn=N&destination=")
time.sleep(2)
driver.maximize_window()


### 로그인 
time.sleep(2)
username_input = driver.find_element(By.XPATH, '/html/body/div/section/div/div[1]/div[1]/form/input[11]')
username_input.send_keys("mp5kar7")
time.sleep(1)
password_input = driver.find_element_by_xpath('/html/body/div/section/div/div[1]/div[1]/form/span/input')
password_input.send_keys("ms041005a")
password_input.send_keys(Keys.RETURN)
time.sleep(3)


# 팝업창 
driver.find_element_by_xpath('/html/body/div[2]/section/div[5]/div/div[3]/button/span').click()
time.sleep(2)
# 팝업창 2
driver.find_element_by_xpath('/html/body/div[2]/nav/div/div[1]/div/ul/li[5]/a').click()
time.sleep(2)
# 기출
driver.find_element_by_xpath('/html/body/div[2]/nav/div/div[1]/div/ul/li[5]/a').click()

driver.find_element_by_xpath('/html/body/div[2]/section/div/div[2]/form/div[2]/div[1]/dl/dd[1]/select[1]').click()

driver.find_element_by_xpath('/html/body/div[2]/section/div/div[2]/form/div[2]/div[1]/dl/dd[1]/select[1]/option[9]').click()

driver.find_element_by_xpath('/html/body/div[2]/section/div/div[2]/form/div[2]/div[1]/dl/dd[2]/div/span[1]/input').click()



for i in range(3,10,3):
    time.sleep(0.2)
    driver.find_element_by_id(f'month0{i}').click()



driver.find_element_by_id('subj%d'%subject[sub]).click()
driver.find_element_by_xpath('/html/body/div[2]/section/div/div[2]/form/div[2]/div[2]/button').click()
time.sleep(2)

for i in range(int(round(how_times/15,0)+1)):
    for times in range(0, how_times*3, 3):
        number = int(times/3) - a_link
        if number == 15:
            driver.find_element_by_xpath('/html/body/div[2]/section/div/div[2]/div/div/a[3]').click()
            break
        time.sleep(1)
        file_name = driver.find_elements_by_css_selector('.tit')[number+2].text
        pdflink = driver.find_elements_by_class_name('btn_L_col2.has_down')[times].get_attribute('onclick')
        url = 'https://wdown.ebsi.co.kr/W61001/01exam%s'%str(pdflink.split("'")[1])
        response = urllib.request.urlopen(url)
        file = open(f"Crawling\ebsi\pdf\{file_name}.pdf", 'wb')
        file.write(response.read())
        file.close()
    how_times -= 15
driver.close()