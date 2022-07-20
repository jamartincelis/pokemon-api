import os
from pokemon import MODULE_SETTINGS as settings
import json

def build_path(base_dir="",file_name=""):
    return os.path.join(base_dir, file_name)

def load_json(file_name=""):
    json_path = build_path(settings['JSON_DIR'], file_name)

    with open(json_path) as f:
        # load json file
        json_file = json.load(f)
    return json_file
