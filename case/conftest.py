#coding:utf-8

import pytest


@pytest.fixture(scope="function")
def startPage(driver,host):
    print("---让每个用例都从登录首页开始:---start!---")
    driver.get(host + "/zentao/user-login.html")
    driver.delete_all_cookies()
    driver.refresh()