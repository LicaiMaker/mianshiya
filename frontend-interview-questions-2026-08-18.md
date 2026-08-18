# 前端每日面试题（2026-08-18）

> 出题参考：仓库 `mianshiya` 标签体系（前端、html、css、javascript、typescript、nodejs、vue、angular）+ 主流大厂面试题库。每天按方向轮换出题，每个方向 2 道以上。

---

## 一、HTML

**1. 请说一下 `<script>` 标签的 `defer` 和 `async` 属性有什么区别？它们的执行顺序是怎样的？**

- 关键点：阻塞渲染、`DOMContentLoaded` 前后、多个脚本执行顺序。
- 参考：默认 `<script>` 同步加载并阻塞解析；`defer` 并行下载，DOM 解析完、`DOMContentLoaded` 之前按顺序执行；`async` 下载完立即执行，不保证顺序，谁先下载完谁先执行。
- 追问：动态插入的 `<script>` 默认行为是什么？`type="module"` 时表现？

**2. 什么是 DOM？什么是虚拟 DOM？为什么要用虚拟 DOM？**

- 关键点：DOM 树结构、虚拟 DOM 是 JS 对象、diff 算法、跨平台。
- 追问：虚拟 DOM 一定比直接操作 DOM 快吗？什么情况下反而更慢？

**3. 简述 HTML5 语义化标签及其优势。**

- `<header>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<aside>`、`<footer>` 等。
- 优势：可读性、SEO、可访问性、利于爬虫解析。

---

## 二、CSS 基础与布局

**1. 说一下 BFC（块级格式化上下文）是什么？触发条件有哪些？常见的应用场景是什么？**

- 触发：`overflow: hidden`、`display: flex/grid/inline-block`、`position: absolute/fixed`、浮动元素等。
- 应用：清除浮动、解决 margin 合并、实现自适应两栏布局。

**2. Flex 布局中 `flex: 1` 等价于什么？`flex-basis`、`flex-grow`、`flex-shrink` 三个属性的作用分别是什么？**

- `flex: 1` = `flex: 1 1 0%`。
- `flex-grow`：放大比例；`flex-shrink`：缩小比例；`flex-basis`：主轴初始大小。

**3. Grid 布局中如何实现一个九宫格？`grid-template-columns: repeat(auto-fit, minmax(200px, 1fr))` 含义？**

- auto-fit + minmax 实现响应式网格。
- 追问：与 `auto-fill` 的区别？

---

## 三、CSS 进阶

**1. 说一下 CSS 盒模型，`box-sizing` 的 `content-box` 和 `border-box` 区别？哪种更常用？**

- 标准 vs IE 盒模型；移动端/组件库多采用 `border-box`。

**2. 如何实现一个元素水平垂直居中？至少说出 5 种方案。**

- flex/grid 居中、`position + transform`、`position + margin: auto`、`line-height`、`table-cell`、`absolute calc`。

**3. 什么是 CSS 硬件加速？`transform: translateZ(0)` 和 `will-change` 的作用和副作用？**

- 触发 GPU 合成层、避免重绘；副作用：内存占用、层爆炸。

---

## 四、JavaScript 基础

**1. `typeof` 和 `instanceof` 的区别？`typeof null` 的结果是什么？**

- `typeof`：基本类型判断；`instanceof`：原型链判断。
- `typeof null === 'object'` 是历史 bug。

**2. `==` 和 `===` 的区别？`[] == ![]` 的结果是？**

- `[] == ![]` → `'' == false` → `0 == 0` → `true`。
- 追问：`null == undefined`？

**3. 什么是事件冒泡和事件捕获？`event.target` 和 `event.currentTarget` 的区别？**

- 第三个参数 `useCapture` / `addEventListener` 第三参数控制阶段。
- 追问：什么是事件委托？有什么好处？

---

## 五、JavaScript 进阶

**1. 说一下闭包。闭包有哪些应用场景和副作用？**

- 应用：数据封装、函数柯里化、防抖节流；副作用：内存泄漏。
- 追问：怎么排查闭包导致的内存泄漏？

**2. 说一下 JavaScript 的原型链。构造函数、`prototype`、`__proto__` 三者关系？**

- 实例 → `__proto__` → 构造函数的 `prototype` → `Object.prototype` → `null`。
- 追问：`new` 做了哪几件事？

**3. 说说 `this` 的指向规则（普通函数、箭头函数、call/apply/bind、new）。**

- 箭头函数没有自己的 `this`，继承外层。
- 追问：`call`、`apply`、`bind` 的区别和手写实现。

---

## 六、ES6+ 新特性

**1. 说说 `let`、`const`、`var` 的区别。暂时性死区（TDZ）是什么？**

- 块级作用域、不能重复声明、TDZ。

**2. `Promise` 的三种状态是什么？`then` 返回的新 Promise 状态由什么决定？**

- pending / fulfilled / rejected；返回值决定下一个 Promise 状态。
- 追问：如何手写一个 `Promise.all` 和 `Promise.race`？

**3. 什么是 `async/await`？它和 `Promise` 的关系？错误如何捕获？**

- 本质是 `Generator` + `Promise` 的语法糖；用 `try/catch`。

**4. 说说 `Map`、`Set`、`WeakMap`、`WeakSet` 的区别和使用场景。**

- 弱引用场景：避免内存泄漏（如 Vue 3 的响应式 targetMap）。

---

## 七、TypeScript

**1. TypeScript 中 `interface` 和 `type` 的区别？什么情况下用哪个？**

- `type` 支持联合、交叉、计算属性；`interface` 支持声明合并、自动合并。
- 追问：同名 interface 合并、type 重复会报错。

**2. 什么是泛型？手写一个 `Pick<T, K extends keyof T>`。**

- 关键点：类型参数、约束、映射类型。
- 追问：什么是 `infer`？手写 `ReturnType<T>`。

**3. `any`、`unknown`、`never` 三者的区别？**

- `any` 绕过类型检查；`unknown` 安全未知（使用前需断言）；`never` 表示永不存在（如抛错函数）。

---

## 八、异步与事件循环

**1. 浏览器的事件循环（Event Loop）执行顺序是怎样的？宏任务和微任务分别有哪些？**

- 先清空微任务队列（Promise.then、queueMicrotask、MutationObserver）再取下一个宏任务（setTimeout、setInterval、I/O、UI 渲染）。
- 追问：`async/await` 在事件循环中如何执行？

**2. `setTimeout(fn, 0)` 真的是 0ms 执行吗？最小延迟是多少？**

- 受嵌套层级限制，浏览器最小 4ms，HTML5 规范定义。

**3. 什么是 `requestAnimationFrame`？和 `setTimeout` 的区别？**

- 跟随浏览器刷新率（一般 60Hz），回调在重绘前执行；tab 隐藏时不执行。

---

## 九、浏览器原理

**1. 从输入 URL 到页面展示，浏览器经历了哪些过程？**

- URL 解析 → DNS 解析 → TCP 三次握手 → TLS 握手 → HTTP 请求 → 响应 → 解析 HTML（构建 DOM 树）→ 解析 CSS（构建 CSSOM）→ 合成渲染树 → Layout → Paint → Composite。

**2. 浏览器渲染流水线中，重排（reflow）、重绘（repaint）、合成（composite）分别是什么？怎么避免？**

- 重排代价最大（layout 重新计算）；重绘：颜色/背景等；合成只动 transform/opacity 不重排重绘。
- 追问：什么属性会触发 GPU 加速？

**3. 什么是浏览器的同源策略？跨域解决方案有哪些？**

- JSONP、CORS、nginx 反向代理、postMessage、WebSocket、document.domain。
- 追问：CORS 预检（OPTIONS）什么时候触发？哪些请求会触发？

---

## 十、网络协议

**1. HTTP 和 HTTPS 的区别？TLS 握手过程是怎样的？**

- HTTPS = HTTP + TLS；TLS 1.2 四次握手（Client Hello、Server Hello、证书验证、密钥交换）；TLS 1.3 三次握手。

**2. HTTP 常见状态码：`301`、`302`、`304`、`401`、`403`、`404`、`500`、`502`、`503` 的含义和区别？**

- 301 永久重定向（缓存），302 临时；304 协商缓存命中；502 上游错误，503 服务不可用。

**3. 强缓存和协商缓存的区别？`Cache-Control`、`ETag`、`Last-Modified` 优先级？**

- `Cache-Control` 优先级最高（`max-age`），`ETag` 比 `Last-Modified` 精确（解决秒级问题）。

**4. TCP 三次握手和四次挥手？为什么是三次不是两次？**

- 防止已失效的连接请求突然传到服务器导致错误。
- 追问：TIME_WAIT 状态为什么是 2MSL？

---

## 十一、前端安全

**1. 什么是 XSS？怎么防御？**

- 存储型、反射型、DOM 型。
- 防御：输入过滤、输出转义、CSP、HttpOnly Cookie。

**2. 什么是 CSRF？怎么防御？**

- 利用用户登录态发起跨站请求。
- 防御：SameSite Cookie、Token 验证、Referer 校验、验证码。

**3. 点击劫持（Clickjacking）的原理和防御？**

- iframe 嵌套 + 透明层；X-Frame-Options、CSP frame-ancestors。

---

## 十二、性能优化

**1. 前端性能优化从哪些方面入手？**

- 网络层：CDN、gzip/brotli、HTTP/2、HTTP/3、缓存、预加载/预连接、懒加载。
- 渲染层：减少重排重绘、虚拟列表、requestIdleCallback、SSR/SSG。
- 资源层：Tree Shaking、Code Splitting、压缩、字体子集化、WebP。

**2. 首屏加载慢怎么排查？常用工具和方法？**

- Chrome DevTools Performance / Lighthouse / WebPageTest；Long Task、长任务、FMP/LCP/CLS 指标。
- 追问：FCP、LCP、CLS、INP 分别衡量什么？

**3. 什么是虚拟列表？为什么能提升长列表性能？**

- 只渲染视口内的 DOM；减少 DOM 数量、避免重排重绘。
- 追问：如何实现不定高度的虚拟列表？

---

## 十三、React

**1. React 中 `useState` 的更新是同步还是异步？连续多次 `setState` 怎么合并？**

- 在 React 18 之前是异步批处理；之后所有更新自动批处理。
- 追问：React 18 的 `useTransition` 和 `useDeferredValue` 解决了什么问题？

**2. 说说 React 的 Diff 算法（调和算法）。key 的作用？为什么不推荐用 index 作为 key？**

- 同层比较、类型不同直接卸载重建、key 复用。
- index 作为 key 在列表重排时会导致组件状态错乱、输入框内容串位。

**3. React 中 `useEffect` 和 `useLayoutEffect` 的区别？**

- `useEffect` 异步执行（paint 之后）；`useLayoutEffect` 同步执行（DOM 更新后、paint 前），用于读 DOM 避免闪烁。

**4. React Fiber 是什么？解决了什么问题？**

- 增量协调（可中断渲染）；解决栈式调和无法中断、长时间占用主线程的问题。
- 追问：时间分片（Time Slicing）和优先级调度（Scheduler）？

**5. 类组件和函数组件的区别？Hooks 解决了什么问题？**

- 复用逻辑、避免 HOC / render props 的地狱；逻辑更聚合。

---

## 十四、Vue

**1. Vue 2 和 Vue 3 的响应式原理有什么区别？**

- Vue 2：`Object.defineProperty` 劫持 getter/setter，无法监听新增/删除属性、数组需要重写方法。
- Vue 3：`Proxy` 全代理、Reflect 操作。

**2. Vue 3 的 Composition API 相比 Options API 的优势？**

- 逻辑复用、TS 友好、按需引入、性能（tree shaking）。

**3. 说说 Vue 的 `nextTick` 原理和使用场景。**

- 异步队列（Promise.then / MutationObserver / setImmediate / setTimeout）。
- 使用：在数据变化后获取更新后的 DOM。

**4. Vue 中 `v-if` 和 `v-show` 的区别？`v-for` 和 `v-if` 为什么不建议一起用？**

- `v-if` 真正的条件渲染（销毁/创建组件）；`v-show` 仅切 display。
- `v-if` 优先级低于 `v-for`，会在每次循环都判断；Vue 3 中 `v-if` 优先级更高。

**5. Vue 的 diff 算法和 React 有什么不同？**

- Vue 静态标记（patchFlag）优化、模板编译期分析。

---

## 十五、状态管理

**1. Redux 的三大原则是什么？中间件机制是怎么实现的？**

- 单一数据源、State 只读、纯函数修改。
- 中间件：洋葱模型 `compose` 串联。

**2. Pinia 相比 Vuex 的优势？**

- 去 mutation、完整 TS 支持、模块化更轻。

**3. MobX 和 Redux 的核心思想差异？**

- MobX：响应式 + 面向对象；Redux：函数式 + 不可变数据。

---

## 十六、前端工程化（Webpack / Vite）

**1. Webpack 的构建流程是怎样的？**

- 初始化 → 解析入口 → loader 编译 → 收集依赖 → 递归构建依赖图 → 输出 chunk → 输出资源。
- 追问：Loader 和 Plugin 的区别？

**2. Vite 为什么比 Webpack 快？开发环境和生产环境分别做了什么？**

- 开发：基于浏览器原生 ESM，按需编译（esbuild 预构建依赖）。
- 生产：Rollup 打包 + esbuild 压缩。

**3. 什么是 Tree Shaking？需要满足什么条件才能生效？**

- 静态分析 + 副作用（sideEffects）声明 + ES Module。

**4. 常见的 Loader 和 Plugin：**

- Loader：`babel-loader`、`css-loader`、`style-loader`、`file-loader`、`url-loader`、`vue-loader`。
- Plugin：`HtmlWebpackPlugin`、`MiniCssExtractPlugin`、`DefinePlugin`、`CleanWebpackPlugin`、`SplitChunksPlugin`。

---

## 十七、Node.js

**1. Node.js 的事件循环和浏览器有什么区别？**

- Node 有 6 个阶段（timers、pending callbacks、idle/prepare、poll、check、close callbacks）；`process.nextTick` 和 `Promise` 微任务在每个阶段后清空。

**2. 什么是中间件？Express 和 Koa 的中间件模型区别？**

- Koa 用 async/await 洋葱模型，Express 基于回调（next()）。
- 追问：Koa 的 `ctx` 是什么？

**3. 什么是流（Stream）？什么场景下使用？**

- 大文件读写、网络传输、内存友好。
- 追问：Readable / Writable / Transform / Duplex 区别？

**4. 说说 `EventEmitter` 原理和手写实现。**

- 维护事件 → 回调映射列表；`on` 注册、`emit` 触发。

---

## 十八、数据结构与算法

**1. 实现一个防抖（debounce）和节流（throttle）函数，并说明区别。**

- 防抖：多次触发只执行最后一次（搜索框）。
- 节流：固定时间执行一次（滚动事件）。

**2. 数组去重至少 3 种方式，以及时间复杂度。**

- Set、indexOf、双重循环、对象 key、排序后相邻比较。

**3. 写一个深拷贝函数。需要考虑哪些边界？**

- 循环引用、Date / RegExp / Map / Set、函数、原型链。
- 追问：`structuredClone` 的局限性？

**4. 二分查找的边界条件。**

- `left <= right` 还是 `left < right`？返回什么？

**5. 说说常见排序（冒泡、插入、归并、快排）的时间复杂度和稳定性。**

- 归并/插入稳定，快排不稳定。

---

## 十九、设计模式

**1. 单例模式在前端的应用？**

- 全局弹窗、Store、缓存管理器；ES6 Module 天然单例。
- 追问：如何实现惰性单例？

**2. 观察者模式和发布订阅模式的区别？**

- 观察者：直接订阅；发布订阅：通过事件中心解耦（Vue EventBus、Node EventEmitter）。

**3. 工厂模式、策略模式、装饰器模式各举一个前端例子。**

- 工厂：React `createElement`；策略：表单校验规则；装饰器：TS / Babel 装饰器、AOP 增强。

---

## 二十、移动端 / H5

**1. 移动端 1px 边框问题怎么解决？**

- 物理像素与 CSS 像素比 `devicePixelRatio`；`transform: scale(0.5)` + 伪元素 / `box-shadow` / `border-image` / SVG。

**2. 移动端适配方案：rem、vw/vh、rpx 的原理和差异？**

- rem：基于根字体大小，配合 `postcss-pxtorem`。
- vw/vh：视口单位，无 JS 介入。
- rpx：微信小程序专用，750rpx = 屏幕宽。

**3. 移动端点击 300ms 延迟怎么解决？**

- 禁用缩放 `<meta viewport>`、FastClick 库、`touch-action: manipulation`。

**4. H5 唤起 App（Schema / Universal Link）原理？**

- Schema URL scheme + Intent / Universal Links / App Links；降级到应用商店。

---

## 二十一、前端架构 / 微前端

**1. 什么是微前端？常见的微前端方案及对比？**

- qiankun（基于 single-spa）、Module Federation（Webpack 5）、micro-app（基于 Web Components）、wujie。
- 追问：qiankun 的 JS 沙箱和样式隔离怎么实现？

**2. 单页应用（SPA）和多页应用（MPA）的优缺点？**

- SPA：体验流畅，SEO 差，首屏慢。
- MPA：SEO 好，首屏快，切换体验差。

**3. SSR、SSG、ISR 的区别？**

- SSR：服务端渲染（每次请求）；SSG：构建时生成（Next.js `getStaticProps`）；ISR：增量静态再生（Next.js）。

---

## 二十二、跨端与小程序

**1. 微信小程序的双向绑定和 Vue 的双向绑定有什么区别？**

- 小程序 `model:value` 是单向 + 事件回传，并非真正的双向。

**2. 说说 Taro、uni-app、Remax 这类跨端框架的原理。**

- 编译时 + 运行时；将统一 DSL 编译为各端代码（小程序/H5/RN）。

**3. React Native 和 Flutter 的区别？**

- RN：JS Bridge + 原生组件；Flutter：自绘 Skia，无 Bridge，原生性能。

---

## 二十三、测试

**1. 单元测试、集成测试、E2E 测试的区别？**

- 单元：函数/模块；集成：模块协作；E2E：用户场景（Cypress / Playwright）。

**2. Jest 中的 `describe`、`it`、`beforeEach`、`mock` 各自的作用？**

- `mock` 可以 mock 模块、函数、定时器；`jest.fn()` / `jest.spyOn()` / `jest.mock()` 区别。

**3. 什么是测试覆盖率？100% 覆盖能保证零 Bug 吗？**

- 不能，只代表执行过所有路径，无法证明逻辑正确。

---

## 二十四、可访问性 / SEO

**1. 什么是 Web 可访问性（A11y）？常见实践？**

- 屏幕阅读器、键盘导航、`aria-*` 属性、足够的对比度。
- 追问：哪些元素必须有 `alt` / `label`？

**2. 前端做 SEO 的常见方案？**

- 语义化 HTML、SSR / SSG、TDK（Title/Description/Keyword）、canonical、`robots.txt`、sitemap、SSR 注水。

---

## 二十五、存储

**1. `cookie`、`localStorage`、`sessionStorage`、`IndexedDB` 的区别？**

- 大小、有效期、是否随请求发送、是否支持结构化存储。
- 追问：登录态一般存哪里？为什么不推荐 localStorage？

**2. 什么是 `SameSite` Cookie？`Strict`、`Lax`、`None` 区别？**

- CSRF 防御；Chrome 80+ 默认 `Lax`。

**3. 浏览器存储满了怎么办？LRU 策略手写思路？**

- 用 Map 维护访问顺序，超出容量删除最久未使用。

---

## 二十六、进阶编程题（手写）

1. 手写 `Promise.all` / `Promise.allSettled` / `Promise.race`。
2. 手写 `instanceof`。
3. 手写 `new`。
4. 手写 `call` / `apply` / `bind`。
5. 手写深拷贝（处理循环引用、Date、RegExp、Map、Set）。
6. 手写发布订阅模式。
7. 手写防抖 / 节流（含立即执行和取消）。
8. 手写 `EventEmitter`。
9. 手写 JSON.parse。
10. 手写 LRU 缓存。
11. 手写虚拟 DOM 的 diff（按 tag、key 比较）。
12. 实现 `compose` / `pipe` 函数式工具。
13. 手写 Vue3 的 `ref` / `reactive`（核心 reactive + effect + track/trigger）。
14. 实现一个大文件上传 + 断点续传 + 秒传。

---

## 每日出题计划建议

| 日期 | 涉及方向 |
| --- | --- |
| 周一 | JavaScript 基础 + 进阶 + 异步 |
| 周二 | CSS / 浏览器原理 / 性能优化 |
| 周三 | 框架（React / Vue 各 2~3 题） |
| 周四 | 网络 / 安全 / 存储 / 跨域 |
| 周五 | 工程化（Webpack / Vite / CI/CD） |
| 周六 | 算法 + 设计模式 + 手写题 |
| 周日 | 综合 / 架构 / 移动端 / 跨端 / Node |

> 想要我按某一天定向出题、或针对某方向加深难度，可以直接告诉我「今天出 React 进阶 5 题」等。
