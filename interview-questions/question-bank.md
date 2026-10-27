# 前端面试题库（轮转版）

- 来源：[面试鸭 mianshiya.com](https://www.mianshiya.com/tag/%E5%89%8D%E7%AB%AF) 题库 + 本仓库（`/workspace`，面试鸭自身：React 17 + UmiJS 3 + Ant Design Pro + TypeScript + Less + Express/ES/Redis 服务端）自编延伸题
- 覆盖 12 个前端技术方向，每方向 5 题（共 60 题），每次发放按方向取 2~3 题
- 编号规则：`方向缩写-序号`，发放时在「使用记录」中登记日期，后续轮转跳过已用题
- 难度标注：🟢 简单 / 🟡 中等 / 🔴 困难

---

## 1. HTML

**HTML-1** 🟡 script 标签中 `defer` 和 `async` 有什么区别？
> 来源：<https://www.mianshiya.com/question/1810654507466534913>
- `defer`：异步下载，解析到该标签时暂停解析，等文档解析完成、DOMContentLoaded 前按顺序执行；不阻塞 HTML 解析。
- `async`：异步下载，下载完立即执行，**不保证执行顺序**，也不保证在 DOMContentLoaded 前完成；会阻塞依赖该脚本的 DOMContentLoaded 触发。
- 都不阻塞 HTML 解析；都不支持 `document.write`。

**HTML-2** 🟡 什么是 HTML 语义化？为什么要语义化？
> 来源：<https://www.mianshiya.com/question/1810654507105824769>
- 用 `header/nav/main/article/aside/footer/section` 等有明确含义的标签表达结构，而不是全用 `div`。
- 收益：① SEO（搜索引擎按语义结构抓取）；② 无障碍（读屏软件按标签朗读、键盘可达）；③ 代码可读性与维护性；④ 浏览器与工具（样式重置、阅读模式）行为更可预期。

**HTML-3** 🟡 Canvas 和 SVG 有什么区别？
> 来源：<https://www.mianshiya.com/question/1810654509664350210>
- Canvas：位图，绘制命令驱动，状态全在 JS 侧；适合上万点、动画、3D；不能单独选中和做无障碍语义，需自行实现命中检测。
- SVG：矢量 DOM 元素，浏览器渲染，天然可 CSS 样式化、可点击、可 `viewBox` 无损缩放；节点多时性能下降。
- 实践：图标/图表用 SVG，海量数据/动画用 Canvas。

**HTML-4** 🟢 `src` 和 `href` 属性有什么区别？
> 来源：<https://www.mianshiya.com/question/1810654506023694337>
- `src`：嵌入资源，会被浏览器下载并**替换**当前元素内容（`script`/`img`/`iframe`/`video`）；`script` 加载失败会影响页面执行。
- `href`：超链接引用，指向外部资源但不嵌入当前文档（`a`/`link`）；`link rel=stylesheet` 是例外，会加载样式。

**HTML-5** 🟡 HTML5 的离线存储怎么用？原理是什么？
> 来源：<https://www.mianshiya.com/question/1810654508355727362>
- `localStorage` / `sessionStorage`：同步、只存字符串、单域约 5MB、`sessionStorage` 关闭标签页即失效。
- IndexedDB：异步、事务型、支持结构化数据与索引、容量大。
- Cache Storage + Service Worker：缓存资源实现真正的离线可用（需 HTTPS）。
- 原理：数据按 origin 隔离存储在浏览器内部，`storage` 事件可跨标签页同步。

---

## 2. CSS

**CSS-1** 🟢 什么是 CSS 盒子模型？`box-sizing` 的作用？
> 来源：<https://www.mianshiya.com/question/1773177337010020353>
- 标准模型 `content-box`：`width` 只算内容区，实际占位 = content + padding + border。
- 边框模型 `border-box`：`width` 含 padding 与 border，更符合设计稿直觉（全局 `* { box-sizing: border-box }`）。
- 另有 `padding-box`（少用）。

**CSS-2** 🟡 CSS 选择器有哪些？优先级如何计算？
> 来源：<https://www.mianshiya.com/question/1773176837539717122>、<https://www.mianshiya.com/question/1810655444922830849>
- 基础：`*`、类型、`.class`、`#id`；关系：后代 ` `、子 `>`、相邻 `+`、兄弟 `~`；伪类 `:hover/:first-child/:not()`；伪元素 `::before/::after`；属性 `[attr=val]`。
- 优先级（从高到低）：`!important` > 内联 style > `#id` > 类/属性/伪类 > 标签/伪元素 > 通配符；**同权重看书写顺序，后者覆盖前者**。
- 特殊：`:not()/:is()` 权重取参数自身最高权重；`:where()` 权重恒为 0。

**CSS-3** 🟡 有哪些方式可以隐藏页面元素？区别是什么？
> 来源：<https://www.mianshiya.com/question/1810655446143373314>
| 方式 | 占位 | 可交互 | 可被读屏读取 | 触发重排 |
|---|---|---|---|---|
| `display:none` | 否 | 否 | 否 | 是 |
| `visibility:hidden` | 是 | 否 | 否 | 否 |
| `opacity:0` | 是 | 是 | 是 | 否（重绘） |
| `position:absolute` 移出屏幕 | 是 | 是 | 是 | 否 |
- 常用技巧：`text-indent:-9999px`、伪元素遮罩、`clip-path`。

**CSS-4** 🟡 有哪些常见 CSS 布局方案？实现水平垂直居中你会怎么写？
> 来源：<https://www.mianshiya.com/question/1773177018335191041>
- 传统：`float` + `clearfix`；`position:absolute`；`table-cell`。
- 现代：Flex（`display:flex` + `justify-content/align-items`）、Grid（`place-items:center`）、`gap` 替代 margin hack。
- 居中：① Flex：`display:flex; justify-content:center; align-items:center`；② Grid：`place-items:center`；③ 绝对定位 + `transform:translate(-50%,-50%)`（不依赖父元素尺寸，推荐）；④ `margin:auto`（仅单轴或需固定宽高时）。

**CSS-5** 🟡 有哪些 CSS 性能优化的技巧？
> 来源：<https://www.mianshiya.com/question/1773178830719115265>
- 减少选择器层级与嵌套深度，避免 `*` 通配符 + 后代选择器。
- 动画只用 `transform` / `opacity`（走合成层，不触发重排重绘），必要时 `will-change`。
- 避免频繁读取 `offsetWidth/Top` 等会强制同步布局的属性，读写分离。
- 用 `contain: strict/content` 限制布局与绘制影响范围；大列表用 `content-visibility: auto`。
- `@import` 换成 `<link>`，CSS 合并压缩，媒体查询按需加载。

---

## 3. JavaScript 语言基础

**JS-1** 🟡 深拷贝和浅拷贝有什么区别？JS 怎么实现深拷贝？
> 来源：<https://www.mianshiya.com/question/1773179610322788354>
- 浅拷贝只复制一层，嵌套对象仍是同一引用：`Object.assign` / 展开运算符 / `Array.prototype.slice`。
- 深拷贝递归复制每一层。实现方式：① `structuredClone`（原生，支持循环引用、Map/Set、但不支持函数/DOM）；② `JSON.parse(JSON.stringify())`（丢 `undefined`/函数/Symbol，`Date` 变字符串，遇循环引用报错）；③ 手写递归 + `WeakMap` 记录已拷贝对象处理循环引用；④ `lodash.cloneDeep`。
- 注意：函数、DOM 节点、`WeakMap` 等无法真正深拷贝。

**JS-2** 🟢 什么是防抖和节流？如何用 JS 实现？
> 来源：<https://www.mianshiya.com/question/1773180517613658113>
- 防抖 debounce：连续触发只执行最后一次，等待 `wait` 后才执行 → 搜索联想、输入校验、表单提交。
- 节流 throttle：固定时间窗口内最多执行一次 → 滚动加载、鼠标移动、resize。
- 实现要点：记录定时器 id，`this` 与参数透传，提供 `cancel`；`lodash` 的 `debounce` 支持 `leading/trailing/maxWait`。

**JS-3** 🟡 JS 中 `Map` 和 `WeakMap` 有什么区别？
> 来源：<https://www.mianshiya.com/question/1773179969673977857>
- `Map`：键可为任意类型、有序（插入序）、可迭代、有 `size`、有 `forEach`。
- `WeakMap`：键只能是**对象或 Symbol**、弱引用（键被回收则条目自动消失）、**不可枚举/不可迭代、无 `size`**、不可 `clear`。
- 典型用途：`WeakMap` 做私有数据、按 DOM 节点缓存数据，避免内存泄漏。

**JS-4** 🟢 什么是箭头函数？能用 `new` 创建箭头函数吗？
> 来源：<https://www.mianshiya.com/question/1773182297827270658>
- 特性：`this` 取定义时的词法作用域（不可被 `call/apply/bind` 改变）；没有自己的 `arguments`（用剩余参数代替）；没有 `prototype` 属性；不能作为构造函数（`new` 抛 `TypeError`）；返回对象字面量需加括号。
- 不能用 `new` 创建。

**JS-5** 🟡 JS 中数组是如何在内存中存储的？
> 来源：<https://www.mianshiya.com/question/1773179845656797186>
- V8 中数组元素连续存储，但按「元素类型」优化：全是整数 → `PACKED_SMI_ELEMENTS`（直接存值）；混入浮点 → `PACKED_DOUBLE_ELEMENTS`；混入任意对象 → `PACKED_ELEMENTS`（存指针）。
- 变成混合类型或删除元素会产生 `HOLEY_*` 形态，后续访问略慢。
- 超长数组（长度与实际元素差距大）转为字典模式 `DICTIONARY_ELEMENTS`，查找变慢。
- `push` 扩容按约 1.5 倍增长并复制；预分配 `new Array(n)` 可能造成 hole。

---

## 4. 异步编程与事件循环

**ASYNC-1** 🟡 介绍一下 JS 中 `setTimeout` 的运行机制 / 事件循环
> 来源：<https://www.mianshiya.com/question/1773181875494412289>
- 单线程 + 任务队列：同步代码执行完 → 清空微任务队列 → 取一个宏任务执行 → 再清微任务，循环。
- 宏任务：`setTimeout/setInterval`、I/O、UI 事件、`MessageChannel`。微任务：`Promise.then/catch/finally`、`queueMicrotask`、`MutationObserver`。
- Node.js 额外：`process.nextTick` 优先于 Promise 微任务队列；libuv 分 timers/poll/check/close 阶段。

**ASYNC-2** 🟡 什么是前端异步编程？Promise、async/await 的作用与用法
> 来源：<https://www.mianshiya.com/question/1771012709932871681>
- `Promise` 三态 pending/fulfilled/rejected，状态只能变一次；`.then/.catch/.finally` 返回新 Promise 支持链式；`Promise.all`（任一失败即失败）、`allSettled`、`race`、`any`。
- `async/await` 是 Promise 的语法糖：`async` 函数返回 Promise，`await` 会挂起当前函数并把后续代码放入微任务；用 `try/catch` 捕获异常；`for await...of` 处理异步迭代器。
- 常见坑：`await` 在循环中串行导致请求慢，用 `Promise.all` 并发。

**ASYNC-3** 🟡 JS 如何顺序执行 10 个异步任务？
> 来源：<https://www.mianshiya.com/question/1773181719361445890>
- 链式串行：`tasks.reduce((p, t) => p.then(() => t()), Promise.resolve())`。
- `for await (const t of asyncIterable) { await t() }` 依次等待。
- 批量接口优先：合并请求或 `Promise.all` 并发 + 按结果排序，串行只在有依赖时使用。

**ASYNC-4** 🟢 JS 中如何中止网络请求？
> 来源：<https://www.mianshiya.com/question/1773179304394448897>
- `fetch` + `AbortController`：`controller.abort()`，通过 `signal` 传给 fetch。
- axios：`AbortController`（新版本）或 `CancelToken`（旧版）。
- `XMLHttpRequest.abort()`。
- 组件卸载 / 路由切换时中止，避免竞态与内存泄漏。

**ASYNC-5** 🟡 怎么用 JS 实现大型文件上传？要考虑哪些问题？
> 来源：<https://www.mianshiya.com/question/1773182079404695554>
- 切片：`Blob.slice` 按固定大小切分并记录 `start/end`。
- 并发控制：请求池限制并发数（避免打满带宽）。
- 完整性：用 Web Worker 计算文件 hash 校验；记录已上传分片，支持**断点续传**与**秒传**。
- 合并：全部完成后调用服务端合并接口，注意分片顺序与失败重试。

---

## 5. TypeScript

**TS-1** 🟡 TypeScript 的类型别名和接口有什么区别？
> 来源：<https://www.mianshiya.com/question/1810656264628260866>
- `interface`：**声明合并**、可 `extends` 类/接口、可实现类；不能用于联合类型、映射类型、函数类型别名。
- `type`：**可以**联合/交叉/条件/映射/模板字面量类型；不能被 `extends` 合并（3.0 前）。
- 实践：描述对象结构用 `interface`，组合复杂类型用 `type`。

**TS-2** 🟡 `unknown` 和 `any` 有什么区别？
> 来源：<https://www.mianshiya.com/question/1810656265571979265>
- `any`：关闭类型检查，所有操作放行，错误推迟到运行时。
- `unknown`：top type（任何值的父类型），**必须先收窄**（typeof/instanceof/类型谓词/断言）才能使用，是 `any` 的安全替代。

**TS-3** 🟡 TypeScript 的泛型、`infer`、条件类型分别有什么作用？
> 来源：<https://www.mianshiya.com/question/1810656265903329281>、<https://www.mianshiya.com/question/1810656265802665986>、<https://www.mianshiya.com/question/1810656266100461570>
- 泛型：`<T>` 让类型参数化，`T extends约束`，默认泛型 `<T = unknown>`，泛型约束与推断。
- `infer`：在条件类型中从实参类型"反推"出子类型，如 `type Unwrap<T> = T extends Promise<infer U> ? U : T`。
- 条件类型：`T extends U ? X : Y`； distributive（`T` 为 naked type param 时对联合类型逐个分发）；常配合 `infer` 做类型体操。

**TS-4** 🟡 TypeScript 中如何做类型收窄（narrowing）？
> 来源：延伸自 <https://www.mianshiya.com/question/1810656263013453825>
- `typeof x === 'string'`、`instanceof`、`in`、真值判断、判别式（discriminant union）+ `switch`。
- 自定义类型守卫：`function isFoo(v: unknown): v is Foo`。
- `as const` 得到字面量类型与只读元组。
- 兜底断言 `as Foo`，但尽量用守卫代替断言。

**TS-5** 🟡 `readonly`、`static`、类成员可见性分别有什么作用？
> 来源：<https://www.mianshiya.com/question/1810656265001553922>、<https://www.mianshiya.com/question/1810656264900890626>
- `readonly`：编译期只读（`readonly` 数组只读元素但仍可 push 元素），配合 `as const`。
- `static`：成员属于类本身而非实例，可用于静态方法/静态属性/静态块。
- 可见性：`public`（默认）、`protected`（子类可访问）、`private`（仅类内，编译期约束）。

---

## 6. React

**REACT-1** 🟡 什么是 Virtual DOM？它一定更快吗？React 为什么用它提升性能？
> 来源：<https://www.mianshiya.com/question/1772209331631075329>、<https://www.mianshiya.com/question/1817828036632944641>
- 思想：JS 对象描述 UI 树 → diff 出最小变更 → 批量提交到真实 DOM。优势：声明式编程、跨平台（React Native）、避免直接操作 DOM 的错误、批量更新减少重排。
- 不一定更快：首次渲染要构建虚拟树，diff 本身有成本；小而频繁的更新直接改 DOM 可能更快。React 18 的并发渲染（transition/并发特性）进一步优化调度。
- 关键：`key` 决定节点复用与移动判定，`key` 不当会造成状态错位与无谓重建。

**REACT-2** 🟡 React Hooks 里最容易踩的坑是什么？（闭包/依赖）
> 来源：<https://www.mianshiya.com/question/1772210034734837761>、<https://www.mianshiya.com/question/1773189173906333697>
- `useEffect` 依赖数组决定何时重跑；遗漏依赖 → 读到过期值（stale closure）。
- 解决：补全依赖、用函数式更新 `setState(prev => ...)`、用 `useRef` 保存最新值、拆分 Effect、把纯计算放 `useMemo`。
- 自定义 Hook 需正确透传依赖；`useEffect` 返回函数用于清理（定时器、事件监听、订阅、请求中止）。
- 常见 Hook：`useState`、`useEffect`、`useRef`、`useMemo`、`useCallback`、`useContext`、`useReducer`、`useLayoutEffect`、`useSyncExternalStore`。

**REACT-3** 🟡 `React.memo()` 和 `useMemo()` 有什么区别？
> 来源：<https://www.mianshiya.com/question/1773190029888282626>
- `React.memo`：组件级 memo，对 props 做**浅比较**，相同则跳过子组件重渲染。
- `useMemo`：在组件内**缓存一个值**（计算结果或对象引用），依赖不变则复用。
- `useCallback` 是缓存函数引用的特例（`useMemo(() => fn, deps)`）。
- 注意：`memo` 失效的常见原因是 props 每次新建对象/函数，或 context 变化导致全量更新；`useMemo` 不能替代语义化 memo。

**REACT-4** 🟡 React 组件之间怎么通信？
> 来源：<https://www.mianshiya.com/question/1773189888045309954>
- 自上而下：`props`（含 `children`/`render props`）；单向数据流，父控子。
- 向上：子组件调用父组件传入的回调。
- 跨层级：`Context`（适合主题、语言等低频变更；React 18 可用 `use` + `useSyncExternalStore` 优化）。
- 复杂全局状态：Redux / Zustand / MobX 等，Redux 用 reducer + 中间件处理异步与副作用（thunk、redux-saga）。
- 引用共享：`ref` + `useImperativeHandle`；非 React 生态（第三方图表、地图实例）也常用 ref 通信。

**REACT-5** 🟡 React 组件的生命周期有哪些？函数组件怎么替代？
> 来源：<https://www.mianshiya.com/question/1772208970740576258>
- 类组件：`constructor → getDerivedStateFromProps → componentDidMount → shouldComponentUpdate → getSnapshotBeforeUpdate → componentDidUpdate → componentWillUnmount`。
- 函数组件用 `useEffect` 承担 `componentDidMount/DidUpdate/WillUnmount`（按依赖重跑，返回值即清理函数）；`useLayoutEffect` 对应同步阶段（DOM 变更后、绘制前），用于测量、聚焦、动画，避免 SSR 警告。
- `shouldComponentUpdate` → `React.memo` + `useMemo/useCallback`。
- React 18：`StrictMode` 下 effect 会二次执行以暴露副作用问题。

---

## 7. Vue

**VUE-1** 🔴 使用 `Object.defineProperty` 做数据劫持有什么缺点？
> 来源：<https://www.mianshiya.com/question/1817828876194177025>
- 无法监听**新增属性**与**删除属性** → Vue2 需 `Vue.set` / `Vue.delete`。
- 无法监听**数组下标变化**与数组长度变化 → 需重写数组方法（`push/splice` 等）来拦截。
- 需递归遍历每个属性（Vue2 初始化时深度遍历），性能开销大。
- Vue3 改用 `Proxy`，可拦截新增/删除、任意 key，惰性代理且能拦截数组下标。

**VUE-2** 🟡 Vue 3 有哪些新特性？相比 Vue 2 有哪些变化？
> 来源：<https://www.mianshiya.com/question/1771013725784911874>
- 响应式：`Proxy` 替代 `defineProperty`，支持删除/新增属性与数组。
- API：Composition API + `<script setup>`（逻辑复用、TS 友好）；`setup` 替代 `data/created` 前的逻辑。
- 性能：编译期优化（静态提升、Patch Flag）、Tree-shaking 更好、更小运行时（不再需要 `Vue.set`）。
- 新增：`Teleport`、`Suspense`、`defineCustomElement`（自定义元素）、`v-model` 多值、Fragment（多根节点）、`emits` 选项。

**VUE-3** 🟡 Vue 中 `computed` 和 `watch` 有什么区别？分别适用于什么场景？
> 来源：<https://www.mianshiya.com/question/1773186189252190210>
- `computed`：**缓存**的派生值，依赖不变则不重算，本质是「有缓存的 getter」，用于格式化、筛选、联动计算；可 `computed` 传参（Vue 3.4+）。
- `watch`（`watchEffect`）：**副作用**，依赖变化时执行回调，常用于请求数据、写缓存、操作 DOM；`deep: true` 深度监听、`immediate` 立即执行、`flush` 控制时机（pre/post/sync）。
- 选型：能用 computed 表达就用 computed；watch 只在有副作用时使用。

**VUE-4** 🟡 说说 Vue 的 diff 算法
> 来源：<https://www.mianshiya.com/question/1773185887534931970>、<https://www.mianshiya.com/question/1817828875967684609>
- 核心是**同层比较 + 双端 diff**（头尾指针向中间收缩）：`key` 相同且标签相同则 patch，不同则直接替换；一轮比较后若剩余一侧有节点则批量创建/移动。
-  Vue2 四指针：oldStartIdx/oldEndIdx/newStartIdx/newEndIdx，先比 `sameVnode`（key + tag），再处理中间剩余的 old/new 列表（移动 + 查 keyMap 复用）。
- `key` 决定节点复用与移动策略；无 key 时按索引匹配，列表中间插入会导致大量重建。

**VUE-5** 🟡 Vue Router 有哪些路由模式？`$route` 和 `$router` 有什么区别？
> 来源：<https://www.mianshiya.com/question/1773188556848717825>、<https://www.mianshiya.com/question/1773186662935912449>
- 模式：`hash`（`#/path`，默认，无需服务端配合）与 `history`（`/path`，需服务端 fallback 到 index.html，否则刷新 404）。
- `$route`：当前路由的**只读**信息对象（`path/params/query/meta/fullPath`）；`$router`：路由**实例**，提供 `push/replace/go/back/forward`。
- 路由守卫：`beforeEach/afterEach`（全局）、`beforeEnter`（单路由）、组件内 `beforeRouteEnter`；常用于登录鉴权与标题动态设置。

---

## 8. Node.js

**NODE-1** 🟢 什么是 Node.js？有哪些特点？适用于哪些场景？
> 来源：<https://www.mianshiya.com/question/1843904417691103234>
- V8 + 事件驱动 + 非阻塞 I/O + 单线程 JS + libuv 线程池。
- 适合：I/O 密集型（API 网关、BFF、SSR、构建工具、实时通信）。
- 不适合：CPU 密集型（用 `worker_threads` 或多进程/集群解决）。
- 生态：npm 巨量包、跨平台。

**NODE-2** 🟡 Express.js 和 Koa.js 有什么区别？
> 来源：<https://www.mianshiya.com/question/1831172730825748481>
- Koa：极简核心、**洋葱模型**中间件（`await next()`）、默认 async/await，官方中间件少、需自己搭（错误处理要自己 try/catch 或用 koa-compose + 错误中间件）。
- Express 5：中间件模型成熟、生态与文档最全、错误处理有约定（`next(err)`），上手快；Express 5 修复了异步错误处理。
- 本仓库服务端用的是自研 Express + ES/Redis（见 `server/src`）。

**NODE-3** 🟢 `package.json` 文件有什么作用？
> 来源：<https://www.mianshiya.com/question/1843904427073761282>
- `name`/`version`（发布到 npm 必填）、`main`/`module`/`exports`（入口）、`type`（ESM/CJS）、`scripts`、`dependencies`/`devDependencies`/`peerDependencies`、`engines`、`browserslist`、`sideEffects`、`workspaces`。
- semver：`^1.2.3` 允许 minor/patch，`~1.2.3` 只允许 patch，`1.2.3` 精确。
- `npm ci` 依据 lock 文件严格安装（CI 首选）。

**NODE-4** 🟡 Node.js 中同步和异步代码有什么区别？事件循环与 I/O 是怎样的？
> 来源：<https://www.mianshiya.com/question/1843904425417011202>
- 同步代码在主线程执行并阻塞后续代码；异步通过事件回调/await 让出主线程。
- libuv 把 I/O 交给线程池（默认 4 线程，`UV_THREADPOOL_SIZE` 可调），完成后回调进入事件循环。
- `Buffer` 用于二进制数据，`Stream`（Readable/Writable）处理大文件流式读写，避免一次性读入内存。
- `process.nextTick` > Promise 微任务 > 宏任务。

**NODE-5** 🟡 npm 包管理与发布：`npm workspaces` 解决了什么问题？如何发布一个包？
> 来源：<https://www.mianshiya.com/question/1831172726589501442>、<https://www.mianshiya.com/question/1831172725381541889>
- workspaces：monorepo 统一管理多包，根目录一次 `npm install`，子包间用 `workspace:` 协议互相依赖，脚本可 `npm run -ws` 批量执行。
- 发布流程：初始化 `npm init` → 完善 `package.json`（name/version/main/files/keywords/repository/license）→ `npm login` → `npm publish`（`--access public` 发布 scoped 包）→ 版本用 `npm version` 升并打 tag。
- `npm cache`：`~/.npm/_cacache` 缓存包，`npm cache verify/clean` 维护；离线安装 `--offline`。
- `peerDependencies` 声明宿主需提供的依赖，避免重复安装。

---

## 9. 前端工程化

**FE-1** 🟡 什么是前端工程化 / 前端模块化？`export default` 和 `module.exports` 有什么区别？
> 来源：<https://www.mianshiya.com/question/1831172725813555202>、<https://www.mianshiya.com/question/1831172725524148225>
- 工程化：模块化、组件化、自动化（构建、lint、测试、CI/CD）、部署，用工程手段提升协作效率与可维护性。
- 模块化演进：命名空间 → CommonJS（运行时加载、require）→ AMD → ESM（**编译期静态分析**、静态 import/export、tree-shaking 前提）。
- `export default` 是 ESM 语法，导出匿名默认值、可有多个导出；`module.exports` 是 CommonJS，导出整个对象、可用 `exports.a` 具名。二者可混用但同一文件不可混写；`export default` 与 `import x from` 对应，`module.exports` 与 `require` 对应。

**FE-2** 🟡 Webpack 的核心概念有哪些？Tree Shaking 和代码分割的原理是什么？
> 来源：<https://www.mianshiya.com/question/1831172726191042562>、<https://www.mianshiya.com/question/1831172726316871681>
- 核心：`entry`/`output`/`module`/`chunk`；**loader** 处理非 JS 资源（转换）；**plugin** 介入构建生命周期（注入变量、压缩、生成 HTML）。
- Tree Shaking：基于 ESM 静态结构 + `package.json` 的 `sideEffects` 标记，摇掉未使用且无副作用的导出；CommonJS 与有副作用的模块无法摇树。
- 代码分割：`import()` 动态导入生成异步 chunk；配合 `splitChunks` 抽公共依赖；`webpack5` 内置 `splitChunks` 优化。

**FE-3** 🟡 Vite 的原理是什么？为什么启动比 Webpack 快？
> 来源：<https://www.mianshiya.com/question/1771015498541051906>
- 开发环境：基于浏览器原生 ESM，**按需编译**——浏览器请求哪个模块才转译哪个（O(模块数) 而非 O(依赖数)）；用 esbuild 做依赖预构建（把 CJS 依赖转 ESM 并合并，减少请求）；HMR 边界清晰、源码级即时更新。
- 生产环境：仍用 Rollup 打包，配合 `manualChunks` 拆分、`terser`/esbuild 压缩、`assetsInlineLimit` 内联小资源。
- 产物优化：动态 import 分包、`rollupOptions.output.manualChunks` 抽 vendor。

**FE-4** 🟡 如何保证项目编码规范？用到哪些技术？各自作用是什么？
> 来源：<https://www.mianshiya.com/question/1772206645779148801>、<https://www.mianshiya.com/question/1772206883709431809>
- ESLint：静态检查 JS/TS 规则（`@umijs/fabric` 预设）。
- Prettier：代码格式化，统一风格（`prettier -c --write`）。
- Stylelint：CSS/Less 规范（本仓库用 `stylelint --fix`）。
- Husky + lint-staged：Git hooks 在提交前只对暂存文件跑检查（`lint-staged`），失败阻止提交。
- commitlint：规范 commit message（如 Conventional Commits）；TypeScript 用 `tsc --noEmit` 做类型检查。
- CI 上再跑一次 `npm run lint` 作为门禁。

**FE-5** 🟡 如何使用 Docker 部署前端项目？
> 来源：<https://www.mianshiya.com/question/1831172725134077954>
- 多阶段构建：builder 阶段 `npm ci && npm run build`，runtime 阶段只拷贝 `dist`（本仓库已有 `Dockerfile`）。
- 静态服务：Nginx（仓库 `docker/nginx.conf` 已配置）托管 `dist`，配置 `try_files` fallback、gzip、缓存头。
- 资源指纹：构建开启 `hash: true`（本仓库 `config/config.ts` 已开启），静态资源长缓存 + HTML 不缓存；`publicPath` 指向 CDN。
- 容器化收益：环境一致、构建可复现、镜像瘦身（`-prune`）、CI 中自动构建推送。

---

## 10. 网络 / HTTP / 跨域

**NET-1** 🟡 如何处理跨域请求？常见方案及优缺点？
> 来源：<https://www.mianshiya.com/question/1772209516365000705>
- **CORS**：官方标准，服务端设 `Access-Control-Allow-Origin` 等响应头；简单请求直接发，预检请求（OPTIONS）需后端配合；支持携带凭证时不能 `*`。
- **JSONP**：利用 `<script>` 不受同源限制，只支持 GET，有注入风险（XSS），已不推荐。
- **开发代理**：本仓库 `config/proxy.ts` + Umi proxy、webpack devServer proxy，绕开浏览器同源限制；生产用 Nginx 反向代理。
- **postMessage**：跨窗口/iframe 通信。
- **WebSocket**：不受同源策略限制（需后端配合）。

**NET-2** 🟡 HTTP 缓存机制是怎样的？强缓存与协商缓存
- 强缓存：命中则不发请求。`Cache-Control: max-age=31536000, immutable`（配合 hash 指纹）、`no-cache`（缓存但每次校验）、`no-store`（不缓存）；老式 `Expires` 已被 `Cache-Control` 取代。
- 协商缓存：发请求但返回 304。`ETag`/`If-None-Match`、`Last-Modified`/`If-Modified-Since`；`ETag` 精度更高。
- 实践：HTML 不缓存，静态资源长缓存 + hash；接口按需 `no-cache`。

**NET-3** 🟡 从输入 URL 到页面显示，发生了什么？
- DNS 解析 → TCP 三次握手 → TLS 握手（HTTPS）→ 发送 HTTP 请求 → 响应 → 浏览器解析 HTML 构建 DOM → 解析 CSS 构建 CSSOM → 合成 Render Tree → Layout（布局/回流）→ Paint → Composite（合成）。
- 优化抓手：减少关键资源数量（关键请求链）、减小资源体积、提前建连（preconnect/dns-prefetch）、服务端渲染减少白屏。

**NET-4** 🟡 HTTP/1.1、HTTP/2、HTTP/3 的区别？
- HTTP/1.1：持久连接，但同一连接上请求需按序返回，存在**队头阻塞**；文本报文。
- HTTP/2：二进制分帧、**多路复用**（一个连接跑多个流）、头部压缩（HPACK）、服务端推送；仍受 TCP 层队头阻塞影响。
- HTTP/3（QUIC）：基于 UDP 自实现可靠传输，**流级**独立队头阻塞、0-RTT 握手、连接迁移。

**NET-5** 🟡 前端常见安全风险与防护手段
- XSS（存储型/反射型/DOM 型）：输出转义、避免 `innerHTML`/拼接 DOM、`CSP`、Cookie 设 `HttpOnly`。
- CSRF：SameSite Cookie、CSRF Token、校验 `Origin/Referer`、敏感操作二次验证。
- 点击劫持：`X-Frame-Options` / `frame-ancestors`；`iframe` 第三方内容用 `sandbox`。
- 供应链安全：锁定 lock 文件、`npm audit`、SRI（`integrity`）校验 CDN 资源；敏感信息不要打进前端包（见本仓库 `.env` 与 `publicPath` CDN 策略）。

---

## 11. 性能优化与浏览器渲染

**PERF-1** 🟡 前端性能优化有哪些核心指标？如何衡量？
- 指标：**LCP**（最大内容绘制）、**FCP**（首次内容绘制）、**CLS**（累积布局偏移）、**INP**（交互到下一次绘制）、**TTFB**；配合 DevTools Performance / Lighthouse / RUM 真实用户监控。
- 思路：先测量定位瓶颈（网络、主线程、渲染），再优化；区分「实验室数据」与「真实用户指标」。

**PERF-2** 🟡 什么是重排（reflow）与重绘（repaint）？如何避免？
- 重排：几何/尺寸变化，需重新计算布局，代价最高；触发：改变 width/height/margin、读写 offset* 后再写样式、字体加载完成、窗口 resize。
- 重绘：颜色/背景等变化，不涉及布局；触发：color/background/box-shadow。
- 合成：transform/opacity 由合成线程处理，最省。
- 优化：读写分离（批量读一次再批量写）、用 transform 代替 top/left 动画、`contain`/`content-visibility` 隔离、`will-change` 慎用（过多反而耗内存）。

**PERF-3** 🟡 React 路由懒加载的原理是什么？还有哪些加载性能优化手段？
> 来源：<https://www.mianshiya.com/question/1773189002707427330>
- 原理：`import()` 返回 Promise，编译为独立 chunk 请求；配合 `React.lazy` + `<Suspense>` 渲染加载态（Vue 用 `() => import()` + 路由懒加载）。
- 其他手段：图片懒加载与响应式（`srcset`/`loading="lazy"`）、`preload/prefetch` 提前建连、CDN + Brotli/Gzip、首屏数据与接口并行请求、骨架屏消除布局抖动。

**PERF-4** 🟡 长列表（上千行）如何优化？
- 虚拟滚动：只渲染可视区域 + 缓冲区，用容器 `padding/transform` 模拟总高度，`scrollTop` 计算可视区间；`react-window`/`react-virtualized`/`vue-virtual-scroller` 等现成方案。
- 分页 / 无限滚动 + 上拉加载；用 IntersectionObserver 做触底与图片懒加载；避免每行都创建复杂组件与内联样式对象。

**PERF-5** 🟡 JS 脚本延迟加载有哪些方式？
> 来源：<https://www.mianshiya.com/question/1773181083978915841>
- `defer` / `async`（HTML 层面）、动态 `import()`、`<script type="module">`（默认 defer）、把非关键脚本放到 `requestIdleCallback`、worker 中执行。
- 第三方脚本（如埋点、客服）用 `async` + 延后注入，不阻塞首屏。

---

## 12. 移动端适配与前端场景题

**MOB-1** 🟡 移动端网站和响应式网站有什么区别？项目中如何做移动端适配？
> 来源：<https://www.mianshiya.com/question/1771014079343767553>
- 区别：移动端站点是独立站点（独立域名/模板/UA），响应式是同一套代码适配多端（媒体查询 + 弹性布局）。
- 适配手段：`rem`/`vw` 方案（`postcss-pxt-to-viewport`）配合 flexible.js 或 `vw` 单位；Flex 弹性布局；`@media` 断点（375/414/768）；`viewport` meta 设置 `width=device-width, initial-scale=1`；处理刘海屏安全区 `env(safe-area-inset-bottom)`；输入框字号 ≥16px 防 iOS 自动缩放；1px 边框用 `transform: scaleY(0.5)` 方案。

**MOB-2** 🟡 什么是点击穿透？怎么解决？
> 来源：<https://www.mianshiya.com/question/1773181293622812674>
- 原因：移动端 300ms 点击延迟 + 事件冒泡，父层遮罩/弹层消失前，点击穿透到下层元素触发其行为。
- 解决：优先用 `pointer-events: none` 处理遮罩穿透；`touchstart` + `preventDefault` 消除 300ms 延迟（现代浏览器已移除该延迟，可不用 fastclick）；事件触发后立即隐藏遮罩并 `stopPropagation`；`touch-action: manipulation` 去掉双击缩放延迟。

**MOB-3** 🟡 首屏加载慢，你会怎么排查和优化？
- 排查：DevTools Network/Performance 看关键请求链与主线程长任务、查 LCP 元素与资源体积。
- 优化：路由级懒加载 + 分包、CDN + 缓存策略、图片 WebP/AVIF + 响应式尺寸、预连接关键域名、数据并行请求、骨架屏/流式渲染（SSR/SSG）、把非关键 JS 延后到空闲期。

**MOB-4** 🟡 做一个「题目列表 + 筛选 + 详情」的管理后台页面，你会怎么设计前端实现？
> 来源：延伸自本仓库 `src/pages/Questions`、`src/components/QuestionList`、`src/components/QuestionDetailCard`
- 状态分层：URL query 承载筛选与分页（可分享、可回退），全局态（用户信息、权限）交给全局 store，局部态留在组件内。
- 数据层：统一 `services/question.ts` 封装请求，`utils/request.ts` 统一错误码提示与凭证；分页用服务端分页避免深分页问题；筛选输入做防抖。
- 渲染与体验：长列表虚拟滚动、加载骨架、乐观更新与失败回滚、空态/错误态/加载态三态齐全。
- 组件复用：`FormTagTree`、`TagList`、`CommentItem` 等抽成通用组件；样式用 Less + 主题变量统一。

**MOB-5** 🟡 前端如何做错误监控与埋点？
- 错误捕获：`window.onerror` / `window.addEventListener('error')` 捕获同步错误，`unhandledrejection` 捕获 Promise 未处理异常；框架层用 `ErrorBoundary`（React）、`errorHandler`（Vue3）。
- 上报信息：用户信息、页面/路由、UA、堆栈、sourceMap 还原；Sentry 等商业方案或自建上报接口（可结合本仓库 `server/src/service` 自建）。
- 埋点：设计事件规范（名称、参数、上报时机），用 `requestIdleCallback` 批量上报 + `sendBeacon` 兜底；区分 PV/UV、点击/曝光、性能数据（Web Vitals）。

---

## 使用记录

| 日期 | 发放题目编号 |
|---|---|
| 2026-10-27 | HTML-1, HTML-2, CSS-1, CSS-2, JS-1, JS-2, ASYNC-1, ASYNC-2, TS-1, TS-2, REACT-1, REACT-2, VUE-1, VUE-2, NODE-1, NODE-2, FE-1, FE-2, NET-1, NET-3, PERF-1, PERF-3, MOB-1, MOB-2 |
