from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

import time
import pyautogui

driver = webdriver.Chrome(executable_path="/home/pi/Desktop/chromedriver") # write your path to chromedriver
print("browser open")
elm = driver.find_element_by_tag_name('body').send_keys(Keys.F11)

driver.get("https://trello.com/login?returnUrl=%2F")
driver.implicitly_wait(3)

driver.find_element_by_name('user').send_keys('someone@somewhere.com') # write your team ID here
driver.find_element_by_name('password').send_keys('password') # write your team password here

driver.find_element_by_xpath('//*[@id="login-form"]/div/input').click()



title = WebDriverWait(driver, 20) \
        .until(EC.presence_of_element_located((By.XPATH, '//nav[@class="home-left-sidebar-container"]')))
driver.get("https://trello.com/b/fhjxomhu/your-board-url") # write your board page url here


def loop_memo() :
    waiting_time = 2
    max_loop_time = 2 # how many times to loop from one edge to the other edge before show calendar
    list_num_in_screen = 7 # the number of list on the board when it is fullscreen 
    direction = 1
    loop_check = 0
    loop_time = 0
    scroll_width = driver.execute_script("return document.body.scrollWidth")

    stop_time = 0

    elm = driver.find_element_by_tag_name('body')

    while loop_time < max_loop_time:

        bef_width = driver.execute_script("return window.pageXOffset;")

        if (direction == 1):
            elm.send_keys(Keys.ARROW_RIGHT)
        else:
            elm.send_keys(Keys.ARROW_LEFT)

        print("scroll!")

        time.sleep(waiting_time)

        cur_width = driver.execute_script("return window.pageXOffset;")

        if bef_width == cur_width:
            stop_time += 1
        else:
            stop_time = 0

        if (cur_width == scroll_width or stop_time >= list_num_in_screen) :
            print("direction change")
            direction *= -1
            loop_check += 1
            stop_time = 0

        if (loop_check == 2) :
            loop_check = 0
            loop_time += 1

while True :
    cal_wait_time = 20

    #driver.switch_to.window(driver.window_handles[0])
    print("tab switch")

    loop_memo()

    print("memo loop completed")

    pyautogui.click(1622, 74) # you might have to change this coordinate for calendar button

    time.sleep(cal_wait_time)

    pyautogui.click(1622, 74)
