# простите за код, я не умею этого делать, но если дают задние, значит надо делать. Как-то, но работает:)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://only.digital/")

try:
    footer = driver.find_element(By.CLASS_NAME, "Footer_root___6Q28")
    print("footer true")
except NoSuchElementException:
    print("footer falls")

#тут попыталась через цикл понаходить элементы
elements_to_check = [
    'button[class*="Button_root"][class*="Button_primary"]',
    'a[class*="Button_root"][class*="Button_primary"][href*="/projects"]'
]

found_elements = []

for selector in elements_to_check:
    try:
        element = driver.find_element(By.CSS_SELECTOR, selector)
        found_elements.append(True)
    except NoSuchElementException:
        found_elements.append(False)

if all(found_elements):
    print("button true")
else:
    print("button falls")

driver.quit()

