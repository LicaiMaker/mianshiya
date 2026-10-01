# 前端面试题集 - 2026-10-01

> 覆盖 12 个前端技术方向，每个方向 2 道题。

---

## 一、HTML

### 1. 什么是语义化 HTML？为什么要使用语义化标签？
- **参考答案要点**：语义化是指使用恰当的 HTML 标签描述内容含义（如 `<header>`、`<nav>`、`<article>`、`<section>`、`<footer>` 等），而不是一堆无意义的 `<div>`。优点：提升可读性与可维护性；有利于 SEO；便于无障碍阅读器解析；代码结构更清晰，便于团队协作。

### 2. `<script>` 标签中的 `defer` 和 `async` 有什么区别？
- **参考答案要点**：两者都不会阻塞 HTML 解析。
  - `async`：脚本下载完成后立即执行，执行时机不确定，可能在 DOMContentLoaded 之前或之后，且多个 async 脚本执行顺序不保证。
  - `defer`：脚本下载完成后会等待 HTML 解析完成，在 DOMContentLoaded 之前按顺序执行，适合需要操作 DOM 或依赖顺序的场景。

---

## 二、CSS

### 1. 说说 CSS 盒模型，以及标准盒模型和 IE 盒模型的区别
- **参考答案要点**：`box-sizing` 控制盒模型。
  - `content-box`（标准/W3C）：width 仅指内容区，元素总宽度 = content + padding + border。
  - `border-box`（IE）：width 包含 content + padding + border，布局更可控，推荐使用。

### 2. CSS 选择器优先级是如何计算的？
- **参考答案要点**：优先级（特异性）从高到低：`!important` > 内联样式 > ID 选择器 > 类/属性/伪类选择器 > 元素/伪元素选择器 > 通配符/继承。
- 可用 (a, b, c, d) 四元组理解：内联为 a；ID 为 b；类/伪类/属性为 c；元素/伪元素为 d。逐位比较，!important 优先级最高但应避免滥用。

---

## 三、JavaScript

### 1. 什么是闭包？闭包有哪些应用场景？
- **参考答案要点**：闭包是指有权访问另一个函数作用域中变量的函数。常见应用：
  - 函数封装与私有变量；
  - 防抖/节流；
  - 函数柯布化、偏函数；
  - 模块化（IIFE）；
  - 在循环中保存变量（如经典 `for var` 问题用闭包或 `let` 解决）。

### 2. 说说原型与原型链的理解
- **参考答案要点**：每个对象都有 `__proto__`，指向其构造函数的 `prototype`；函数有 `prototype` 属性用于挂载共享方法。访问属性时，沿 `__proto__` 向上查找形成的链就是原型链，末端为 `Object.prototype.__proto__ === null`。常考 `instanceof` 原理、构造函数与原型方法的区别。

### 3. ES6 箭头函数与普通函数的区别
- **参考答案要点**：
  - 箭头函数无自己的 `this`，继承外层作用域的 `this`；
  - 不能作为构造函数（无 `prototype`，不能 `new`）；
  - 没有 `arguments` 对象；
  - 不能用作 Generator；
  - 不能通过 `call/apply/bind` 改变 `this`。

### 4. 简述 JavaScript 事件循环（Event Loop）机制
- **参考答案要点**：JS 是单线程，通过事件循环调度异步任务。任务分为宏任务（script、setTimeout、setInterval、I/O、UI 渲染）和微任务（Promise.then、queueMicrotask、MutationObserver）。执行规则：每个宏任务结束后清空微任务队列，再执行下一个宏任务；微任务优先级高于宏任务。

---

## 四、TypeScript

### 1. TypeScript 中 `interface` 和 `type` 有什么区别？
- **参考答案要点**：
  - `interface` 专注对象/类结构，可 `extends`、可重复声明合并；
  - `type` 更通用，可表示联合、交叉、原始类型、函数签名、元组等，使用 `&` 交叉；
  - 写法上：`type A = { a: string }`，`interface A { a: string }`；
  - 一般对象类型倾向用 `interface`，联合/工具类型/函数重载时用 `type`。

### 2. 什么是泛型？泛型有什么好处？
- **参考答案要点**：泛型允许在定义函数、接口、类时不指定具体类型，使用时再传入，从而获得类型复用 + 类型安全。例如 `function identity<T>(arg: T): T`，可避免使用 `any` 导致的类型丢失。常结合约束使用：`<T extends { length: number }>` 限制传入类型。

---

## 五、Vue

### 1. Vue 2 与 Vue 3 的响应式原理分别是什么？
- **参考答案要点**：
  - Vue 2：通过 `Object.defineProperty` 劫持对象属性的 getter/setter，无法监听新增/删除属性（需 `Vue.set`/`Vue.delete`），数组通过重写方法实现。
  - Vue 3：使用 ES6 `Proxy` 代理整个对象，能监听新增/删除、`in` 操作符等，性能更好。

### 2. Vue 中 `v-if` 和 `v-show` 的区别？分别在什么场景使用？
- **参考答案要点**：
  - `v-if` 是真正的条件渲染，惰性渲染，切换时会销毁/重建组件，适合不频繁切换的场景；
  - `v-show` 只是切换 `display`，元素始终保留在 DOM 中，适合频繁切换的场景（如 Tab 切换）。

---

## 六、React

### 1. React Hooks 是什么？为什么要使用 Hooks？
- **参考答案要点**：Hooks 是 React 16.8 引入的特性，让函数组件可以使用 state、生命周期等能力（如 `useState`、`useEffect`、`useMemo`、`useCallback`、`useRef`、`useContext` 等）。优势：
  - 告别 class 组件的 this、生命周期繁琐；
  - 逻辑复用更方便（自定义 Hook）；
  - 代码更扁平、可读性更高。

### 2. React 受控组件和非受控组件有什么区别？
- **参考答案要点**：
  - 受控组件：表单数据由 React state 完全控制，每次输入都触发 `onChange` 更新 state（如 `<input value={v} onChange={...}>`）。
  - 非受控组件：通过 `ref` 直接读取 DOM 值（`defaultValue`），状态由 DOM 维护，更像传统 HTML。
  - 受控更易做校验、联动；非受控性能开销小、集成第三方 DOM 库更方便。

---

## 七、Node.js

### 1. Node.js 的事件循环和浏览器的事件循环有什么区别？
- **参考答案要点**：
  - 浏览器事件循环基于宏任务与微任务，渲染在宏任务之间进行。
  - Node（libuv）使用 6 个阶段：timers → pending callbacks → idle/prepare → poll → check → close callbacks；每个阶段执行宏任务，阶段间清空微任务（process.nextTick 优先于 Promise 微任务）。
  - Node 中 `setImmediate` 与 `setTimeout(fn, 0)` 在不同场景执行顺序不同（poll 阶段区分）。

### 2. 什么是中间件？在 Express/Koa 中是如何实现的？
- **参考答案要点**：中间件是处理请求/响应的函数，可串联形成处理链。
  - Express：基于回调的洋葱模型，`next()` 决定是否进入下一层（不完全是洋葱）。
  - Koa：基于 `async/await` 的真正洋葱模型，`await next()` 后代码会在下层中间件返回后再执行，便于统一收尾（如异常处理、性能统计）。

---

## 八、前端工程化

### 1. Webpack 和 Vite 的区别？
- **参考答案要点**：
  - Webpack：打包思路，启动时进行全量模块编译构建，启动慢但生态成熟。
  - Vite：基于原生 ES Module + esbuild 预构建依赖 + Rollup 打包；开发期按需加载，启动极快，HMR 几乎无延迟。生产构建底层仍是 Rollup。
  - 选择：现代项目、追求开发体验选 Vite；老项目、复杂兼容性/插件生态选 Webpack。

### 2. 什么是 Tree Shaking？它的实现原理是什么？
- **参考答案要点**：Tree Shaking 是消除未被引用（dead code）模块/导出的优化。原理：
  - 基于 ES Module 的静态结构（`import/export`）进行依赖分析；
  - 配合 `sideEffects: false` 在 package.json 声明无副作用；
  - 生产环境使用 minifier（如 Terser/esbuild）删除未使用代码。
  - CommonJS 无法做 Tree Shaking，因此需用 ESM。

---

## 九、计算机网络

### 1. HTTP 和 HTTPS 的区别？
- **参考答案要点**：
  - HTTPS = HTTP + TLS/SSL，在传输前进行加密握手；
  - HTTPS 默认 443，需 CA 证书，有加密、完整性校验、身份认证；
  - HTTP 明文传输，端口 80，已逐步被现代浏览器标记为不安全；
  - HTTPS 比 HTTP 多一次 TLS 握手（RTT），可结合 TLS 1.3、Session Resumption、0-RTT 优化。

### 2. 简述 TCP 三次握手和四次挥手
- **参考答案要点**：
  - 三次握手：客户端发送 SYN → 服务端回复 SYN+ACK → 客户端发送 ACK，建立可靠连接。
  - 四次挥手：主动方发送 FIN → 被动方 ACK → 被动方发送 FIN → 主动方 ACK，等待 2MSL 后关闭。
  - 挥手比握手多一次的原因：服务端收到 FIN 后可能还有数据要传，需先 ACK 再发 FIN。

---

## 十、浏览器与性能优化

### 1. 从输入 URL 到页面渲染完成，浏览器经历了哪些过程？
- **参考答案要点**（关键链路）：
  1. URL 解析；
  2. DNS 解析（域名 → IP）；
  3. TCP 连接（三次握手）；
  4. TLS 握手（HTTPS）；
  5. 发送 HTTP 请求；
  6. 服务器响应（状态码、首部、Body）；
  7. 解析 HTML 构建 DOM Tree；
  8. 解析 CSS 构建 CSSOM；
  10. 合成 Render Tree → Layout（回流） → Paint（重绘） → Composite（合成）；
  11. JS 加载/执行可能阻塞 DOM 构建。

### 2. 前端常见的性能优化手段有哪些？
- **参考答案要点**：
  - 资源层面：合并/压缩、雪碧图、WebP/AVIF、CDN、HTTP 缓存（强缓存/协商缓存）、Service Worker 离线缓存；
  - 加载层面：路由/组件懒加载、preload/prefetch、代码分割、Tree Shaking；
  - 渲染层面：减少回流重绘（避免逐行修改样式、虚拟 DOM、Fragment）、CSS 放头部、JS 放底部、`defer/async`；
  - 运行时：节流防抖、虚拟列表、Web Worker、长列表冻结、图片懒加载、骨架屏；
  - 监控：Lighthouse、Performance API、FCP/LCP/CLS/INP 等 Core Web Vitals。

---

## 十一、数据结构与算法

### 1. 快速排序的时间复杂度和空间复杂度分别是多少？最坏情况下如何优化？
- **参考答案要点**：
  - 平均时间 O(nlogn)，最坏 O(n²)（有序数组且基准选首尾）；
  - 空间复杂度：原地排序 O(logn)（递归栈），非原地 O(n)；
  - 优化：
    - 随机选基准或三数取中；
    - 小区间切换插入排序；
    - 尾递归优化；
    - 双轴快排（V8 Sort 的快排变种）。

### 2. 说说防抖（debounce）和节流（throttle）的区别，并手写实现思路
- **参考答案要点**：
  - 防抖：连续触发只执行最后一次（停止触发 n ms 后执行），适合搜索输入、resize。
  - 节流：在一定时间窗口内最多执行一次（立即执行或尾部执行），适合 scroll、mousemove、点击防重。
  - 实现核心：利用闭包 + `setTimeout` + 时间戳/定时器混合版本（leading + trailing）。

---

## 十二、设计模式

### 1. 什么是发布订阅模式？在前端哪些场景应用过？
- **参考答案要点**：发布订阅模式（Pub/Sub）由调度中心维护事件频道，发布者向频道发送事件，订阅者从频道订阅事件，发布者和订阅者解耦。前端应用：
  - `EventTarget` / `addEventListener`；
  - Vue 的 `$on/$off/$emit`；
  - Node 的 `EventEmitter`；
  - 跨组件通信（mitt、tiny-emitter）、WebSocket 消息分发。

### 2. 观察者模式和发布订阅模式有什么区别？
- **参考答案要点**：
  - 观察者模式（Observer）：观察者直接订阅目标（Subject），目标维护观察者列表，状态变化时主动通知观察者（如 Vue 的响应式 watch 机制）。
  - 发布订阅模式：引入第三方调度中心（Event Bus），发布者和订阅者互不感知对方，仅通过事件频道通信，解耦更彻底。
  - 简言之：观察者是一对多强耦合，发布订阅是多对多松耦合。

---

## 今日小结
- 共 12 个方向、20 道题，覆盖 HTML/CSS/JS/TS/Vue/React/Node/工程化/网络/浏览器/算法/设计模式。
- 建议按顺序自测：先答思路 → 再写代码 → 最后对照参考答案查漏。
- 明日计划：聚焦「性能优化 + 微前端 + 工程化（CI/CD、Monorepo）」深挖。