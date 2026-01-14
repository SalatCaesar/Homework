# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

browser = webdriver.Chrome()
site_saby = "https://fix-online.saby.ru/"
saby_dialogs = "https://fix-online.saby.ru/page/dialogs"
user_login, user_password = 'Strutandol', 'пароль123'
user_name = 'Струтынский Андрей Олегович'
text_msg = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 15)))

try:
    browser.get(site_saby)
    browser.maximize_window()

    login = browser.find_element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled') # Поле логина
    login.send_keys(user_login, Keys.ENTER) # Вводим логин, жмём энтер

    password = browser.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled')
    password.send_keys(user_password, Keys.ENTER) # Вводим пароль, жмём энтер

    time.sleep(2) # Ждём, пока загрузится
    browser.get(saby_dialogs) # Открываем реестр контактов

    time.sleep(2) # Ждём, пока загрузится
    plus = browser.find_element(By.CSS_SELECTOR, 'span[class="controls-icon_size-m  extControls-addButton-icon-brand icon-RoundPlus controls-icon"]')
    plus.click()

    time.sleep(2) # Ждём, пока загрузится
    poisk = browser.find_element(By.CSS_SELECTOR, '.controls-Search__nativeField_caretEmpty_theme_default')
    poisk.send_keys(user_name)

    time.sleep(2) # Ждём, пока загрузится
    strut = browser.find_element(By.CSS_SELECTOR, 'span[title="Струтынский Андрей Олегович"]')
    strut.click()

    time.sleep(2) # Ждём, пока загрузится
    text = browser.find_element(By.CSS_SELECTOR, 'div[class="textEditor_slate_Field textEditor_slate_Container textEditor__textField"]')
    text.send_keys(text_msg, Keys.CONTROL + Keys.ENTER)

    time.sleep(2) # Ждём, пока загрузится
    text_2 = browser.find_element(By.XPATH, f'//p[text()="{text_msg}"]')
    assert text_2.is_displayed(), 'Сообщение не появилось в реестре'
    text_2.click()

    time.sleep(2) # Ждём, пока загрузится
    del_msg = browser.find_element(By.CSS_SELECTOR, 'span[class="controls-icon_size-m  controls-BaseButton__icon  icon-Erase controls-icon"]')
    del_msg.click()
    time.sleep(2)
    assert len(browser.find_elements(By.XPATH, f'//p[text()="{text_msg}"]')) == 0, 'Элемент не удалён'

finally:
    browser.quit()