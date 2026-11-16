// 从 vitepress 引入配置助手；它提供类型提示，写错字段会直接报错
import { defineConfig } from 'vitepress'

// defineConfig 的参数就是整站配置；改动后需要重新 pnpm docs:build
export default defineConfig({
  // 站点标题：浏览器标签页后缀、导航栏左侧文字、SEO 标题都会用到
  title: '知答 ZhiAssist · 实战笔记',

  // 站点描述：写进 <meta name="description">，是搜索结果里那段摘要
  description: '从零上线一个可访问、可评测、可写进简历的行业知识库客服 Agent',

  // 语言标记：影响 <html lang>，也影响内置 UI（如「上一篇」）的默认文案
  lang: 'zh-CN',

  // 【关键】GitHub Pages 项目页挂在 /仓库名/ 下，资源 URL 必须带这个前缀
  // 换自定义域名或 Vercel 根路径时改成 '/'，同时把 public/CNAME 一并处理
  base: '/zhiassist/',

  // 生成 sitemap.xml；hostname 必须是最终对外可访问的完整地址（含 base）
  // 上线前把 your-name 替换为真实 GitHub 用户名 / 自定义域名
  sitemap: {
    hostname: 'https://A-xyg.github.io/zhiassist/'
  },

  // 让页面底部显示「最后更新于」，时间取自 Git 提交时间
  lastUpdated: true,

  // 不要开 cleanUrls：GitHub Pages 不会把 /path 回退到 /path.html
  // cleanUrls: true,

  // Markdown 配置：lineNumbers 打开代码块行号；高亮由内置 Shiki 完成
  markdown: {
    lineNumbers: true
  },

  // 追加到 <head> 的标签：图标 + SEO / 社交分享元信息
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['meta', { name: 'keywords', content: 'AI Agent, RAG, LangGraph, 实战笔记' }],
    ['meta', { property: 'og:title', content: '知答 ZhiAssist · 实战笔记' }],
    ['meta', { property: 'og:description', content: '15 章从空仓库到上线的 Agent 实战记录' }],
    ['meta', { name: 'viewport', content: 'width=device-width, initial-scale=1.0' }]
  ],

  themeConfig: {
    // 顶部导航：对应手册要求的三个栏目 + 归档
    nav: [
      { text: '首页', link: '/' },
      { text: '文章', link: '/chapters/ch01-environment' },
      { text: '归档', link: '/archives' },
      { text: '项目展示', link: '/projects/' },
      { text: '关于我', link: '/about' }
    ],

    // 侧边栏：以 '/' 开头、相对 docs/ 根、不带 .md 后缀
    sidebar: [
      {
        text: '第一篇 · 工程底座',
        items: [
          { text: '第 1 章 环境搭建复盘', link: '/chapters/ch01-environment' }
        ]
      }
    ],

    // 内置本地搜索（免费、无需第三方服务）；中文分词限制见 P9
    search: { provider: 'local' },

    // 右侧本页目录只收 h2/h3，避免长文目录过长
    outline: { level: [2, 3], label: '本页目录' },

    // 中文化上下篇与更新时间文案
    docFooter: { prev: '上一篇', next: '下一篇' },
    lastUpdated: { text: '最后更新于' },

    // 「在 GitHub 上编辑此页」：:path 会被替换成当前文件相对路径
    editLink: {
      pattern: 'https://github.com/A-xyg/zhiassist/edit/main/blog/docs/:path',
      text: '在 GitHub 上编辑此页'
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/A-xyg/zhiassist' }
    ]
  }
})