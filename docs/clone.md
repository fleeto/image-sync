# 镜像复制

任务启动后，根据 [`conf/clone.json`](../conf/clone.json) 进行镜像复制。配置文件格式：

- `name`：源镜像名称，例如 `dustise/sleep`；
- `later-than`: 仅复制晚于该时间的 Tag，**此选项会严重降低效率**，例如 `2021-06-15T22:19:37.842991933Z`，空字符串代表复制所有 Tag；
- `target-pattern`: 复制目标 URL 的构成方式，内置变量来自源镜像，包括 `host`、`project`、`repo`、`tag`，例如 `127.7.7.1/sub/{repo}:{tag}`。
