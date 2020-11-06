from selenium import webdriver
import time,math, os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # label = WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID,"price"), "100"))
    # button = browser.find_element_by_id("book")
    # button.click()



    x = browser.find_element_by_id("input_value").text
    zn = math.log(abs(12 * math.sin(int(x))))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(zn))

    button = browser.find_element_by_id("solve")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
