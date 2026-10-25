#!/usr/bin/env node
/**
 * 每日前端面试题生成器
 * ---------------------------------------------------------------------------
 * 用法:
 *   node daily.mjs                      # 生成今天（Asia/Shanghai）的题目
 *   node daily.mjs --date=2026-11-01    # 指定日期
 *   node daily.mjs --per=3              # 每个方向出 3 题（默认 2）
 *   node daily.mjs --stdout             # 只打印，不写文件
 *
 * 规则:
 *   - 题目库见 questions.json（20 个前端方向，每方向 6 题）
 *   - 选题由「日期 + 方向序号」确定性推导，同一天永远得到同一套题
 *   - 每个方向至少出 2 题；题池按轮转消费，3 天覆盖全部题目后循环
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const BANK_PATH = path.join(__dirname, 'questions.json');
const OUT_DIR = path.join(__dirname, 'days');

const bank = JSON.parse(fs.readFileSync(BANK_PATH, 'utf8'));

/* ------------------------------ 参数解析 ------------------------------ */
const args = process.argv.slice(2);
const argValue = (name, fallback) => {
  const hit = args.find((a) => a.startsWith(`--${name}=`));
  return hit ? hit.slice(name.length + 3) : fallback;
};

const TZ = 'Asia/Shanghai';
const todayStr = () =>
  new Date().toLocaleDateString('sv-SE', { timeZone: TZ }); // sv-SE => YYYY-MM-DD

const dateStr = argValue('date', todayStr());
const perDirection = Math.max(1, Number(argValue('per', bank.meta.perDirectionPerDay)) || 2);
const writeFile = !args.includes('--stdout');

if (!/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
  console.error(`日期格式错误: ${dateStr}，应为 YYYY-MM-DD`);
  process.exit(1);
}

/* --------------------------- 轮转选题（确定性） --------------------------- */
const DAY_MS = 24 * 60 * 60 * 1000;
const anchor = new Date(`${bank.meta.anchorDate}T00:00:00Z`);
const target = new Date(`${dateStr}T00:00:00Z`);
const dayIndex = Math.round((target - anchor) / DAY_MS);
if (Number.isNaN(dayIndex)) {
  console.error(`无法解析日期: ${dateStr}`);
  process.exit(1);
}

/** 取方向 dirIdx 在第 dayIndex 天的 perDirection 道题 */
const pickFor = (pool, dirIdx) => {
  const len = pool.length;
  if (len <= perDirection) return [...pool];
  const stride = Math.max(1, Math.floor(len / perDirection));
  const offset = (((dayIndex * perDirection + dirIdx * 3) % len) + len) % len;
  const picked = [];
  for (let i = 0; i < perDirection; i += 1) {
    const idx = (offset + i * stride) % len;
    if (!picked.includes(pool[idx])) picked.push(pool[idx]);
  }
  // 轮转补齐，避免出现重复项
  for (let i = 0; i < len && picked.length < perDirection; i += 1) {
    if (!picked.includes(pool[i])) picked.push(pool[i]);
  }
  return picked;
};

const daily = bank.directions.map((dir, dirIdx) => ({
  ...dir,
  picked: pickFor(dir.questions, dirIdx),
}));

const total = daily.reduce((sum, d) => sum + d.picked.length, 0);

/* ------------------------------ 渲染 Markdown ------------------------------ */
const CN = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十'];
const cnNum = (n) => (n < CN.length ? CN[n - 1] : String(n));

const lines = [];
lines.push(`# 前端每日面试题 · ${dateStr}（第 ${dayIndex + 1} 天）`);
lines.push('');
lines.push(
  `> 题库来源：${bank.meta.source}`,
);
lines.push(
  `> 覆盖 ${bank.directions.length} 个前端技术方向，共 ${total} 题（每方向至少 ${perDirection} 题）`,
);
lines.push('');
lines.push('---');
lines.push('');

daily.forEach((dir, i) => {
  lines.push(`## ${cnNum(i + 1)}、${dir.name}（${dir.picked.length} 题）`);
  lines.push('');
  dir.picked.forEach((q, j) => {
    lines.push(`### ${i + 1}.${j + 1} [${q.lv}] ${q.q}`);
    lines.push('');
    lines.push(`**参考要点**：${q.a}`);
    lines.push('');
  });
});

lines.push('---');
lines.push('');
lines.push('## 今日方向分布');
lines.push('');
lines.push('| 方向 | 题数 | 难度 |');
lines.push('| --- | --- | --- |');
daily.forEach((dir) => {
  const levels = dir.picked.map((q) => q.lv).join('、');
  lines.push(`| ${dir.name} | ${dir.picked.length} | ${levels} |`);
});
lines.push('');
lines.push(
  `> 下一次轮转：同一方向会换用题库中的其他题目；题池全部消费完（3 天）后从头循环。`,
);

const md = lines.join('\n');

if (writeFile) {
  fs.mkdirSync(OUT_DIR, { recursive: true });
  const outPath = path.join(OUT_DIR, `${dateStr}.md`);
  fs.writeFileSync(outPath, md, 'utf8');
  console.log(`已生成: ${outPath}`);
  console.log(`方向 ${bank.directions.length} 个 · 题目 ${total} 道 · 第 ${dayIndex + 1} 天`);
} else {
  console.log(md);
}
