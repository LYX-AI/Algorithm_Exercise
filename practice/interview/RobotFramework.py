# StringUtility.py
class StringUtility:
    """自定义关键字库：提供字符串处理功能"""

    def concatenate_strings(self, str1, str2, separator=""):
        """连接两个字符串，可选分隔符"""
        return f"{str1}{separator}{str2}"

    def string_contains(self, text, substring):
        """检查字符串是否包含子串"""
        return substring in text

    def get_string_length(self, text):
        """返回字符串长度"""
        return len(text)

# *** Settings ***
# Library    StringUtility.py  # 导入自定义关键字库
#
# *** Test Cases ***
# Example Test for String Concatenation
#     [Documentation]    测试字符串连接功能
#     ${result}    Concatenate Strings    Hello    World    ,  # 调用关键字
#     Should Be Equal    ${result}    Hello,World             # 使用内置关键字验证结果
#
# Verify Substring Check
#     [Documentation]    测试子串检查功能
#     ${contains}    String Contains    Python is cool    cool
#     Should Be True    ${contains}
#
# Check String Length
#     [Documentation]    测试字符串长度计算
#     ${length}    Get String Length    RobotFramework
#     Should Be Equal As Integers    ${length}    14