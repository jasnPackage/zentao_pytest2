#coding:utf-8
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from py._xmlgen import html
import os,shutil


_driver = None

def pytest_addoption(parser):
    '''添加命令行参数--browser、--host'''
    parser.addoption(
        "--browser",action="store",default="chrome",
        help="browser option: firefox or chrome"
    )


    #添加host参数，设置默认测试环境地址
    parser.addoption(
        "--host",action="store",default="http://127.0.0.1:80",
        help="test host->http://127.0.0.1:80"
    )






@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        report.description = str(item.function.__doc__)
        report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")



@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('Description'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)

def _capture_screenshot():
    '''
    截图保存为base64
    :return:
    '''
    return _driver.get_screenshot_as_base64()



# 有界面浏览器
# @pytest.fixture(scope='session')
# def driver(request):
#     '''定义全局driver参数'''
#     global _driver
#     if _driver is None:
#         name = request.config.getoption("--browser")
#         if name == "firefox":
#             _driver = webdriver.Firefox()
#         elif name == "chrome":
#             _driver = webdriver.Chrome()
#         else:
#             _driver = webdriver.Chrome()
#         _driver.maximize_window()
#         print("正在启动浏览器名称：%s" % name)
#
#
#     def fn():
#         print("当全部用例执行完之后：teardown quit driver！")
#         _driver.quit()
#     request.addfinalizer(fn)
#     return _driver



# 无界面浏览器
@pytest.fixture(scope='session')
def driver(request):
    '''定义全局driver参数'''
    global _driver
    if _driver is None:
        name = request.config.getoption("--browser")
        if name == "firefox":
            _driver = webdriver.Firefox()
        elif name == "chrome":
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            _driver = webdriver.Chrome(options=chrome_options)
        else:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            _driver = webdriver.Chrome(options=chrome_options)
        _driver.maximize_window()
        print("正在启动浏览器名称：%s" % name)


    def fn():
        print("当全部用例执行完之后：teardown quit driver！")
        _driver.quit()
    request.addfinalizer(fn)
    return _driver




# 获取cmd命令行中host参数的值

@pytest.fixture(scope='session')
def host(request):
    return request.config.getoption("--host")




# 执行用例前，清空allure_raw文件夹
@pytest.fixture(scope='session',autouse=True)
def clearAllure():
    print("清空allure_raw文件夹")
    case_path = os.getcwd()
    allureReport_path = os.path.join(case_path,r'report\allure_raw')
    print("allureReport_path的路径：%s"%allureReport_path)

    # 如果report下没有allure_raw文件夹，先创建
    if not os.path.exists(allureReport_path):
        os.makedirs(allureReport_path)
    else:
        shutil.rmtree(allureReport_path)  # 清空allure_raw文件夹
        os.makedirs(allureReport_path)    # 清空完allure_raw文件夹后，allure_raw是空文件夹，会把allure_raw文件夹删掉，所以在清空完后再创建allure_raw文件夹文件夹





