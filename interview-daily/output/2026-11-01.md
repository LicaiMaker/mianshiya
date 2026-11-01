# 前端每日面试题 · 2026-11-01

> 共 **76** 题，覆盖 **23** 个前端技术方向，每个方向至少 2 题。题目来自[面试鸭](https://mianshiya.com)前端题库，附官方解析摘要。

## 目录

- **HTML / HTML5**（3 题）— 文档结构、语义化、常见标签与属性、多媒体与离线能力
- **CSS / 布局 / 响应式**（3 题）— 选择器、盒模型、布局（Flex/Grid/定位）、BFC、动画、响应式与移动端适配
- **JavaScript 基础**（4 题）— 数据类型与类型判断、原型与继承、作用域与闭包、this、数组与对象、ES6+ 语法
- **异步编程 / 事件循环**（3 题）— Promise、async/await、事件循环与宏任务微任务、防抖节流、错误处理
- **手写代码 / 代码分析**（3 题）— 经典手写题（Promise、深拷贝、事件总线、LRU 等）与代码阅读分析
- **TypeScript**（3 题）— 类型系统、泛型、类型体操、类型工具与工程配置
- **React 基础与 Hooks**（4 题）— 组件与 Props/State、Hooks 用法、生命周期、受控组件、事件与 key
- **React 原理与进阶**（3 题）— Fiber、虚拟 DOM 与 Diff、渲染调度、版本演进与源码原理
- **React 状态管理**（3 题）— Redux / Mobx / Context / useReducer 的设计理念与实践
- **React / Next.js 生态**（4 题）— React Router、组件库、Hooks 库、Next.js 路由与渲染策略、SSR/SSG
- **Vue 基础与 Vue3**（3 题）— 模板与指令、组件、Composition API、Vue3 新特性与迁移
- **Vue 进阶与原理**（4 题）— 响应式原理、Proxy 动态代理、渲染与 diff、生命周期进阶
- **Vue 状态管理与生态**（3 题）— Vuex / Pinia、Vue Router、Vue CLI、组件库与工具链
- **前端工程化 (Webpack / Vite / Babel / npm)**（4 题）— 构建工具、模块化、包管理、编译转译、脚手架、工程规范与测试
- **前端性能优化**（3 题）— 首屏与加载优化、渲染性能、长列表、缓存与监控
- **移动端 / 跨端 (React Native / 鸿蒙 / Flutter)**（3 题）— React Native、鸿蒙 ArkTS/ArkUI、Flutter/Dart 等跨端与移动端开发
- **Electron / 桌面应用**（3 题）— Electron 主渲染进程模型、窗口管理、IPC 通信、预加载与安全配置
- **GraphQL / 接口数据层**（3 题）— GraphQL schema、query、resolver、分页、缓存与错误处理，Apollo Client 实践
- **WebAssembly / 高性能计算**（3 题）— WASM 基础、模块与内存模型、工具链与性能对比
- **浏览器 / 网络 / Web 安全**（3 题）— 浏览器渲染机制、HTTP 与缓存、跨域、XSS/CSRF、Web 安全与密码存储
- **Node.js**（4 题）— Node 运行时、模块规范、事件循环、Express/Koa 与服务端开发（BFF）
- **前端场景 / 系统设计**（4 题）— 真实项目场景题、架构设计、系统设计与技术选型
- **UI 组件库 / 图表**（3 题）— Ant Design / Element UI / Vant 等组件库与 ECharts 图表

---

## HTML / HTML5

> 文档结构、语义化、常见标签与属性、多媒体与离线能力

### 1. HTML 中，label 标签的作用是什么？如何使用？

**难度：简单**　**标签：HTML**　**热度：4441 次浏览**

**参考答案要点**

`<label>` 标签用于提升表单的可用性和可访问性，它把文本标签和相应的表单控件（如输入框）关联起来，让用户点击标签时，输入焦点自动跳到相应控件上。

作用
1）提升可用性：用户点击 `<label>` 标签时，会自动聚焦到对应的表单控件。
2）增强可访问性：对使用屏幕阅读器的用户尤为重要，屏幕阅读器会读取 `<label>` 的内容，帮助用户理解表单控件的用途。

使用方法
1、包裹控件
将 `<label>` 标签直接包裹表单控件：

```htm

[查看原题与完整解析](https://www.mianshiya.com/question/1810654509467217921)

### 2. 什么是 HTML 语义化？为什么要语义化？

**难度：中等**　**标签：HTML**　**热度：705 次浏览**

[查看原题与完整解析](https://www.mianshiya.com/question/1773176565945950209)

### 3. 前端如何判断一个点是否在 Canvas 的图形内？

**难度：中等**　**标签：前端场景 / JavaScript / Canvas**　**热度：2433 次浏览**

**参考答案要点**

回答重点

前端判断一个点是否在 Canvas 的图形内，最常用的方法是借助 CanvasRenderingContext2D 的 isPointInPath 和 isPointInStroke 这两个 API。

1）isPointInPath 方法

isPointInPath(x, y) 用于判断指定的点（x, y）是否在当前路径（Path）内部。你需要先用 moveTo、lineTo、arc 等方法构建路径，然后调用 isPointInPath。

2）is

**追问要点**

- **前端如何判断一个点是否在 Canvas 的图形内？**
  前端通常使用 CanvasRenderingContext2D 提供的 isPointInPath 和 isPointInStroke 方法来判断。isPointInPath(x, y) 用于判断点是否在路径的填充区域内，isPointInStroke(x, y) 用于判断点是否在路径的描边区域内。使用前需要先通过 moveTo、lineTo、arc 等方法构建好路径。
- **使用 isPointInPath 时需要注意哪些问题？**
  必须确保在调用 isPointInPath 前已经构建好路径；路径会在调用 beginPath 后重置；该方法只对当前路径有效，不会自动识别 Canvas 上已绘制但未重建的图形。
- **如何在 Canvas 中处理多个图形的点击判断？**
  可以为每个图形创建独立的 Path2D 对象并保存，然后在鼠标事件中遍历所有图形路径，依次调用 ctx.isPointInPath(path, x, y) 判断点击点是否在某个图形内，从而实现多图形交互。
- **Path2D 有什么作用？**
  Path2D 允许将路径定义与绘制分离，可以复用路径对象，并用于多个绘制或检测操作。它支持将路径作为参数传给 isPointInPath 和 isPointInStroke，便于管理复杂或多个图形的路径。

[查看原题与完整解析](https://www.mianshiya.com/question/1824744519082479617)

---

## CSS / 布局 / 响应式

> 选择器、盒模型、布局（Flex/Grid/定位）、BFC、动画、响应式与移动端适配

### 4. 什么是替换元素？说说其概念及计算规则

**难度：简单**　**标签：CSS**　**热度：3069 次浏览**

**参考答案要点**

回答重点

替换元素是指在CSS中，元素的内容不是由CSS所控制的，而是由外部资源来决定的，例如图像 (`<img>`)、视频 (`<video>`)、嵌入内容 (`<iframe>`) 等。这类元素的内容及尺寸通常是由其自身的属性或外部资源来决定，浏览器根据资源的固有尺寸来渲染这些元素。

扩展知识

1、**常见的替换元素**：
   - `<img>`：显示外部图片。
   - `<video>`：嵌入外部视频。
   - `<object>`：嵌入外部对象

**追问要点**

- **什么是替换元素？**
  替换元素是指在CSS中，元素的内容不由HTML标签或文本决定，而是由外部资源来控制的元素。例如 `<img>`、`<video>`、`<iframe>` 等，它们的内容和尺寸通常由外部资源（如图片文件、视频文件）的固有属性决定，浏览器根据这些资源的原始尺寸进行渲染。
- **常见的替换元素有哪些？**
  常见的替换元素包括：`<img>`（显示图片）、`<video>`（嵌入视频）、`<object>`（嵌入对象）、`<embed>`（嵌入插件或程序）、`<iframe>`（嵌入另一个HTML文档）等。这些元素的内容来源于外部资源，而非HTML内部的文本内容。
- **替换元素的计算规则是什么？**
  替换元素通常具有固有尺寸（如图片的分辨率），可以通过HTML属性或CSS的 `width` 和 `height` 属性设置其宽高，CSS属性会覆盖固有尺寸。默认使用 `content-box` 盒模型，即设置的宽高不包含padding和border。还可以通过CSS添加边框、内边距、外边距等样式。
- **替换元素与非替换元素的主要区别是什么？**
  主要区别在于内容来源和尺寸控制：替换元素的内容来自外部资源，有固有尺寸；而非替换元素（如 `<div>`、`<p>`）的内容由HTML标签和文本构成，其尺寸完全由CSS控制，没有固有尺寸。

[查看原题与完整解析](https://www.mianshiya.com/question/1810655447166783490)

### 5. 使用 clear 属性清除浮动的原理？

**难度：中等**　**标签：CSS / 布局**　**热度：2258 次浏览**

**参考答案要点**

回答重点
使用 `clear` 属性清除浮动的原理其实很简单。它的主要作用是阻止元素周围的浮动元素影响到它。具体来说，`clear` 属性定义了元素的哪些边不能与前面的浮动元素相邻。

举个例子，如果你有两个左浮动的元素，需要在第三个元素开始一个新的行，那么在第三个元素上使用 `clear: left;` 就可以达到效果。在这一行上，第三个元素的左侧就不会有任何浮动的元素。

扩展知识
1）`clear` 属性的取值：
- `none`：这是默认值，不会清除任何浮

**追问要点**

- **使用 clear 属性清除浮动的原理是什么？**
  clear 属性用于控制元素的边是否允许有浮动元素相邻。当设置 clear: left 时，元素将被下移直到其左侧没有浮动元素；clear: right 同理；clear: both
 则确保两侧都没有浮动元素。这样可以防止浮动元素对后续元素的布局造成影响，从而解决因浮动脱离文档流导致的布局错乱问题。
- **clear 属性有哪些取值？分别有什么作用？**
  clear 属性有四个取值：none（默认值，不清除任何浮动）、left（清除左侧浮动，元素下移到左侧无浮动元素为止）、right（清除右侧浮动）、both（同时清除左右两侧的浮动）。实际开发中常用 both 来确保元素在新的一行开始。
- **为什么需要清除浮动？**
  因为浮动元素会脱离正常的文档流，导致父容器无法正确包含子元素的高度，后续非浮动元素也可能被‘挤上去’，造成布局混乱。清除浮动可以让元素避开浮动元素的影响，恢复正常的文档流布局。
- **如何用伪元素方法清除浮动？**
  通过为父容器添加一个 clearfix 类，并利用 ::after 伪元素插入一个不可见的内容块，设置 display: table 和 clear: both，从而清除内部浮动的影响。这种方式无需额外 HTML 标签，结构更简洁。示例：.clearfix::after { content: ''; display: table; clear: both; }

[查看原题与完整解析](https://www.mianshiya.com/question/1810655449456873473)

### 6. 有哪些默认 display: block 元素和 display: inline 元素？你还知道哪些 display 取值？

**难度：中等**　**标签：CSS**　**热度：1795 次浏览**

**参考答案要点**

回答重点
默认情况下，常见的 `display: block` 元素包括：
1. `<div>`
2. `<p>`
3. `<h1>` 至 `<h6>`
4. `<ul>`
5. `<ol>`
6. `<li>`
7. `<header>`
8. `<footer>`
9. `<section>`
10. `<article>`

而常见的 `display: inline` 元素有：
1. `<span>`
2. `<a>`
3. `<strong>`
4. `<em

**追问要点**

- **常见的 display: block 元素有哪些？**
  常见的 display: block 元素包括：div、p、h1 至 h6、ul、ol、li、header、footer、section、article 等。这些元素默认独占一行，可以设置宽高和盒模型属性。
- **常见的 display: inline 元素有哪些？**
  常见的 display: inline 元素有：span、a、strong、em、img、br、code、s、u、b 等。这些元素不会独占一行，宽高由内容决定，不能直接设置宽高。
- **display 属性有哪些常见取值？**
  display 的常见取值包括：block、inline、inline-block、flex、inline-flex、grid、inline-grid、none、table、table-row、table-cell 等。
- **什么是 display: inline-block？它有什么特点？**
  display: inline-block 使元素表现为行内块级元素，既可以在一行内排列，又能设置宽度、高度和内外边距，常用于需要同行排列且控制尺寸的场景。

[查看原题与完整解析](https://www.mianshiya.com/question/1810655450853576705)

---

## JavaScript 基础

> 数据类型与类型判断、原型与继承、作用域与闭包、this、数组与对象、ES6+ 语法

### 7. 为什么 JavaScript 中 0.1 + 0.2 !== 0.3，如何让其相等？

**难度：中等**　**标签：JavaScript / 数据类型**　**热度：12239 次浏览**

**参考答案要点**

在 JavaScript 中，数字是以二进制浮点数表示的。这种表示方式会导致某些十进制小数在二进制下无法精确表示，例如 0.1 和 0.2。它们在二进制中是无限循环的小数，示例如下：

```
0.1 的二进制表示约为：0.0001100110011001100110011001100110011001100110011001101...

0.2 的二进制表示约为：0.00110011001100110011001100110011001100110011001100110

**追问要点**

- **为什么 JavaScript 中 0.1 + 0.2 不等于 0.3？**
  因为 JavaScript 使用二进制浮点数表示数字，而像 0.1 和 0.2 这样的十进制小数在二进制中是无限循环的，无法被精确表示。当它们相加时，由于精度限制，结果是一个非常接近但不完全等于 0.3 的值，例如 0.30000000000000004，因此使用全等比较时返回 false。
- **JavaScript 中如何解决 0.1 + 0.2 !== 0.3 的问题？**
  可以通过以下方法解决：1）使用 Number.EPSILON 判断两个数的差值是否在可接受的误差范围内；2）使用 toFixed() 方法将结果四舍五入到指定小数位后再转换为数字进行比较；3）使用 toPrecision() 方法控制数值的有效数字位数来减少精度误差。
- **Number.EPSILON 在比较浮点数时的作用是什么？**
  Number.EPSILON 表示 JavaScript 中可以表示的最小差异值，用于定义一个可接受的误差范围。通过判断两个数的绝对差是否小于 Number.EPSILON，可以安全地比较浮点数是否“近似相等”。
- **使用 toFixed() 方法时需要注意什么？**
  toFixed() 方法会返回一个字符串类型的结果，而不是数字类型。因此在进行数值比较之前，需要使用 Number() 或 parseFloat() 将其转换回数字类型，否则可能导致类型不匹配的问题。

[查看原题与完整解析](https://www.mianshiya.com/question/1810886884738539521)

### 8. 说说你对 JS 模块化方案的理解，比如 CommonJS、AMD、CMD、ES Module 分别是什么？

**难度：中等**　**标签：JavaScript**　**热度：279 次浏览**

**参考答案要点**

JS 模块化是指将一个 JS 应用拆分成多个模块或文件，并通过一定的规范或语法定义它们之间的依赖关系，从而达到复用、维护、扩展的目的。常见的 JS 模块化方案有以下几种：

1. CommonJS：一种用于服务器端的模块化规范，主要用于 Node.js，它通过 require 来引入模块，通过 module.exports 或 exports 来导出模块。
2. A

[查看原题与完整解析](https://www.mianshiya.com/question/1773183396873330690)

### 9. 以下 JavaScript 代码的输出结果是什么？请解释原因

**难度：中等**　**标签：JavaScript / 原型 / 代码分析**　**热度：262 次浏览**

**参考答案要点**

输出结果

```结果输出
foo
bar
foo
TypeError: f.bar is not a function
```

代码分析

变量和函数的声明

1）声明构造函数 FuncObj：

-   FuncObj 是一个空的构造函数，function Object 类型。

原型链设置方法

2）给 Object.prototype 添加方法 foo：

-   Object.prototype 是所有 JavaScript 对象的原

**追问要点**

- **FuncObj.foo() 为什么能输出 'foo'？**
  因为 foo 方法被添加到了 Object.prototype 上，而 FuncObj 作为一个函数对象，其原型链最终指向 Object.prototype，因此可以继承并调用 foo 方法。
- **FuncObj.bar() 为什么能输出 'bar'？**
  因为 bar 方法被添加到了 Function.prototype 上，而 FuncObj 是一个函数，其构造函数原型链基于 Function.prototype，因此可以直接访问 bar 方法。
- **f.foo() 为什么能成功调用并输出 'foo'？**
  f 是 FuncObj 的
实例对象，它是一个普通对象，其原型链会指向 Object.prototype，因此可以通过原型链访问到 foo 方法并成功调用。
- **f.bar() 为什么会抛出 TypeError？**
  f 是一个普通对象实例，不是函数，它的原型链不会继承 Function.prototype，因此无法访问定义在其上的 bar 方法，调用时就会报错：f.bar is not a function。

[查看原题与完整解析](https://www.mianshiya.com/question/1810940841976492033)

### 10. 以下 JavaScript 代码的输出结果是什么？请解释原因

**难度：中等**　**标签：JavaScript / 对象 / 作用域 / 代码分析**　**热度：318 次浏览**

**参考答案要点**

输出结果

```结果输出
// 严格模式
undefined
// 非严格模式
2
```

代码分析

全局上下文和函数声明

1）声明 function test：

-   函数 test 被声明。此时只是在全局上下文中定义了 test 函数，函数内部的 console.log(this.num) 实际上并未执行。

2. 声明 function doTest

-   函数 doTest 被声明，它只是简单地调用了 test 函数。同样，函数

**追问要点**

- **这段代码在严格模式和非严格模式下的输出结果分别是什么？**
  在严格模式下输出 undefined，在非严格模式下输出 2。
- **为什么在非严格模式下输出的是 2？**
  因为在非严格模式下，函数 test 被直接调用时，this 指向全局对象（浏览器中是 window）。全局变量 num = 2 被提升为 window.num，因此 this.num 取到的是 2。
- **为什么在严格模式下输出的是 undefi
ned？**
  在严格模式下，函数调用时如果没有明确的调用者，this 的值为 undefined，而不是指向全局对象。因此 this.num 会报错无法读取 undefined 的属性，但因为只是访问属性而非调用方法，所以返回 undefined。
- **test 函数中的 this 指向什么取决于什么？**
  test 函数中的 this 指向取决于它的调用方式。由于 test 是被直接调用（没有通过对象调用），在非严格模式下 this 指向全局对象，在严格模式下为 undefined。

[查看原题与完整解析](https://www.mianshiya.com/question/1810940839476686849)

---

## 异步编程 / 事件循环

> Promise、async/await、事件循环与宏任务微任务、防抖节流、错误处理

### 11. 以下 JavaScript 代码的输出结果是什么？请解释原因

**难度：中等**　**标签：JavaScript / 异步 / 代码分析**　**热度：334 次浏览**

**参考答案要点**

输出结果

```结果输出
promise
```

代码分析

调用 runAsync 并处理 await

1）调用 runAsync 函数:

- 调用 runAsync 函数，立即开始执行。

2）进入 await 表达式并调用 promiseFunc:

- 在 runAsync 函数内部，遇到 await 表达式，它会调用 promiseFunc 函数。
- 进入 promiseFunc 函数，创建一个新的 Promise。在 Promise

**追问要点**

- **以下 JavaScript 代码的输出结果是什么？**
  输出结果是："promise"。
- **为什么只输出 "promise" 而没有输出 "async" 或 "async result"？**
  因为 promiseFunc 返回的 Promise 状态为 rejected，导致 await 处理时抛出异常，runAsync 函数返回一个 rejected 的 Promi
se。由于后续的 .then 没有对应的 .catch 来捕获错误，因此 then 中的代码不会执行，所以 "async" 和 "async result" 都不会被输出。
- **在 promiseFunc 中发生了什么？**
  在 promiseFunc 中创建了一个 Promise，并立即执行了 console.log('promise')，然后调用 reject('error') 将该 Promise 置为 rejected 状态。
- **await 在处理 rejected 的 Promise 时会怎样？**
  当 await 遇到一个 rejected 的 Promise 时，它会中断当前 async 函数的执行，并使该 async 函数返回一个以对应原因（这里是 'error'）rejected 的 Promise。

[查看原题与完整解析](https://www.mianshiya.com/question/1810940838503608321)

### 12. 以下 JavaScript 代码的输出结果是什么？请解释原因

**难度：中等**　**标签：JavaScript / 异步 / 代码分析**　**热度：281 次浏览**

**参考答案要点**

输出结果

```结果输出
main start
promise
main end
promise succeed
timer1
timer
timer succeed
timer2
```

代码分析

1）主线程与同步代码执行

主线程开始执行：主线程首先执行同步代码，输出 "main start"。

2）设置第一个定时器

第一个 setTimeout：设置一个定时器，回调函数将在当前事件循环（宏任务）完成后执行。此回调中的 console.log 将输

**追问要点**

- **JavaScript 中宏任务和微任务的区别是什么？**
  宏任务（如 setTimeout、setInterval、I/O、script 脚本整体执行）由事件循环每次取一个执行；微任务（如 Promise.then、MutationObserver）在当前宏任务结束后立即执行，且会清空整个微任务队列。微任务的执行优先级高于下一个宏任务。
- **为什么 'promise succeed' 在 'main end' 之后输出？**
  因为 Promise 的 then 回调属于微任务，会在
当前宏任务（主线程同步代码）执行完毕后、下一个宏任务执行前立即执行，所以 'promise succeed' 在 'main end' 之后、所有 setTimeout（宏任务）之前输出。
- **为什么 'timer1' 在 'promise succeed' 之后输出？**
  因为 'timer1' 来自第一个 setTimeout 的回调，属于宏任务，而 'promise succeed' 是微任务。事件循环先执行完当前宏任务中的所有微任务，再执行下一个宏任务，因此 'timer1' 在 'promise succeed' 之后输出。
- **为什么 'timer succeed' 在 'timer' 之后输出，而不是在 'timer2' 之后？**
  因为 'timer' 是第二个 setTimeout 的回调（宏任务），其内部创建了一个已解决的 Promise，其 then 回调被加入微任务队列。该微任务在当前宏任务（即 'timer' 的执行）结束后立即执行，因此 'timer succeed' 紧随 'timer' 输出，早于下一个宏任务 'timer2'。

[查看原题与完整解析](https://www.mianshiya.com/question/1810940839023702018)

### 13. setTimeout、setInterval、requestAnimationFrame 各有什么特点？

**难度：中等**　**标签：JavaScript / 异步**　**热度：1370 次浏览**

**参考答案要点**

回答重点

setTimeout、setInterval 和 requestAnimationFrame 是 JavaScript 中三种不同的定时执行机制，其特点和适用场景如下：

1）setTimeout

- 用于延迟执行一段代码。
- 只执行一
次。
- 不保证精确的执行时间，受事件循环影响。

2）setInterval

- 用于按照固定时间间隔重复执行代码。
- 持续执行直到被清除。
- 同样不保证精确的时间间隔。

3）reques

**追问要点**

- **setTimeout 的主要特点是什么？**
  setTimeout 用于延迟执行一段代码，只执行一次。其时间参数表示最小延迟时间，不保证精确执行，实际执行时间受 JavaScript 事件循环影响。
- **setInterval 和 setTimeout 有什么区别？**
  setTimeout 只执行一次回调函数，而 setInterval 会按照指定的时间间隔重复执行，直到被 clearInterval 清除。两者都不保证精确的时间控制，且 setInterval 可能出现回调堆积问题。
- **requestAnimationFrame 是做什么的？**
  requestAnimationFrame 是浏览器专为动画设计的定时器 API，它会在下一次屏幕重绘之前调用回调函数，执行频率与设备屏幕刷新率同步（通常为每秒60帧），能提供更流畅的动画效果。
- **为什么 requestAnimationFrame 比 setTimeout 或 setInterval 更适合做动画？**
  因为 requestAnimationFrame 与屏幕刷新率同步，能够避免不必要的重绘，提升性能和流畅度。同时在页面不可见时会自动暂停，节省 CPU、GPU 和电池资源，而 setTimeout 和 setInterval 不具备这些优化。

[查看原题与完整解析](https://www.mianshiya.com/question/1810877645173325826)

---

## 手写代码 / 代码分析

> 经典手写题（Promise、深拷贝、事件总线、LRU 等）与代码阅读分析

### 14. 如何在 JS 中实现继承（用尽可能多的方式）？请写出具体代码

**难度：中等**　**标签：JavaScript / 前端手写代码**　**热度：4072 次浏览**

**参考答案要点**

题目分析
在 JavaScript 中，实现继承有多种方式，
包括原型链继承、构造函数继承、组合继承、寄生组合继承以及 ES6 的 class 语法。

实现代码

1. 原型链继承

主要通过将子类的原型（prototype）指向父类的实例来实现。优点是实现简单，缺点是所有实例共享父类属性，修改子类实例会影响到所有实例。

```javascript
function Coder() {
    this.type = 'Coder';
}

Coder

**追问要点**

- **JavaScript 中有哪些常见的继承方式？**
  JavaScript 中常见的继承方式有：原型链继承、构造函数继承、组合继承、寄生组合继承以及 ES6 的 class 语法。其中寄生组合继承和 class 语法是目前最推荐的实现方式。
- **原型链继承的实现原理是什么？有什么缺点？**
  原型链继承通过将子类的 prototype 指向父类的实例来实现，从而使子类实例可以访问父类原型上的方法和属性。缺点是所有子类实例共享父类的引用类型属性，修改一个实例会影响其他实例，且无法向父类构造函数传参。
- **构造函数继承如何实现？它解决了什么问题？**
  构造函数继承是在子类构造函数中通过 call 或 apply 调用父类构造函数，从而让每个子类实例都拥有独立的父类属性副本。它解决了原型链继承中属性共享的问题，但无法继承父类原型上的方法。
- **组合继承为什么被称为‘经典继承’？它的主要缺点是什么？**
  组合继承结合了构造函数继承和原型链继承的优点，既能继承父类实例属性
，又能继承原型方法，因此被称为‘经典继承’。其主要缺点是会两次调用父类构造函数，造成性能浪费。

[查看原题与完整解析](https://www.mianshiya.com/question/1820428733589258241)

### 15. 如何使用 JS 解析 URL 参数为对象？请写出具体代码

**难度：中等**　**标签：JavaScript / 前端手写代码**　**热度：642 次浏览**

**参考答案要点**

题目分析

解析 URL 参数是一个非常常见的需求，尤其是在处理 GET 请求和查询参数时。URL 参数通常以键值对的形式存在查询字符串中，例如 `?key1=value1&key2=value2`。目标是将这些参数解析为一个 JavaScript 对象，以便更方便地访问和使用。

实现思路

实现这个需求可以分为以下几个步骤：

1） 获取 URL 的查询字符串部分，即从问号 ? 开始的部分。

2） 去掉查询字符串开头的问号 ?。

3） 将查询字符串按 &

**追问要点**

- **如何使用 JavaScript 将 URL 参数解析为对象？**
  可以通过手动解析查询字符串或使用原生的 URLSearchParams 接口将 URL 参数解析为对象。首先提取 URL 中问号（?）后的查询字符串，然后按 & 分割成键值对，再按 = 分割每个键和值，并使用 decodeURIComponent 解码后存入对象中返回。
- **如何获取 URL 中的查询字符串？**
  可以使用 String.prototype.indexOf('?') 找到查询字符串的起始位置，然后用 slice 方法截取从 ? 之后的部分。或者使用 new URL(url).search 获取查询字符串（包含 ?），也可用 urlObj.searchParams 直接操作参数。
- **如何处理 URL 中编码的参数？**
  应使用 decodeURIComponent 函数对键和值进行解码，以正确解析中文字符或特殊符号等被编码的内容，避免乱码问题。
- **JavaScript 中有没有内置 API 可用于解析 URL 参数？**
  有，现代浏览器提供了 URLSearchParams 接口，可用于方
便地解析和操作查询字符串。例如：new URLSearchParams(new URL(url).search) 可以创建一个可迭代的参数对象。

[查看原题与完整解析](https://www.mianshiya.com/question/1820428736374276097)

### 16. 如何使用 JS 实现数组的乱序输出？请写出具体代码

**难度：简单**　**标签：JavaScript / 前端手写代码**　**热度：440 次浏览**

**参考答案要点**

题目分析

题目要求我们使用 JavaScript 实现数组的乱序输出。乱序输出的意思是将数组中的元素随机打乱顺序。下面详细介绍几种常见的方法:

实现代码

使用 Fisher-Yates 洗牌算法：

Fisher-Yates 洗牌算法是一种高效且公平的随机打乱数组的方法。它通过遍历数组，从后向前随机选择一个元素与当前元素交换位置，从而实现数组的乱序。

```javascript
function shuffleArray(arr) {
    co

**追问要点**

- **如何使用 Fisher-Yates 洗牌算法实现数组乱序？**
  Fisher-Yates 洗牌算法通过从后往前遍历数组，每次随机选择一个位置与当前元素交换。代码如下：
```javascript
function shuffleArray(arr) {
const array = arr.slice();
for (let i = array.length - 1; i > 0; i--) {
const j = Math.floor(Math.random() * (i + 1));
[array[i], array[j]] = [array[j], array[i]];
}
return array;
}
```
该方法时间复杂度为 O(n)，公平且高效。
…
- **能否使用 sort 方法实现数组乱序？有什么问题？**
  可以使用 sort 配合随机比较函数实现乱序：

```javascript
function shuffleArray(arr) {
    return arr.slice().sort(() => Math.random() - 0.5);
}
```

但这种方法不推荐，因为 sort 的行为依赖于内部排序算法，可能导致某些排列概率更高，无法保证公平性。
- **为什么 Fisher-Yates 算法比 sort 更好？**
  Fisher-Yates 算法能保证每个排列出现的概率相等（数学上均匀分布），而 sort 方
法因依赖浏览器的排序实现（如快排、插入排序等），会导致分布不均，因此 Fisher-Yates 更公平、更可靠。
- **如何避免修改原数组？**
  可以通过 arr.slice() 或 [...arr] 创建数组的浅拷贝，在副本上进行操作，从而保护原始数组不被更改。

[查看原题与完整解析](https://www.mianshiya.com/question/1820428730841989121)

---

## TypeScript

> 类型系统、泛型、类型体操、类型工具与工程配置

### 17. 为什么要使用 TypeScript？TypeScript 有哪些常用特性？

**难度：简单**　**标签：TypeScript**　**热度：1419 次浏览**

**参考答案要点**

回答重点

为什么使用 TypeScript？

TypeScript 是 JavaScript 的超集，它为 JavaScript 添加了 **静态类型检查** 和更多现代语言特性（比如箭头函数、解构赋值、模块化等），再配合 WebStorm、VSCode 等主流 IDE，可以实现智能提示、代码补全、自动重构等功能，使得代码更加健壮、可维护性更高。

TypeScript 的常用特性

TypeScript 的特性非常多，在官方文档可以看到详细的介绍，

**追问要点**

- **为什么要使用 TypeScript？**
  TypeScript 是 JavaScript 的超集，提供了静态类型检查，能在编译时发现类型错误，减少运行时异常。它增强了代码的可读性、可维护性和可重构性，尤其适合大型项目和团队协作。同时，TypeScript 支持最新的 ECMAScript 特性，并提供优秀的 IDE 支持，如智能提示、自动补全和重构工具，提升开发效率。
- **TypeScript 的核
心特性是什么？**
  TypeScript 的核心特性是静态类型检查，允许开发者在编码阶段定义变量、函数参数和返回值的类型，从而在编译时捕获类型错误，提高代码健壮性。
- **TypeScript 中接口（Interface）的作用是什么？**
  接口用于定义对象的结构，规定其应包含的属性和方法。它可以用于类型检查，确保传入的对象符合预期格式，使代码更清晰、更易于维护。
- **类型别名（Type Alias）有什么用途？**
  类型别名用于为复杂类型创建简洁的名称，特别适用于联合类型或嵌套对象类型，提高代码可读性和复用性。例如：`type ID = string | number;`。

[查看原题与完整解析](https://www.mianshiya.com/question/1824040092228325377)

### 18. TypeScript 的类型别名和接口有什么区别？

**难度：中等**　**标签：TypeScript**　**热度：2081 次浏览**

**参考答案要点**

回答重点
TypeScript 的类型别名和接口都有助于定义复杂类型，但它们存在一些关键区别：
1）用途不同
2）扩展方式不同
3）合并机制不同

1）用途不同
类型别名（Type Aliases）可以用于定义原始类型、联合类型、元组以及复杂对象等各种类型。接口（Interfaces）则主要用于定义对象类型。

2）扩展方式不同
接口可以通过`extends`关键字进行扩展，而类型别名则需要使用交叉类型 `&` 来进行组合。

3）合并机制不同

**追问要点**

- **TypeScript 中类型别名和接口的主要区别有哪些？**
  主要区别有三点：1）用途不同，类型别名可用于定义原始类型、联合类型、元组等，而接口主要用于定义对象类型；2）扩展方式不同，接口使用 `extends` 
继承，类型别名使用交叉类型 `&` 组合；3）合并机制不同，接口支持声明合并，类型别名不支持。
- **能否用接口定义联合类型？**
  不能。接口不能直接表示联合类型（如 string | number）或元组类型，这是类型别名的优势之一。
- **什么是接口的声明合并？**
  接口的声明合并是指可以多次使用相同的名称定义接口，TypeScript 会自动将这些定义合并成一个接口。例如，在不同位置定义同名的 `User` 接口，最终的 `User` 类型会包含所有属性。
- **类型别名是否可以重复定义？**
  不可以。在 TypeScript 中重复定义同名的类型别名会导致编译错误，因为类型别名不支持声明合并。

[查看原题与完整解析](https://www.mianshiya.com/question/1810656264628260866)

### 19. 什么是 TypeScript 的映射类型？

**难度：中等**　**标签：TypeScript**　**热度：1087 次浏览**

**参考答案要点**

回答重点
TypeScript 的映射类型是一种高级类型，它允许我们根据已有类型生成新的类型。通过使用映射类型，可以将特定的变换应用到类型的属性上，生成一个新的类型。例如，假设我们有一个接口 `Person`，其中包含一些属性，现在我们想要创建一个新类型，将 `Person` 中所有属性都设为可选属性（`Partial`类型）；或者我们想要创建一个新类型，使 `Person` 中所有属性变为只读（`Readonly`类型）。这些操作都可以通过映射类型来实现。

扩

**追问要点**

- **什么是 TypeScript 的映射类型？**
  TypeScript 的映射类型是一种高级类型，它允许我们基于已有的类型生成新的类型。通过遍历已有类型的属性键（keyof T），对每个属性进行变换，从而创建一
个具有新特性的类型。常见的映射类型包括 Partial、Readonly、Pick 和 Record 等。
- **映射类型的基本语法是什么？**
  映射类型的基本语法是：`{ [P in keyof T]: T[P]; }`，其中 T 是源类型，`keyof T` 获取 T 的所有键名，P 遍历这些键名，T[P] 表示对应属性的类型，最终生成一个新类型。
- **如何使用映射类型实现 Partial？**
  Partial 映射类型将原类型的每个属性变为可选。其定义为：`type Partial<T> = { [P in keyof T]?: T[P]; }`，通过在属性后添加 `?` 实现可选。
- **Readonly 映射类型的作用是什么？**
  Readonly 映射类型将原类型的每个属性设为只读，防止被重新赋值。其定义为：`type Readonly<T> = { readonly [P in keyof T]: T[P]; }`。

[查看原题与完整解析](https://www.mianshiya.com/question/1810656266192736258)

---

## React 基础与 Hooks

> 组件与 Props/State、Hooks 用法、生命周期、受控组件、事件与 key

### 20. 如何在 React 中实现一个全局的 Dialog 组件？

**难度：困难**　**标签：React / React进阶 / 组件设计**　**热度：445 次浏览**

**参考答案要点**

回答重点
在 React 中实现一个全局的 Dialog 组件，可以使用 React Context 来管理全局状态，并结合 Portals 技术来实现模态框的展示。大体步骤如下：

1）创建一个 Dialog Context，用于管理 Dialog 的显示与隐藏状态。
2）创建一个 Dialog Provider，提供全局范围内的状态管理和行为。
3）实现全局 Dialog 组件，它会从 Context 中获取状态并根据状态来显示或隐藏自己。
4）通过 Portals

**追问要点**

- **如何在 React 中实现全局状态管理以控制 Dialog 的显示与隐藏？**
  可以使用 React Context API 创建一个 DialogContext，通过 DialogProvider 提供全局的 isOpen（是否打开）、content（弹窗内容）状态以及 openDialog 和 closeDialog 方法，使得任何组件都可以通过 useDialog Hook 访问和控
制对话框的状态。
- **为什么在实现全局 Dialog 时需要使用 React Portals？**
  使用 React Portals 可以将 Dialog 渲染到 body 等远离父组件的 DOM 节点中，避免父组件的 CSS 样式（如 overflow: hidden、z-index 或 transform）对 Dialog 布局造成影响，确保其作为模态框正确展示。
- **如何实现点击遮罩层关闭 Dialog？需要注意什么？**
  可以在 Portal 渲染的外层 div（即 backdrop）上绑定 onClick 事件调用 closeDialog 方法来关闭对话框。同时必须在内部 dialog 容器上阻止事件冒泡（e.stopPropagation），防止点击内容区域也被误判为点击遮罩层而关闭。
- **如何从任意组件中打开一个自定义内容的 Dialog？**
  通过 useDialog 获取 openDialog 方法，传入任意 JSX 内容（如 <div>自定义内容</div>），即可动态渲染该内容到全局 Dialog 中，实现灵活复用。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828047101927426)

### 21. React 的 createElement 和 cloneElement 有什么区别？

**难度：中等**　**标签：React / React基础 / React原理**　**热度：960 次浏览**

**参考答案要点**

回答重点
createElement 和 cloneElement 是 React 中两个用于创建元素的 API，它们有以下主要区别：
1）创建方式不同

createElement 是从零开始创建一个新的 React 元素：

- 需要指定元素类型(type)
- 可以设置新的 props
- 可以添加子元素(children)

cloneElement 是基于现有元素克隆并创建一个新的 React 元素：

- 使用原始元素的 type
- 可以添加或覆

**追问要点**

- **React 中 createElement 和 cloneElement 的主要区别是什么？**
  createElement 是从零创建一个新的 React 元素，需要指定类型、props 和子元素；而 cloneElement 是基于现有元素进行克隆并创建新元素，保留原始元素的 type，并可合并新的 props 或替换 children。
- **createElement 的参数有哪些？**
  createElemen
t 接收三个参数：type（元素类型）、props（属性对象）和 ...children（一个或多个子元素）。
- **cloneElement 如何处理 props 和 children？**
  cloneElement 会将新传入的 props 与原始元素的 props 进行浅合并，而新的 children 会完全替换原有的 children。
- **为什么 cloneElement 不推荐过度使用？**
  因为 cloneElement 会使组件间的数据流向变得不清晰，难以追踪 props 的变化，降低代码可读性和可维护性，建议使用 render props、Context 或自定义 Hook 替代。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828054777503746)

### 22. 在 React 的 JSX 中如何写注释？

**难度：简单**　**标签：React / React基础 / JSX**　**热度：1741 次浏览**

**参考答案要点**

回答重点

在 React JSX 中写注释需要使用特定的语法，主要有以下几种方式：

1）单行注释

在 JSX 中使用单行注释需要包裹在花括号中：

{/*这是一个单行注释*/}

2）多行注释

多行注释同样需要包裹在花括号中：

{/*
  这是一个
  多行注释
*/}

3）行内注释

在标签属性或其他行内位置添加注释：

<div className="container" {/* 这是行内注释 */}>

扩展知

[查看原题与完整解析](https://www.mianshiya.com/question/1817828046430838785)

### 23. 什么是无状态组件？无状态组件的应用场景有哪些？

**难度：简单**　**标签：React / React基础**　**热度：932 次浏览**

**参考答案要点**

回答重点

1）无状态组件的定义

无状态组件是一种最简单的 React 组件形式，它是一个纯函数，接收 props 作为参数并返回 React 元素，不包含内部状态（state）、生命周期方法和副作用。

例如：

```jsx
function Welcome({ name }) {
  return <h1>Hello, {name}</h1>;
}
```

2）无状态组件的特点

1）不使用 state，只依赖传入的 props
2）不包含生

**追问要点**

- **什么是无状态组件？**
  无状态组件是一种简单的 React 组件形式，它是一个纯函数，接收 props 作为输入并返回 React 元素，不包含内部状态（state）、生命周期方法和副作用。它只依赖传入的 props 进行渲染，通常以函数式组件的形式书写。
- **无状态组件有哪些特点？**
  无状态组件的特点包括：不使用 state，只依赖 props；不包含生命周期方法；不使用 this 关键字；通常写成函数式组件；代码简洁，易于测试和维护。
- **无状态组件的应用场景有哪些？**
  主要应用于展示型组件，如纯 UI 展示、根据 props 渲染静态内容；作为可复用的基础组件在多个场景中使用；也适用于性能敏感的场景，因其无状态和无生命周期，渲染开销小，可结合 React.memo 优化性能。
- **如何优化无状态组件的性能？**
  可以通过使用 React.memo 对无状态组件进行包裹，避免不必要的重新渲染。当组件的 props 没有变化时，React.memo 会缓存上一次的渲染结果，从而提升性能。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828059852611586)

---

## React 原理与进阶

> Fiber、虚拟 DOM 与 Diff、渲染调度、版本演进与源码原理

### 24. React 的 setState 的第二个参数作用是什么？

**难度：中等**　**标签：React / React进阶 / React原理**　**热度：410 次浏览**

**参考答案要点**

回答重点
在 React 中，`setState` 方法的第二个参数是一个回调函数。这个回调函数会在组件的状态（state）更新完成并且重新渲染之后立即执行。换句话说，这个回调是你
在状态更新完毕且DOM更新完成后执行额外操作的一种手段。

```jsx
this.setState({ count: this.state.count + 1 }, () => {
  console.log('State has been updated and component re-

**追问要点**

- **React 的 setState 第二个参数的作用是什么？**
  setState 的第二个参数是一个回调函数，它会在状态更新完成并且组件重新渲染后执行。用于在状态更新完成后执行依赖新状态的逻辑操作。
- **为什么 setState 是异步的？**
  setState 是异步的为了提高性能和避免频繁的 DOM 更新。React 会批量合并多个状态更新，减少不必要的渲染，从而提升应用效率。
- **如何在 setState 完成后执行某些操作？**
  可以通过 setState 的第二个参数传入一个回调函数，在状态更新和组件重新渲染后执行该回调，也可以使用封装成 Promise 的方式结合 then 或 async/await 使用。
- **能否用 Promise 封装 setState 以支持 async/await？**
  可以，通过返回一个在 setState 回调中调用 resolve 的 Promise，就能实现 setStateAsync，从而支持 async/await 语法，使代码更清晰易读。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828050138603521)

### 25. 如何在 React 中使用 innerHTML？

**难度：简单**　**标签：React / React进阶 / React原理**　**热度：223 次浏览**

**参考答案要点**

回答重点
在 React 中，你可以使用 `innerHTML` 通过设置组件的 `dangerouslySetInnerHTML` 属性来实现。具体的使用方法如下：

```js
function MyComponent() {
  const htmlString = "<div><strong>Hello World!</strong></div>";

  return (
    <div dangerouslySetInnerHTML={{ __html:

**追问要点**

- **如何在 React 中使用 innerHTML？**
  在 React 中，可以通过设置 `dangerouslySetInnerHTML` 属性来实现类似 `innerHTML` 的功能。需要传递一个对象，其 `__html` 字段包含要插入的 HTML 字符串。例如：`<div dangerouslySetInnerHTML={{ __html: htmlString }} />`。
- **为什么 React 中不直接支持 innerHTML？**
  React 不直接支持 `innerHTML` 是为了防止 XSS 攻击，并鼓励开发者使用声明式组件构建 UI。直接操作 DOM 容易引入安全漏洞，因此 React 提供了更安全的替代方式，如状态驱动渲染和组件化结构。
- **使用 dangerouslySetInnerHTML 有什么风险？**
  `dangerouslySetInnerHTML` 可能导致跨站脚本攻击（XSS），
如果插入的 HTML 来自不可信用户输入（如评论、表单内容），可能执行恶意脚本。因此必须确保内容可信或先进行净化处理。
- **如何安全地使用 dangerouslySetInnerHTML？**
  为安全使用 `dangerouslySetInnerHTML`，应对 HTML 内容进行净化处理。推荐使用如 `DOMPurify` 等库对 HTML 字符串进行消毒，移除潜在危险标签和脚本后再插入。例如：`DOMPurify.sanitize(dirtyHtml)`。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828070887825409)

### 26. 你是否阅读过 React 源码？它的源码有哪些值得学习的地方？

**难度：困难**　**标签：React / React进阶 / React原理**　**热度：310 次浏览**

**参考答案要点**

回答重点
React 的源码中包含了许多值得
借鉴的设计思想和编程技巧：

1) **Virtual DOM 的实现**：React 使用了 Virtual DOM 来提高性能，避免直接操作真实的 DOM。阅读代码可以了解 Virtual DOM 的数据结构和 diff 算法（即 reconciliation 过程），这些知识在其他前端框架甚至在后端的高效渲染中都很有用。
   
2) **Hooks 的实现**：React Hooks 是 React 16.8 引入的一

**追问要点**

- **React 为什么要使用 Virtual DOM？**
  React 使用 Virtual DOM 是为了提高性能。真实 DOM 的操作成本很高，涉及布局、重绘等耗时操作。Virtual DOM 通过在内存中构建虚拟节点树，并利用 diff 算法比对变化，仅将实际变更的部分更新到真实 DOM，从而减少不必要的操作，提升渲染效率。
- **React 的 diff 算法是如何工作的？**
  React 的 diff 算法基于三个核心假设：两个不同类型的元素会产生不同的树结构；可以通过 key 属性来识别列表中的元素；组件的层级结构保持稳定。在此基础上，React 采用分层对比策略，只在同一层级的节点之间进行比较，避免全量遍历，大大提升了 diff 效率。
- **Fiber 架构解决了什么问题？**
  Fiber 架构解决了旧版 React 在协调过程中无法中断、容易阻塞主线程的问题。它将渲染任务拆分为多个可中断的小单元（fiber 节点），结合调度器实现时间切片和优先级调度，使得高优先级更新可以中断低优先级任务，提升了应用的响应能力和流畅性。
- **useEffect 是如何模拟类组件生命周期的？**
  useEffect 可以根据依赖数组的不同实现不同生命周期的效果：空依赖数组相当于 componentDidMount 和 componentWillUnmount；无依赖数组则相当于 componentDidMount 和 componentDidUpdate；返回清理函数时可在组件卸载或重新执行前执行清理逻辑，模拟 componentWillUnmount 和更新前的清理行为。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828070531309569)

---

## React 状态管理

> Redux / Mobx / Context / useReducer 的设计理念与实践

### 27. Redux 由哪些组件构成？

**难度：中等**　**标签：React / React进阶 / Redux / React状态管理**　**热度：204 次浏览**

**参考答案要点**

回答重点

Redux 主要由以下几个核心组件构成：

1）Store

应用状态的集中存储容器，通过 createStore 方法创建。它维护了整个应用的状态树，并提供了一些方法来访问和更新状态。

2）Reducer

纯函数，接收当前状态和 action 作为参数，返回新的状态。它定义了状态如何响应不同的 action 进行更新。

3）Action

描
述状态变化的普通 JavaScript 对象，必须包含 type 属性来表示要执行的

**追问要点**

- **Redux 由哪些核心组件构成？**
  Redux 主要由四个核心组件构成：Store（存储应用状态）、Reducer（定义状态如何更新的纯函数）、Action（描述状态变化的普通对象，必须包含 type 属性）、Middleware（用于扩展功能，如处理异步操作和日志记录）。
- **Store 的作用是什么？**
  Store 是 Redux 中应用状态的集中存储容器，通过 createStore 创建。它维护整个应用的状态树，并提供 getState、dispatch、subscribe 等方法来访问状态、派发 action 和监听状态变化。
- **什么是 Reducer？有什么特点？**
  Reducer 是一个纯函数，接收当前状态 state 和 action 作为参数，返回新的状态。它的特点是无副作用、相同输入始终返回相同输出，且不能直接修改原状态，必须返回新对象以保证状态不可变性。
- **Action 在 Redux 中扮演什么角色？**
  Action 是一个普通 JavaScript 对象，用于描述状态变化意图，必须包含 type 字段表示操作类型，还可以包含其他数据字段（如 payload）。它通过 store.dispatch(action) 被发送到 store，触发状态更新流程。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828073614123009)

### 28. 为什么 Redux 能做到局部渲染？

**难度：困难**　**标签：React / React进阶 / Redux / React状态管理**　**热度：323 次浏览**

**参考答案要点**

回答重点

Redux 实现局部渲染主要依赖以下几个核心机制：

1）选择器订阅机制

通过 connect 或 useSelector 实现组件对 store 的订阅，只订阅组件需要的那部分状态：

```javascript
const mapStateToProps = state => ({
  todos: state.todos,
  // 只订阅 todos，不会订阅其他状态
})

export default connect(mapStat

**追问要点**

- **为什么 Redux 能做到局部渲染？**
  Redux 能做到局部渲染主要依赖于 React-Redux 提供的选择器订阅机制和浅比较更新检查。通过 connect 或 useSelector，组件只会订阅 store 中关心的那部分状态。当 store 更新时，React-Redux 会执行 mapStateToProps 获取新的状态，并使用浅比较（shallowEqual）判断返回值是否变化，只有在数据真正发生变化时才会触发组件重新渲染，从而实现局部更新。
- **React-Redux 如何判断组件是否需要重新渲染？**
  React-Redux 在 store 状态更新后，会重新执行 mapStateToProps 函数获取新的属性值，并使用浅比较（shallowEqual）将新旧属性进行对比。如果发现引用或值有变化，则触发组件重新渲染；否则跳过渲染，避免不必要的更新。
- **什么是 shallowEqual 浅比较？它在 Redux 中的作用是什么？**
  shallowEqual 是一种浅层比较机制，只比较对象的第一层属性。在 Redux 中，它用于判断 mapStateToProps 返回的对象前后是否相同。若第一层的引用未变，则认为数据未变，不触发渲染，从而提升性能。
- **如何优化 Redux 的渲染性能？**
  可以通过以下方式优化：1）使用 reselect 创建记忆化选择器，避免重复计算；2）合理划分状态结构，减少无关状态更新的影响；3）避免在 mapStateToProps 中创建新对象；4）结合 React.memo 对组件进行缓存；5）对大量数据使用虚拟列表或分页加载。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828055150796801)

### 29. Redux 如何实现多个组件之间的通信？多个组件使用相同状态时如何进行管理？

**难度：中等**　**标签：React / React进阶 / Redux / React状态管理**　**热度：3144 次浏览**

**参考答案要点**

回答重点

Redux 通过统一的状态管理实现多组件通信，主要包含以下几个关键点：

1）集中管理状态

所有共享状态都存储在一个统一的 store 对象中，这个 store 是唯一的数据源，确保了数据的一致性。

2）状态更新流程

组件通过 dispatch 发送 action 到 reducer 来更新状态。更新后的状态会通过 store 订阅机制自动通知到所有相关组件。

3）组件访问状态

组件通过 connect 高阶组件或 use

**追问要点**

- **Redux 是如何实现多个组件之间通信的？**
  Redux 通过将应用的共享状态集中存储在单一的 store 中，实现多个组件之间的通信。任何组件都可以通过 dispatch 发送 action 来更新状态，reducer 处理 action 后生成新状态并更新 store。其他组件通过订阅 store（如使用 useSelector 或 connect）获取最新的状态变化，从而实现跨组件的数据传递和同步。
- **Redux 中的 store 有什么作用？**
  store 是 Redux 中用于集中管理应用状态的核心对象，它保存了整个应用的 state 树。store 提供 getState() 获取当前状态、dispatch(action) 更新状态，以及 subscribe(listener) 订阅状态变化的功能，确保所有组件能访问统一的数据源并响应状态更新。
- **action 和 reducer 在 Redux 中分别扮演什么角色？**
  action 是一个描述状态变更的普通对象，包含 type 字段和可选的 payload 数据，用于通知 reducer 需要执行的操作。reducer 是一个纯函数，接收旧的 state 和 action，根据 action.type 计算并返回新的 state，负责定义状态如何随 action 变化。
- **组件如何从 Redux store 中读取状态？**
  类组件可以通过 connect 高阶组件配合 mapStateToProps 将 store 中的状态映射为组件的 props；函数组件可以使用 useSelector Hook 直接从 store 中选择所需的状态片段，每当状态更新时自动重新渲染。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828039220830209)

---

## React / Next.js 生态

> React Router、组件库、Hooks 库、Next.js 路由与渲染策略、SSR/SSG

### 30. Next.js 中 public 目录和 assets 目录有什么区别？

**难度：简单**　**标签：Next.js / Next.js 基础**　**热度：100 次浏览**

**参考答案要点**

回答重点
Next.js 中处理静态资源主要涉及两个概念：public 目录用于存放不需要处理的静态文件，assets（或其他目录）用于存放需要 Webpack 处理的资源。

public 目录下的文件会被直接映射到根路径，不经过 Webpack 处理。比如 `public/logo.png` 可以通过 `/logo.png` 访问。public 目录适合存放 robots.txt、favicon.ico、sitemap.xml 等不需要优化的文件。

```type

**追问要点**

- **Next.js 中 public 目录和 assets 目录的主要区别是什么？**
  public 目录用于存放不需要构建处理的静态文件，如 
favicon.ico、robots.txt 等，文件会直接映射到根路径，不经过 Webpack 处理，也不会有哈希指纹。assets 目录（或自定义目录如 src/assets）用于存放需要 Webpack 处理的资源，如图片、字体等，通过 import 导入后会被构建系统处理，生成带哈希的文件名，支持缓存优化和构建压缩。
- **为什么推荐使用 assets 目录中的资源配合 next/image 组件？**
  因为 next/image 组件可以对导入的资源进行自动优化，包括响应式图片大小调整、格式转换（如 WebP）、懒加载、防止布局偏移等。当使用 import 引入 assets 中的图片时，next/image 能获取图片元数据，实现更智能的优化，提升页面性能。
- **public 目录有哪些使用限制？**
  public 目录下的文件不会被 Webpack 处理，因此没有文件哈希，不利于长期缓存；文件名不能与路由冲突，例如不能存在 public/about.html，因为 /about 可能已被页面路由占用；此外，大量文件会直接复制到输出目录，增加构建时间和部署体积。
- **如何在生产环境中将静态资源部署到 CDN？**
  可以通过配置 next.config.js 中的 assetPrefix 字段，将所有静态资源（包括 public 目录文件和构建产物）指向 CDN 地址。例如设置 assetPrefix: 'https://cdn.example.com' 后，所有静态资源请求都会自动加上该前缀。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796906942046210)

### 31. Next.js 中如何获取数据？有哪些方式？

**难度：中等**　**标签：Next.js / Next.js 数据获取**　**热度：58 次浏览**

**参考答案要点**

回答重点
Next.js 15 提供了多种数据获取方式，根据组件类型和使用场景选择。

**Server Components 中获取数据**：可以直接在组件中使用 async/await，支持 fetch API、数据库查询、文件系统操作等。这是最推荐的方式。

```typescript
// 使用 fetch
export default async function PostsPage() {
  const res = await fetch('https:/

**追问要点**

- **Next.js 中获取数据的主要方式有哪些？**
  Next.js 中获取数据的主要方式包括：在 Server Components 中直接使用 async/await 获取数据；在 Client Components 中使用 useEffect、SWR 或 React Query 等库；通过 API Routes 创建接口供
客户端请求；以及使用 Server Actions 在客户端调用服务器函数。
- **Server Components 中如何获取数据？有什么优势？**
  在 Server Components 中可以直接使用 async/await 进行数据获取，支持 fetch、数据库查询等操作。其优势是无需额外请求开销，数据在服务端预渲染，性能更好，且能直接访问后端资源，是最推荐的方式。
- **Client Components 中如何进行数据获取？常用工具有哪些？**
  在 Client Components 中可以通过 useEffect + fetch 的方式获取数据，也可以使用 SWR 或 React Query 等状态管理库来处理数据请求、缓存和重新验证，适用于需要客户端交互或实时更新的场景。
- **什么是 Server Actions？它在数据获取中起什么作用？**
  Server Actions 是定义在服务端的函数，带有 'use server' 标识，可在 Client Components 中被直接调用。它可以用于提交表单或获取数据，避免编写单独的 API 路由，简化数据变更逻辑。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796912717602818)

### 32. 在 React Router 中如何获取 URL 参数？

**难度：简单**　**标签：React / React基础 / React Router / React库**　**热度：1214 次浏览**

**参考答案要点**

回答重点

在 React Router 中获取 URL 参数主要有以下几种方式：

1）使用 useParams Hook

用于获取动态路由参数（URL 路径中的参数）：

```jsx
import { useParams } from 'react-router-dom';

function UserProfile() {
  const { id } = useParams();
  return <div>用户 ID: {id}</div>;

**追问要点**

- **在 React Router 中如何获取动态路由参数？**
  使用 useParams Hook 可以获取动态路由参数。例如，在路由路径为 '/user/:id' 时，通过 const { id } = useParams(); 即可获取路径中的 id 参数。
- **如何获取 URL 中的查询字符串参数（query parameters）？**
  使用 useSearchParams Hook 来获取和操作查询字符串参数。例如：const [searchParams] = useSearchParams(); 然后通过 searchParams.get('key') 获取指定参数值。
- **useLocation Hook 的作用是什么？**
  useLocation Hook 返回当前 URL 的 location 对象，包含 pathname、search、hash 等信息，可用于监听路由变化或解析完整的 URL 结构。
- **React Router 中有哪几种常见的 URL 参数类型？**
  主要有三种：1）动态路由参数（如 :id），通过 useParams 获取；2）查询字符串参数（?key=value），通过 useSearchParams 获取
；3）State 参数，通过编程式导航传递，不显示在 URL 中，使用 useLocation().state 获取。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828053926060033)

### 33. 使用 create-react-app 创建新应用时，如果遇到卡顿的问题，如何解决？

**难度：中等**　**标签：React / React基础 / React工具**　**热度：1774 次浏览**

**参考答案要点**

回答重点

当使用 create-react-app 创建新应用遇到卡顿问题时，可以从以下几个方面进行优化：

1）使用国内镜像源

将 npm 默认的镜像源替换为国内镜像源，可以显著提升依赖包的下载速度：

临时使用：npm install --registry=<https://registry.npmmirror.com>
永久设置：npm config set registry <https://registry.npmmirror.com>

**追问要点**

- **使用 create-react-app 创建新应用时遇到卡顿，可能的原因有哪些？**
  可能原因包括：npm 默认源位于国外导致下载依赖速度慢、本地缓存损坏、依赖包过多或体积过大、网络环境差、未合理利用缓存机制等。
- **如何通过更换镜像源解决 create-react-app 创建应用卡顿的问题？**
  可以将 npm 的默认镜像源替换为国内镜像源，例如使用命令 npm install --registry=https://registry.npmmirror.com 临时切换，或执行 npm config set registry https://registry.npmmirror.com 永久设置。
- **为什么使用 npm ci 可以提升依赖安装速度？**
  npm ci 是专为持续集成环境设计的安装命令，它会根据 package-lock.json 精确安装依赖，跳过版本解析过程，并且不允许修改依赖树，因此比 npm install 更快更稳定。
- **pnpm 相比于 npm 有什么优势？**
  pnpm 使用硬链接和符号链接管理依赖，避免重复安装相同包，节省磁盘空间并显著提升安装速度；同时支持并行操作，适合大型项目和 CI/CD 环境。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828045361291265)

---

## Vue 基础与 Vue3

> 模板与指令、组件、Composition API、Vue3 新特性与迁移

### 34. Vue 计算属性的函数名和 data 中的属性可以同名吗？为什么？

**难度：简单**　**标签：Vue / Vue基础**　**热度：17599 次浏览**

**参考答案要点**

回答重点

不建议这样定义。

当 `data` 属性和计算属性同名时，Vue 会发出重复定义警告。通过模板或 `this.xxx` 访问该属性时，最终读取的是 `data` 中的值，同名计算属性会被屏蔽，无法按预期使用。

因此，计算属性不能通过与 `data` 属性同名的方式正常对外提供计算结果。

扩展知识

1）命名冲突的本质

`data` 和 `computed` 中定义的属性，最终都需要通过组件实例对外访问。

例如：

```js
expo

**追问要点**

- **Vue 计算属性的函数名和 data 中的属性可以同名吗？**
  语法上可以同名，但不应该这样定义。Vue 会在开发环境中提示重复定义。通过模板或 this.xxx 访问时，同名的 data 属性会优先，计算属性无法按预期对外提供计算结果。
- **为什么 Vue 中 data 和计算属性同名会导致问题？**
  因为 data 属性和计算属性都需要通过组件实例公开访问。名称相同时，二者会争用同一个访问名称。Vue 2 会跳过同名计算属性的实例定义，Vue 3 的组件代理会优先读取 data，最终都会导致同名计算属性被屏蔽。
- **Vue 中 data 和 computed 哪个优先级更高？**
  对于 Options API，通过模板或 this.xxx 读取同名属性时，data 的访问
优先级更高。Vue 2 和 Vue 3 的底层实现有所不同，但最终读取到的都是 data 中的值。
- **Vue 如何提示 data 与计算属性命名冲突？**
  Vue 会在开发环境的浏览器控制台输出警告，提示计算属性已经在 data 中定义。生产环境通常不会输出这类开发警告，因此不能依赖警告发现所有问题。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828876512944130)

### 35. 什么是 Vue 中的 slot？它有什么作用？

**难度：简单**　**标签：Vue / Vue基础**　**热度：22314 次浏览**

**参考答案要点**

回答重点

slot（插槽）是 Vue 中的一个重要功能，它允许我们向组件传递模板内容。主要有以下几个要点：

1）基本概念

插槽是组件内的一个占位符，让我们可以向组件内部插入内容。父组件可以在使用子组件时，在子组件标签内传入内容，这些内容会被渲染到子组件内部的 slot 标签位置。

2）使用方式

子组件中使用 slot 标签定义插槽位置：

```html
<template>
  <div>
    <slot></slot>
  </di

**追问要点**

- **什么是 Vue 中的 slot？**
  Slot（插槽）是 Vue 中用于内容分发的机制，它允许父组件向子组件内部插入自定义内容。子组件通过 <slot> 标签定义占位位置，父组件在使用子组件时，可以在
其标签内传递模板内容，这些内容会渲染到对应插槽的位置。
- **Vue 中 slot 的主要作用是什么？**
  Slot 的主要作用是实现内容分发和提高组件的可复用性与灵活性。它使得组件可以预留出内容插入的位置，让使用者根据需要传入不同的内容，适用于布局组件、可复用 UI 组件等场景。
- **Vue 中有哪些类型的插槽？**
  Vue 中有三种主要类型的插槽：默认插槽（无名字的插槽）、具名插槽（通过 name 属性标识，可用于多个插槽）和作用域插槽（可以接收子组件传递的数据）。
- **如何使用具名插槽？**
  具名插槽通过在 <slot> 标签上设置 name 属性来定义，例如 <slot name="header"></slot>。父组件使用 <template v-slot:header> 来指定内容插入到对应的插槽中。v-slot:default 可以省略为默认插槽。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828882598879234)

### 36. 什么是 Vue 中的响应式变量？

**难度：中等**　**标签：Vue**　**热度：590 次浏览**

[查看原题与完整解析](https://www.mianshiya.com/question/1773172350255194114)

---

## Vue 进阶与原理

> 响应式原理、Proxy 动态代理、渲染与 diff、生命周期进阶

### 37. Vue 过滤器的作用是什么？如何实现一个 Vue 过滤器？

**难度：简单**　**标签：Vue / Vue进阶**　**热度：472 次浏览**

**参考答案要点**

回答重点
Vue 过滤器的作用主要是对模板数据进行格式化，像数字、日期或字符串的格式化等。它们可以在模板插值和 `v-bind` 表达式中使用，从而帮助开发者更轻松地展现数据。

实现一个 Vue 过滤器大致可以按照以下步骤：
1）定义过滤器。Vue 允许我们全局或局部定义过滤器。
2）在模板中使用定义好的过滤器。

示例代码（实现一个将日期格式化的过滤器）：
1）全局过滤器：
```javascript
Vue.filter('formatDate', fun

**追问要点**

- **Vue 过滤器的主要作用是什么？**
  Vue 过滤器的主要作用是对模板中的数据进行格式化处理，例如格式化日期、数字、字符串等，以便在视图中更友好地展示数据
。它可以在插值表达式 {{ }} 和 v-bind 表达式中使用。
- **Vue 过滤器如何定义和使用？**
  Vue 过滤器可以通过全局或局部方式定义。全局过滤器使用 Vue.filter('name', function) 定义，局部过滤器在组件的 filters 选项中定义。定义后，在模板中通过管道符 | 调用，如 {{ value | filterName }}。
- **Vue 过滤器支持链式调用吗？如果支持，怎么写？**
  是的，Vue 过滤器支持链式调用。可以将多个过滤器串联使用，前一个过滤器的输出作为下一个过滤器的输入。写法为：{{ value | filterA | filterB }}。
- **Vue 过滤器能否接收多个参数？如何传参？**
  可以。除了第一个参数是管道前的值外，过滤器函数还可以接收额外参数。在模板中通过括号传入，如 {{ value | filterName(arg1, arg2) }}，对应过滤器函数的第二、第三个参数。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828896834347010)

### 38. 如何部署 Vue 项目？

**难度：简单**　**标签：Vue / Vue进阶**　**热度：1050 次浏览**

**参考答案要点**

回答重点
部署 Vue 项目主要包括以下几个步骤：
1）开发环境配置。
2）编译打包项目。
3）选择部署方式。
4）配置服务器并上传项目文件。
5）访问并验证项目是否正常运行。

扩展知识
详细步骤：

1）**开发环境配置**：
首先，我们需要确保在开发环境中已经安装 Node.js 和 npm（或者 yarn 作为替代）。接着，需要用 npm 或 yarn 安装 Vue CLI，全局安装方便我们后续的项目创建与开发。
   ```bash
   npm ins

**追问要点**

- **部署 Vue 项目的完整流程是什么？**
  部署 Vue 项目的完整流程包括：1）配置开发环境，安装 Node.js 和 Vue CLI；2）使用 `npm run build` 编译打包项目，生成 dist 文件夹；3）选择部署方式，如静态托管、云服务或传统服务器；4）将 dist 目录下的文件上传至目标服务器或平台；5）访问项目 URL 验证运行状态，并检查路径和服务器配置是否正确。
- **Vue 项目打包命令是什么？打包后输出的文件在哪里？**
  Vue 项目的打包命令是 `npm run build`，该命令会根据 vue.config.js 的配置对项目进行生产环境优化并编译为静态资源，输出文件默认位于项目根目录下的 `dist` 文件夹中。
- **如何在 Vue 项目中配置打包后的静态资源路径？**
  可以通过在项目根目录创建或修改 `vue.config.js` 文件，设置 `publicPath` 选项来控制静态资源的基路径。例如：`module.exports = { publicPath: '/my-app/' }`，这样所有静态资源将基于 `/my-app/` 路径加载。
- **部署 Vue 项目时常用的部署方式有哪些？**
  常用的部署方式包括：使用静态网站托管服务（如 GitHub Pages、Netlify、Vercel），通过云平台部署（如 AWS、Azure、阿里云），或者将打包后的文件通过 FTP/SFTP 上传到传统的自建服务器（如 Nginx、Apache 服务器）。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828885547474945)

### 39. SPA 单页应用的实现方式有哪些？

**难度：中等**　**标签：Vue / Vue进阶**　**热度：1251 次浏览**

**参考答案要点**

回答重点
实现SPA（单页应用）可以通过多种方式，主要有以下几种：

1）使用 Vue.js 等现代前端框架。
2）利用 React.js、Angular.js 等其他流行的前端框架。
3）手动编写原生 JavaScript 实现 SPA。
4）使用现成的 SPA 模板或脚手架工具。

下面，我会具体介绍如何使用 Vue.js 实现一个简单的 SPA 应用，因为这是题目标签中的重点。

扩展知识 

Vue CLI 创建项目
Vue CLI 是 Vue.j

**追问要点**

- **SPA单页应用的实现方式有哪些？**
  SPA（单页应用）的实现方式主要有：1）使用Vue.js等现代前端框架；2）使用React.js、Angular.js等其他流行框架；3）手动编写原生JavaScript实现；4）使用现成的SPA模板或脚手架工具，如Vue CLI、create-react-app等。
- **如何使用Vue.js实现一个简单的SPA？","answe
r":"使用Vue.js实现SPA主要步骤包括：1）通过Vue CLI创建项目；2）安装并配置Vue Router定义路由；3）创建对应的视图组件（如Home.vue、About.vue）；4）在App.vue中使用<router-link>进行导航，并用<router-view>渲染对应组件。"}
60:{"question":"Vue Router的作用是什么？**
  Vue Router是Vue.js官方的路由管理器，它允许我们在不重新加载页面的情况下实现页面跳转，通过映射路径到组件，实现SPA中的多视图切换。
- **如何在Vue项目中安装和使用Vue Router？**
  可以通过npm安装Vue Router：`npm install vue-router`，然后在项目中导入并使用`Vue.use(Router)`注册，再创建Router实例并配置路由规则，最后在Vue实例中挂载该路由器。
- **SPA与多页应用（MPA）的主要区别是什么？**
  SPA只有一个HTML页面，通过JavaScript动态更新内容，页面切换无需重新加载；而MPA每个页面都是独立的HTML文件，跳转时需要重新请求和加载整个页面，体验相对较慢但利于SEO。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828880023576578)

### 40. Vue 的 watch 和计算属性有什么区别？

**难度：中等**　**标签：Vue / Vue进阶**　**热度：653 次浏览**

**参考答案要点**

回答重点
Vue 中的 `watch` 和计算属性（`computed`）都是用来响应数据变化的工具，但是它们的使用场景和特性有所不同。

1）计算属性 `computed` 是基于依赖进行缓存的，只有当依赖发生变化时才会重新计算，适用于依赖其他数据的派生数据。

2）`watch` 监听器允许我们对数据变化做出更复杂的响应，它更适合执行一些副作用操作，例如异步请求或手动操作 DOM。

扩展知识
它们的不同应用场景以及性能影响：

1）**计算属性的优点和应用场

**追问要点**

- **Vue 中 computed 和 watch 的主要区别是什么？**
  computed 是基于依赖的缓存计算，只有当依赖数据变化时才会重新计算，适用于派生数据；而 watch 是监听数
据变化并执行回调，适合处理异步操作或副作用，如 AJAX 请求、DOM 操作等。
- **为什么 computed 具有缓存性，而 methods 没有？**
  computed 会基于其依赖的数据进行缓存，只要依赖不改变，多次访问会直接返回缓存结果；而 methods 每次调用都会执行函数，不会缓存，因此在依赖不变的情况下，computed 性能更高。
- **什么时候应该使用 watch 而不是 computed？**
  当需要在数据变化时执行异步操作（如发送网络请求）或产生副作用（如修改 DOM、存储到 localStorage）时，应使用 watch；而 computed 更适合同步计算且无副作用的场景。
- **watch 如何实现深度监听？**
  通过设置 deep: true 选项，watch 可以监听对象内部嵌套属性的变化。例如：watch: { obj: { handler() {}, deep: true } }，这样即使 obj 的深层属性变化也能触发回调。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828898222661633)

---

## Vue 状态管理与生态

> Vuex / Pinia、Vue Router、Vue CLI、组件库与工具链

### 41. Vue Router 的懒加载如何实现？

**难度：中等**　**标签：Vue / Vue Router / Vue库 / Vue进阶**　**热度：973 次浏览**

**参考答案要点**

回答重点

Vue Router的懒加载是一种优化前端应用性能的技术，它允许我们将路由组件分割成不同的代码块，并且只在访问对应路由时才加载相关组件。这种方式可以显著减小初始加载的JavaScript包体积，提高页面首次加载速度。

Vue Router的懒加载主要通过ES模块的动态导入（Dynamic Import）特性实现。具体实现方式如下：

1）基本语法：

```js
// 将
// import UserDetails from './views/UserD

**追问要点**

- **Vue Router 懒加载的核心实现方式是什么？**
  Vue Router 的懒加载通过 ES 模块的动态导入（Dynamic Import）语法实现，即使用 `() => import('./component.vue')` 的形式定义路由组件。构建工具如 webpack 或 Vite 会自动将该组件打包为独立的代码块（chunk），并在访问对应路由时才异步加载。
- **为什么使用懒加载可以提升应用性能？**
  懒加载将不同路由对应的组件分割成不同的代码块，只在用户访问该路由时才加载对应资源，从而显著减小了初始加载时的 JavaScript 包体积，加快了首屏渲染速度，提
升了用户体验。
- **在 Vue Router 中是否应该使用 defineAsyncComponent 来实现懒加载？**
  不应该。虽然 `defineAsyncComponent` 可以创建异步组件，但在 Vue Router 中推荐直接使用动态导入语法 `() => import()`。这是官方推荐的方式，更简洁且与路由系统集成更好。
- **如何对懒加载的组件进行命名 chunk 优化？**
  在 Webpack 中可以通过注释语法 `/* webpackChunkName: "chunk-name" */` 为动态导入的模块指定名称，使相关组件被打包到同一个 chunk 中。在 Vite 中则需要在 `vite.config.js` 的 `rollupOptions.manualChunks` 中手动配置。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828900974125058)

### 42. 如何解决页面刷新后 Vuex 的 state 数据丢失的问题？

**难度：中等**　**标签：Vue / Vuex / Vue库 / Vue进阶**　**热度：874 次浏览**

**参考答案要点**

回答重点
我们在开发 Vue 应用时，会使用 Vuex 来管理应用的状态。但是一个常见的问题就是，当我们刷新页面时，Vuex 的 state 数据会丢失。要解决这个问题，我们可以通过将 Vuex 的 state 数据持久化到本地存储（如 LocalStorage 或 SessionStorage）来实现。

具体步骤如下：
1）安装 `vuex-persistedstate` 插件，这是一个用于将 Vuex 状态持久化到本地存储的插件。
2）将 `vuex-persis

**追问要点**

- **如何解决页面刷新后 Vuex 的 state 数据丢失问题？**
  可以通过使用 vuex-persistedstate 插件将 Vuex 的 state 持久化到本地存储（如 LocalStorage 或 SessionStorage）中。安装并引入该插件后，将其添加到 Vuex 的 plugins 配置中，即可在页面刷新时自动保存和恢复状态。
- **vuex-persistedstate 插件的安装方法是什么？**
  可以使用 npm 或 yarn 安装 vuex-persistedstate 插件。命令分别为：npm install vuex-persistedstate 或 yarn add vuex-persistedstate。
- **如何配置 vuex-persistedstate 只持久化部分 state 数据？","
answer":"可以在 createPersistedState 插件配置中使用 paths 选项，指定需要持久化的 state 字段路径。例如：plugins: [createPersistedState({ paths: ['user'] })]，这样只有 user 状态会被持久化。"}
65:{"question":"LocalStorage 和 SessionStorage 在 Vuex 持久化中有何区别？**
  LocalStorage 持久化数据长期有效，除非手动清除，否则刷新或关闭页面后依然存在；SessionStorage 则仅在当前会话有效，关闭浏览器标签页或窗口后数据会被清除。可根据需求选择，通过配置 createPersistedState 的 storage 选项设置。
- **为什么敏感数据不建议直接用 vuex-persistedstate 存储在 LocalStorage 中？**
  因为 LocalStorage 存储的数据容易被 XSS 攻击窃取，不适合存储密码、token 等敏感信息。若必须存储，应先加密处理，或结合后端安全机制进行管理。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828899069911041)

### 43. 在 Vue CLI 中，你经常使用的加载器有哪些？

**难度：中等**　**标签：Vue / Vue CLI / Vue工具**　**热度：849 次浏览**

**参考答案要点**

回答重点
在 Vue CLI 中，经常使用的加载器（loader）主要有以下几种：

1）`vue-loader`：这是 Vue 单文件组件（SFC）必不可少的加载器，它能够解析 `.vue` 文件，从而将模板、脚本和样式分离并进行处理。
  
2）`babel-loader`：用于将 ES6+ 的 JavaScript 代码转换为兼容性更好的 ES5 代码，以确保代码能在老旧浏览器中运行。

3）`css-loader` 与 `style-loader`：`css-l

**追问要点**

- **在 Vue CLI 中，vue-loader 的作用是什么？**
  vue-loader 用于解析 Vue 单文件组件（.vue 文件），将其中的模板、脚本和样式部分分离，并交由相应的加载器处理，是支持 .vue 文件开发的核心加载器。
- **babel-loader 在 Vue CLI 项目中起什么作用？**
  babel-loader 用于将 ES6+ 的 JavaScript 代码转换为向后兼容的
 ES5 代码，确保应用能在不支持新语法的旧版浏览器中正常运行。
- **css-loader 和 style-loader 的区别是什么？**
  css-loader 负责解析 CSS 文件及其依赖（如 @import 和 url()）；style-loader 则负责将解析后的 CSS 代码注入到 HTML 页面的 <style> 标签中，使其生效。
- **file-loader 和 url-loader 各自的用途是什么？**
  file-loader 将资源文件（如图片、字体）复制到输出目录并返回其路径；url-loader 可以将小体积文件转换为 base64 Data URL，减少 HTTP 请求，大文件则回退使用 file-loader。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828875497922561)

---

## 前端工程化 (Webpack / Vite / Babel / npm)

> 构建工具、模块化、包管理、编译转译、脚手架、工程规范与测试

### 44. Webpack 的核心原理是什么？

**难度：中等**　**标签：前端工程化 / Webpack**　**热度：1406 次浏览**

**参考答案要点**

回答重点

Webpack 的核心原理是通过模块化的方式将项目中的各种资源（JavaScript、CSS、图片等）进行打包和优化，最终生成可以在浏览器中高效加载的静态文件。其主要工作流程包括以下几个步骤：

1）模块化打包

Webpack 将项目中的所有资源视为模块，通过解析模块之间的依赖关系，递归地将其打包成一个或多个 bundle。

2）Loader 转换

使用 Loader 将非 JavaScript 文件（如 CSS、图片）转换为 Webp

**追问要点**

- **Webpack 的核心原理是什么？**
  Webpack 的核心原理是将项目中的所有资源（如 JavaScript、CSS、图片等）视为模块，通过分析模块间的依赖关系，递归打包成一个或多个 bundle。它利用 Loader 处理非 JavaScript 文件，将其转换为可打包的模块，并通过 Plugin 在构建流程中执行优化、资源管理等扩展功能，最终输出可在浏览器中运行的静态资源。
- **Webpack 是
如何实现模块化打包的？**
  Webpack 从配置的入口文件（entry）开始，解析代码中的模块依赖关系，递归地将每个依赖模块纳入构建过程，形成一个完整的依赖图。然后根据这个依赖图将所有模块打包成一个或多个 bundle 文件，实现模块化打包。
- **Loader 在 Webpack 中的作用是什么？**
  Loader 用于将非 JavaScript 资源（如 CSS、图片、TypeScript 等）转换为 JavaScript 模块，使 Webpack 能够处理这些文件。例如，css-loader 解析 CSS 文件的 import 和 url，style-loader 将 CSS 注入到 DOM 中。
- **Plugin 和 Loader 的区别是什么？**
  Loader 主要用于转换文件类型，将非 JavaScript 文件转换为模块；而 Plugin 则用于执行更广泛的构建任务，在整个编译生命周期中干预打包过程，如生成 HTML 文件、提取 CSS、代码压缩等，功能更加全面和强大。

[查看原题与完整解析](https://www.mianshiya.com/question/1831172727503859714)

### 45. 什么是 npm cache？如何有效管理它？

**难度：中等**　**标签：前端工程化 / npm / 前端包管理**　**热度：1590 次浏览**

**参考答案要点**

回答重点

npm cache 是 npm 用于存储下载的包和相关数据的本地缓存。它的主要作用是加速包的安装过程，减少网络请求次数。

1）缓存作用

npm cache 存储了已下载的包文件，当再次安装相同版本的包时，可以直接从缓存中获取，提升安装速度。

2）缓存管理

有效管理 npm cache 可以避免缓存损坏、节省磁盘空间，并确保安装的包是最新的。

扩展知识

1）查看缓存位置

可以使用以下命令查看 npm

[查看原题与完整解析](https://www.mianshiya.com/question/1831172725251518465)

### 46. 如何在 Webpack 中实现持久化缓存？

**难度：中等**　**标签：前端工程化 / Webpack**　**热度：634 次浏览**

**参考答案要点**

回答重点

Webpack 实现持久化缓存主要通过以下几个关键点：

1）输出文件名使用内容哈希

在生产环境的 webpack 配置中，文件名应包含内容哈希值（contenthash），这样只有文件内容发生变化时，文件名才会改变：

```javascript
module.exports = {
  output: {
    filename: '[name].[contenthash].js',
    chunkFilename: '[nam
e].[c

**追问要点**

- **Webpack 中如何通过文件名实现持久化缓存？**
  在 Webpack 中，可以通过在输出文件名中使用 [contenthash] 来实现持久化缓存。contenthash 根据文件内容生成哈希值，只有当文件内容发生变化时，哈希值才会改变，从而确保浏览器仅在真正需要时重新下载资源，充分利用缓存。
- **为什么推荐使用 contenthash 而不是 hash 或 chunkhash？**
  hash 是整个构建的哈希值，任何文件变动都会导致所有文件哈希变化；chunkhash 基于入口 chunk 的内容，但在多模块共享代码时仍可能导致不必要的缓存失效；而 contenthash 精确基于每个文件的内容，最细粒度地控制缓存，是实现持久化缓存的最佳选择。
- **splitChunks 和 cacheGroups 如何帮助持久化缓存？**
  通过 splitChunks 配置 cacheGroups，可以将第三方库（如 node_modules 中的依赖）提取到独立的 bundle 中。由于第三方库变动较少，分离后其哈希值更稳定，用户可长期缓存，减少重复下载，提升加载性能。
- **runtimeChunk 的作用是什么？**
  runtimeChunk 将 webpack 的运行时代码（如模块加载逻辑、chunk 映射等）提取到单独的文件中。如果不提取，运行时代码会嵌入每个 chunk，导致即使业务代码未变，因运行时更新也会使 chunk 哈希变化，破坏缓存。提取后可避免此类问题，增强缓存稳定性。

[查看原题与完整解析](https://www.mianshiya.com/question/1831172730951577602)

### 47. 如何查看前端项目应该使用的 Node.js 版本？

**难度：简单**　**标签：前端工程化 / Node.js**　**热度：268 次浏览**

**参考答案要点**

如何查看前端项目应该使用的 Node.js 版本？

回答重点

查看前端项目应该使用的 Node.js 版本通常可以通过以下几种方法：

1） package.json 文件：检查项目根目录下的 package.json 文件，通常会在 "engines" 字段中指定所需的 Node.js 版本。例如：

```json
"engines": {
  "node": ">=14.0.0"
}
```

2） .nvmrc 文件：如果项目使用 nvm（Node Ve

**追问要点**

- **如何通过 package.json 文件确定前端项目所需的 Node.js 版本？**
  查看项目根目录下的 package.json 文件，检查其中的 "engines" 字段，该字段会明确指定项目所支持的 Node.js 版本范围。例如："node": ">=14.0.0" 表示需要 Node.js 14.0.0 或更高版本。
- **如果项目中存在 .nvmrc 文件，它有什么作用？**
  .nvmrc 文件用于指定项目所需的 Node.js 版本，通常只包含一个版本号（如 14.17.0）。当使用 nvm 时，运行 `nvm use` 命令会自动读取该文件并切换到对应的 Node.js 版本，确保开发环境一致性。
- **如何使用 nvm 安装和切换不同版本的 Node.js？**
  使用 `nvm install <version>` 安装指定版本的 Node.js，例如 `nvm install 16.15.0`；使用 `nvm use <version>` 切换到该版本，例如 `nvm use 14.17.6`，切换后当前 shell 会话将使用指定版本。
- **如何查看当前已安装的 Node.js 版本？**
  运行 `nvm list` 命令可以列出当前系统中所有通过 nvm 安装的 Node.js 版本，并显示当前正在使用的版本。

[查看原题与完整解析](https://www.mianshiya.com/question/1831172745551949826)

---

## 前端性能优化

> 首屏与加载优化、渲染性能、长列表、缓存与监控

### 48. 企业级 AI 网关项目中，从哪些方面进行了系统优化？请举例说明

**难度：中等**　**标签：性能优化**　**热度：8 次浏览**

**参考答案要点**

系统主要从性能、可用性、安全性、成本和可观测性这 5 个方面进行了全面优化。

下面以性能优化中的**缓存优化**为例详细说明：

**优化背景：**

在项目初期，每次用户请求都需要从数据库查询模型列表、定价信息、路由策略等数据，这些数据虽然不常变化，但查询频繁，给数据库带来了不必要的压力，也增加了接口的响应时间。

**优化方案：**

我采用了 **Redis 缓存 + 本地缓存（Caffeine）** 的多级缓存架构：

**1) 一级缓存（Caffeine 本地缓存

[查看原题与完整解析](https://www.mianshiya.com/question/2039961995763036162)

### 49. 前端如何使用 Webpack 进行高效分包优化？

**难度：中等**　**标签：前端工程化 / Webpack / 前端性能优化**　**热度：2200 次浏览**

**参考答案要点**

回答重点

1）Webpack 分包优化的概念
  
Webpack 的分包优化主要是通过合理地拆分和打包代码，减少浏览器首次加载的资源大小，提高页面的加载速度。通过将应用的代码拆分成多个小的包，浏览器可以按需加载，从而避免一次性加载过多的代码。

2）常见的分包优化策略

Webpack 提供了几种常见的分包优化策略，以下是一些常用的方法：

**入口分
包（Entry Point Splitting）**  

Webpack 允许你配置多个入口文件，这样可以为不同的

**追问要点**

- **什么是 Webpack 的分包优化？**
  Webpack 的分包优化是指通过合理的代码拆分策略，将应用打包成多个较小的文件，从而减少首次加载时的资源体积，提升页面加载速度。通过按需加载和缓存优化，改善用户体验。
- **Webpack 常见的分包优化策略有哪些？**
  常见的分包优化策略包括：入口分包（多入口配置）、公共代码提取（splitChunks）、懒加载（import() 动态导入）、异步模块提取、Tree Shaking（移除未使用代码）以及长缓存优化（contenthash）。
- **如何通过 entry 配置实现入口分包？**
  通过在 webpack 配置中设置多个入口文件，例如 entry: { main: './src/main.js', admin: './src/admin.js' }，Webpack 会为每个入口生成独立的 bundle 文件，适用于多页面应用。
- **splitChunks 的作用是什么？常用配置有哪些？**
  splitChunks 用于提取多个 chunk 之间的公共代码，减少重复打包。常用配置包括 chunks（指定拆分类型）、minSize/maxSize（大小限制）、name（输出名）、cacheGroups（自定义分组规则，如提取 node_modules 中的第三方库）。

[查看原题与完整解析](https://www.mianshiya.com/question/1831172739663147010)

### 50. 有哪些 Vue 性能优化的方法？

**难度：困难**　**标签：Vue / Vue进阶 / 前端性能优化**　**热度：3165 次浏览**

**参考答案要点**

回答重点
Vue 性能优化的方法有很多，重点包括以下几个方面：

1）使用生产环境版本：生产环境版本的 Vue 去掉了一些开发过程中用于调试的警告和提示信息，相比开发环境要轻量得多，性能更高。

2）懒加载与按需加载：利用代码分割技术，按需加载组件和模块，减少初始加载的体积，提高页面加载速度。

3）使用缓存：合理利用 `keep-alive` 标签将不需要频繁更新的组件缓存起来
，避免重复渲染。

4）减少 watch 和 computed 计算的次数：通过优化依赖关系

**追问要点**

- **为什么要使用 Vue 的生产环境版本？**
  生产环境版本的 Vue 移除了开发时的警告和调试信息，文件体积更小，执行效率更高，能显著提升应用性能。
- **如何通过懒加载优化 Vue 应用的性能？**
  利用代码分割和动态导入（如 import()）实现路由或组件的按需加载，减少首屏加载体积，加快页面渲染速度。
- **keep-alive 在 Vue 性能优化中有什么作用？**
  keep-alive 可以缓存不常变化的组件实例，避免重复创建和渲染，提升切换组件时的响应速度和性能。
- **为什么需要减少 watch 和 computed 的计算次数？**
  过多或不必要的侦听器和计算属性会增加依赖追踪开销，优化依赖关系可减少无效更新，提高性能。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828903473930241)

---

## 移动端 / 跨端 (React Native / 鸿蒙 / Flutter)

> React Native、鸿蒙 ArkTS/ArkUI、Flutter/Dart 等跨端与移动端开发

### 51. 鸿蒙开发中的装饰器是什么？有哪些常用的装饰器？

**难度：简单**　**标签：鸿蒙 / ArkTS 装饰器**　**热度：99 次浏览**

**参考答案要点**

回答重点
装饰器是 ArkTS 和 ArkUI 的核心特性，用于给类、方法、属性添加元数据和行为。在鸿蒙开发中，装饰器无处不在，从组件声明到状态管理都离不开装饰器。

最常用的装饰器包括几类。@Component 用于声明自定义组件，告诉 ArkUI 这是一个可复用的 UI 组件。@Entry 用于声明页面入口组件，一个页面必须有一个 @Entry 组件。这两个装饰器是组件开发的基础。

状态管理装饰器包括 @State、@Prop、@Link 等。@State 声明组

**追问要点**

- **鸿蒙开发中的装饰器是什么？**
  装饰器是 ArkTS 和 ArkUI 的核心特性，用于给类、方法、属性添加元数据和行为。在鸿蒙开发中，装饰器广泛应用于组件声明、状态管理、数据传递等方面，帮助开发者更高效地构建 UI 和管理组件状态。
- **鸿蒙开发中有哪些常用的组件声明装饰器？**
  常用的组件声明装饰器有 @Component 和 @Entry。@Component 用于定义一个可复用的自定义 UI 组件；@Entry 标记页面的入口组件，每个页面必须有一个且仅有一个 @Entry 装饰的组件。
- **@State 装饰器的作用是什么？**
  @State 用于声明组件内部的状态变量。当被 @State 装饰的变量发生变化时，ArkUI 会自动触发组件的重新渲染。该变量必须是 struct 类的属性，支持基本类型、对象、数组等，但修改对象属性时需整体重新赋值才能触发更新。
- **@Prop 和 @Link 有什么区别？**
  @Prop 实现父组件向子组件的单向数据传递，子组件不能修改父组件的数据；@Link 实现父子组件间的双向数据绑定，子组件对数据的修改会同步到父组件。选择使用哪个取决于是否需要子组件回传修改。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796783260409857)

### 52. Dart 语言有哪些特点？为什么 Flutter 选择 Dart？

**难度：简单**　**标签：Flutter / Dart 语言**　**热度：261 次浏览**

**参考答案要点**

回答重点
Dart 是 Google 开发的一门编程语言，专门为构建用户界面优化。它的核心特点是支持 JIT（即时编译）和 AOT（提前编译）两种编译模式，这也是 Flutter 选择它的关键原因。

Dart 的主要特点包括：语法简洁现代，如果会 Java 或 JavaScript，学习 Dart 很快。强类型但也支持类型推断，既有类型安全又不繁琐。空安全（Null Safety）能在编译期避免空指针异常。支持异步编程（async/await、Future、Strea

**追问要点**

- **Dart 语言的主要特点是什么？**
  Dart 语言具有语法简洁现代、强类型但支持类型推断、空安全（Null Safety）、支持异步编程（async/await、Future、Stream）、面向对象等特性。它融合了 Java、JavaScript、Kotlin 等语言的优点，学习成本低，同时具备类型安全和开发效率。
- **为什么 Flutter 选择 Dart 作为开发语言？**
  Flutter 选择 Dart 的主要原因是其支持 JIT（即时编译）和 AOT（提前编译）双模式。JIT 模式支持热重载，提升开发效率；AOT 模式在发布时将代码编译为机器码，保证高性能运行。这种平衡开发效率与运行性能的能力是其他语言难以同时实现的。
- **JIT 和 AOT 在 Flutter 开发中分别起到什么作用？**
  在开发阶段，Dart 使用 JIT 模式，支持增量编译，实现毫秒级热重载，极大提升开发效率。在发布阶段，使用 AOT 模式，将 Dart 代码预先编译为原生机器码，提升启动速度和运行性能，接近原生应用体验。
- **Dart 的空安全特性有什么好处？**
  Dart 的空安全特性可以在编译期就发现并阻止可能导致空指针异常的代码，减少运行时崩溃，提高应用的稳定性和安全性，使开发者能更早地修复潜在问题。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796920296710146)

### 53. ArkUI 中常用的基础组件有哪些？各有什么作用？

**难度：简单**　**标签：鸿蒙 / ArkUI 组件**　**热度：98 次浏览**

**参考答案要点**

回答重点
ArkUI 提供了丰富的基础组件，可以分为几大类：容器组件、显示组件、输入组件和导航组件。

容器组件用于布局和组织子组件。Column 是垂直容器，子组件从上到下排列。Row 是水平容器，子组件从左到右排列。Stack 是层叠容器，子组件相互重叠。Flex 是弹性容器，提供灵活的布局方式。这些是最常用的布局组件，大部分界面都用它们构建。

显示组件用于展示内容。Text 显示文本，支持多种样式设置。Image 显示图片，支持本地图片和网络图片。Button

**追问要点**

- **ArkUI中常用的容器组件有哪些？它们的作用分别是什么？**
  ArkUI中常用的容器组件包括Column、Row、Stack和Flex。Column用于垂直排列子组件，从上到下布局；Row用于水平排列子组件，从左到右布局；Stack使子组件层叠显示，支持定位重叠；Flex是弹性布局容器，可根据空间自动调整子组件尺寸，适用于复杂灵活的界面布局。
- **请列举ArkUI中的基本显示组件及其用途。**
  ArkUI中的基本显示组件有Text、Image、Button和Divider。Text用于显示文本内容，支持字体大小、颜色、粗细等样式设置；Image用于展示本地或网络图片；Button是可点击的按钮组件，常用于触发操作；Divider是分割线组件，用于视觉上分隔不同内容区域。
- **ArkUI中常见的输入组件有哪些？它们如何实现用户交互？**
  常见的输入组件包括TextInput、TextArea、Checkbox、Radio、Slider和Toggle。TextInput用于单行文本输入，TextArea支持多行文本输入；Checkbox提供多选功能；Radio实现单选选择；Slider通过滑动选择数值；Toggle是开关组件，用于切换状态。这些组件通过绑定事件和状态，实现与用户的交互。
- **列表和导航类组件在ArkUI中有哪些？适用于什么场景？**
  列表和导航类组件主要包括List、Grid、Swiper和Tabs。List用于高效展示长列表数据，支持滚动和懒加载；Grid以网格形式展示数据，适合相册、菜单等场景；Swiper是轮播组件，常用于广告图或图片展示；Tabs提供标签页切换功能，用于组织不同类别的内容。这些组件在处理大量数据时具有良好的性能表现。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796781519773698)

---

## Electron / 桌面应用

> Electron 主渲染进程模型、窗口管理、IPC 通信、预加载与安全配置

### 54. Electron 中 webContents 是什么？有什么作用？

**难度：简单**　**标签：Electron / webContents**　**热度：133 次浏览**

**参考答案要点**

回答重点
webContents 是 Electron 中负责渲染和控制网页的对象，每个 BrowserWindow 实例都包含一个 webContents 对象。可以把 webContents 理解成网页内容的管理器，它提供了操作和监控网页的各种方法和事件。

webContents 的主要作用包括几个方面。第一是控制网页的加载和导航，比如 loadURL 加载页面、reload 刷新页面、goBack 后退、goForward 前进。第二是与网页内容交互，比如 ex

**追问要点**

- **Electron 中 webContents 是什么？**
  webContents 是 Elec
tron 中负责渲染和控制网页内容的核心对象，每个 BrowserWindow 实例都包含一个 webContents 对象。它相当于网页的‘内容管理器’，提供了对页面加载、执行脚本、事件监听等操作的能力。
- **webContents 和 BrowserWindow 有什么区别？**
  BrowserWindow 负责窗口的外观和窗口级操作（如关闭、最小化、移动），而 webContents 负责窗口中网页内容的渲染与控制（如加载页面、执行 JS、监听页面事件）。可以理解为 BrowserWindow 是‘外壳’，webContents 是‘内容’。通过 win.webContents 可以访问对应的 webContents 实例。
- **如何使用 webContents 控制页面导航？**
  可以通过 webContents 提供的方法控制页面导航，例如：loadURL 加载指定 URL，reload 重新加载页面，goBack 后退，goForward 前进。这些方法允许主进程直接控制渲染页面的浏览行为。
- **如何在主进程中执行渲染进程中的 JavaScript 代码？**
  使用 webContents 的 executeJavaScript 方法可以在渲染进程中执行 JavaScript 代码。例如：win.webContents.executeJavaScript('document.title') 获取页面标题。该方法返回 Promise，可获取执行结果，常用于获取页面数据或修改 DOM。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796814965153794)

### 55. Electron 中如何实现全局快捷键？globalShortcut 有什么注意事项？

**难度：中等**　**标签：Electron / 全局快捷键**　**热度：95 次浏览**

**参考答案要点**

回答重点
Electron 通过 globalShortcut 模块实现全局快捷键，即使应用窗口未获得焦点也能响应。这个功能让应用可以提供系统级的快捷操作，比如截图工具的快捷键、音乐播放器的媒体控制等。

使用 globalShortcut 很简单，在主进程中导入模块，调用 register 方法注册快捷键和回调函数。快捷键使用加速键字符串表示，如 'CommandOrControl+X'、'Alt+Shift+F12'。注册成功后，无论应用是否在前台，按下快捷键都会触

**追问要点**

- **Electron 中如何注册全局快捷键？**
  在 Electron 的主进程中，使用 globalShortcut 模块的 register 方法注册全局快捷键。传入快捷键字符串（如 'CommandOrControl+Shift+S'）和对应的回调函数即可。注册后即使应用不在前台也能响应快捷键。
- **globalShortcut 必须在哪个时机注册？**
  必须在 app 的 ready 事件之后注册。如果在 ready 之前调用 globalShortcut.register，注册会失败或无效，因为 Electron 主进程尚未完全初始化。
- **如何处理全局快捷键注册失败的情况？**
  调用 globalShortcut.register 后应检查返回值，若返回 false 表示注册失败，通常是因为快捷键已被系统或其他应用占用。此时应提示用户更换快捷键，并提供自定义设置功能。
- **为什么需要在应用退出时注销全局快捷键？**
  应用退出前必须调用 globalShortcut.unregister 或 unregisterAll 注销已注册的快捷键，否则可能导致系统级快捷键冲突，影响其他应用甚至操作系统的正常行为。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796817989246977)

### 56. Electron 如何实现原生菜单？主菜单和右键菜单有什么区别？

**难度：中等**　**标签：Electron / 原生菜单**　**热度：114 次浏览**

**参考答案要点**

回答重点
Electron 通过 Menu 模块实现原生菜单，可以创建应用的主菜单（Menu Bar）和右键上下文菜单（Context Menu）。Menu 提供了符合各个操作系统规范的原生菜单样式，用户体验更好。

主菜单是应用顶部的菜单栏，在 Windows 和 Linux 上显示在窗口顶部，在 macOS 上显示在屏幕顶部。创建主菜单使用 Menu.buildFromTemplate 构建菜单模板，然后用 Menu.setApplicationMenu 设置为应用

**追问要点**

- **Electron 如何
实现原生菜单？**
  Electron 通过 Menu 模块实现原生菜单。使用 Menu.buildFromTemplate 根据模板构建菜单，然后通过 Menu.setApplicationMenu 设置为主菜单，或通过 menu.popup 显示右键上下文菜单。菜单项可以包含标签、快捷键、点击事件和预定义角色（如 copy、quit 等），从而提供符合各操作系统规范的原生体验。
- **主菜单和右键菜单有什么区别？**
  主菜单是应用顶部的固定菜单栏，在 Windows/Linux 上位于窗口顶部，在 macOS 上位于屏幕顶部，通常包含文件、编辑、查看等全局功能，通过 Menu.setApplicationMenu 设置；右键菜单是按需弹出的上下文菜单，根据用户右键点击的位置动态显示，提供与当前上下文相关的操作，通过监听 context-menu 事件并调用 menu.popup 方法在鼠标位置展示。
- **如何为 Electron 应用创建主菜单？**
  创建主菜单需要定义一个菜单模板数组，每个菜单项可包含 label、submenu、accelerator、click 回调或 role。使用 Menu.buildFromTemplate 构建菜单实例，并通过 Menu.setApplicationMenu 设置为应用的主菜单。在 macOS 上建议在菜单开头添加应用名称菜单项以符合系统规范。
- **如何实现 Electron 的右键上下文菜单？**
  实现右键菜单需先构建一个菜单模板并用 Menu.buildFromTemplate 创建菜单实例。然后监听 BrowserWindow 实例的 webContents 的 'context-menu' 事件，在事件回调中获取点击参数（如 x, y 坐标），调用 menu.popup({ window, x, y }) 在指定位置弹出菜单。可根据 params 判断上下文（如选中文本、元素类型）动态调整菜单内容。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796817385267201)

---

## GraphQL / 接口数据层

> GraphQL schema、query、resolver、分页、缓存与错误处理，Apollo Client 实践

### 57. GraphQL 的 Schema 是什么？如何定义 Schema？

**难度：简单**　**标签：GraphQL / GraphQL Schema**　**热度：12 次浏览**

**参考答案要点**

回答重点
Schema 是 GraphQL 的核心，定义了 API 的完整数据结构和可以执行的操作。Schema 就像是 API 的合约，明确规定了客户端可以查询什么数据、可以执行什么操作、每个字段的类型是什么。

Schema 使用 GraphQL 的类型定义语言（SDL）编写，语法简洁清晰。一个基本的 Schema 包含类型定义、Query 定义、Mutation 定义。

```graphql
定义类型
type User {
  id: ID!
  name

**追问要点**

- **GraphQL 的 Schema 是什么？**
  GraphQL 的 Schema 是 API 的核心，定义了数据结构、支持的操作（查
询、修改、订阅）以及每个字段的类型。它充当客户端与服务端之间的契约，确保双方对数据交互方式有明确共识。Schema 使用 GraphQL 的类型定义语言（SDL）编写，具有清晰简洁的语法。
- **Schema 中的类型定义有什么作用？**
  类型定义描述了数据的结构，比如 User 或 Post 类型包含哪些字段及其类型。例如，User 类型可以有 id、name、email 等字段，并指定是否为非空（用 ! 表示），是构建数据模型的基础。
- **Query 和 Mutation 在 Schema 中的作用分别是什么？**
  Query 定义了所有可执行的数据查询操作，是读取数据的入口；Mutation 定义了所有会修改数据的操作，如创建、更新或删除数据，是写入数据的入口。两者都是根类型，查询必须从它们开始。
- **如何在 Schema 中定义字段参数？**
  字段可以定义参数，参数可以设置默认值、是否必需（使用 !）。例如 posts(limit: Int = 10, orderBy: OrderBy!) 中 limit 有默认值，orderBy 是必需参数，filter 可以是可选的输入类型。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796660111450113)

### 58. GraphQL 中的 Subscription 是什么？如何实现实时数据推送？

**难度：困难**　**标签：GraphQL / GraphQL 实时通信**　**热度：4 次浏览**

**参考答案要点**

回答重点
Subscription（订阅）是 GraphQL 的第三种操作类型，用于实时数据推送。当服务器数据发生变化时，会主动推送给订阅的客户端，实现实时更新。

Subscription 的定义和 Query 类似，但语义不同。Query 是一次性请求，Subscription 是持续的数据流。

```graphql
type Subscription {
  messageAdded: Message!
  userOnline(userId: ID!): Us

**追问要点**

- **GraphQL 中的 Subscription 是什么？**
  Subscription 是 GraphQL 的三种操作类型之一，用于实现实时数据推送。与 Query（一次性请求）和 Mutation（
修改数据）不同，Subscription 建立的是一个持续的数据流，当服务器端的数据发生变化时，会主动将更新推送给已订阅的客户端，从而实现页面的实时更新，例如在聊天应用中接收新消息。
- **Subscription 与 Query 和 Mutation 有什么区别？**
  Query 用于从服务器获取一次性的数据，Mutation 用于修改服务器数据并返回结果，两者都是基于请求-响应模式的 HTTP 操作。而 Subscription 是一种持久连接，允许服务器在数据变化时主动向客户端推送更新，适用于需要实时响应的场景，如消息通知、在线状态更新等。
- **GraphQL 的 Subscription 如何实现底层通信？**
  GraphQL 的 Subscription 通常基于 WebSocket 实现。WebSocket 提供了全双工通信通道，客户端通过订阅建立持久连接后，服务器可以在任何时候将数据推送给客户端。Apollo Server 默认支持 WebSocket，并使用 graphql-ws 或 subscriptions-transport-ws 等库来处理连接。
- **如何在服务端定义一个 Subscription？**
  在 Schema 中定义 Subscription 类型，指定可订阅的事件。然后在 Resolver 中使用 PubSub 机制（如 graphql-subscriptions 提供的 PubSub 或 RedisPubSub）创建异步迭代器。当某个 Mutation 触发数据变更时，调用 pubsub.publish() 发布事件，触发对应订阅的响应。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796671641591810)

### 59. GraphQL 中如何实现分页？有哪些分页方案？

**难度：中等**　**标签：GraphQL / GraphQL 分页**　**热度：4 次浏览**

**参考答案要点**

回答重点
GraphQL 的分页有两种主要方案：基于偏移量的分页（Offset-based）和基于游标的分页（Cursor-based）。

基于偏移量的分页最简单直接，使用 limit 和 offset 参数控制。这种方式类似于 SQL 的 LIMIT 和 OFFSET，开发者很容易理解，实现起来也很简单：

```graphql
type Query {
  posts(limit: Int, offset: Int): [Post!]!
}

query {

**追问要点**

- **GraphQL 中常见的分页方案有哪些？**
  GraphQL 中主要有两种分页方案：基于偏移量的分页（Offset-based）和基于游标的分页（Cursor-based）。前者使用 limit 和 offset 参数，实现简单
但易受数据变动影响；后者通过 cursor 标识位置，能更可靠地处理动态数据，常用于大规模或实时性要求高的场景。
- **基于偏移量的分页有什么优缺点？**
  优点是实现简单、直观，类似于 SQL 的 LIMIT/OFFSET，易于理解和使用。缺点是在数据频繁变化时可能导致数据错位，出现重复或遗漏的问题，不适合对一致性要求高的分页场景。
- **基于游标的分页是如何工作的？**
  游标分页使用一个不透明的字符串（cursor）来标记数据的位置，客户端通过 after 或 before 参数指定起始位置，并结合 first 或 last 获取一定数量的数据。每条数据的 cursor 通常由 ID 或时间戳 base64 编码生成，服务端据此定位查询起点，确保分页的连续性和一致性。
- **什么是 Relay Cursor Connections 规范？**
  Relay Cursor Connections 是 GraphQL 社区的事实标准分页规范，定义了 Connection、Edge 和 PageInfo 等类型结构。它支持高效的双向分页，便于客户端自动管理分页逻辑，被 Apollo Client、Relay 等主流客户端良好支持。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796665039757313)

---

## WebAssembly / 高性能计算

> WASM 基础、模块与内存模型、工具链与性能对比

### 60. WebAssembly 在实际项目中如何和 JavaScript 配合使用？

**难度：困难**　**标签：WebAssembly / 实战应用**　**热度：22 次浏览**

**参考答案要点**

回答重点
WebAssembly 在实际项目中的应用模式是"JavaScript 为主，WASM 为辅"，两者各司其职，互补协作。

典型的架构是三层分工。JavaScript 层负责 UI 渲染、事件处理、业务逻辑、路由管理等。WebAssembly 层负责计算密集型任务，如图像处理、数据计算、算法实现。中间的胶水层负责两者的通信，处理数据转换、调用封装、错误处理等。

具体的实施步骤包括：首先识别性能瓶颈，用性能分析工具找出最耗时的计算部分。然后评估是否适合 WAS

**追问要点**

- **WebAssembly 和 JavaScript 在项目中的分工是怎样的？**
  在实际项目中，通常采用‘JavaScript 为主，WASM 为辅’的模式。JavaScript 负责 UI 渲染、事件处理、业务逻辑和路由管理等；WebAssembly 负责计算密集型任务，如图像处理、数据计算和算法实现；中间通过胶水层进行通信，完成数据转换和调用封装。
- **如何确定某部分功能是否适合用 WebAssembly 实现？**
  应首先使用性能分析工具识别性能瓶颈，若该部分属于计算密集型且跨语言边界调用不频繁，则适合迁移到 WebAssembly。反之，如果频繁与 DOM 交互或调用开销大，则更适合保留在 JavaScript 中。
- **WebAssembly 模块如何集成到 JavaScript 项目中？**
  可通过 npm 包或直接加载 .wasm 文件的方式集成。常用构建工具（如 wasm-pack）将 Rust 或 C/C++ 代码编译为 WASM，并生成对应的 JavaScript 胶水代码，便于在项目中 import 使用。
- **胶水层在 WASM 和 JavaScript 协作中起什么作用？**
  胶水层负责两者之间的通信，包括数据类型转换（如 ArrayBuffer 与 Uint8Array）、函数调用封装、内存管理和错误处理，确保 JavaScript 能安全高效地调用 WASM 模块。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796608781557761)

### 61. 什么是 WASI？它和浏览器中的 WebAssembly 有什么区别？

**难度：中等**　**标签：WebAssembly / WASI**　**热度：13 次浏览**

**参考答案要点**

回答重点
WASI（WebAssembly System Interface）是 WebAssembly 在非浏览器环境中的系统接口标准，让 WASM 能在服务器、命令行、物联网设备等环境运行。

浏览器中的 WebAssembly 通过 JavaScript API 与环境交互，可以调用 Web API（DOM、fetch 等）。但在非浏览器环境（如 Node.js、独立运行时），没有 JavaScript 环境，WASM 需要直接访问系统资源（文件、网络、环境变量等

**追问要点**

- **什么是 WASI？**
  WASI（WebAssembly System Interface）是 WebAssembly 在非浏览器环境中
的系统接口标准，它允许 WASM 模块在服务器、命令行工具、物联网设备等环境中安全地访问系统资源，如文件系统、网络、环境变量和时间等。WASI 的设计目标是提供跨平台、可移植且安全的系统调用机制，实现‘一次编译，到处运行’的愿景。
- **WASI 和浏览器中的 WebAssembly 有什么区别？**
  浏览器中的 WebAssembly 依赖 JavaScript API 与宿主环境交互，通过 Web API 访问 DOM、fetch 等功能，主要用于图形界面和用户交互；而 WASI 是为非浏览器环境设计的系统接口，不依赖 JavaScript，直接提供类似 POSIX 的系统调用，用于文件操作、网络请求等系统级任务。两者运行环境和接口不同，目标场景也不同：浏览器 WASM 面向前端应用，WASI 面向服务端和系统程序。
- **WASI 如何保证安全性？**
  WASI 采用能力安全模型（Capability-based Security），WASM 模块只能访问显式授权的资源。例如，运行时必须通过参数明确授予某个目录的读写权限（如 --dir 参数），模块无法访问未授权的文件或网络地址。这种最小权限原则有效防止了恶意代码对系统的非法访问。
- **WASI 支持哪些系统功能？**
  WASI 提供了标准化的系统接口，包括文件系统访问、网络通信、获取环境变量、读取系统时间、生成随机数、进程退出等基本系统能力。这些接口抽象了底层操作系统差异，使同一个 WASM 模块可以在 Linux、Windows、macOS 上无需修改即可运行。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796606743126018)

### 62. 如何在 WebAssembly 中调用 JavaScript 函数？

**难度：中等**　**标签：WebAssembly / 函数调用**　**热度：12 次浏览**

**参考答案要点**

回答重点
WebAssembly 调用 JavaScript 函数需要通过导入（import）机制，在实例化 WASM 模块时提供 JavaScript 函数。

基本流程是：WASM 模块声明需要导入的函数（类似 C 语言的 extern），JavaScript 在实例化时通过 imports 对象提供这些函数的实现。WASM 代码中就能调用这些"外部函数"，实际执行的是 JavaScript 代码。

**使用示例：**

```javascript
// Java

**追问要点**

- **WebAssembly 如何调用 JavaScript 函数？**
  WebAssembly 通过导入（import）机制调用 JavaScript 函数。在实例化 WASM 模块时，JavaS
cript 提供一个 imports 对象，其中包含要暴露给 WASM 的函数。WASM 模块在定义时声明这些导入函数，之后即可在内部调用它们，实际执行的是 JavaScript 中对应的实现。
- **在 WAT 中如何声明一个从 JavaScript 导入的函数？**
  在 WAT 格式中使用 (import) 语句声明导入函数。例如：(import "env" "log" (func $log (param i32))) 表示从名为 "env" 的模块中导入一个名为 "log" 的函数，该函数接收一个 i32 类型参数。
- **使用 Rust 和 wasm-bindgen 如何调用 JavaScript 的 console.log？**
  可以通过 wasm_bindgen 定义外部 JavaScript 函数绑定，例如：

[wasm_bindgen(js_namespace = console)]
fn log(s: &str);

然后在 Rust 代码中直接调用 log("message")，它会映射到 JavaScript 的 console.log。
- **WebAssembly 调用 JavaScript 函数有哪些性能注意事项？**
  跨边界调用存在类型转换和上下文切换开销，单次调用虽仅几微秒，但频繁调用（如循环中）会显著影响性能。建议减少调用次数，采用批量数据传递方式，将多次调用合并为一次，提升整体效率。

[查看原题与完整解析](https://www.mianshiya.com/question/1991796604503367681)

---

## 浏览器 / 网络 / Web 安全

> 浏览器渲染机制、HTTP 与缓存、跨域、XSS/CSRF、Web 安全与密码存储

### 63. 请描述 Telnet 和 SSH 的区别及其应用场景。

**难度：简单**　**标签：计算机网络 / 网络协议**　**热度：468 次浏览**

**参考答案要点**

回答重点
Telnet 和 SSH 都是远程登录协议，但它们在安全性上有显著的区别。Telnet 是一个不加密的协议，传输的数据包括登录凭证都是明文的，非常容易被截获和探查。SSH（Secure Shell），则是一个加密协议，通过加密和认证机制确保数据传输的安全性。

应用场景上，Telnet 曾经被广泛用于远程管理和维护机器，
但是由于它的安全问题，现在已经基本被更安全的 SSH 替代。SSH 主要用于安全的远程登录、文件传

[查看原题与完整解析](https://www.mianshiya.com/question/1811361508374933505)

### 64. 请描述 RIP 协议的工作原理及其特点。

**难度：简单**　**标签：计算机网络 / 网络协议**　**热度：634 次浏览**

**参考答案要点**

回答重点
RIP（Routing Information Protocol）是一种基于距离向量的动态路由协议，广泛应用于小型和中型网络。其工作原理主要包括两个部分：路由表维护和路由更新。

1）每个路由器维护一张路由表，记录所有已知网络的最短路径和对应的下一跳路由器。
2）每30秒
，RIP路由器会向邻近的路由器发送更新信息，同时也会接收来自邻居的路由更新。
3）当接收到邻居的更新信息后，路由器会根据“最长优先”（即跳数最少）的原则更新自己的路由表。
4）RIP使用跳数作

**追问要点**

- **RIP协议使用什么算法？**
  RIP协议使用距离向量算法（Distance Vector Algorithm），通过交换路由信息来计算到达各个网络的最短路径。
- **RIP协议如何度量路径优劣？**
  RIP协议使用跳数（Hop Count）作为度量标准，跳数越少表示路径越优，最大有效跳数为15，跳数为16表示目的网络不可达。
- **RIP协议的更新周期是多久？**
  RIP协议默认每30秒向相邻路由器发送一次路由更新信息，以维护网络中的路由表一致性。
- **RIP协议使用哪个传输层协议和端口号？**
  RIP协议使用UDP作为传输层协议，端口号为520，既用于发送也用于接收路由更新消息。

[查看原题与完整解析](https://www.mianshiya.com/question/1811361505594109954)

### 65. 什么是 LDAP 协议？请解释其主要用途。

**难度：中等**　**标签：计算机网络 / 网络协议**　**热度：297 次浏览**

**参考答案要点**

回答重点
LDAP（轻量目录访问协议，Lightweight Directory Access Protocol）是一种应用层协议，用于访问和维护分布式目录信息服务。它运行在TCP/IP协议之上，允许用户在网络上添加、删除、修改和查找目录中的资源。

扩展知识
LDAP的主要用途涵盖以下几个方面：

1）**用户认证和授权**：LDAP常用作验证用户身份的标准协议，特别是在企业环境中，用于单点登录（SSO）和访问控制。企业使用LDAP存储用户凭据和权限信息，简化了

**追问要点**

- **什么是LDAP协议？**
  LDAP（轻量目录访问协议，Lightweight Directory Access Protocol）是一种应用层协议，用于访问和维护分布式目录信息服务。它运行在TCP/IP协议之上，支持用户在网络上对目录中的资源进行添加、删除、修改和查找操作。
- **LDAP协议的主要用途有哪些？**
  LDAP主要用于用户认证和授权、信息目录服务、电子邮件和联系人管理、系统配置共享以及组织结构管理。在企业环境中，常用于单点登录（SSO）和集中式用户管理。
- **LDAP如何用于用户认证？**
  LDAP通过存储用户的用户名、密码和权限信
息，提供统一的身份验证服务。当用户登录系统时，系统会通过LDAP验证其凭据，实现集中化的身份管理，常用于企业内部的单点登录场景。
- **LDAP的数据结构是怎样的？**
  LDAP使用树状结构（称为目录树）来组织数据，每个节点是一个目录条目，包含一组属性（如cn、sn、mail等），条目之间通过层次关系连接，类似于文件系统的目录结构。

[查看原题与完整解析](https://www.mianshiya.com/question/1811361508936970241)

---

## Node.js

> Node 运行时、模块规范、事件循环、Express/Koa 与服务端开发（BFF）

### 66. 如何在 Node.js 中实现日志记录，并配置不同级别的日志？

**难度：中等**　**标签：Node.js**　**热度：152 次浏览**

**参考答案要点**

回答重点
可以使用 `winston` 这个强大的 Node.js 日志库来实现日志记录，并配置不同级别的日志。`winston` 不仅灵活易用，还支持多种输出格式和复杂的日志管理策略。

首先需要安装 `winston`：
```bash
npm install winston
```

接下来，我们可以通过以下代码初始化一个 `winston` 日志记录器，并配置不同级别的日志：

```javascript
const winston = require('win

**追问要点**

- **如何在 Node.js 中安装和使用 winston 实现日志记录？**
  首先通过 npm 安装 winston：`npm install winston`，然后在代码中引入并创建一个 logger 实例。配置包括日志级别、格式和传输方式（如控制台和文件），即可使用 `logger.info()`、`logger.error()` 等方法记录不同级别的日志。
- **winston 支持哪些日志级别，它们的优先级顺序是什么？**
  winston 默认支持的日志级别从高到低为：error、warn、info、http、verbose、debug、silly。级别越高越重要，只有等于或高于设置级别的日志才会被输出。
- **如何将日志同时输出到控制台和文件中？**
  在 winston 的 transports 配置中同时添加 Console 和 File 传输：`new winston.transports.Console()` 用于控制台输出，`new winston.transports.File({ filename: 'combined.log' })` 用于写入文件，可分别设置不同文件保存不同级别的日志。
- **如何自定义 winston 的日志输出格式？**
  使用 `winston.format.combine()` 结合多种格式，例如通过 `winston.format.timestamp()` 添加时间戳，再用 `winston.format.printf()` 自定义字符串格式，或者使用 `winston.format.json()` 输出 JSON 格式日志。

[查看原题与完整解析](https://www.mianshiya.com/question/1843904471407554562)

### 67. 在 Express 中如何使用参数匹配路由？

**难度：简单**　**标签：Node.js / Node框架 / Express**　**热度：78 次浏览**

**参考答案要点**

回答重点
在 Express 中使用参数匹配路由非常简单。通过定义带有冒号（:）的路由参数，我们可以将 URL 中的特定部分捕获为参数。以下是一个简单的示例：

```javascript
const express = require('express');
const app = express();

// 使用带有参数的路由
app.get('/user/:userId', (req, res) => {
    const userId = req.param

**追问要点**

- **在 Express 中如何定义带参数的路由？**
  在 Express 中，可以通过在路由路径中使用冒号（:）来定义参数。例如 `app.get('/user/:userId', (req, res) => {...})`，其中 `:userId` 是一个路由参数，可以通过 `req.params.userId` 获取其值。
- **如何在 Express 路由中获取多个参数？**
  可以在路由路径中定义多个带冒号的参数，如 `/user/:userId/book/:bookId`。这些参数会作为属性存储在 `req.params` 对象中，通过 `req.params.userId` 和 `req.params.bookId` 访问各自的值。
- **Express 中如何设置可选的路由参数？**
  在参数名后加上问号（?）可以定义可选参数，例如 `:bookId?`。对应的路由如 `/user/:userId/book/:bookId?`，此时 `bookId` 可以不存在，访问时需判断 `req.params.bookId` 是否存在再处理逻辑。
- **如何用正则表达式限制 Express 路由参数的匹配格式？**
  可以在参数后添加括号包裹的正则表达式来限定匹配规则，例如 `/user/:userId(\d+)` 只会匹配 `userId` 为数字的情况，避免非数字字符串被接受。

[查看原题与完整解析](https://www.mianshiya.com/question/1846395479206785026)

### 68. Node.js 中的 process 对象是什么？它有哪些常用属性？

**难度：简单**　**标签：Node.js**　**热度：1875 次浏览**

**参考答案要点**

回答重点
Node.js 中的 `process` 对象是一个全局对象，它提供了有关当前 Node.js 进程的信息和控制，让我们可以与操作系统进行交互。它不需要通过 `require` 引入，任何地方都可以直接使用。

常用的属性包括：

1）`process.argv`：获取命令行参数的数组。
2）`process.env`：获取用户环境信息的对
象。
3）`process.exit()`：退出当前进程的方法。
4）`process.cwd()`：返回当前进程的工作目

**追问要点**

- **Node.js 中的 process 对象是什么？**
  `process` 是 Node.js 中的一个全局对象，提供了与当前运行进程及操作系统交互的能力。它无需通过 require 引入，可以在任何模块中直接使用，用于获取进程信息、控制进程行为以及处理命令行参数等。
- **`process.argv` 的作用是什么？**
  `process.argv` 是一个数组，包含启动 Node.js 进程时传入的命令行参数。其中前两个元素分别是 node 可执行文件路径和脚本文件路径，从第三个开始是用户传递的实际参数。例如运行 `node script.js arg1 arg2` 时，`process.argv[2]` 为 `'arg1'`，`process.argv[3]` 为 `'arg2'`。
- **如何通过 `process.env` 使用环境变量？**
  `process.env` 是一个包含当前用户环境变量的对象。可以通过在命令行中设置（如 `export NODE_ENV=production`）或使用 `.env` 文件加载配置，在代码中通过 `process.env.NODE_ENV` 等方式读取，以实现不同环境下的应用配置切换。
- **`process.exit()` 方法有什么作用？**
  `process.exit()` 用于终止当前 Node.js 进程。传入的参数是退出码：0 表示正常退出，非 0（如 1）表示异常退出。常用于错误处理后主动结束程序，例如在捕获致命异常后调用 `process.exit(1)`。

[查看原题与完整解析](https://www.mianshiya.com/question/1843904430030745602)

### 69. 如何在 Node.js 中实现模块的懒加载？

**难度：中等**　**标签：Node.js**　**热度：178 次浏览**

**参考答案要点**

回答重点
在 Node.js 中实现模块的懒加载的常用方法是延迟加载模块，即在需要使用模块的时候才去加载它，而不是在应用启动时立即加载所有的模块。可以通过 `require` 语句在需要的时候再调用：

```javascript
let myModule;

function useMyModule() {
  if (!myModule) {
    myModule = require('my-module');
  }
  // 使用 myModule 的逻辑

**追问要点**

- **什么是模块的懒加载？**
  模块的懒加载是一种设计模式，指在需要使用模块时才进行加载，而不是在应用启动或初始化阶段就全部加载。这种方式可以提升应用的启动速度，减少初始内存占用，特别适用于包含大量模块的大型应用。
- **Node.js 中如何实现模块的懒加载？**
  在 Node.js 中可以通过延迟调用 `require` 来实现懒加载。例如，在
首次使用模块时才调用 `require` 加载，并缓存实例供后续使用。也可以使用 ES6 的动态 `import()` 实现异步懒加载，适合需要按需加载的场景。
- **使用 `require` 实现懒加载的原理是什么？**
  `require` 是同步操作，首次加载模块时会执行模块代码并将其缓存到 `require.cache` 中。后续再次 `require` 同一模块时会直接从缓存中读取，因此通过在需要时才首次调用 `require`，即可实现懒加载，同时避免重复加载的开销。
- **动态 `import()` 和 `require` 在懒加载中的区别是什么？**
  `require` 是同步的，必须在函数执行时阻塞等待模块加载完成；而动态 `import()` 返回一个 Promise，是异步操作，可以在不阻塞主线程的情况下加载模块，更适合异步流程和并行加载场景，但使用时需处理异步逻辑。

[查看原题与完整解析](https://www.mianshiya.com/question/1843904473412431873)

---

## 前端场景 / 系统设计

> 真实项目场景题、架构设计、系统设计与技术选型

### 70. 什么是适配器模式？一般用在什么场景？

**难度：简单**　**标签：设计模式**　**热度：4185 次浏览**

**参考答案要点**

回答重点

适配器模式是一种结构型设计模式，核心作用是**把一个类的接口转换成客户端期望的另一个接口**，让原本因为接口不兼容而没法一起工作的类能够协同工作。

生活中最典型的例子就是电源转接头：

<p align="center"><img src="https://pic.code-nav.cn/mianshiya/question_picture/1772087337535152129/POMRwpny_image_mianshiya.webp" alt="im

**追问要点**

- **什么是适配器模式？**
  适配器模式是一种结构型设计模式，用于将一个类的接口转换成客户端期望的另一个接口。它的主要目的是解决接口不兼容的问题，使得原本由于接口不匹配而无法协同工作的类可以一起工作。适配器充当一个中间层，通过继承（类适配器）或组合（对象适配器）的方式，把被适配者的接口转换为目标接口。
- **适配器模式的
核心作用是什么？**
  适配器模式的核心作用是实现接口转换，使不兼容的接口能够协同工作。它通过解耦客户端与被适配类之间的依赖关系，提升系统的灵活性和可复用性，同时符合开闭原则，即在不修改原有代码的前提下扩展功能。
- **适配器模式有哪些典型应用场景？**
  典型应用场景包括：1）已有类的接口与新系统需求不兼容但无法修改源码；2）整合第三方库时其接口与当前系统不一致；3）需要统一多个不同接口以便客户端使用统一方式调用；4）系统升级时将旧接口适配到新接口，如老系统迁移到新框架。
- **适配器模式由哪些角色组成？**
  适配器模式包含三个核心角色：目标接口（Target），定义客户端期望的接口；被适配者（Adaptee），即现有需要适配的类；适配器（Adapter），负责将被适配者的接口转换为目标接口，通常持有被适配者实例并实现目标接口。

[查看原题与完整解析](https://www.mianshiya.com/question/1802171589225422850)

### 71. 让你实现一个分布式单例对象，如何实现？

**难度：困难**　**标签：系统设计 / 场景题**　**热度：7246 次浏览**

**参考答案要点**

回答重点

普通单例是进程内唯一
，**分布式单例**要解决的是跨进程唯一，不管部署了多少台机器、多少个服务实例，全局只有这一个对象。

实现思路分两步：
- 一是用分布式锁控制创建过程，保证同一时刻只有一个进程能创建
- 二是把对象存到外部存储，让所有进程都能访问到。

创建流程是这样的：
1. 多个进程同时尝试获取分布式锁，只有一个能抢到
2. 抢到锁的进程先检查外部存储里有没有这个对象，没有就创建并序列化存进去，有就直接跳过。
3. 最后释放锁，其他进程抢到锁后发现

**追问要点**

- **什么是分布式单例对象？**
  分布式单例对象指的是在分布式系统中，无论有多少个进程或服务实例部署在一台或多台机器上，某个类在整个系统范围内始终只有一个实例存在，并且所有进程都能访问和操作这个唯一的实例。
- **如何保证分布式单例对象的唯一性？**
  通过使用分布式锁机制来保证唯一性。多个进程在创建或修改单例对象时需先竞争获取分布式锁，只有获得锁的进程才能进行创建或更新操作，从而确保同一时间只有一个进程能修改该对象，实现全局唯一。
- **为什么不能将单例对象存储在本地内存中？**
  因为分布式环境下存在多个进程，如果将单例对象存储在某个进程的本地内存中，其他进程无法访问该对象，导致每个进程可能都创建自己的实例，破坏了单例的唯一
性。因此必须将单例对象存储在所有进程均可访问的外部共享存储中，如 Redis 或 ZooKeeper。
- **如何实现分布式锁来控制单例的创建与修改？**
  可以使用 Redis 的 SETNX（SET if Not eXists）命令或 Redlock 算法实现分布式锁。在创建或修改单例对象前，进程尝试获取锁；成功获取锁的进程才能从共享存储读取或写入数据，操作完成后释放锁，确保操作的互斥性和一致性。

[查看原题与完整解析](https://www.mianshiya.com/question/1798614886358245378)

### 72. 什么是里氏替换原则？

**难度：简单**　**标签：设计模式**　**热度：2496 次浏览**

**参考答案要点**

回答重点

**里氏替换原则**是 SOLID 五大设计原则中的 L，全称 Liskov Substitution Principle。

核心思想就是：**子类对象必须能够替换掉父类对象出现的任何地方，并且程序行为保持不变。**

换个说法：子类可以扩展父类的功能，但不能改变父类原有的行为。父类定义的"规矩"，子类必须遵守。

经典反面教材就是正方形和矩形的问题：

```java
class Rectangle {
    private int width;

**追问要点**

- **什么是里氏替换原则？**
  里氏替换原则（Liskov Substitution Principle，LSP）是面向对象设计五大原则SOLID中的L。其核心思想是：子类对象应当能够替换其父类对象出现在任何地方，且程序的行为仍然保持正确。也就是说，子类必须遵循父类的约定，包括方法的功能、输入输出、异常处理等，不能改变父类原有的行为逻辑。
- **里氏替换原则的目的是什么？**
  里氏替换原则的目的是在保证兼容性的前提下进行扩展。当子类可以安全地替换父类而不影响程序的正确性时，系统的可维护性、可扩展性和稳定性就会更强，避免因继承导致的逻辑错误。
- **如何判断一个子类是否符合里氏替换原则？**
  判断子类是否符合里氏替换原则的关键是看它是否遵守了父类的行为约定。即使语法上继承或实现了父类或接口，如果修改了父类方法的语义（如改变了功能逻辑、前置条件变严格、后置条件变弱等），就可能违反该原则。例如，重写方法导致原本成立的断言失败，则说明不满足LSP。
- **正方形继承矩形的例子为什么违反了里氏替换原则？**
  因为Rectangle父类允许独立设置宽和高，而Square子类在重写setWidth和setHeight时强制长宽相等，破坏了父类‘宽高可独立变化’的约定。当调用resizeRectangle(Rectangle r)方法期望面积为50时，传入Square对象会导致实际面积为100或25，行为与预期不符，因此违反了里氏替换原则。

[查看原题与完整解析](https://www.mianshiya.com/question/1803657348456636417)

### 73. AI 热点监控工具项目中，不同数据源的搜索结果是如何统一为相同格式的？

**难度：中等**　**标签：架构设计**　**热度：2 次浏览**

**参考答案要点**

由于项目对接了 8+ 个数据源，每个数据源返回的数据格式都不一样，我需要把它们统一成相同的 `SearchResult` 类型才能进入后续的去重、AI 分析和入库流程。

我在 `types.ts` 中定义了统一的 `SearchResult` 接口，包含 title、content、url、source（标识来自哪个数据源）、sourceId（原始平台的 ID）、publishedAt、以及各种互动数据字段（likeCount、retweetCount、viewCount

[查看原题与完整解析](https://www.mianshiya.com/question/2039963170679861250)

---

## UI 组件库 / 图表

> Ant Design / Element UI / Vant 等组件库与 ECharts 图表

### 74. Element UI 如何支持国际化？你如何在一个多语言项目中切换语言？

**难度：中等**　**标签：Vue / Vue组件库 / Vue库 / Element UI / Vue进阶**　**热度：540 次浏览**

**参考答案要点**

回答重点
Element UI 支持国际化，通过配置其国际化插件并在 Vue 实例中引入即可。首先，你需要安装 `element-ui` 和 `vue-i18n` 两个库。然后配置国际化插件和 Vue i18n 实例，最后在项目中动态切换语言。

具体步骤如下：

1）安装 `element-ui` 和 `vue-i18n`：
```bash
npm install element-ui vue-i18n --save
```

2）在项目中配置国际化：
```java

**追问要点**

- **Element UI 如何实现国际化？**
  Element UI 通过集成 vue-i18n 实现国际化。需要安装 element-ui 和 vue-i18n，引入对应语言包（如中文 zh-CN 和英文 en），配置 VueI18n 实例，并将 i18n 实例传递给 ElementUI 插件，从而实现组件库的多语言支持。
- **如何在项目中切换 Element UI 的显示语言？**
  通过修改 VueI18n 实例的 locale 属性来切换语言，例如设置 i18n.locale = 'zh' 或 i18n.locale = 'en'，Element UI 组件和自定义文本会自动更新为对应语言。
- **如何让语言切换后用户偏好持久化？**
  可以在切换语言时将当前语言保存到 localStorage 中，如 localStorage.setItem('language', lang)；应用初始化时读取该值并设置为 i18n.locale，实现语言记忆功能。
- **如何为 Element UI 添加自定义语言支持？**
  可以通过引入 Element UI 提供的其他语言包（如 esLocale、frLocale 等）并合并到 messages 配置中，扩展对西班牙语、法语等更多语言的支持。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828901674573825)

### 75. 你有二次封装过 Element UI 的组件吗？

**难度：中等**　**标签：Vue / Vue组件库 / Vue库 / Element UI / Vue进阶**　**热度：797 次浏览**

**参考答案要点**

回答重点
二次封装的动机通常是为了实现更高的封装度、灵活的业务需求，以及统一的界面风格和功能拓展。可以这样说，之前在项目中封装过以下几种组件类型：

1）表单
组件：为了业务需求而定制表单元素，如带有特定验证逻辑的输入框、特定格式的日期选择器等。
2）表格组件：封装了通用的表格操作，如分页、排序、过滤，以及自定义列显示等。
3）弹窗组件：基于 Element UI 的 Dialog 组件，封装了一些通用的确认和提示功能，使得调用更加简洁。
4）常用布局组件：例如经常用到的

**追问要点**

- **你为什么需要二次封装 Element UI 的组件？**
  二次封装的主要目的是提升封装度、满足灵活的业务需求、统一界面风格和增强功能。通过封装可以实现组件的高度复用、统一交互逻辑，并在多个项目中保持一致的用户体验，同时还能扩展 Element UI 原有组件不具备的功能。
- **你在项目中封装过哪些类型的 Element UI 组件？**
  我封装过表单组件、表格组件、弹窗组件以及常用布局组件。例如，带有自定义验证规则的输入框、支持分页和排序的通用表格、简化调用流程的确认弹窗，以及可复用的左侧菜单栏和顶部导航栏等。
- **二次封装组件时如何保证灵活性和可定制化？**
  通过合理使用 props、events 和 slots 来提高组件的灵活性。例如，使用 props 传递配置项如验证规则或初始值，通过 slots 插入自定义内容，暴露必要的事件供父组件监听，从而让封装的组件适应不同场景的需求。
- **如何通过二次封装实现团队的统一风格和开发规范
？**
  在封装组件时，统一设置默认样式、尺寸、颜色、动画等视觉规范，以及预设常用的交互行为。这样所有成员在使用这些组件时都会遵循相同的设计语言，确保了界面的一致性，也提升了协作效率。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828895869657089)

### 76. 如何修改 Element UI 组件的默认样式？

**难度：中等**　**标签：Vue / Vue组件库 / Vue库 / Element UI / Vue进阶**　**热度：2228 次浏览**

**参考答案要点**

回答重点
要修改 Element UI 组件的默认样式，最直接的方法是覆盖其CSS样式。Element UI 使用的是基于 BEM (Block Element Modifier) 规范的类名，所以你可以直接在你的项目的样式文件里进行覆盖。

例如，如果你想修改 Element UI 中 Button 的样式，可以在你的项目的全局样式文件（如 App.vue 或者一个单独的 .css/.scss 文件）中添
加以下代码：

```css
/* 覆盖默认的 Element

**追问要点**

- **如何修改 Element UI 组件的默认样式？**
  可以通过覆盖 CSS 样式来修改 Element UI 组件的默认样式。由于 Element UI 使用 BEM 规范命名类名，可以直接在项目样式文件中针对类名（如 .el-button）编写样式规则进行覆盖。确保自定义样式在 Element UI 样式之后引入，以保证生效。
- **如果样式覆盖不生效，可能是什么原因？**
  最常见的原因是样式引入顺序问题。CSS 样式遵循后定义覆盖前定义的原则，因此必须确保自定义样式在 Element UI 的样式文件之后引入，否则无法成功覆盖。
- **在 Vue 单文件组件中如何对 Element UI 组件进行局部样式覆盖？**
  在使用 scoped 样式时，需要通过 Vue 的 deep 选择器（如 ::v-deep）穿透作用域，才能正确应用到子组件。例如：::v-deep .el-button { background-color: #409EFF; }
- **Element UI 是否支持主题定制？**
  是的，Element UI 支持主题定制。可以使用官方提供的工具生成自定义主题包，并通过替换默认主题文件的方式实现整体风格的统一修改。详细方法可参考 Element UI 官方主题定制教程。

[查看原题与完整解析](https://www.mianshiya.com/question/1817828877444079618)


---

*题目来源：面试鸭 mianshiya.com · 生成于 2026-11-01 · 共 76 题 / 23 个方向*
