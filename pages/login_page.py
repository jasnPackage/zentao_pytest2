#coding:utf-8

from selenium import webdriver
from common.base import Base
import time

# ---------------定位元素信息-------------------- #
loc1 = ("id","account")
loc2 = ("css selector","[name='password']")
loc3 = ("xpath","//*[@id='submit']")

result_loc = ("xpath", ".//*[@id='userMenu']/a")


def _login(driver,host,user="admin",psw="123456"):
    '''普通登录函数'''
    zen = Base(driver)
    driver.get(host+"/zentao/user-login-L3plbnRhby8=.html")
    zen.sendKeys(loc1, user)
    zen.sendKeys(loc2, psw)
    zen.click(loc3)
    time.sleep(2)


def _login_result(driver,_text):
    '''
    登录成功后，获取当前页面的用户名，判断用户名
    :param driver:
    :param _text: 用户名
    :return: True or False
    '''
    zen = Base(driver)
    r = zen.is_text_in_element(result_loc,_text)
    return r



def _get_alert(driver):
    '''判断alert在不在,存在返回text文本内容，不存在返回空字符'''
    zen = Base(driver)
    try:
        alert = zen.is_alert()
        text = alert.text
        alert.accept()  # 点alert确定
        return text
    except:
        return ""
