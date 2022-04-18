import os

# 当前路径
PATH = os.path.dirname(__file__)

# config文件路径
config_file = os.path.join(PATH, 'config', 'config.yaml')

# excel文件路径
excel_file = os.path.join(PATH, 'data', 'data.xlsx')

# log输出文件路径
log_file = os.path.join(PATH, 'log\\')  # windows环境
