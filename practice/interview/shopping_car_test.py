import unittest
from shopping_cart import calculate_total

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.commodity = {
            "电子": ["ipad", "iphone", "显示器", "笔记本电脑", "键盘"],
            "食品": ["面包", "饼干", "蛋糕", "牛肉", "鱼", "蔬菜"],
            "日用品": ["餐巾纸", "收纳箱", "咖啡杯", "雨伞"],
            "酒类": ["啤酒", "白酒", "伏特加"]
        }

    def test_case_A(self):
        input_text = """2013.11.11 | 0.7 | 电子

1 * ipad : 2399.00
1 * 显示器 : 1799.00
12 * 啤酒 : 25.00
5 * 面包 : 9.00

2013.11.11
2014.3.2 1000 200
"""
        expected_result = 3083.60
        result = calculate_total(self.commodity, input_text)
        self.assertAlmostEqual(result, expected_result, places=2)

    def test_case_B(self):
        input_text = """


3 * 蔬菜 : 5.98
8 * 餐巾纸 : 3.20

2014.01.01

"""
        expected_result = 43.54
        result = calculate_total(self.commodity, input_text)
        self.assertAlmostEqual(result, expected_result, places=2)

if __name__ == '__main__':
    unittest.main()
