---
title: 文章归档
description: 按标签筛选与分页浏览全部实战复盘文章
---

# 文章归档

<script setup>
// Vue 的响应式原语：ref 存可变值，computed 存由它派生出的值
import { ref, computed } from 'vue'
// withBase：给站内路径自动加上 config.mts 里配置的 base，避免自定义域名时 404
import { withBase } from 'vitepress'
// 构建期生成的文章数据：数组，每项含 url / frontmatter / excerpt
import { data as posts } from './posts.data'

const pageSize = 5                 // 每页显示几篇，文章多了可改小
const page = ref(1)                // 当前页码
const activeTag = ref('全部')       // 当前选中的标签

// 从所有文章的 tags 字段里汇总出去重后的标签列表
const tags = computed(() => [
  '全部',
  ...new Set(posts.flatMap((p) => p.frontmatter.tags || []))
])

// 按标签过滤；选「全部」时不过滤
const filtered = computed(() =>
  activeTag.value === '全部'
    ? posts
    : posts.filter((p) => (p.frontmatter.tags || []).includes(activeTag.value))
)

// 总页数至少为 1，避免空列表出现 0 页
const totalPages = computed(() => Math.max(1, Math.ceil(filtered.value.length / pageSize)))

// 当前页要显示的文章切片
const shown = computed(() =>
  filtered.value.slice((page.value - 1) * pageSize, page.value * pageSize)
)

// 切换标签时把页码重置为 1，否则可能停在不存在的页上
function pick(tag) {
  activeTag.value = tag
  page.value = 1
}
</script>

<div class="tag-bar">
  <button v-for="t in tags" :key="t" @click="pick(t)" :class="{ active: activeTag === t }">
    {{ t }}
  </button>
</div>

<ul>
  <li v-for="p in shown" :key="p.url">
    <a :href="withBase(p.url)">{{ p.frontmatter.title }}</a>
    <span> · {{ p.frontmatter.date }} · {{ (p.frontmatter.tags || []).join(' / ') }} · {{ p.frontmatter.category }}</span>
  </li>
</ul>

<div class="pager">
  <button :disabled="page === 1" @click="page--">上一页</button>
  <span>第 {{ page }} / {{ totalPages }} 页，共 {{ filtered.length }} 篇</span>
  <button :disabled="page === totalPages" @click="page++">下一页</button>
</div>