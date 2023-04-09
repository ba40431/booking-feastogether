from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 設定 chrome driver 執行檔路徑
options = Options()
options.chrome_executable_path = r"C:\Users\ba404\Desktop\CODE\booking-feastogether\chromedriver.exe"

# 建立 driver 物件實體
driver = webdriver.Chrome(options=options)

# 連線到饗賓登入頁面
driver.get("https://www.feastogether.com.tw/")
time.sleep(0.5)

# 輸入帳號密碼，按下登入按鈕
signInButton = driver.find_element(By.XPATH, "//*[@id=\"header\"]/div[2]/div/ul/li[2]/p")

print(signInButton)

phoneNumberInput = driver.find_element_by_name("phoneNumber")
passwordInput = driver.find_element_by_name("password")

print(phoneNumberInput.get_attribute("name"))

signInBtn =driver.find_element_by_css_selector("sc-hKMtZM euuhBV login")
signInBtn.send_keys(Keys.ENTER)
driver.close()

