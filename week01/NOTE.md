# 学习笔记

## 使用VScode远程控制WSL配置开发环境

在微软商店下载WSL，我第一次选择的是Ubuntu 20.04 LTS，其自带的python3版本是3.8，我在下载python虚拟环境的时候报错，后来转而使用python3.6也没有成功，果断卸载，选择了Ununtu 18.04 LTS版本，自带的python3是3.6版本，成功创建了虚拟环境。

1. 下载安装WSL，https://docs.microsoft.com/zh-cn/windows/wsl/install-win10
2. 使用VSCode控制WSL，https://docs.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-vscode
3. 换下载源，使用国内源，提高下载速度，使用`apt-get update`更新软件包，`apt-get upgrade`更新软件
4. 安装pip3，`apt-get install python3-pip`
5. 安装虚拟环境，`apt-get install python3-venv`
6. 创建虚拟环境,`python3 -m venv {venv_name}`，激活虚拟环境`source {venv_name}/bin/activate`，退出虚拟环境`deactivate`

## 爬虫开发

### requests

- 官方文档：https://cn.python-requests.org/zh_CN/latest/
- requests是一个用于发送HTTP/HTTPS请求的python第三方库，通过传入headers和url就可以模拟浏览器发起请求。

### BeautifulSoup

- 官网：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
- BeautifulSoup是一个基于HTML的页面解析器，用于对通过requests等工具获得的response进行解析，提取需要的字段信息。

### lxml与XPath
- XPath是一门用于在XML文档中查找信息的语言，可以在XML文档中查找元素和属性。
- XPath的常用路径表达式：
    - // 表示从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
    - / 表示从根节点选取
    - . 表示选取当前节点
    - .. 表示选取当前节点的父节点
    - @ 表示选取属性
- https://www.w3school.com.cn/xpath/index.asp
- lxml是python语言用来处理XML和HTML的功能丰富、使用方便的第三方库。https://lxml.de/

### Scrapy

- 官方文档：https://docs.scrapy.org/en/latest/topics/architecture.html
- Scrapy是一个成熟的爬虫框架，包括engine、scheduler、spider、downloader、item pipelines、spider middleware、downloader middleware七个部分，其中engine负责控制数据流向，scheduler负责接收engine的request并进行调度，downloader负责从互联网发起请求获得页面，spider负责对页面进行解析获得需要的信息，item pipelines负责处理spider解析后的数据。
- 用法

1. 创建项目，`scrapy startproject {project_name}`
2. 进入项目`cd {project_name}`，新建爬虫`scrapy genspider {spider_name} {spider_domain}`
3. 编写items.py，定义需要的数据字段
4. 编写spiders/{project_name}.py，编写页面解析方法
5. 编写pipeline.py，处理解析后的数据
6. 运行爬虫`scrapy crawl {spider_name}`