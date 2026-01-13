# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
site_saby = "https://fix-online.saby.ru/"

try:
    browser.get(site_saby)
    browser.maximize_window()

    user_login, user_password = 'Strutandol', 'пароль123'

    login = browser.find_element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled')
    login.send_keys(user_login)

    enter = browser.find_element(By.CSS_SELECTOR, '.controls-BaseButton__wrapper')
    enter.click()

    password = browser.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled')
    password.send_keys(user_password)

    enter = browser.find_element(By.CSS_SELECTOR, '.controls-BaseButton__wrapper')
    enter.click()

    time.sleep(5)

finally:
    browser.quit()