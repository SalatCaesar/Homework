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
from selenium.webdriver import ActionChains, Keys  # C Keys роще авторизоваться оказалось, хотя и всего минус 4 строки кода


site_fix = "https://fix-online.saby.ru/"  # Здесь записываем адрес сайта
saby_dialogs = "https://fix-online.saby.ru/page/dialogs"  # Здесь записываем адрес реестра контактов
user_login, user_password = 'Strutandol', 'пароль123'  # Логин/пароль для авторизации
user_name = 'Струтынский Андрей Олегович'  # Пользователь для отправки сообщения
text_msg = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 15))) # Текст сообщения. Я хотел добавить обычный текст, но тогда возможна ситуация,
                                                                                          # что, раз не удалившись, сообщение останется в реестре. А это позволит
                                                                                          # не перепутать старое с новым т.к. ищу я его через текст сообщения

browser = webdriver.Chrome()  # Открываем браузер

try:
    # Открываем на весь экран, а то замучался вглядываться, и переходим на сайт
    browser.maximize_window()
    browser.get(site_fix)
    time.sleep(1)  # Ждём загрузки, а то тормозит

    # Тут авторизуемся. Сначала ищем поле логина, вводим его, жмакаем Enter, а потом тоже самое с паролем
    login = browser.find_element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled')
    login.send_keys(user_login, Keys.ENTER)
    password = browser.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled')
    password.send_keys(user_password, Keys.ENTER)
    time.sleep(3)  # Ждём загрузки, а то тормозит

    # Переходим в реестр контактов
    browser.get(saby_dialogs)
    time.sleep(3)  # Ждём загрузки, а то тормозит

    # Открываем диалог сообщений по плюсу в реестре
    new_msg = browser.find_element(By.CSS_SELECTOR, 'span[class="controls-icon_size-m  extControls-addButton-icon-brand icon-RoundPlus controls-icon"]')
    new_msg.click()
    time.sleep(3)  # Ждём загрузки, а то тормозит

    # Найдем пользователя через поиск, выберем его для отправки сообщения
    search_user = browser.find_element(By.CSS_SELECTOR, '.controls-Search__nativeField_caretEmpty_theme_default')
    search_user.send_keys(user_name)
    time.sleep(2)  # Ждём загрузки, а то тормозит
    strut = browser.find_element(By.CSS_SELECTOR, 'span[title="Струтынский Андрей Олегович"]')
    strut.click()
    time.sleep(2)  # Ждём загрузки, а то тормозит

    # Найдём поле для ввода текста и введём туда случайное сообщение, а после отправим сообщение нажатием CONTROL + Enter
    text = browser.find_element(By.CSS_SELECTOR, 'div[class="textEditor_slate_Field textEditor_slate_Container textEditor__textField"]')
    text.send_keys(text_msg, Keys.CONTROL + Keys.ENTER)
    time.sleep(2)  # Ждём загрузки, а то тормозит

    # Проверяю отображение сообщения в реестре. Из-за сгенерированного случайного текста точно могу найти его через XPath
    text_2 = browser.find_element(By.XPATH, f'//p[text()="{text_msg}"]')
    assert text_2.is_displayed(), 'Сообщение не появилось в реестре'

    # С помощью ActionChains вызываем опции записи и удаляем сообщение
    action = ActionChains(browser)
    action.context_click(text_2)
    action.perform()
    del_msg = browser.find_element(By.CSS_SELECTOR, 'span[class="controls-icon_size-m controls-icon_style-danger controls-Menu__icon controls-Menu__icon_m-left icon-Erase controls-icon"]')
    del_msg.click()
    time.sleep(2)  # Ждём загрузки, а то тормозит

    # Проверяем, осталось ли сообщение в реестре. Проверяем, что нет сообщений с введенным ранее текстом.
    # Как раз тут могла сломаться логика, если бы сообщение было не уникальным
    assert len(browser.find_elements(By.XPATH, f'//p[text()="{text_msg}"]')) == 0, 'Сообщение не удалено'

finally:
    browser.quit()