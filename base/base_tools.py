from time import sleep
from selenium import webdriver
from base.chrome_options import chrome_options
from selenium.webdriver.support.wait import WebDriverWait
from base.yaml_tools import yaml_read


class Base:
    def __init__(self, config_file_path):
        self.config_dict = yaml_read(config_file_path)
        self.driver = webdriver.Chrome(options=chrome_options())

    def open(self, data_dict):
        """打开浏览器"""
        if data_dict['txt'] is None:
            base_url = self.config_dict['url']
        else:
            base_url = self.config_dict['url'] + data_dict['txt']
        try:
            self.driver.get(base_url)
        except Exception:
            raise

    def locate(self, data_dict):
        """定位"""
        try:
            ele = WebDriverWait(self.driver, 6, 0.5).until(lambda s: s.find_element(data_dict['locate_by'],
                                                                                    data_dict['locate_value']))
            return ele
        except Exception:
            raise

    def input(self, data_dict):
        """输入"""
        try:
            self.locate(data_dict).send_keys(data_dict['txt'])
        except Exception:
            raise

    def click(self, data_dict):
        """单击"""
        try:
            self.locate(data_dict).click()
        except Exception:
            raise

    def max_window(self):
        """窗口最大化"""
        self.driver.maximize_window()

    def switch_to_iframe(self, data_dict):
        """切换到iframe"""
        try:
            self.driver.switch_to.frame(data_dict['txt'])
        except Exception:
            raise

    def switch_to_window(self, data_dict):
        """切换到窗口"""
        windows = self.driver.window_handles
        try:
            self.driver.switch_to.widnow(windows[data_dict['txt']])
        except Exception:
            raise

    def assert_locate(self, data_dict):
        assert self.locate(data_dict) is not None, '断言失败'

    @staticmethod
    def wait(data_dict):
        """固定等待"""
        sleep(int(data_dict['txt']))

    def quit(self):
        """退出浏览器"""
        try:
            self.driver.quit()
        except Exception:
            raise
