#coding:utf-8

from selenium import webdriver
from common.base import Base
import time,allure


class AddBugPage(Base):

    # 添加Bug
    loc_test = ("link text", "测试")
    loc_bug = ("link text", "Bug")
    loc_addbug = ("xpath", ".//*[@id='createActionMenu']/a")
    loc_truck = ("xpath", ".//*[@id='openedBuild_chosen']/ul")
    loc_truck_add = ("xpath", ".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id", "title")
    # 需要先切换iframe
    loc_input_body = ("class name", "article-content")
    loc_avse = ("css selector", "#submit")

    # 新增的列表
    loc_new = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")


    @allure.step("输入bug必填项")
    def add_bug(self,title="测试提交BUG"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_truck)
        self.click(self.loc_truck_add)


        self.sendKeys(self.loc_input_title,title)
        # 输入body
        frame = self.findElement(("class name","ke-edit-iframe"))
        self.driver.switch_to.frame(frame)
        # 富文本不能clear
        body = '''[测试步骤]xxx
                [结果]xxx
                [期望结果]xxx
                '''
        self.sendKeys(self.loc_input_body,body)
        self.driver.switch_to.default_content()

        self.highLightElement(self.loc_avse)

        save_button = self.findElement(self.loc_avse)
        self.driver.execute_script("arguments[0].click();",save_button)


    @allure.step("验证bug列表中有添加的bug")
    def is_add_bug_sucess(self,_text):
        '''从bug列表中取出第一个bug的text文本'''
        bug_text = self.get_text(self.loc_new)
        print("bug_text:%s"%bug_text)
        return self.is_text_in_element(self.loc_new,_text)


