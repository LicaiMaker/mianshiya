# 前端面试题日报 · 轮换计划

本目录用于「每天出前端面试题」的持续产出。

## 目录结构

```
frontend-interview/
├── 2026-10-26-day01.md              # Day 01 成品（59 题 / 20 方向）
├── DAILY-ROTATION.md                # 本文件：方向清单 + 轮换规则 + 每日提示词
└── data/
    ├── mianshiya-frontend-questions.json   # 面试鸭前端 20 题库抓取的 374 道真题（含原题链接）
    └── used-day01.json                    # Day 01 已用题目索引（按题库）
```

## 题源

| 来源 | 说明 |
|------|------|
| 面试鸭（https://www.mianshiya.com） | 前端分类下的 20 个子题库，已离线抓取 374 道真题标题 + 详情链接，见 `data/mianshiya-frontend-questions.json` |
| 本仓库（/workspace） | 面试鸭站点源码：React 17 + TypeScript + UmiJS 3 + Ant Design 4 + Less + Axios + Workbox Service Worker + Node/Express + 腾讯云开发。第 20 组「本仓库实战」即由此出题 |

语料未用完（374 题），按下面的轮换规则可持续出题 **约 12 天**不重复；每天再叠加 3 道仓库实战题，题量随仓库演进更新。

## 20 个方向与对应题库

| # | 方向 | 题库 URL | 语料题数 |
|---|------|----------|----------|
| 1 | HTML | https://www.mianshiya.com/bank/1810644197003362306 | 18 |
| 2 | CSS | https://www.mianshiya.com/bank/1810644318667538433 | 20 |
| 3 | JavaScript 基础 | https://www.mianshiya.com/bank/1810644471159848962 | 20 |
| 4 | ES6 / 现代 JavaScript | https://www.mianshiya.com/bank/1810644716832817154 | 14 |
| 5 | JavaScript 进阶 | https://www.mianshiya.com/bank/1810644667913785345 | 20 |
| 6 | TypeScript | https://www.mianshiya.com/bank/1810644420521152513 | 20 |
| 7 | React 基础 | https://www.mianshiya.com/bank/1817900465338241026 | 20 |
| 8 | React 进阶 | https://www.mianshiya.com/bank/1817900573026996225 | 20 |
| 9 | Vue 基础 | https://www.mianshiya.com/bank/1817900864917000193 | 20 |
| 10 | Vue 进阶 | https://www.mianshiya.com/bank/1817900926871064578 | 20 |
| 11 | Node.js | https://www.mianshiya.com/bank/1843955995837042689 | 20 |
| 12 | Node.js 框架（Koa/Express） | https://www.mianshiya.com/bank/1846179720813404162 | 20 |
| 13 | 手写代码 | https://www.mianshiya.com/bank/1820434920244424705 | 20 |
| 14 | 前端工程化 | https://www.mianshiya.com/bank/1831174767836995585 | 20 |
| 15 | Webpack | https://www.mianshiya.com/bank/1831174878121283585 | 20 |
| 16 | 性能优化 | https://www.mianshiya.com/bank/1831175125723631618 | 20 |
| 17 | 前端系统设计 | https://www.mianshiya.com/bank/1824748303969992706 | 20 |
| 18 | 前端场景题 | https://www.mianshiya.com/bank/1824748170947006466 | 20 |
| 19 | 代码分析 | https://www.mianshiya.com/bank/1810644905160396801 | 2 |
| 20 | 前端热门/综合 | https://www.mianshiya.com/bank/1860931478862618626 | 20 |

> 第 19 组语料只有 2 条且无题干代码，需**自行命题**（JS 输出顺序、闭包/var、事件循环、Promise 等），可从第 3/4/5 组改写。
> 第 20 组与仓库实战组同样以自命题为主（仓库源码 + 面试鸭热门考点）。

## 轮换规则

1. **覆盖优先**：每天必须覆盖全部 20 个方向，每个方向 **≥ 2 题**（第 1 天已用满 3 题/方向）。
2. **不重复**：优先从 `data/mianshiya-frontend-questions.json` 中挑**历史日报未出现过**的题目；出题前先检索 `data/used-*.json` 与历史日报文件。
3. **梯度加深**：
   - Day 01：全景覆盖（每方向 2–3 题，重在知识面）
   - Day 02–04：每方向 3–4 题，重在原理与追问
   - Day 05+：每方向 4 题 + 1 道仓库实战题，重在场景设计与源码
4. **保持原味**：题干尽量用面试鸭原句或轻度改写，附原题链接；参考要点 2–4 条，只写「关键词 + 易错点」，不写成教程。
5. **只出前端**：Java / MySQL / Redis / 算法 / 后端场景题一律不出；Node.js 只出与前端工程、构建、SSR、BFF 相关的部分。
6. **仓库实战组**每期都要更新：优先挑 `src/`、`config/`、`server/` 中近期被改动或技术含量高的文件出题。

## 每日产出格式（固定）

```
frontend-interview/YYYY-MM-DD-dayNN.md
```

结构与 Day 01 保持一致：目录表 → 20 个方向分组 → 每题「题干 + 参考要点 + 原题链接/仓库文件链接」→ 复盘建议。

## 每日生成提示词（可直接粘贴给任意会话 / 定时任务）

```text
你是前端面试题出题助手。请按下面的要求生成「前端面试题日报」，并把结果写入 /workspace/frontend-interview/YYYY-MM-DD-dayNN.md（NN 为递增的期号，今天的日期用系统当前日期）。

【题源】
1. 面试鸭前端题库：读取 /workspace/frontend-interview/data/mianshiya-frontend-questions.json（374 道真题，含题干与原题链接）。若该文件缺失，可从以下 20 个题库页重新抓取（页面内 JSON-LD 的 ItemList 即为题目列表）：
   https://www.mianshiya.com/bank/1810644197003362306 （HTML）
   https://www.mianshiya.com/bank/1810644318667538433 （CSS）
   https://www.mianshiya.com/bank/1810644471159848962 （JavaScript 基础）
   https://www.mianshiya.com/bank/1810644716832817154 （ES6）
   https://www.mianshiya.com/bank/1810644667913785345 （JavaScript 进阶）
   https://www.mianshiya.com/bank/1810644420521152513 （TypeScript）
   https://www.mianshiya.com/bank/1817900465338241026 （React 基础）
   https://www.mianshiya.com/bank/1817900573026996225 （React 进阶）
   https://www.mianshiya.com/bank/1817900864917000193 （Vue 基础）
   https://www.mianshiya.com/bank/1817900926871064578 （Vue 进阶）
   https://www.mianshiya.com/bank/1843955995837042689 （Node.js）
   https://www.mianshiya.com/bank/1846179720813404162 （Node.js 框架）
   https://www.mianshiya.com/bank/1820434920244424705 （手写代码）
   https://www.mianshiya.com/bank/1831174767836995585 （前端工程化）
   https://www.mianshiya.com/bank/1831174878121283585 （Webpack）
   https://www.mianshiya.com/bank/1831175125723631618 （性能优化）
   https://www.mianshiya.com/bank/1824748303969992706 （前端系统设计）
   https://www.mianshiya.com/bank/1824748170947006466 （前端场景题）
   https://www.mianshiya.com/bank/1810644905160396801 （代码分析）
   https://www.mianshiya.com/bank/1860931478862618626 （前端热门）
2. 本仓库 /workspace（面试鸭站点源码：React 17 + TypeScript + UmiJS 3 + Ant Design 4 + Less + Axios + Workbox + Node/Express + 腾讯云开发）：第 20 组「本仓库实战」题必须基于真实源码，引用具体文件路径。

【硬性要求】
- 只出前端面试题，不出 Java / MySQL / Redis / 算法 / 后端题；Node.js 只保留与前端工程、构建、SSR、BFF 相关的内容。
- 必须覆盖下面 20 个方向，每个方向至少 2 题：HTML、CSS、JavaScript 基础、ES6/现代 JavaScript、JavaScript 进阶、TypeScript、React 基础、React 进阶、Vue 基础、Vue 进阶、Node.js、Node.js 框架、手写代码、前端工程化、Webpack、性能优化、前端系统设计、场景题、代码分析、本仓库实战。
- 不重复历史日报：先检索 /workspace/frontend-interview/ 下已有的 day*.md 与 data/used-*.json，已出过的题目不得再用。
- 每题给「题干 + 参考要点（2–4 条，只写关键词与易错点）+ 来源链接」，引用仓库源码时给出文件路径。
- 题干优先使用面试鸭原句或轻度改写，不要自造脱离题库的偏题。
- 文档结构：开头的目录表（方向 / 题数 / 题库链接）→ 20 个方向分组 → 文末复盘建议。

【收尾】
- 把本次使用的题目按题库追加写入 /workspace/frontend-interview/data/used-dayNN.json（格式参考 used-day01.json）。
- 在回复里给出当日题量、覆盖方向数，以及文件路径链接。
```

## 关于「每天自动执行」

本环境（远程沙箱）**没有提供定时任务能力**：`schedule` 技能依赖的 `Schedule` 工具在当前环境不可用（工具清单、MCP 服务器、CLI 三处均未找到），因此无法在会话内注册真正的「每日自动执行」。

可行替代方式（任选其一）：

1. **本机 cron**：把上面的提示词保存为脚本（例如 `gen-daily.sh`），由系统 crontab 每日调用一次 CLI 执行。
2. **宿主恢复调度能力后**：用 `schedule` 技能创建每日任务，`message` 直接填上面「每日生成提示词」整段内容。
3. **手动触发**：每天在会话里说一句「出今天的题」，助手按同一套规则生成，产物落在同一目录，编号连续、不重复。
