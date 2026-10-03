# 每日前端面试题 - 2026-10-03

> 来源参考：mianshiya.com 及当前仓库 `/workspace`，覆盖前端各技术方向。

---

## 一、HTML（2 道）

**1.1 script 标签的 defer 和 async 有什么区别？它们对 DOMContentLoaded 事件的影响分别是什么？**

参考答案要点：
- 普通 `<script>`：阻塞 HTML 解析，下载并执行完后才继续解析。
- `async`：下载完成后立即中断解析并执行，执行时机不确定，可能在 DOMContentLoaded 之前或之后；**不保证执行顺序**（适合独立脚本，如统计脚本）。
- `defer`：下载不阻塞解析，等 HTML 解析完成后、DOMContentLoaded 触发前按顺序执行；**保证顺序执行**。
- type="module" 的脚本默认带 defer 语义。

**1.2 什么是 FOUC（Flash of Unstyled Content）？如何避免？**

参考答案要点：
- 现象：页面先以默认样式渲染，再突然应用 CSS 样式，导致内容"闪烁"。
- 常见原因：CSS 放在底部、被 `@import` 阻塞、JS 动态注入样式等。
- 避免方式：把 CSS 通过 `<link>` 放在 `<head>` 中、避免使用 `@import`、使用 critical CSS 内联首屏样式、对字体使用 `font-display` 控制。

---

## 二、CSS（2 道）

**2.1 解释 BFC（Block Formatting Context）的概念，如何创建一个 BFC？BFC 能解决哪些布局问题？**

参考答案要点：
- BFC 是独立的渲染区域，内部元素不影响外部，外部也不影响内部。
- 触发条件：`overflow: hidden/auto/scroll`、`float`、`position: absolute/fixed`、`display: inline-block/table-cell/flex/grid`、`root` 元素。
- 解决的问题：清除浮动（防止父元素高度塌陷）、阻止 margin 合并、两栏自适应布局（避免文字环绕）。

**2.2 谈谈 CSS 盒模型，box-sizing: content-box 和 border-box 的区别是什么？**

参考答案要点：
- 标准盒模型（content-box）：width = 内容宽度；总宽度 = width + padding + border。
- IE 盒模型（border-box）：width = 内容 + padding + border；总宽度 = width。
- 推荐全局设置 `*, *::before, *::after { box-sizing: border-box; }`。

---

## 三、JavaScript（2 道）

**3.1 谈谈事件循环（Event Loop）中宏任务和微任务的执行顺序，并举例说明。**

参考答案要点：
- JS 单线程，事件循环协调执行。
- 一次循环：从宏任务队列取一个任务执行 -> 执行过程中产生的微任务全部清空 -> 渲染 -> 取下一个宏任务。
- 常见宏任务：script、setTimeout、setInterval、I/O、UI 渲染。
- 常见微任务：Promise.then/catch/finally、queueMicrotask、MutationObserver、async/await 中 await 后续。
- 例子：

```js
console.log('1');
setTimeout(() => console.log('2'), 0);
Promise.resolve().then(() => console.log('3'));
console.log('4');
// 输出：1 4 3 2
```

**3.2 闭包是什么？闭包的常见使用场景和潜在的内存问题是什么？**

参考答案要点：
- 闭包：函数能够访问其词法作用域中定义的变量，即使该函数在词法作用域外执行。
- 用途：数据封装/私有变量、函数柯里化、防抖节流、模块化。
- 风险：不释放的闭包会持有外部变量引用，导致内存泄漏（特别是 DOM 引用）。解决：手动置空引用、避免在循环中创建大闭包、组件销毁时解绑事件。

---

## 四、TypeScript（2 道）

**4.1 TypeScript 中 `interface` 和 `type` 有什么区别？实际使用中如何取舍？**

参考答案：
- 相同点：都可以描述对象和函数类型。
- 不同点：
  - `interface` 只能描述对象/函数/类结构，支持声明合并（同名会自动合并），可被 `extends` 和 `implements`。
  - `type` 可以描述联合类型、交叉类型、原始类型、元组、映射类型，功能更强大；不支持声明合并。
- 建议：描述对象结构优先用 `interface`（语义清晰、可扩展），涉及联合、工具类型、复杂类型运算时用 `type`。

**4.2 解释 TypeScript 的协变、逆变与双变，并说明 strictFunctionTypes 的作用。**

参考答案：
- 协变：子类型可以赋值给父类型（输出位置常见）。
- 逆变：参数位置期望严格（理想为逆变）。
- 双变：参数既可宽又可严（TS 早期默认，宽松但不安全）。
- `strictFunctionTypes: true` 后，函数参数变为逆变校验（除方法签名外），更安全。
- 实际影响：开发通用类型工具时需注意回调参数的方向。

---

## 五、Vue（2 道）

**5.1 Vue 3 的响应式原理是什么？与 Vue 2 的 Object.defineProperty 相比，Proxy 的优势在哪里？**

参考答案：
- Vue 3 使用 `Proxy` + 反射 `Reflect` 实现响应式。
- 优势：
  - 可以监听数组下标变化和 `push/pop/shift` 等方法。
  - 可以监听动态新增/删除属性（无需 `Vue.set`）。
  - 性能更好：懒代理（lazy reactive），只有访问嵌套对象时才深度代理。
  - 拦截更多操作（has、ownKeys 等）。

**5.2 Vue 3 中 Composition API 的 setup 函数执行时机是什么？和 Vue 2 的 data、methods 相比有什么区别？**

参考答案：
- `setup` 在组件创建之前执行（`beforeCreate` 之前），此时组件实例还未创建，`this` 不可用。
- 与 Options API 对比：
  - Composition API 把相关逻辑（数据、方法、生命周期、计算属性）聚合在一起，逻辑复用更方便（自定义 `useXxx` 函数）。
  - 更好的 TS 类型推导。
  - 与 React Hooks 思想接近，但每次组件实例只执行一次 setup（不像 Hooks 每次渲染都执行）。

---

## 六、React（2 道）

**6.1 React 中 useState 和 useReducer 的使用场景分别是什么？**

参考答案：
- `useState`：适合独立、简单的状态字段。
- `useReducer`：当状态更新逻辑复杂、依赖前一状态、或者多个子状态相互关联时更适合；类似 Redux 的 reducer 模式，便于测试和复用。
- 经验法则：状态字段超过 2~3 个且相互依赖时优先 useReducer。

**6.2 React Hooks 为什么不能在条件语句中调用？React 是如何知道对应哪个 Hook 的？**

参考答案：
- React 用单向链表按调用顺序存储 Hook（current hook、next hook）。
- 每次渲染时按"调用顺序"匹配 hook 状态，若条件分支改变调用顺序，状态就会错位（"hooks 规则"）。
- 因此 React 提供了 ESLint 插件 `eslint-plugin-react-hooks` 来强制约束。
- 注意：React 18+ 引入了编译器（React Forget）尝试优化，但调用顺序约束短期内仍是基础。

---

## 七、Node.js（2 道）

**7.1 Node.js 中的事件循环和浏览器中的事件循环有什么区别？**

参考答案：
- Node 事件循环分阶段：timers -> pending callbacks -> idle, prepare -> poll -> check -> close callbacks。
- 每个阶段处理一类任务（如 timers 处理 setTimeout/setInterval；poll 处理 I/O）。
- `process.nextTick` 和微任务（Promise）的执行时机：每个阶段切换之间会清空微任务队列；`process.nextTick` 优先级高于 Promise 微任务（在每个操作后立即执行，可能造成 I/O 饥饿）。
- 浏览器只关心渲染，Node 还要处理 I/O、libuv 线程池。

**7.2 什么是 EventEmitter？常见的内存泄漏场景有哪些？**

参考答案：
- Node 内置的发布订阅模式，`on/once/emit/removeListener`。
- 常见泄漏：未移除监听器（如重复 `on` 但未 `removeListener`），最大监听数（默认 10）超出时给出警告。
- 解决方案：使用 `once`、`removeListener`、`setMaxListeners`，或在组件销毁时统一清理。

---

## 八、构建工具与工程化（2 道）

**8.1 Vite 为什么开发环境启动很快？和 Webpack 的核心区别是什么？**

参考答案：
- Vite 利用浏览器原生 ESM（`<script type="module">），按需编译，无需打包整个项目；冷启动时间与项目大小基本无关。
- Webpack 启动时需要打包所有依赖；冷启动慢但生态成熟，适合生产环境的复杂优化（splitChunks、loader、plugin 体系）。
- Vite 生产环境仍使用 Rollup 打包，保证兼容性和优化。

**8.2 什么是 Tree Shaking？使用它需要满足什么条件？**

参考答案：
- Tree Shaking：基于 ES Module 静态分析，去除未使用的代码（dead-code elimination）。
- 条件：
  - 代码必须使用 ES Modules（import/export），不能是 CommonJS。
  - package.json 中 `"sideEffects": false`（或显式列出有副作用的文件）。
  - 编译器（如 Terser）启用对应选项。
- 注意：CSS、图片等资源需要对应插件（如 PurgeCSS）才能被摇树。

---

## 九、性能优化（2 道）

**9.1 常见的前端首屏性能优化手段有哪些？**

参考答案：
- 网络层：HTTP/2、HTTP/3、Brotli 压缩、DNS 预解析（`<link rel="dns-prefetch">）、preload/prefetch。
- 资源层：路由/代码分割（dynamic import）、Tree Shaking、图片懒加载 + 现代格式（WebP/AVIF）、字体子集化。
- 渲染层：SSR/SSG、Critical CSS、骨架屏、避免 layout thrashing。
- 运行时：虚拟列表、debounce/throttle、Web Worker、长任务切片（scheduler.yield）。

**9.2 浏览器渲染流水线是怎样的？哪些操作会导致重排（reflow）？**

参考答案：
- 流水线：JS -> Style -> Layout -> Paint -> Composite。
- 重排触发：DOM 几何变化（width、height、margin、display）、读取布局信息（offsetTop、getComputedStyle）等。
- 减少重排：批量修改（DocumentFragment）、transform/opacity 做合成层动画、读写分离、使用 CSS containment。

---

## 十一、浏览器与安全（2 道）

**11.1 常见的 Web 前端攻击方式（XSS / CSRF）是什么？如何防御？**

参考答案：
- XSS：恶意脚本注入到页面中执行。
  - 类型：存储型、反射型、DOM 型。
  - 防御：输入校验、CSP、`httpOnly` cookie、对输出做 HTML 转义（React 默认转义）。
- CSRF：利用用户身份发起跨站请求。
  - 防御：CSRF Token、SameSite Cookie、Referer 校验、关键操作二次确认。

**11.2 浏览器同源策略是什么？CORS 的简单请求和预检请求如何区分？**

参考答案：
- 同源策略：协议 + 域名 + 端口三者一致。限制了跨域读取数据、cookie 等。
- CORS 简单请求：方法为 GET/HEAD/POST、Content-Type 为 text/plain / multipart/form-data / application/x-www-form-urlencoded，且无自定义头。
- 非简单请求：发送 OPTIONS 预检，服务器返回 Access-Control-Allow-Origin/Methods/Headers 等。
- 注意点：携带 cookie 需 `withCredentials: true`，服务端需设置 `Access-Control-Allow-Credentials: true` 且不允许 `*`。

---

## 十二、算法与数据结构（2 道）

**12.1 用 JavaScript 实现一个防抖（debounce）函数，并说明它和节流（throttle）的区别。**

```js
function debounce(fn, wait) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), wait);
  };
}
```

- 防抖：触发后延迟执行，若再次触发则重新计时（最后一次触发为准）。
- 节流：固定间隔执行一次（一定时间内只触发一次），保证频率。

**12.2 请写出二叉树的层序遍历（LeetCode 102）。**

```js
function levelOrder(root) {
  if (!root) return [];
  const res = [], queue = [root];
  while (queue.length) {
    const level = [];
    const size = queue.length;
    for (let i = 0; i < size; i++) {
      const node = queue.shift();
      level.push(node.val);
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    res.push(level);
  }
  return res;
}
```

---

> 共 12 个技术方向、24 道题。可根据公司或岗位需要组合成不同卷次。