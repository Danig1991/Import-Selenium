from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    options=options,
    service=ChromeService(ChromeDriverManager().install())
)
#базовый url
base_url = 'https://www.saucedemo.com/'
# команда для открытия ссылки
driver.get(base_url)
# команда для открытия окна в нужном разрешении
# (корректно ли открывается в этом разрешении)
driver.set_window_size(1920,1080)

# команда для открытия окна в максимальном для монитора разрешении
# driver.maximize_window()