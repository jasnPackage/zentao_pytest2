#coding:utf-8
import pytest
import time
from pages.login_page import _login_result,_login,_get_alert


class TestLogin():

    @pytest.fixture(scope="funtion",autouse=True)
    def startPage(self,driver,host):
        print("---让每个用例都从登录首页开始:---start!---")
        driver.get(host+"/zentao/user-login.html")
        driver.delete_all_cookies()
        driver.refresh()



    def test_login_fail(self,driver,host):
        """禅道-登录失败案例：admin111-111111"""
        _login(driver,host,"admin111","111111")
        result1 = _get_alert(driver)
        print("测试结果：%s" % result1)
        assert "登录失败" in result1



    def test_login_pass(self,driver,host):
        """禅道-登录成功案例"""
        _login(driver,host,"admin","123456")
        result2 = _login_result(driver,"admin")
        print("测试结果：%s" % result2)
        assert result2
