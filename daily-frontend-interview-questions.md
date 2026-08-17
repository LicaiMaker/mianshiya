# 前端每日面试题（2026-08-17）

> 来源参考：本仓库（面试鸭 mianshiya）题库结构 + 前端高频考点。覆盖方向：HTML/CSS、JavaScript 基础、JS 进阶、ES6+、TypeScript、Vue、React、浏览器原理、计算机网络、性能优化、前端安全、工程化、Node.js、设计模式、数据结构与算法、移动端。每方向 ≥2 题。

---

## 一、HTML / CSS

**1. 盒模型有哪两种？它们有什么区别？`box-sizing` 如何切换？**
- `content-box`（W3C 标准盒模型）：`width`/`height` 只包含 content。
- `border-box`（IE 盒模型）：`width`/`height` 包含 content + padding + border。
- 通过 `box-sizing: content-box | border-box` 切换；工程上常全局设为 `border-box`。

**2. 什么是 BFC？触发条件有哪些？常见应用场景是什么？**
- BFC（Block Formatting Context，块级格式化上下文）是一个独立的渲染区域，内部元素的布局不会影响外部。
- 触发条件：`overflow` 不为 visible、`display: flow-root / inline-block / table-cell / flex / grid`、`position: absolute/fixed`、`float` 不为 none 等。
- 应用：清除浮动、避免 margin 合并、实现两栏/三栏自适应布局。

**3. `position: absolute` 的定位基准是什么？`fixed` 一定相对于视口吗？**
- `absolute` 相对于最近的「定位祖先」(`position` 不为 static) 的 padding box。
- `fixed` 正常情况相对视口；当祖先有 `transform`/`perspective`/`filter` 等会创建「包含块」时，会相对该祖先定位（这是常考易错点）。

**4. CSS 优先级如何计算？`!important`、内联、ID、类、伪类、伪元素、标签哪个更高？**
- 优先级：`!important` > 内联样式 > ID > 类/属性/伪类 > 标签/伪元素。
- 同级别后写覆盖前写；可记为四组数 (a, b, c, d) 比较。

**5. 说说 CSS 预处理器（Less/Sass/PostCSS）的核心能力与区别。**
- 变量、嵌套、mixin、函数、模块化、运算。
- Sass 功能最丰富，Less 偏简单，PostCSS 是插件平台（如 autoprefixer、postcss-preset-env）。

---

## 二、JavaScript 基础

**1. 数据类型有哪些？`typeof` 与 `instanceof` 的区别？**
- 基本类型：`number / string / boolean / null / undefined / symbol / bigint`。
- 引用类型：`object`（含 Array、Function、Date、RegExp 等）。
- `typeof null === 'object'` 是历史 bug；`instanceof` 沿原型链判断引用类型。

**2. 闭包是什么？它有什么作用和副作用？**
- 函数能访问其外层作用域变量，即使外层函数已执行结束。
- 作用：封装私有变量、函数柯里化、防抖节流、模块化。
- 副作用：内存泄漏（变量无法被回收）、过度使用导致性能下降。

**3. 深拷贝的实现思路？JSON 方式有什么坑？**
- 递归 + 类型判断处理 Date/RegExp/Map/Set/循环引用（WeakMap 缓存）。
- `JSON.parse(JSON.stringify(obj))` 会丢失函数、`undefined`、Symbol、循环引用会报错。

**4. 事件循环（Event Loop）？宏任务和微任务分别有哪些？执行顺序？**
- 每个宏任务执行完后清空微任务队列。
- 宏任务：setTimeout/setInterval、I/O、UI 渲染、MessageChannel。
- 微任务：Promise.then、queueMicrotask、MutationObserver、process.nextTick（Node 优先）。

**5. `this` 指向有哪些规则？箭头函数有什么不同？**
- 默认绑定、隐式绑定、显式绑定（call/apply/bind）、new 绑定、箭头函数继承外层 this 且不可改。

**6. 原型与原型链：`__proto__`、`prototype`、`constructor` 的关系？**
- 构造函数有 `prototype` 指向原型对象；实例通过 `__proto__` 指向它；原型对象通过 `constructor` 指回构造函数。访问属性时沿链向上查找。

---

## 三、ES6+ 新特性

**1. `let/const` 与 `var` 的区别？暂时性死区是什么？**
- `var` 函数提升 + 重复声明；`let/const` 块级作用域 + 暂时性死区（TDZ，先声明后使用）。
- `const` 修饰的引用类型只保证地址不变。

**2. Promise 的状态有哪些？`all / race / allSettled / any` 的区别？**
- pending / fulfilled / rejected，状态不可逆。
- `all` 全成功才成功；`race` 第一个结束即决定；`allSettled` 全部结束后返回状态数组；`any` 第一个成功即成功（区别于 race）。

**3. `async/await` 的本质？错误如何捕获？**
- Generator + 自动执行器 + Promise 语法糖。
- try/catch 包住 await 块；或用 `Promise.catch` 链式处理。

**4. Map 与 Object 的区别？什么时候该用 Map？**
- Map 的 key 可以是任意类型、有序、有 size、增删频繁性能更优；Object 适合固定结构、做 JSON 序列化。

**5. 展开运算符、解构、可选链 `?.`、空值合并 `??` 各自的用途？**
- 数组/对象浅拷贝与合并；解构赋值；`?.` 安全访问深层属性；`??` 只在 null/undefined 时取默认值（区别于 `||`）。

---

## 四、TypeScript

**1. `interface` 与 `type` 的区别？什么时候用哪个？**
- `interface` 描述对象/类的形状，可声明合并、继承；`type` 更通用（联合、交叉、元组、映射）。
- 写 API/对象结构优先 interface，写工具类型/联合类型用 type。

**2. 泛型（Generics）是什么？常见应用场景？**
- 把类型当参数传递，提升复用性。常见于工具函数（`identity<T>(x: T): T`）、Hook、组件 props。

**3. `any / unknown / never` 的区别？**
- `any` 绕过类型检查；`unknown` 是类型安全的 top type，使用前需收窄；`never` 是 bottom type，表示永无值（穷尽判断时常用）。

**4. 什么是协变、逆变、双向协变？函数参数类型为什么是双变？**
- 子类型在更复杂场景下的赋值规则。TS 早期为简化在严格模式下默认函数参数双向协变；`strictFunctionTypes` 开启后参数变为逆变。

**5. 联合类型、交叉类型、类型守卫（type guard）怎么用？**
- `A | B` 取并集；`A & B` 取交集；`typeof / in / instanceof` 或自定义 `is` 谓词用于收窄类型。

---

## 五、Vue

**1. Vue2 与 Vue3 响应式原理有何不同？**
- Vue2：`Object.defineProperty` 劫持 getter/setter，无法监听新增/删除属性（需 `Vue.set`）。
- Vue3：`Proxy` + `Reflect`，可监听数组下标变化、属性增删、Map/Set，性能更好。

**2. Vue 组件通信方式有哪些？**
- props / emit / $parent-$children / provide-inject / EventBus / Vuex/Pinia / attrs & listeners / refs。

**3. `v-if` 与 `v-show` 的区别？使用场景？**
- `v-if` 条件渲染（DOM 增删）；`v-show` 仅切换 `display`。频繁切换用 v-show，条件少变用 v-if。

**4. keep-alive 的原理和作用？**
- 缓存组件实例，避免重复创建。`include/exclude` 过滤；提供 `activated / deactivated` 钩子。

**5. Composition API 与 Options API 的区别？何时使用？**
- Composition API 按逻辑组织代码（setup + ref/reactive/computed/watch），复用性更强；Options API 写法简单、适合小型组件。

**6. Vue 路由懒加载如何实现？**
- `component: () => import('@/views/xxx.vue')` 或 `defineAsyncComponent`；配合 webpack/vite 的代码分割。

---

## 六、React

**1. React 中 `setState` 是同步还是异步？批量更新（batching）怎么理解？**
- 在 React 事件、生命周期中为异步、批量合并；在 setTimeout、原生事件中为同步。React 18 后所有场景默认自动批处理。

**2. 函数组件与类组件的区别？Hooks 解决了什么问题？**
- 函数组件无 this、复用通过组合；Hooks 让状态/副作用等能力在函数组件中复用，免去 HOC / render props 嵌套。

**3. 虚拟 DOM 是什么？Diff 算法核心策略？**
- 用 JS 对象描述 DOM 树。Diff 策略：同层比较、key 优化列表、type 不同直接替换。

**4. `useEffect` 与 `useLayoutEffect` 的区别？**
- `useEffect` 在 commit 后异步执行；`useLayoutEffect` 在 DOM 更新后、浏览器绘制前同步执行，避免闪烁。

**5. React Fiber 是什么？解决了什么问题？**
- 16+ 重写的协调器，将渲染拆成可中断的小单元，支持时间切片和并发模式（Concurrent Mode）。

**6. 受控组件与非受控组件？refs 的使用方式？**
- 表单值由 React state 管控为受控；通过 ref 拿 DOM 值为非受控。`useRef`、`forwardRef`、`useImperativeHandle`。

---

## 七、浏览器原理

**1. 从输入 URL 到页面展示，发生了什么？**
- DNS 解析 → TCP 三次握手 → HTTPS TLS 握手 → HTTP 请求 → 服务器响应 → 解析 HTML/CSS/JS → 渲染树 → Layout → Paint → Composite。

**2. 浏览器渲染流程？重排（reflow）与重绘（repaint）？**
- HTML 解析成 DOM，CSS 解析成 CSSOM，合成 Render Tree → Layout（几何信息）→ Paint（像素）→ Composite（图层合成）。
- 重排影响几何、触发 layout；重绘仅样式变化；重排必触发重绘。

**3. 跨标签页通信有哪些方式？**
- `localStorage` + `storage` 事件、`BroadcastChannel`、`SharedWorker`、`window.postMessage`、Service Worker、Cookie。

**4. 浏览器本地存储有哪些？区别？**
- cookie：随请求、4KB；localStorage：5–10MB、永久；sessionStorage：关闭标签失效；IndexedDB：结构化、大容量、异步。

**5. V8 引擎的垃圾回收机制（GC）？**
- 新生代（Scavenge / Minor GC）使用复制算法；老生代（Major GC）使用标记-清除 + 标记-整理 + 增量标记减少停顿。

---

## 八、计算机网络

**1. HTTP 与 HTTPS 的区别？HTTPS 握手过程？**
- HTTPS = HTTP + TLS，在 TCP 之上加密。
- TLS 1.2 握手：ClientHello → ServerHello + 证书 → Key Exchange → Finished；TLS 1.3 简化为 1-RTT/0-RTT。

**2. HTTP 常见状态码分类与典型代表？**
- 1xx 信息、2xx 成功（200/201/204）、3xx 重定向（301/302/304）、4xx 客户端错误（400/401/403/404/405/429）、5xx 服务端错误（500/502/503/504）。

**3. GET 与 POST 区别？**
- GET 幂等、可缓存、参数在 URL 长度受限；POST 非幂等、参数在 body 更大更安全；本质无大区别，但语义与约定不同。

**4. 强缓存与协商缓存？相关 HTTP 头？**
- 强缓存：`Cache-Control`（max-age）/ `Expires`；不发请求直接命中。
- 协商缓存：`Last-Modified/If-Modified-Since`、`ETag/If-None-Match`，返回 304。

**5. TCP 三次握手、四次挥手？为什么三次？TIME_WAIT 作用？**
- 三次：SYN → SYN+ACK → ACK，防止已失效的连接请求被服务器接收。
- 四次：FIN+ACK 双向。TIME_WAIT 保证最后一个 ACK 能到达对端，并让旧连接报文消逝。

**6. WebSocket 与 HTTP 长轮询区别？**
- WebSocket 是独立全双工协议（基于 HTTP 升级握手），长轮询是阻塞式模拟；前者实时性、效率更高。

---

## 九、性能优化

**1. 首屏加载优化有哪些手段？**
- 路由懒加载、资源压缩、CDN、HTTP 缓存、Tree Shaking、SSR/SSG、骨架屏、关键 CSS 内联、preload/prefetch。

**2. 防抖（debounce）与节流（throttle）的区别与实现？**
- 防抖：连续触发只执行最后一次（搜索输入）。
- 节流：固定时间窗口内只执行一次（滚动监听）。
- 都可以用 `setTimeout` + 时间戳 / 闭包实现。

**3. 图片懒加载原理？**
- 使用 `IntersectionObserver` 监听图片进入视口，替换 `data-src` 为真实地址；或通过 scroll + getBoundingClientRect。

**4. Web 性能指标（Core Web Vitals）？**
- LCP（最大内容渲染）、INP（交互到下一次绘制，取代 FID）、CLS（布局偏移）。优化 LCP、降低 JS 主线程长任务、稳定布局。

**5. 长列表优化方案？**
- 虚拟滚动（react-virtuoso / vue-virtual-scroller）、分页、requestAnimationFrame 渲染、Canvas 渲染、Object.freeze 不可变数据。

---

## 十、前端安全

**1. XSS（跨站脚本）的类型？如何防御？**
- 类型：反射型、存储型、DOM 型。
- 防御：输入过滤 + 输出编码、CSP、HttpOnly Cookie、避免 `innerHTML` 拼接用户输入。

**2. CSRF（跨站请求伪造）的原理和防御？**
- 利用用户已登录的身份诱导发请求。
- 防御：SameSite Cookie、CSRF Token、Referer/Origin 校验、关键操作二次验证。

**3. 点击劫持（Clickjacking）？**
- 透明 iframe 覆盖诱骗点击。防御：`X-Frame-Options: DENY/SAMEORIGIN`、CSP `frame-ancestors`。

**4. HTTPS 中间人攻击？**
- 攻击者劫持网络、伪造证书。防御：可信 CA、证书校验、HSTS 强制 HTTPS。

**5. 什么是 SRI（Subresource Integrity）？**
- 资源外链带 hash 校验，文件被篡改时浏览器拒绝加载。

---

## 十一、前端工程化

**1. Webpack 的构建流程？核心概念？**
- 入口 → Loader 链转换 → 收集依赖 → 封装模块 → Plugin 触发钩子 → 输出 bundle。
- 核心：entry/output/loader/plugin/mode/module/chunks。

**2. Tree Shaking 原理？生效条件？**
- 依赖 ES Module 静态结构 + 副作用分析（`sideEffects: false`）+ minifier 移除未引用代码。

**3. Vite 为什么比 Webpack 快？**
- 开发期使用原生 ES Module 按需编译 + esbuild 预构建依赖（Go 编写，10–100x 速度），生产用 Rollup 打包。

**4. Babel / SWC / esbuild 的差异？**
- Babel：JS AST 转换、插件最全；esbuild：Go 实现、极快、不支持 AST 插件；SWC：Rust 实现、速度快、兼容 Babel 插件生态。

**5. CI/CD 与灰度发布在前端怎么落地？**
- Lint/Test/TypeCheck → 自动化构建 → CDN 灰度（按域名/版本号切换）→ 监控异常 → 回滚。

---

## 十二、Node.js

**1. Node 事件循环的 6 个阶段？与浏览器有何不同？**
- timers → pending callbacks → idle/prepare → poll → check → close callbacks。
- `process.nextTick` 与微任务（Promise）的优先级：每个阶段切换前都会清空 nextTick 与微任务。

**2. `require` 与 `import` 的区别？**
- `require` 是运行时同步加载 CommonJS；`import` 是 ESM 静态编译时加载、异步、树摇友好。

**3. 进程与线程？Node 的 `cluster` 与 `worker_threads`？**
- 进程是资源分配单位、线程是 CPU 调度单位。`cluster` 多进程共享端口；`worker_threads` 共享内存、适合 CPU 密集。

**4. 流（Stream）是什么？背压（backpressure）？**
- 顺序处理数据。背压指消费者处理慢时上游减少写入，避免内存爆掉。`pipe`、`pipeline`、Transform 流。

**5. Koa 与 Express 的区别？**
- Koa 洋葱模型 + async/await 中间件、可控性强；Express 线性中间件、生态丰富。

---

## 十三、设计模式

**1. 单例模式的多种实现？前端场景？**
- 静态变量、闭包、ES Module 缓存。应用：全局弹窗、Store、Vuex/Pinia 实例。

**2. 发布-订阅 vs 观察者模式？**
- 观察者：目标直接通知观察者；发布-订阅：中间 EventChannel 解耦，更灵活。EventEmitter 是发布订阅。

**3. 工厂模式在前端的体现？**
- React `createElement`、组件工厂函数、Vue 的 `createApp`。

**4. 装饰器模式？高阶函数 / HOC？**
- 不改原对象、动态增加职责。React HOC、Vue mixin（思想类似）、TS 装饰器、JS Proxy 包装。

**5. 策略模式的使用？**
- 表单校验、权限判定、动画曲线切换。把 if/else 拆成可替换的策略对象。

---

## 十四、数据结构与算法

**1. 数组去重有哪些方式？时间/空间复杂度？**
- Set：`[...new Set(arr)]` O(n)。
- 双 for 循环 O(n²)；排序后去重 O(nlogn)；Map 计数 O(n)。

**2. 排序算法：快排、归并、堆排的思想与复杂度？**
- 快排：分治 + 基准 partition，期望 O(nlogn)，最坏 O(n²)。
- 归并：分治 + 合并，O(nlogn) 稳定、需 O(n) 空间。
- 堆排：堆调整，O(nlogn) 原地不稳定。

**3. 链表与数组的差异？**
- 数组连续存储、随机访问 O(1)、插入删除 O(n)；链表分散、查找 O(n)、插入删除 O(1)。

**4. 二叉树遍历方式？JS 实现？**
- 前/中/后序（DFS）递归与栈，层序（BFS）队列。

**5. 动态规划（DP）经典题？**
- 爬楼梯、零钱兑换、最长子序列（LIS）、最长公共子序列、背包问题。

**6. LRU 缓存如何设计？**
- Map（保留插入顺序） + 双向链表：get O(1)、put O(1)；到达容量淘汰最久未用。

---

## 十五、移动端 / H5

**1. 1px 边框问题及解决方案？**
- 高 DPR 屏下 `1px` 实际渲染为多倍物理像素。方案：transform scale + 伪元素、`border-image`、`viewport` + 媒体查询 rem 适配。

**2. 移动端适配方案？rem / vw / vh / 弹性盒？**
- rem + 动态根字号（lib-flexible）、vw/vh 直接使用、`postcss-px-to-viewport`、Flex 布局。

**3. 移动端点击 300ms 延迟？**
- 早期 double-tap 缩放导致。方案：`<meta name="viewport" content="width=device-width">`、`touch-action: manipulation`、FastClick。

**4. 软键盘顶起页面？**
- 监听 `focusin/focusout` / `resize` 调整 scroll；或 IntersectionObserver 滚动到可视区；使用 `visualViewport`。

**5. 移动端调试工具？**
- Chrome DevTools 远程调试、Weinre、vConsole、Eruda、Charles / Whistle 抓包、Safari Web Inspector（iOS）。

---

## 十六、跨端 / 小程序 / 进阶

**1. 小程序双线程模型（逻辑层/渲染层）？**
- 逻辑层 JSCore 跑 JS、渲染层 WebView 渲染；通过 JSBridge 通信（setData 异步、JSON 序列化）。

**2. Taro / Uni-app / React Native 的实现差异？**
- Taro/Uni：JS 编译到多端 DSL；RN：JS 桥接原生组件；Flutter 自绘引擎；Weex 类 RN 但基于 Vue。

**3. PWA 的核心能力？**
- manifest、Service Worker（缓存、推送、后台同步）、HTTPS、可安装。

**4. Web Components 的三大技术？**
- Custom Elements + Shadow DOM + HTML Templates / `<slot>`。

**5. WebAssembly 的应用？**
- 把 C/C++/Rust 编译到 wasm 在浏览器运行，处理图像/视频/游戏/AI 推理等 CPU 密集型任务。

---

> 使用建议：每天抽 1 个方向刷 2–3 题，结合「面试鸭」项目中的题库（`/tag/前端` 标签）搜索相似题做对照训练，效率最高。
