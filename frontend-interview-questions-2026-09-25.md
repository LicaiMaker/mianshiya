# 前端每日面试题 · 2026-09-25

> 出题风格参考面试鸭（mianshiya.com）题库，覆盖前端主流技术方向，每个方向 2 道以上。建议自测时间 90 分钟。

---

## 一、HTML / 语义化

**1. 请说明 `<section>`、`<article>`、`<div>`、`<aside>` 在语义上的区别，并分别给出一个合适的典型使用场景。**

**2. 为什么现代前端推崇语义化标签？只使用 `<div>` + class 能否达到同样的可访问性与 SEO 效果？请从屏幕阅读器、SEO、代码可维护性三个维度分析。**

---

## 二、CSS / 布局

**3. 请解释 BFC（Block Formatting Context）的触发条件与作用。能否用 BFC 解决 margin 塌陷和外边距合并问题？**

**4. Flex 布局中 `justify-content: center` 与 `align-items: center` 已经能让子元素居中，为什么还要出现 `place-items: center` / `margin: auto`？它们各自的适用场景是什么？**

**5. 请解释 CSS 盒模型中 `box-sizing: border-box` 与 `content-box` 的区别，以及为什么工程上几乎都默认采用 `border-box`。**

---

## 三、JavaScript 核心

**6. `var`、`let`、`const` 在声明提升、暂时性死区、可重复声明、块级作用域四个维度上有什么本质区别？**

**7. 请写出下面代码的执行结果，并解释：**

```js
console.log(a);
var a = 1;
foo();
function foo() { console.log('foo'); }

console.log(b);
let b = 2;
```

**8. 闭包是什么？它有哪些典型应用场景？又为什么会带来内存泄漏风险？**

**9. 请解释 JavaScript 的事件循环（Event Loop）中宏任务与微任务的执行顺序，并写出 `setTimeout(()=>console.log(1), 0); Promise.resolve().then(()=>console.log(2)); console.log(3);` 的输出与原因。**

---

## 四、ES6+ 特性

**10. 请说出 `Map` / `WeakMap` / `Set` / `WeakSet` 的核心区别，并解释为什么 WeakMap 适合做「对象私有数据存储」。**

**11. 请说明 `Proxy` 与 `Object.defineProperty` 在实现数据响应式时的差异，以及 Vue 3 为何选择 Proxy。**

---

## 五、TypeScript

**12. `interface` 与 `type` 有什么异同？什么场景下必须使用 `interface`，什么场景下必须使用 `type`？**

**13. 请解释 TypeScript 中的「协变」「逆变」「双向协变」分别是什么含义，并说明函数参数为何采用逆变。**

**14. `any`、`unknown`、`never` 的使用边界分别是什么？请举例说明。**

---

## 六、Vue

**15. 请说明 Vue 2 与 Vue 3 在响应式原理上的核心差异，以及为什么 Vue 3 需要 `ref` 与 `reactive` 两套 API。**

**16. 请解释 Vue 中 `computed` 与 `watch` 的区别，并说明 `computed` 的缓存是如何实现的。**

**17. 为什么 Vue 模板里不推荐使用箭头函数？请从 this 绑定与渲染机制两个角度分析。**

---

## 七、React

**18. 请说明 React 中 `useState` 与 `useRef` 的区别，以及为什么 `useState` 的更新「看起来」是异步的。**

**19. 请解释 React 18 中「自动批处理（Automatic Batching）」与「并发模式（Concurrent Mode）」的关系，以及 `useTransition` / `useDeferredValue` 的使用场景。**

**20. 什么是 React Fiber？它解决了什么问题？为什么要把渲染过程变成可中断的？**

---

## 八、Node.js

**21. 请说明 Node.js 的事件循环与浏览器事件循环的差异，特别是 `process.nextTick`、`setImmediate` 与 `setTimeout` 的执行顺序。**

**22. 什么是「回调地狱」？请分别用 Promise、async/await、EventEmitter 三种方案改写一个典型场景。**

---

## 九、浏览器原理

**23. 请描述从输入 URL 到页面渲染完成的完整过程（包含 DNS、TCP、HTTP、缓存、解析、布局、绘制、合成）。**

**24. 浏览器中「重排（Reflow）」与「重绘（Repaint）」有什么区别？分别举出 3 个会触发的操作。**

**25. 请解释 `localStorage`、`sessionStorage`、`cookie`、`IndexedDB` 四种存储方案在容量、有效期、是否随请求发送、API 易用性上的差异。**

---

## 十、计算机网络

**26. HTTP/1.1、HTTP/2、HTTP/3 各自解决了上一代的什么核心问题？请从「队头阻塞」「多路复用」「连接迁移」三个关键词展开。**

**27. 简单说一下 HTTPS 的握手过程，以及为什么需要 CA 证书？**

---

## 十一、性能优化

**28. 请从「加载」「渲染」「运行时」三个阶段分别给出至少 3 个前端性能优化手段。**

**29. Webpack 的分包（SplitChunks）策略有哪些常用配置？`chunks: 'all' / 'initial' / 'async'` 的含义是什么？**

---

## 十二、工程化 / 构建

**30. Webpack 和 Vite 在「开发态」和「生产态」构建思路上有什么根本差异？为什么 Vite 启动速度远快于 Webpack？**

**31. 什么是 Tree Shaking？它生效的前提条件有哪些？CommonJS 模块为什么无法被 Tree Shaking？**

---

## 十三、前端安全

**32. XSS 与 CSRF 的攻击原理分别是什么？请各给出至少 2 种防御手段。**

**33. 什么是 CORS？预检请求（Preflight）在什么条件下会触发？请说明 `Access-Control-Allow-Origin: *` 与指定域名的安全差别。**

---

## 十四、移动端 / 跨端

**34. 移动端 1px 像素问题产生的原因是什么？请至少给出 2 种解决方案并比较优劣。**

**35. 请对比 React Native、Flutter、小程序、原生 H5 容器四种跨端方案的「渲染机制」与「性能天花板」。**

---

> 答题提示：每题先讲原理，再举 1~2 个真实场景，最后给出代码示例或反例。面试官通常更看重「为什么这样做」，而非「答案本身」。