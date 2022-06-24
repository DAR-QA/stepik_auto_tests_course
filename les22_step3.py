from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    #переход по ссылке
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    
    number1 = browser.find_element(By.ID, "num1")
    number1_Num = int(number1.text)
    number2 = browser.find_element(By.ID, "num2")
    number2_Num = int(number2.text)
    
    y = (number1_Num + number2_Num)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(value = str(y))
    time.sleep(1)
    
    # жмем кнопку
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()