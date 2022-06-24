from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    #переход по ссылке
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
     # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Dmitriy")
    
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ryabinin")
    
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("blackskillow@gmail.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    
    button = browser.find_element(By.ID, "file")
    button.send_keys(file_path)
    
    # жмем кнопку
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()