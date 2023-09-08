import json


def write_conf(setting_obj):
    with open('config.json','w') as conf_file:
        conf = json.dumps(setting_obj)
        conf_file.write(conf)
        
        
def read_conf():
    with open('config.json','r') as conf_file:
        conf = json.loads(conf_file.read())
        return conf
        