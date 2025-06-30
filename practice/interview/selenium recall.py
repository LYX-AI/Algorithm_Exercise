from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
wd = webdriver.Chrome(service=Service(r'D:\chromedriver-win64\chromedriver-win64\chromedriver.exe'))
wd.get('https://www.baidu.com')
element =wd.find_element(By.ID,'kw')

input('等待回车结束程序')


#获取一个元素并且在里面填入值：
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('http://www.example.com')
elem = driver.find_element(By.ID,"textInputID")
elem.send_keys("Hello,selenium")
driver.quit()

#判断元素是否存在如果返回链表长度为0则元素不存在；可以使用try/execpt 捕获
from selenium.common.exceptions import NoSuchElementException
try:
    driver.find_element(By.ID,'foo')
    print("元素存在")
except NoSuchElementException:
    print("元素不存在")

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverwait
driver =webdriver.Chrome()
driver.get("http://example.com")
submit_btn = WebDriverwait(driver,10).until(
    EC.visibility_of_element_located((By.ID,"submit"))
)
submit_btn.click()


#IFrame 与多窗口操作
driver.switch_to.frame("login_fram")
#在iframe内定位并操作元素
driver.find_element(By.ID,'username').send_keys('user123')
#切换回主文档
driver.switch_to.default_content()


#滚动到顶部
driver.execute_script("window.scrollTo(0,0);")
#滚动到底部
driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
#滚动到指定元素
elem = driver.find_element(By.ID,"target")
driver.execute_script("arguments[0].scrollIntoView(true);",elem)

#文件的上传
driver.get("https://testupload.example.com")
file_input = driver.find_element(By.ID, 'fileupload')
file_input.send_keys('/path/to/targetfile.png')

import unittest

class TestExampleWithUnitest(unittest.TestCase):
        def setUp(self):
            self.driver = webdriver.Chrome()
        def test_title(self):
            self.driver.get('http://example.com')
            self.assertIn("Example",self.driver.title)
        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
'''
| 断言方法                               | 用途示例                         |
| ---------------------------------- | ---------------------------- |
| `assertEqual(a, b)`                | 检查 a == b                     |
| `assertNotEqual(a, b)`             | 检查 a != b                     |
| `assertTrue(x)`                    | 检查 x 是 True                  |
| `assertFalse(x)`                   | 检查 x 是 False                 |
| `assertIs(a, b)`                   | 检查 a is b（是同一个对象）        |
| `assertIsNone(x)`                  | 检查 x is None                  |
| `assertIn(a, b)`                   | 检查 a 在 b 里                   |
| `assertRaises(error, func, *args)` | 检查调用 func(\*args) 时会抛出 error |

'''

#和pytest做集成操作
import pytest

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()

def test_example(driver):
    driver.get("http://example.com")
    assert 'Example' in driver.title

#隐示等待
driver.implicitly_wait(10)
#显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)

#弹窗处理：
alert = driver.switch_to.alert
alert.accept()      # 点击确认
alert.dismiss()     # 点击取消
alert.text          # 获取弹窗文本
