from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service(r'D:\chromedriver-win64\chromedriver-win64\chromedriver.exe'))
wd.get('https://www.baidu.com')
element =wd.find_element(By.ID,'kw')

input('等待回车结束程序')
