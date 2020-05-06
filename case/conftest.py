#coding:utf-8

import pytest
from pages.login_page import _login
import os,shutil



# 登录功能
@pytest.fixture(scope="session")
def login(driver,host):
    _login(driver,host)





@pytest.fixture(scope="function")
def startPage(driver,host):
    print("---让每个用例都从登录首页开始:---start!---")
    driver.get(host + "/zentao/user-login.html")
    driver.delete_all_cookies()
    driver.refresh()


