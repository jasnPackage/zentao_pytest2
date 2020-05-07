#coding:utf-8

from pages.add_bug_page import AddBugPage
import pytest
import time
import allure

"""
case/test_add_bug.py文件
添加bug功能流程
"""


@allure.epic("添加bug测试用例")
@allure.feature("新增bug")
class TestAddBug():


    @allure.story("添加bug成功场景")
    @allure.title("添加bug成功")
    @pytest.mark.usefixtures("login") # 先登录
    def test_add_bug(self,driver):

        """测试添加BUG流程"""
        bug = AddBugPage(driver)
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "测试提交bug" + timestr
        print("title的值:%s"%title)
        bug.add_bug(title)

        result = bug.is_add_bug_sucess(title)
        print("测试结果：%s" % result)
        assert result


if __name__ == "__main__":
    pytest.main(["-s", "test_add_bug.py"])