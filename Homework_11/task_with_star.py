# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time
import os
import platform
import glob

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pathlib import Path


site_saby = "https://saby.ru/"  # Адрес сайта
platforma = platform.system()  # ОС системы
work_dir = Path.cwd()  # Рабочая директория папки
file_name = 'saby-setup'  # Имя файла, который скачиваем

# Создаём опции для браузера, чтобы он позволил скачать файл и выбираем паку для скачивания
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory': f'{work_dir}', "safebrowsing.enabled": True})

# Открываем браузер с выбранными выше опциями
browser = webdriver.Chrome(options=chrome_options)

try:
    # Преходим в полноэкранный режим и переходим по адресу сайта
    browser.maximize_window()
    browser.get(site_saby)

    # Переходим на страницу с версиями для скачивания
    site_download = browser.find_element(By.CSS_SELECTOR, 'a[href="/download"]')
    site_download.click()
    time.sleep(2)

    # Получаем список вкладок на странице  переходим на нужную в зависимости от ОС.
    # На вкладке проверяем расширение файла для скачивания скачиваем его
    tabs_system = browser.find_elements(By.CSS_SELECTOR, 'div[class*="controls-tabButton__overlay"]')
    download_button = browser.find_elements(By.CSS_SELECTOR, '[title*="Скачать"]')
    if platforma == 'Windows':
        assert download_button[0].get_attribute('href').split('/')[-1] == f'{file_name}.exe', "Неверное расширение файла"
        download_button[0].click()
    elif platforma == 'Linux':
        tabs_system[11].click()
        assert download_button[1].get_attribute('href').split('/')[-1] == f'{file_name}.AppImage', "Неверное расширение файла"
        download_button[1].click()
    elif platforma == 'Darwin':
        tabs_system[13].click()
        arch = platform.machine()
        if arch == 'arm64':
            assert download_button[2].get_attribute('href').split('/')[-1] == f'{file_name}.dmg', "Неверное расширение файла"
            download_button[2].click()
        elif arch == 'x86_64':
            assert download_button[3].get_attribute('href').split('/')[-1] == f'{file_name}.dmg', "Неверное расширение файла"
            download_button[3].click()
    time.sleep(10)  # Ждём пока скачается

    # Проверяем, что файл скачан и выводим его размер
    setup_file = glob.glob(f'{file_name}.*')
    assert len(setup_file) == 1, 'Файл не найден'
    print(round(os.path.getsize(setup_file[0])/(1024*1024)))

finally:
    browser.quit()

    # Удаляем файл
    for i in glob.glob(f'{file_name}*'):
        os.remove(i)