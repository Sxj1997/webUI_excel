import yaml

def yaml_read(file_path):
    """read"""
    f = open(file_path, 'r')
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    return yaml_data

def yaml_a_write(file_path, data):
    """追加写入"""
    f = open(file_path, 'a')
    yaml.dump(data, f, allow_unicode=True)
    f.close()

def yaml_w_write(file_path, data):
    """覆盖写入"""
    f = open(file_path, 'w')
    yaml.dump(data, f, allow_unicode=True)
    f.close()

def yaml_dict_update(file_path, dict_data):
    """对yaml（only for dict）进行更新"""
    x = dict()
    x.update(dict_data)
    yaml_w_write(file_path, x)
