from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from dotenv import load_dotenv
import string
import requests
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from pyvirtualdisplay import Display
from selenium import webdriver

def getFiles():


    # display = Display(visible=0, size=(800, 600))
    # display.start()

    # options = webdriver.ChromeOptions()
    # options.add_argument('--no-sandbox')

    # driver = webdriver.Chrome(chrome_options=options)
    # service=Service(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    driver.get("https://socs1.binus.ac.id/quiz/public/login.php")

    driver.find_element(By.ID, "login").send_keys(username)
    driver.find_element(By.ID, "passwd").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td[2]/input").click()

    os.makedirs("problems", exist_ok=True)
    os.chdir("./problems")

    Weeks = len(Select(driver.find_element(By.ID, "cid")).options)

    for week in range(1, Weeks + 1):
        driver.find_element(By.XPATH, '//*[@id="cid"]/option[' + str(week) + ']').click()
        curr_path = driver.find_element(By.XPATH, '//*[@id="cid"]/option[' + str(week) + ']').text
        os.makedirs(curr_path, exist_ok=True)
        os.chdir("./" + curr_path)

        sub1 = "-"
        sub2 = "-"
        
        test_str = curr_path.replace(sub1,"*")
        test_str = curr_path.replace(sub2,"*")
        re = test_str.split("*")
        lab = re[1]

        driver_cookies = driver.get_cookies()
        
        c = {c['name']:c['value'] for c in driver_cookies}
        alp = list(string.ascii_uppercase)
            
        for i in range(0, 6):
            url = driver.find_element(By.LINK_TEXT, alp[i]).get_attribute("href")
            print(url)

            response = requests.get(url, cookies=c)
            file = open(lab + "-week-" + str(week) + "-prob-" + alp[i] + ".pdf", "wb")
            file.write(response.content)
            file.close()

        os.chdir("..")


if __name__ == "__main__":
    load_dotenv()

    username = os.getenv("EMAIL_BINUS")
    password = os.getenv("PASS_BINUS")

    getFiles()