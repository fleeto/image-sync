#!/usr/bin/env python3

import json
import datetime
import os.path
from franken import crane, trivy

with open("conf/scan.json") as config_file:
    config_data = json.load(config_file)

result = {}
date_str = datetime.datetime.now().strftime("%Y%m%d%H")
output_home = os.path.join("output", "scan-" + date_str)
if not os.path.exists(output_home):
    os.mkdir(output_home)

for key, value in config_data.items():
    tag_list = crane.get_tag_list(value["repo"])
    for tag in tag_list:
        repo_path = os.path.join(output_home, key)
        if not os.path.exists(repo_path):
            os.mkdir(repo_path)
        result = trivy.scan(value["repo"], tag, os.path.join(repo_path, tag + ".json"))
