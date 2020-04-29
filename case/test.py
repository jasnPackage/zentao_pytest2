# #coding:utf-8
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# import time
#
#
#
# driver = webdriver.Chrome()
# driver.get("http://127.0.0.1/zentao/user-login.html")
# # driver.maximize_window()
# driver.find_element_by_id("account").send_keys("admin")
# driver.find_element_by_css_selector("[name='password']").send_keys("123456")
# driver.find_element_by_xpath("//*[@id='submit']").click()
#
#
# driver.find_element_by_link_text("测试").click()
# driver.find_element_by_link_text("Bug").click()
# driver.find_element_by_xpath(".//*[@id='createActionMenu']/a").click()
# driver.find_element_by_xpath(".//*[@id='openedBuild_chosen']/ul").click()
# driver.find_element_by_xpath(".//*[@id='openedBuild_chosen']/div/ul/li").click()
#
# driver.find_element_by_id("title").send_keys("测试提交BUG")
#
# button = driver.find_element_by_id("submit")
# driver.execute_script("arguments[0].click();",button)
#
# time.sleep(5)
#
# result = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,".//*[@id='bugList']/tbody/tr[1]/td[4]/a"),u'测试提交BUG'))
#
# print(result)
#
#
# time.sleep(3)
# driver.quit()




# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

try:

    driver = webdriver.Chrome()
    url = "https://www.baidu.com"
    driver.get(url)

    locator = ("name", "tj_trnews")
    text = u"新闻"
    result = EC.text_to_be_present_in_element(locator, text)(driver)
    print(result)
except Exception as e:
    print(e)
finally:
    driver.quit()