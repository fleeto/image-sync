# 镜像复制和批量扫描

使用 `crane` 进行镜像复制，`trivy` 进行镜像扫描

## 构建

执行命令 `./build.sh [image-name]` 生成镜像。

### 运行镜像
`docker run -v /absolute_path_to_conf/conf:/atomworker/conf -it ${image-name}:latest`

## 镜像复制（clone.py）

`./clone.py`，根据 [`conf/clone.json`](conf/clone.json) 进行镜像复制。配置文件格式：

~~~json
{
  "alpine": {
    "sourceRepo": "alpine",
    "tagFilter": "^3\\.9.*?$",
    "later-than": "",
    "targetPattern":"dustise/{repo}:{tag}"
  }
}
~~~

- `sourceRepo`：源镜像名称，例如 `alpine`；
- `later-than`: 仅复制晚于该时间的 Tag，**此选项会严重降低效率**，例如 `2021-06-15T22:19:37.842991933Z`，空字符串代表复制所有 Tag；
- `tagFilter`：正则表达式，仅复制匹配该规则的 Tag；
- `target-pattern`: 复制目标 URL 的构成方式，内置变量来自源镜像，包括 `host`、`project`、`repo`、`tag`，例如 `127.7.7.1/sub/{repo}:{tag}`。

> 如果需要登录信息，需要将 Docker 认证的 JSON 文件复制到 `/root/.docker/config.json`

## 搜集信息（gather.py）

获取指定镜像的 `manifest`、`config`，配置文件为 [`conf/scan.json`](conf/scan.json)，格式如下：

~~~json
{
  "alpine": {
    "repo": "dustise/alpine",
    "desc": "alpine linux"
  }
}
~~~

运行后，会在 `output/` 目录下生成 `info-[datetime]` 的 json 文件，例如：

~~~plaintext
output/
├── info-2021062515
    └── alpine
        ├── 3.9
        │   ├── config.json
        │   └── manifest.json
...
~~~

## 漏洞扫描（scan.py）

> 使用 Trivy 扫描指定镜像的漏洞，建议使用 `GITHUB_TOKEN` 环境变量，防止 Trivy 被限流。

配置文件和信息收集相同，同样在 `output` 目录生成结果文件，例如：

~~~plaintext
└── scan-2021062515
    └── alpine
        ├── 3.9.2.json
        ├── 3.9.3.json
        ├── 3.9.4.json
        ├── 3.9.5.json
        ├── 3.9.6.json
        └── 3.9.json
~~~