import os

# 当前路径
PATH = os.path.dirname(__file__)

# 测试路径
test_dir = os.path.join(PATH, 'test_dir')

# config文件路径
config_file = os.path.join(PATH, 'config', 'config.yaml')

# excel文件路径
excel_file = os.path.join(PATH, 'data', 'data.xlsx')

# log输出文件路径
log_file = os.path.join(PATH, 'log\\')

# html-report文件路径
report_dir = os.path.join(PATH, 'pytest_report\\')

# 失败次数
max_fail = '3'

# 重试次数
rerun = '3'
