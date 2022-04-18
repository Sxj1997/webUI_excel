from selenium import webdriver
from base.yaml_tools import yaml_read
from common import config_file


def chrome_options():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 禁用自动栏
    options.add_argument('start-maximized')  # 窗口最大化
    prefs = {"credentials_enable_service": False, "profile.password_manager_enable": False}
    options.add_experimental_option("prefs", prefs)  # 去掉密码管理弹窗
    options.add_argument("--no-sandbox")  # 关闭沙盒模式
    config_dict = yaml_read(config_file)
    if 'webdriver_type' in config_dict.keys():
        options.add_argument("--headless")  # 无头模式，无界面运行，降低GPU使用率，利于多线程执行用例
    options.add_argument("--kiosk-printing")  # 弹出打印窗口，自动按下打印按钮

    return options
