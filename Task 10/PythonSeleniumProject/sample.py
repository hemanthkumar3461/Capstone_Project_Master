from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Test:

    def __init__(self):
        self.s = Service(r"C:\\Users\\heman\\Desktop\\UST_Workspace\\chromedriver.exe")
        browser = webdriver.Chrome(service=self.s)
        url = 'https://www.urbanladder.com/'

        browser.get(url)
        browser.maximize_window()

        browser.find_element(By.XPATH, "//*[@id='header']/div[1]/div/section[3]/ul/li[2]/span").click()
        time.sleep(1)
        browser.find_element(By.LINK_TEXT, "Log In").click()
        time.sleep(5)
        browser.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/div[2]/div[3]/form/div/input").send_keys(
            "abc1111@gmail.com")
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div/div[2]/div[3]/form/div/div/div/input"). \
            send_keys("Fk#mM!wGS9jvx4Z")
        browser.find_element(By.ID, "ul_site_login").click()
        print("Login successful")

        browser.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div/ul/li[2]/span").click()
        time.sleep(2)
        #browser.find_element(By.LINK_TEXT, "Sofa Set").click();
        print("Navigated to Sofa set page");

        browser.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/nav/div/ul/li[2]/div/div/ul/li[1]/ul/li[1]/a/span").click()
        time.sleep(4)
        browser.find_element(By.ID, "filters_availability_In_Stock_Only").click()
        print("Check boxing availablity stock")
        time.sleep(10)

        browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div/form/div[1]/div/div/ul/li[4]/div[1]").click()
        print("Clicking on brand")
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div/form/div[1]/div/div/ul/li[4]/div[2]/div/div/div/ul/li[2]/label").click()
        print("Seleting brand")
        time.sleep(1)

        browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div/form/div[1]/div/div/ul/li[1]/div[1]").click()
        print("Clicking on price")
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/div/form/div[1]/div/div/ul/li[1]/div[2]/div/div/ul/li[2]/div[2]/label/input").click()
        print("Seleting price filter button")
        time.sleep(3)

        browser.close()


ob1 = Test()
