#coding:utf-8
import pytest
import time
from pages.login_page import _login_result,_login,_get_alert




test_login_data = [("admin","123456","admin"),("wux","111111","无锡")]

class TestLogin():

    # @pytest.fixture(scope="function",autouse=True)
    # def startPage(self,driver,host):
    #     print("---让每个用例都从登录首页开始:---start!---")
    #     driver.get(host+"/zentao/user-login.html")
    #     driver.delete_all_cookies()
    #     driver.refresh()


    # 先调用conftest.py中的startPage函数
    @pytest.mark.parametrize("user,psw,expect",test_login_data)
    def test_login_pass(self, startPage, driver, host,user,psw,expect):
        """禅道-登录成功案例"""
        _login(driver, host, user, psw)
        result2 = _login_result(driver, expect)
        print("测试结果：%s" % result2)
        assert result2



    # 先调用conftest.py中的startPage函数
    def test_login_fail(self,startPage,driver,host):
        """禅道-登录失败案例：admin111-111111"""
        _login(driver,host,"admin111","111111")
        result1 = _get_alert(driver)
        print("测试结果：%s" % result1)
        assert "登录失败" in result1





if __name__ == "__main__":
    pytest.main(["-s","test_login.py"])
