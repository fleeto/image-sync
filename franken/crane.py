import subprocess
import logging
import json


def get_tag_list(repo):
    logging.info("Fetching tag list form " + repo)
    command = ["crane", "ls", repo]
    resp = subprocess.check_output(command)
    return [item for item in resp.decode("UTF-8").split('\n') if len(item.strip()) > 0]


def copy_image_tag(source, target):
    logging.info("Copy {} to {} ...".format(source, target))
    command = ["crane", "copy", source, target]
    return subprocess.check_output(command)


def fetch_tag_history(repo, tag):
    fullname = "{}:{}".format(repo, tag)
    logging.info("Fetching history for " + fullname)
    command = ["crane", "config", fullname]
    resp = json.loads((subprocess.check_output(command)).decode("UTF-8"))
    return resp


def get_manifest(repo, tag):
    fullname = "{}:{}".format(repo, tag)
    logging.info("Fetching manifest of " + fullname)
    command = ["crane", "manifest", fullname]
    resp = json.loads((subprocess.check_output(command)).decode("UTF-8"))
    return resp


def get_config(repo, tag):
    fullname = "{}:{}".format(repo, tag)
    logging.info("Fetching manifest of " + fullname)
    command = ["crane", "config", fullname]
    resp = json.loads((subprocess.check_output(command)).decode("UTF-8"))
    return resp
