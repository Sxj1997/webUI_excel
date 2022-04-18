from config.log_config import MyLog

class CaseRunner:
    def __init__(self, excel_obj, base_tool):
        self.excel_obj = excel_obj
        self.b = base_tool
        self.my_log = MyLog().logger

    def case_runner(self, sheet_name):
        # 获取Sheet页的值
        sheet_obj = self.excel_obj[sheet_name]  # 获取一个sheet对象
        self.my_log.debug("执行sheet页：" + sheet_name)
        values = sheet_obj.values  # sheet页的值
        # 每一行解析为一行代码
        for value in values:
            data_dict = dict()
            if value[0] != "编号" and value[1] == 1:
                data_dict['no'] = value[0]
                data_dict['step_name'] = value[2]
                data_dict['kw'] = value[3]
                data_dict['locate_by'] = value[4]
                data_dict['locate_value'] = value[5]
                data_dict['txt'] = value[6]
                data_dict['note'] = value[7]
                data_dict['expect'] = value[8]
                try:
                    self.my_log.debug("执行步骤：" + data_dict['step_name'])
                    getattr(self.b, data_dict['kw'])(data_dict)  # 执行代码
                except Exception as e:
                    self.my_log.error("执行步骤：" + data_dict['step_name'] + ' 失败')
                    self.my_log.error(e)
                    raise
