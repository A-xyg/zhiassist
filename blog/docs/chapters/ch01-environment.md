---
title: 第 1 章复盘：Windows 上把第一个可访问链接做出来
date: 2026-11-15
category: 工程底座
tags: [环境搭建, Git, CI/CD, 踩坑]
draft: false
description: 记录 corepack EPERM、缺 package.json、点开头文件名无效三个真实问题的定位与修复
---

# 第 1 章复盘：把第一个可访问链接做出来

## 我做了什么

用 VitePress 1.6.4 搭作品集门面，配 GitHub Actions 做到推送即发布到 GitHub Pages。

## 配图示例

下面是本站构建产物目录示意（图片统一放 `docs/public/images/`，用 webp 减小体积）：

![构建产物示意](/images/build-output.webp)

## 代码高亮示例

配置里开了 `markdown.lineNumbers`，代码块会自动带行号并着色：

```python
def build_site() -> str:
    """构建静态站点并返回产物路径。"""
    return "blog/docs/.vitepress/dist"