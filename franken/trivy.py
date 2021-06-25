#!/usr/bin/env python3

import subprocess
import json


def scan(repo, tag, filename=""):
    if len(filename) == 0:
        command = ["trivy", "i", "--no-progress",
                   "-f", "json", ":".join([repo, tag])]
        result = subprocess.check_output(command)
        return json.loads(result.decode("UTF-8"))
    else:
        command = ["trivy", "i", "--no-progress",
                   "-f", "json", "-o", filename,
                   ":".join([repo, tag])]
        return subprocess.check_output(command)
