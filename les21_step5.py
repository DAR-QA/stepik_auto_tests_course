from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    #переход по ссылке
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # ищем переменное число. сохраняем в переменную. считаем по формуле выше 
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
   
    # ищем поле и вводим в него результат
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    time.sleep(2)
   
    # ставим чекбоксы и радио
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    time.sleep(2)
    
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    time.sleep(2)

    # жмем кнопку
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()