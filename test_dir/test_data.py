import openpyxl
from base.base_tools import Base
from base.case_runner import CaseRunner
from base.excel_tools import get_sheet_column_value, put_config_yaml
from base.yaml_tools import yaml_read
import pytest
from common import excel_file, config_file


class TestData:
    def setup_class(self):
        """前置的 数据初始化内容"""
        # 获取excel对象，得到数据
        self.excel_obj = openpyxl.load_workbook(excel_file)
        # 把配置项读取并存入config.yaml并返回config_dict
        config_dict = put_config_yaml(self.excel_obj, config_file)
        # 获取要执行的用例
        get_sheet_column_value(self.excel_obj, config_dict)
        # 实例化Base
        self.b = Base(config_file)
        # 实例化case运行器
        self.cr = CaseRunner(self.excel_obj, self.b)

    def teardown_class(self):
        """后置的 数据初始化内容"""
        # 退出浏览器和excel对象
        self.excel_obj.close()
        self.b.quit()

    @pytest.mark.parametrize('case_name', get_sheet_column_value(openpyxl.load_workbook(excel_file),
                                                                 yaml_read(config_file)))
    def test_case(self, case_name):
        self.cr.case_runner(case_name)
