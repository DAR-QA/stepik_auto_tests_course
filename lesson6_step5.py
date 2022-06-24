from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    
    
    link = browser.find_element(By.LINK_TEXT, "224592")
    link.click()
    

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    time.sleep(0.5)
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    time.sleep(0.5)
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
