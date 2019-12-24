# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled":True,
    "repo": "wuyuyang2/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "ACRDIK's"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-24T18:15+08:00"
author = "ACRDIK"
email = "wuyuyang2@qq.com"
author_homepage = "https://wuyuyang2.github.io/Blog-With-GitHub-Boilerplate"
description = "wuyuyang。"
key_words = ['acrdik', 'wyy', '吴禹旸', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "unsplash",
        "url": "https://unsplash.com",
        "brief": "🏄‍ unsplash."
    },
    {
        "name": "百度",
        "url": "https://www.baidu.com",
        "brief": "百度。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "ins",
        "url": "https://instagram.com/wuyuyang2",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/wuyuyang2",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/acrdik/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
