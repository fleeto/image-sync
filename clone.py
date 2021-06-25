#!/usr/bin/env python3

import json
import re
import logging

from franken import crane

with open("conf/clone.json") as cfg:
    workList = json.load(cfg)

for repo_index, repo_item in workList.items():
    logging.info("Processing " + repo_index)
    repo_name = repo_item["sourceRepo"]

    # extract source tag
    parts = repo_name.split('/')
    source_host = parts[0]
    source_repo = parts[-1]
    source_project = '/'.join(parts[1:-1])

    # get tag list and
    tagQueue = []
    needed = True
    if "tagFilter" in repo_item.keys() and len(repo_item["tagFilter"]) > 0:
        tagFilter = re.compile(repo_item["tagFilter"])
    else:
        tagFilter = None

    for tag in crane.get_tag_list(repo_item["sourceRepo"]):
        logging.info("Processing tag " + tag)
        needed = True
        if "later-than" in repo_item.keys() and len(repo_item["later-than"]) > 0:
            last_time = crane.fetch_tag_history(repo_name, tag)["history"][-1]["created"]
            if last_time > repo_item["later-than"]:
                needed = False
        if tagFilter is not None and tagFilter.match(tag) is None:
            print("Tag {} is skipped.".format(tag))
            needed = False
        if needed:
            tagQueue.append(tag)

    # copy tag list
    for tag in tagQueue:
        targetUrl = repo_item["targetPattern"]
        targetUrl = targetUrl.replace("{project}", source_project)
        targetUrl = targetUrl.replace("{repo}", source_repo)
        targetUrl = targetUrl.replace("{tag}", tag)
        logging.info("Copying " + repo_name)
        try:
            crane.copy_image_tag(repo_name + ":" + tag, targetUrl)
        except Exception:
            logging.error(repo_name + " Failed.")
