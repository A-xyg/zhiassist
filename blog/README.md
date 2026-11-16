# ZhiAssist Blog

基于 VitePress 1.6.4 的项目文档站。

## 环境基线

- Node.js 22（根目录 `.nvmrc`）
- pnpm 12.21.0（`package.json` 的 `packageManager`）
- VitePress 1.6.4

## 运行命令

```bash
# 安装依赖（首次或 lock 变更后）
pnpm install

# 本地开发，热更新预览
pnpm docs:dev

# 生产构建，产物在 docs/.vitepress/dist（不提交）
pnpm docs:build

# 本地预览构建产物
pnpm docs:preview
```

## 标准更新流程（新增一篇文章）

1. 在 `docs/chapters/` 新建 `chXX-slug.md`。
2. 文件顶部写好 frontmatter：`title`、`date`、`tags`、`excerpt`。
3. 配图放入 `docs/public/images/`（webp），正文以 `/images/xxx.webp` 引用。
4. 在 `docs/.vitepress/config.mts` 的 `sidebar`（必要时 `nav`）中挂上链接。
5. 本地 `pnpm docs:dev` 确认排版、标签与归档页正常。
6. 提交时务必带上更新后的 `pnpm-lock.yaml`；`dist/`、`cache/`、`node_modules/` 不提交。

## 自定义域名

- 默认 GitHub Pages 项目页无需 `public/CNAME`；若绑定自定义域名，把该文件里的示例域名改成真实域名，未绑定时删除本文件。
