// 引入VitePress的默认主题： 它提供导航、侧边栏、搜索、阴暗切换等全部基础功能UI
import DefaultTheme from 'vitepress/theme'
// 引入自定义 CSS：Vitepress 会在构建时把它打包进产物
import './custom.css'

export default {
  extends: DefaultTheme,
}
