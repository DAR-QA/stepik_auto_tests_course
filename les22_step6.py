from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #переход по ссылке
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # ищем элемент число. подставляем в формулу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    # в поле ответа вводим результат
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    # ищем и выбираем чекбокс я робот
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    
        # скроллим вниз
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    # ищем и выбираем радио роботы рулят
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    
    # жмем кнопку
    button = browser.find_element_by_tag_name("button")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()