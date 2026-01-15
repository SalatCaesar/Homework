# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import platform


browser = webdriver.Chrome()
site_saby = "https://saby.ru/"
platforma = platform.system()

try:
    # Преходим в полноэкранный режим и переходим по адресу сайта
    browser.maximize_window()
    browser.get(site_saby)
    time.sleep(1)

    site_download = browser.find_element(By.CSS_SELECTOR, 'a[href="/download"]')
    site_download.click()
    time.sleep(2)

    tabs_download = browser.find_elements(By.CSS_SELECTOR, 'span[class="sbis_ru-DownloadNew-innerTabs__title sbis_ru-DownloadNew-innerTabs__title--default"]')

    if platforma == 'Windows':
        tabs_download[0].click()
    if platforma == 'Linux':
        tabs_download[1].click()
    if platforma == 'Darwin':
        tabs_download[2].click()

finally:
    browser.quit()