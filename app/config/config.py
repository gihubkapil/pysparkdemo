import yaml
from yaml.loader import SafeLoader
import os
from app.utils.root import get_project_root

root = get_project_root()
#print(root)

#print(os.path.dirname(os.path.abspath(__file__)))

#config.read(os.path.join(os.path.dirname(__file__), 'config', 'conf.yaml'))

# Open the file and load the file
config_path = 'conf.yaml'
def conf():
    path = os.path.join(os.path.dirname(__file__), 'conf.yaml')
    with open(path) as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data