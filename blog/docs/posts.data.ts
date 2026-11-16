// createContentLoader：构建期扫描 Markdown，产出可被引用的静态数据
import { createContentLoader } from 'vitepress'

// 只扫描 chapters/ 下的一级 Markdown；参数一是相对 docs/ 的 glob
export default createContentLoader('chapters/*.md', {
  // 生成摘要字段（文章里可用  控制截断位置）
  excerpt: true,
  // transform 在构建期执行，返回的数据就是归档页 import 到的 data
  transform(raw) {
    return raw
      // 过滤草稿：Front-matter 里 draft: true 的文章不会出现在归档和 sitemap
      .filter((post) => post.frontmatter.draft !== true)
      // 按日期倒序，新文章排前面；缺 date 的排最后
      .sort((a, b) =>
        String(b.frontmatter.date ?? '').localeCompare(String(a.frontmatter.date ?? ''))
      )
  }
})