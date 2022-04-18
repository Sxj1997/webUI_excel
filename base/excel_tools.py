from base.yaml_tools import yaml_dict_update

def get_sheet_column_value(excel_obj, config_dict):
    """获取sheet页列的值"""
    # 读取配置项中需要运行的测试管理集
    run_cases_config = config_dict['run_cases']
    # 读取测试集需要运行的sheet页
    run_cases_values = excel_obj[run_cases_config].values
    run_cases = []
    for run_cases_data in run_cases_values:
        if run_cases_data[1] == 1:
            run_cases.append(run_cases_data[2])
    return run_cases

def put_config_yaml(excel_obj, config_file):
    # 把配置项读取并存入config.yaml
    config_sheet_values = excel_obj['配置项'].values
    config_dict = dict()
    for config_data in config_sheet_values:
        if config_data[0] != "编号" and config_data[1] == 1:
            config_dict[config_data[2]] = config_data[3]
    yaml_dict_update(config_file, config_dict)
    # 返回config_dict
    return config_dict
