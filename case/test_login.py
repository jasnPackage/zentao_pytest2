#coding:utf-8
import pytest
import time
from pages.login_page import _login_result,_login,_get_alert
import allure



# 以元祖形式参数化
# test_login_data = [("admin","123456","admin"),("wux","111111","无锡")]


# 以字典形式参数化
test_login_data = [{"user":"admin","psw":"123456","expect":"admin"},
                   {"user":"wux","psw":"111111","expect":"无锡"}]


@allure.epic("登录测试用例")
@allure.feature("禅道登录")
class TestLogin():

    @allure.story("登录失败场景")
    @allure.title("测试用户登录失败")
    def test_login_fail(self, startPage, driver, host):
        """用例描述：测试用户名和密码输入错误，登录失败\n
        预置条件: 打开登录页面\n
        步骤1: 输入用户名和密码错误\n
        步骤2: 点登录按钮\n
        断言: 登录失败，提示：登录失败，请检查您的用户名或密码是否填写正确
        """

        _login(driver, host, "admin111", "111111")
        result1 = _get_alert(driver)
        print("测试结果：%s" % result1)
        assert "登录失败" in result1


    @allure.story("登录成功场景")
    @allure.title("测试用户登录成功")
    @pytest.mark.parametrize("login_data",test_login_data)
    def test_login_pass(self, startPage, driver, host,login_data):
        """用例描述：测试用户名和密码输入正确，登录成功\n
        预置条件: 打开登录页面\n
        步骤1: 输入用户名和密码正确\n
        步骤2: 点登录按钮\n
        断言: 登录成功
        """

        _login(driver, host, login_data["user"], login_data["psw"])
        result2 = _login_result(driver, login_data["expect"])
        print("测试结果：%s" % result2)
        assert result2



if __name__ == "__main__":
    pytest.main(["-s","test_login.py"])
