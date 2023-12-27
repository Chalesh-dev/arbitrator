import requests
from bs4 import BeautifulSoup
import re
from requests_html import HTMLSession
from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By

i = 1
while True:
    driver = Firefox()
    driver.get('https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsearch%3Fq%3D%5C%26type%3Dcode')
    driver.find_element(By.XPATH,'//*[@id="login_field"]').send_keys("tahasoltani3118@gmail.com")
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("")
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[13]').click()

    f"https://github.com/search?q={search}&type=code"

"https://raw.githubusercontent.com/xerpi/linux_vita/22b952417eb99edf0ab31ea6db0233a1010f5ec2/drivers/infiniband/hw/hfi1/common.h"
"https://raw.githubusercontent.com/EbookFoundation/free-programming-books/18330182887642285cc0a3ee3a50aaae12f5c84b/courses/free-courses-ml.md"
"https://raw.githubusercontent.com/EbookFoundation/free-programming-books/18330182887642285cc0a3ee3a50aaae12f5c84b/courses/free-courses-ml.md"



    # url_git = f"https://github.com/search?q=\"&type=code&p={i}"
    res = requests.get(url_git)
    html_contract = res.text
    soup = BeautifulSoup(html_contract, "html.parser")
    text_content = soup.get_text()

    pattern1 = re.compile(r"^0x[0-9a-fA-F]{64}")
    pattern2 = re.compile(r"[0-9a-fA-F]{64}")

    matches1 = pattern1.findall(text_content)
    matches2 = pattern2.findall(text_content)
    matches = []
    matches.append(matches1)
    matches.append(matches2)
    if matches != 0:
        print(matches)
    i += 1
