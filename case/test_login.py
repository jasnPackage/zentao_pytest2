#coding:utf-8
import pytest
import time
from pages.login_page import _login_result,_login,_get_alert



# 以元祖形式参数化
# test_login_data = [("admin","123456","admin"),("wux","111111","无锡")]


# 以字典形式参数化
test_login_data = [{"user":"admin","psw":"123456","expect":"admin"},
                   {"user":"wux","psw":"111111","expect":"无锡"}]

class TestLogin():

    # 先调用conftest.py中的startPage函数
    @pytest.mark.parametrize("login_data",test_login_data)
    def test_login_pass(self, startPage, driver, host,login_data):
        """禅道-登录成功案例"""
        _login(driver, host, login_data["user"], login_data["psw"])
        result2 = _login_result(driver, login_data["expect"])
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
