#!/usr/bin/env python3

import json
import datetime
import os.path
from franken import crane

config_data = {}
with open("conf/scan.json") as config_file:
    config_data = json.load(config_file)

result = {}
date_str = datetime.datetime.now().strftime("%Y%m%d%H")
output_home = os.path.join("output", "info-" + date_str)
os.mkdir(output_home)
for key, value in config_data.items():
    repo = value["repo"]
    repo_path = os.path.join(output_home, key)
    os.mkdir(repo_path)
    tags = crane.get_tag_list(repo)
    for tag in tags:
        manifest = crane.get_manifest(repo, tag)
        config = crane.get_config(repo, tag)
        tag_path = os.path.join(repo_path, tag)
        os.mkdir(tag_path)
        with open(os.path.join(tag_path, "manifest.json"), "w") as writer:
            json.dump(manifest, writer, indent=2)
        with open(os.path.join(tag_path, "config.json"), "w") as writer:
            json.dump(config, writer, indent=2)
