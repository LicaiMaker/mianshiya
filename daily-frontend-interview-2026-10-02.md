# 前端每日面试题 — 2026-10-02

> 来源参考：mianshiya.com（面试鸭）前端题库分类，覆盖 HTML / CSS / JavaScript / ES6 / TypeScript / Vue / React / Node.js / Webpack / 性能优化 / 系统设计 / 设计模式 / 手写代码 / 场景题 等。本日精选 22 道题（每个方向 2 道）。

---

## 1. HTML

**Q1. 请简述 HTML 语义化的意义，并列举 5 个常见的语义化标签。**

参考答案要点：
- 语义化指用合适的标签表达合适的结构，而非全部 div + span。
- 意义：提升可访问性（屏幕阅读器、辅助设备更好解析）、代码可读性与可维护性、利于 SEO 搜索引擎抓取、便于其他设备（无障碍）正确渲染。
- 常见语义化标签：`<header>`、`<nav>`、`<main>`、`<article>`、`<section>`、`<aside>`、`<footer>`、`<h1>~<h6>`、`<ul>/<ol>/<dl>`、`<time>`、`<figure>/<figcaption>` 等。

---

**Q2. `<script>` 标签的 `async` 和 `defer` 有什么区别？DOMContentLoaded 与它们的执行顺序是怎样的？**

参考答案要点：
- 两者都不会阻塞 HTML 解析，仅在下载阶段表现不同。
- `async`：脚本下载完成后立即中断解析并执行脚本，执行顺序不固定（谁先下载完成谁先执行），适用于独立第三方脚本（如统计脚本）。
- `defer`：脚本下载与解析并行，脚本在 DOM 解析完成、DOMContentLoaded 触发之前按文档顺序执行。
- 执行顺序：
  - 普通 `<script>`：阻塞解析，下载并执行完才继续。
  - `defer`：DOMContentLoaded 之前按顺序执行。
  - `async`：加载完立即执行，可能早于也可能晚于 DOMContentLoaded。
- `type="module"` 的 script 默认具备 defer 行为。

---

## 2. CSS

**Q1. 请解释 BFC（Block Formatting Context）的概念，并说明触发 BFC 的方式及典型应用场景。**

参考答案要点：
- BFC 是一个独立的渲染区域，内部的块级盒子按照一定规则布局，且与外部互不影响。
- 触发条件：
  - 根元素 `<html>`
  - `float` 不为 none
  - `position` 为 absolute / fixed
  - `overflow` 不为 visible（auto / scroll / hidden）
  - `display` 为 inline-block / table-cell / table-caption / flex / grid / flow-root
- 典型场景：清除浮动（包含浮动元素）、阻止 margin 重叠、阻止元素被浮动元素覆盖、实现自适应两栏布局。

---

**Q2. CSS 中的盒模型有哪几种？`box-sizing` 属性的取值含义是什么？**

参考答案要点：
- 盒模型分类：标准盒模型（content-box）与怪异盒模型（border-box，IE 盒模型）。
- `box-sizing: content-box`（默认）：width / height 仅指 content 区域，border + padding 会撑大盒子。
- `box-sizing: border-box`：width / height 包含 content + padding + border，开发中常用。
- 实践建议：通常在全局 reset 中设置 `*, *::before, *::after { box-sizing: border-box; }`。

---

## 3. JavaScript 基础

**Q1. 什么是闭包？请举例说明闭包的应用与可能带来的内存问题。**

参考答案要点：
- 闭包是指函数能够访问并记住其创建时所处的词法作用域中的变量，即使该外部函数已经执行完毕。
- 典型应用：
  - 数据封装与私有变量（模块模式）。
  - 函数柯里化与偏函数。
  - 防抖 / 节流等高阶函数中保留定时器状态。
  - React Hooks 本质也是闭包。
- 内存问题：闭包会使得外层函数中的变量无法被 GC 回收，长期持有大对象或 DOM 引用会内存泄漏。建议在不再使用后手动置 null，或使用 WeakMap。

---

**Q2. 请说明原型链的查找机制，并解释 `instanceof` 的实现原理。**

参考答案要点：
- 每个对象（除 null）都有 `__proto__`，指向其构造函数的 prototype；构造函数的 prototype 也有 `__proto__`，层层向上形成链，最终到 `Object.prototype.__proto__ === null`。
- 属性查找：对象本身 → `__proto__` → 上一层 prototype … → null。
- `instanceof`：判断对象的原型链上是否能找到类型的 `prototype`。手写实现：
  ```javascript
  function myInstanceof(left, right) {
    let proto = Object.getPrototypeOf(left);
    while (proto) {
      if (proto === right.prototype) return;
      proto = Object.getPrototypeOf(proto);
    }
    return false;
  }
  ```

---

## 4. ES6+

**Q1. 请说明 `let`、`const`、`var` 的区别，并解释暂时性死区（TDZ）。**

参考答案要点：
- `var`：函数作用域，存在变量提升（声明提升 + 值 undefined），可重复声明。
- `let`：块级作用域，不存在变量提升，存在 TDZ，声明前访问报错，不可重复声明。
- `const`：块级作用域，声明时必须初始化，值（引用地址）不可再赋值，但对象属性可变。
- TDZ：变量在块级作用域内已创建但未初始化期间，处于"暂时性死区"，访问会抛 ReferenceError。

---

**Q2. Promise 的状态有哪些？`.then`、`.catch`、`.finally` 返回的新 Promise 状态如何决定？**

参考答案要点：
- Promise 三种状态：pending（进行中）、fulfilled（已成功）、rejected（已失败）。状态一旦确定不可再变。
- `.then(onFulfilled, onRejected)`：
  - 若 onFulfilled/onRejected 返回普通值，新 Promise 状态为 fulfilled，值为该返回值。
  - 若抛出异常，新 Promise 状态为 rejected。
  - 若返回 Promise，新 Promise 状态由其决定。
- `.catch(fn)` 等价于 `.then(null, fn)`，只处理 reject。
- `.finally(fn)` 不接收参数，fn 返回值不会传递给下一链（除非显式 return）；无论成功失败都会执行。

---

## 5. TypeScript

**Q1. TypeScript 中 `interface` 与 `type` 的异同是什么？什么情况下更推荐 `type`？**

参考答案要点：
- 相同点：都可描述对象结构，都支持 extends。
- 区别：
  - `interface`：可重复声明自动合并（声明合并），更适合面向对象描述对象 / 类的形状。
  - `type`：可描述联合类型、交叉类型、元组、工具类型映射等，更灵活，不支持声明合并。
- 推荐 `type` 的场景：联合类型 / 工具类型 / 元组 / 函数签名等复杂组合。

---

**Q2. 解释 TypeScript 中的协变、逆变与双向协变，并说明 `strictFunctionTypes` 的作用。**

参考答案要点：
- 协变：子类可以赋值给父类（结构兼容的方向相同）。
- 逆变：参数类型只能父类赋值给子类（方向相反）。
- 双向协变：参数与返回值都允许父子类型互转。
- TS 中函数参数默认是双向协变（为了兼容 JS），开启后参数变为逆变校验，更严格。返回值始终协变。

---

## 6. Vue

**Q1. 请说明 Vue 2 与 Vue 3 在响应式原理上的核心区别。**

参考答案要点：
- Vue 2：基于 `Object.defineProperty` 劫持对象属性，对象新增 / 删除属性需借助 `Vue.set / Vue.delete`，数组通过重写原型方法实现。无法直接监听 Map / Set。
- Vue 3：基于 ES6 `Proxy`，可监听对象整体（包括新增、删除、in 操作符），原生支持 Map / Set 等。性能更优，递归惰性按需触发。
- 此外 Vue 3 采用 Composition API + `ref / reactive`，逻辑复用更灵活。

---

**Q2. Vue 中的 `nextTick` 是什么？其实现原理与使用场景是什么？**

参考答案要点：
- `nextTick`：在下次 DOM 更新循环结束之后执行延迟回调，常用于在数据变化后获取更新后的 DOM。
- 原理：在调用栈清空后，采用微任务（Promise.then / MutationObserver）或宏任务（setTimeout）异步执行回调。
- 典型场景：created 中操作 DOM（需等挂载完成）、watch 单次 DOM 同步、列表更新后获取最新 DOM 尺寸等。

---

## 7. React

**Q1. React 中受控组件与非受控组件的区别是什么？各举一个典型场景。**

参考答案要点：
- 受控组件：表单元素的值由 React state 控制，通过 `onChange` 同步更新 state，输入完全由 React 管理。
  - 场景：登录表单需要实时校验、禁用提交按钮。
- 非受控组件：通过 `ref` 直接读取 DOM 值，React 不管理输入状态。
  - 场景：文件 `<input type="file" />` 上传、简单的搜索框、避免每次输入都触发 setState。
- 注意：非受控组件提交时一次性 `ref.current.value` 取值。

---

**Q2. React Hooks 的闭包陷阱是什么？`useEffect`、`useCallback`、`useMemo` 的依赖项如何正确书写？**

参考答案要点：
- 闭包陷阱：在事件回调 / effect 中捕获了过时的 state 或引用。常见于 `setTimeout`、异步回调、订阅回调。
- 解决方式：使用 `useRef` 保存最新值，或将依赖加入 deps。
- 依赖项：必须是回调 / effect 内使用的所有响应式值（state、props、context、衍生变量）。
- 工具：`useCallback` 用于稳定函数引用（避免子组件 re-render），`useMemo` 用于缓存计算结果，二者都依赖 deps 的正确书写。

---

## 8. Node.js

**Q1. Node.js 中的事件循环（Event Loop）是什么？请按宏任务 / 微任务顺序描述一次完整循环。**

参考答案要点：
- Node 基于 libuv 实现事件循环，分为多个阶段：timers → pending callbacks → idle / prepare → poll → check → close callbacks。
- 每轮循环：在各阶段处理对应队列的回调，阶段切换前清空 nextTick / 微任务队列（process.nextTick 与 Promise 微任务）。
- 常见微任务优先级：`process.nextTick` 高于 Promise 微任务（同一阶段中先清空 nextTick 队列）。
- 常见宏任务：setTimeout / setInterval、setImmediate（check 阶段）、I/O 回调（poll 阶段）。

---

**Q2. Node.js 中 `process.nextTick`、`setImmediate` 与 `setTimeout(fn, 0)` 的执行顺序是怎样的？**

参考答案要点：
- `process.nextTick`：在当前操作结束后、下一阶段切换前执行（微任务级别，最高优先级）。
- `setImmediate`：在事件循环 check 阶段执行（I/O 回调之后）。
- `setTimeout(fn, 0)`：在 timers 阶段执行，最小阈值约 1ms（受系统限制）。
- 一般顺序：nextTick → Promise 微任务 → setTimeout → setImmediate（依上下文略有差异）。

---

## 9. Webpack / 构建工具

**Q1. 请简述 Webpack 的构建流程，并解释 Loader 与 Plugin 的区别。**

参考答案要点：
- 构建流程：初始化参数 → 加载配置 → 确定入口 → 编译模块（Loader 转换）→ 解析依赖图 → 输出 chunk → 写入文件。
- Loader：模块转换器，本质是函数，处理非 JS 资源（CSS / 图片 / TS 等），按 `module.rules` 配置。
- Plugin：基于 Tapable 生命周期钩子介入打包流程，做更广泛的事情（HtmlWebpackPlugin、CleanWebpackPlugin、DefinePlugin 等）。
- 区别：Loader 作用于单个文件，Plugin 作用于整个构建生命周期。

---

**Q2. Vite 为什么比 Webpack 快？其核心原理是什么？**

参考答案要点：
- Vite 基于浏览器原生 ES Module，开发期不做完整打包，按需编译、按需加载。
- 利用 esbuild 进行预构建依赖（Go 实现，速度快）。
- HMR 基于 ESM，按模块热更新，不重建整包。
- 生产环境使用 Rollup 打包，仍保持较优产物体积与 tree-shaking 效果。

---

## 10. 前端性能优化

**Q1. 请列举至少 8 种常见的前端性能优化手段，并说明它们分别优化的是哪个阶段。**

参考答案要点：
- 网络阶段：DNS 预解析、HTTP/2、TLS1.3、CDN 加速、gzip / brotli 压缩、合理使用 HTTP 缓存（强缓存 / 协商缓存）。
- 加载阶段：路由懒加载、组件按需 import、图片懒加载（`loading="lazy"` / IntersectionObserver）、字体子集化、preload / prefetch。
- 渲染阶段：减少重排重绘、CSS contain、虚拟列表、骨架屏、SSR / SSG。
- 运行阶段：Web Worker、长任务拆分、防抖节流、事件委托、避免内存泄漏。
- 打包阶段：tree-shaking、code splitting、source map 按需、esbuild / swc 压缩。

---

**Q2. 什么是 LCP / FID / CLS（Core Web Vitals）？如何优化它们？**

参考答案要点：
- LCP（Largest Contentful Paint）：最大内容绘制时间，衡量加载性能，目标 < 2.5s。
  - 优化：预加载 LCP 元素资源、图片优化、字体优化、SSR / 流式渲染。
- FID（First Input Delay）：首次输入延迟，衡量交互响应，目标 < 100ms（新版已替换为 INP）。
  - 优化：拆分长任务、Worker 处理重计算、减少主线程阻塞。
- CLS（Cumulative Layout Shift）：累计布局偏移，衡量视觉稳定性，目标 < 0.1。
  - 优化：图片 / 视频指定宽高、字体 fallback 配 `size-adjust`、避免动态插入上方内容、动画使用 transform / opacity。

---

## 11. 前端场景题

**Q1. 在商品列表页中，如何实现"无限滚动加载更多"？如何保证性能与正确性？**

参考答案要点：
- 实现：监听 scroll 事件 + 节流；或使用 `IntersectionObserver` 监听底部哨兵元素，进入视口触发加载。
- 正确性：防抖 / 节流避免重复请求；请求加锁（loading 状态）；接口失败可重试；分页参数基于响应长度判断终止。
- 性能：虚拟列表（如 react-window / vue-virtual-scroller）只渲染视口内 DOM；分页请求数据按需缓存。

---

**Q2. 在前端实现权限控制（菜单 / 按钮 / 路由）时，你通常采用怎样的方案？**

参考答案要点：
- 路由权限：登录后后端下发权限树 / 角色，前端根据权限动态注册路由（addRoute）或过滤路由表。
- 菜单权限：基于过滤后的路由表渲染菜单。
- 按钮权限：自定义指令（如 `v-permission`）或高阶组件包裹按钮，根据权限码控制渲染 / disabled。
- 数据级权限：通常由后端控制，前端隐藏过滤条件。
- 注意：前端权限仅是体验优化，真正的安全必须由后端鉴权。

---

## 12. 设计模式

**Q1. 请简述"发布-订阅模式"与"观察者模式"的区别，并写出发布-订阅的最小实现。**

参考答案要点：
- 观察者模式：目标对象直接维护观察者列表，触发时通知列表中的观察者。
- 发布-订阅模式：存在一个事件中心（事件总线），发布者与订阅者通过事件中心解耦，互不知道对方存在。
- 最小发布-订阅：
  ```javascript
  class EventBus {
    constructor() { this.handlers = {}; }
    on(evt, fn) { (this.handlers[evt] = this.handlers[evt] || []).push(fn); }
    off(evt, fn) {
      this.handlers[evt] = (this.handlers[evt] || []).filter(h => h !== fn);
    }
    emit(evt, ...args) {
      (this.handlers[evt] || []).forEach(fn => fn(...args));
    }
  }
  ```

---

**Q2. 什么是单例模式？在 JS 中有哪些典型实现？有什么坑？**

参考答案要点：
- 单例：全局只有一个实例，多次实例化返回同一对象。
- 典型实现：模块模式（IIFE）、ES Module 天然单例、构造器内 `if (instance) return instance`、闭包缓存。
- 坑：跨多个 script / iframe / worker 不共享单例；HMR 时单例不重置；需注意透明性。

---

## 13. 前端手写代码

**Q1. 手写一个深拷贝函数，需要支持 Date / RegExp / 循环引用的处理。**

参考答案要点：
```javascript
function deepClone(obj, hash = new WeakMap()) {
  if (obj === null || typeof obj !== 'object') return obj;
  if (obj instanceof Date) return new Date(obj);
  if (obj instanceof RegExp) return new RegExp(obj);
  if (hash.has(obj)) return hash.get(obj);
  const target = Array.isArray(obj) ? [] : {};
  hash.set(obj, target);
  for (const k of Reflect.ownKeys(obj)) {
    target[k] = deepClone(obj[k], hash);
  }
  return target;
}
```
- 循环引用通过 WeakMap 记录已拷贝对象避免死循环。
- 进阶：处理 Symbol 属性、函数（默认不拷贝）、Map / Set、原型链。

---

**Q2. 手写防抖（debounce）与节流（throttle），并说明应用场景区别。**

参考答案要点：
- 防抖：连续触发结束后等待 `wait` ms 才执行最后一次。适用于搜索框输入、窗口 resize。
- 节流：一定时间间隔内最多执行一次。适用于滚动事件、按钮防重复点击、射击游戏子弹频率。
- 实现（节流：时间戳 + 定时器混合）：
  ```javascript
  function throttle(fn, wait) {
    let last = 0, timer = null;
    return function (...args) {
      const now = Date.now();
      const remaining = wait - (now - last);
      if (remaining <= 0) {
        if (timer) { clearTimeout(timer); timer = null; }
        last = now; fn.apply(this, args);
      } else if (!timer) {
        timer = setTimeout(() => { last = Date.now(); timer = null; fn.apply(this, args); }, remaining);
      }
    };
  }
  ```

---

## 14. 前端系统设计

**Q1. 如何设计一个前端监控 SDK（错误监控 + 性能监控 + 用户行为）？核心模块如何划分？**

参考答案要点：
- 数据采集层：
  - 错误：window.onerror / unhandledrejection / 框架错误边界（React ErrorBoundary）。
  - 性能：PerformanceObserver 监听 LCP / FID / CLS / FCP；Navigation Timing API。
  - 行为：路由变化（history.pushState 拦截）、点击 / 曝光埋点。
- 数据处理层：上下文信息（用户 / 环境 / 设备）、去重、采样、过滤敏感字段。
- 上报层：navigator.sendBeacon（首选，避免阻塞）、fetch keepalive、图片打点（兜底）、批量聚合上报。
- 后端消费：日志服务（Kafka / SLS）+ 聚合分析（ES / ClickHouse）+ 告警与可视化。

---

**Q2. 如何设计一个支持搜索/筛选/分页的大型列表页前端架构？**

参考答案要点：
- 视图层：列表 + 搜索框 + 筛选条件 + 分页器。
- 状态层：URL 作为单一数据源（query 同步筛选条件），便于分享 / 回溯 / SSR。
- 数据层：使用 SWR / React Query 管理缓存、stale-while-revalidate、分页游标 / 偏移、预加载下一页。
- 性能层：虚拟滚动、骨架屏、防抖搜索、IndexedDB 缓存历史筛选。
- 可维护层：通用 `useTableQuery` / `useSearchFilter` hooks 抽离业务无关的查询逻辑。

---

## 15. 网络 / 安全

**Q1. 简述 HTTPS 的握手流程，TLS 1.2 与 TLS 1.3 的区别是什么？**

参考答案要点：
- TLS 1.2 握手：Client Hello → Server Hello + 证书 → Client Key Exchange（用服务器公钥加密 pre-master）→ 双方派生密钥 → Finished。
- TLS 1.3 简化：1-RTT 握手（0-RTT 可选），使用 X25519 / secp256r1 等密钥交换算法，移除不安全套件（MD5 / SHA1 / RC4 / 3DES 等），握手阶段即加密。
- TLS 1.3 优势：更快、更安全、减少攻击面。

---

**Q2. 常见的 Web 安全攻击与防御：XSS / CSRF / 点击劫持。**

参考答案要点：
- XSS（跨站脚本）：
  - 存储型 / 反射型 / DOM 型。
  - 防御：输出转义、CSP、HTTPS-only cookie、避免使用 `eval / innerHTML / document.write`、使用框架默认转义机制。
- CSRF（跨站请求伪造）：
  - 利用用户已登录身份发起请求。
  - 防御：SameSite=Lax / Strict Cookie、CSRF Token、验证 Origin / Referer、关键操作二次校验。
- 点击劫持：嵌套 iframe 诱导点击。
  - 防御：X-Frame-Options: DENY / SAMEORIGIN、CSP frame-ancestors 指令、关键操作使用 token / 验证码。

---

## 16. 工程化

**Q1. 一个中型前端项目的工程化通常包含哪些维度？请选择你认为最重要的三项展开说明。**

参考答案要点：
- 维度：模块化（ESM / CommonJS）、构建工具（Webpack / Vite）、代码规范（ESLint / Prettier / husky / lint-staged）、测试（Jest / Vitest / Playwright）、CI / CD、版本与发布（semver / changelog）、文档与目录规范、监控与告警。
- 三项举例：
  - 代码规范：提交前 lint + commit hook，避免主干质量崩坏。
  - 测试：单元测试覆盖核心逻辑 + e2e 覆盖关键链路，CI 中跑测试，阻断低级故障。
  - CI / CD：自动化构建 + 静态资源 CDN 灰度发布 + 异常回滚。

---

**Q2. 如何在前端项目中落地 Monorepo？有哪些关键工具链？**

参考答案要点：
- 方案：pnpm workspace、Yarn workspaces、Lerna、Nx、Turborepo。
- 关键能力：
  - 依赖提升与 hoist，避免重复安装。
  - 共享包（utils / components / ui / config）。
  - 增量构建（Turbo 缓存 + 任务 DAG）。
  - 统一 lint / 格式化 / 测试脚本。
  - 跨包类型提示与版本管理（changesets）。

---

## 17. 设计模式 / 架构

**Q1. 什么是 MVVM？它在 Vue / React 中是如何体现的？**

参考答案要点：
- MVVM = Model（数据）+ View（视图）+ ViewModel（视图模型）。
- ViewModel 负责把 Model 转换成 View 可用状态，View 与 ViewModel 双向绑定。
- Vue：模板即 View、data 即 Model、Vue 实例即 ViewModel，通过响应式 + 模板语法实现双向绑定。
- React：严格说更接近单向数据流（View → Action → State → View），但通过状态提升 + 受控组件也可表达双向，类库如 MobX 提供 VM 抽象。

---

**Q2. 什么是 Flux / 单向数据流？它解决了什么问题？**

参考答案要点：
- 单向数据流：Action → Dispatcher → Store → View → 新的 Action。
- 解决多 View 共享状态、双向绑定导致的状态变化难追踪、副作用难调试问题。
- Redux 进一步规范：纯函数 reducer + 单一 store + 中间件机制处理副作用。

---

## 18. 浏览器原理

**Q1. 从输入 URL 到页面渲染完成，浏览器经历了哪些过程？**

参考答案要点：
- URL 解析 → 缓存查找（强缓存 / 协商缓存）。
- TCP 三次握手 / 四次挥手，TLS 握手（HTTPS）。
- HTTP 请求 / 响应。
- 解析 HTML 构建 DOM 树、解析 CSS 构建 CSSOM，合并为 Render Tree。
- Layout（布局）→ Paint（绘制）→ Composite（合成图层）。
- 期间涉及 JS 引擎（V8）、事件循环、重排重绘、合成层等。

---

**Q2. 什么是合成层（Composite Layer）？什么操作会触发新合成层？**

参考答案要点：
- 合成层是浏览器将某些元素提升到独立 GPU 图层进行合成，避免重绘整页。
- 触发条件：
  - 3D transform（如 `translate3d` / `transform: rotateZ` 等）。
  - `will-change: transform / opacity`。
  - `<video>` / `<canvas>` / `<iframe>` 等。
  - `position: fixed` 在某些场景。
- 注意：滥用合成层会占用大量显存，触发层爆炸，反而降低性能。

---

> 建议刷题节奏：每天 1~2 个方向，深度做 5~8 道 + 输出答案要点，长期累计即可覆盖面试高频范围。完整题库可参考 [面试鸭前端题库](https://www.mianshiya.com/?category=frontend)。