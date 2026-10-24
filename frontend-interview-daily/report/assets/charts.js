// assets/charts.js — 每日前端面试题报告图表逻辑
// 数据来自页内 <script type="application/json" id="report-data">，
// 颜色统一取自 CSS 变量，保证与主题一致
(function () {
  var style = getComputedStyle(document.documentElement);
  var accent = style.getPropertyValue('--accent').trim() || '#7aa2ff';
  var accent2 = style.getPropertyValue('--accent2').trim() || '#6ee7b7';
  var ink = style.getPropertyValue('--ink').trim() || '#e8edf7';
  var muted = style.getPropertyValue('--muted').trim() || '#8d99b0';
  var rule = style.getPropertyValue('--rule').trim() || '#222c3e';
  var bg2 = style.getPropertyValue('--bg2').trim() || '#121826';

  var holder = document.getElementById('report-data');
  var data = {};
  if (holder) {
    try {
      data = JSON.parse(holder.textContent || '{}');
    } catch (e) {
      data = {};
    }
  }
  var axisLabel = { color: muted, fontSize: 11 };
  var splitLine = { lineStyle: { color: rule, type: 'dashed' } };

  // 1) 各方向题库覆盖量
  var poolEl = document.getElementById('chart-pool');
  if (poolEl && (data.directions || []).length) {
    var rows = data.directions.slice().sort(function (a, b) { return a.count - b.count; });
    var chart = echarts.init(poolEl, null, { renderer: 'canvas' });
    chart.setOption({
      backgroundColor: 'transparent',
      grid: { left: 8, right: 40, top: 8, bottom: 8, containLabel: true },
      tooltip: {
        trigger: 'axis',
        axisPointer: { type: 'shadow' },
        backgroundColor: bg2,
        borderColor: rule,
        textStyle: { color: ink },
        formatter: function (p) {
          var i = p[0].dataIndex;
          return p[0].name + '<br/>题库覆盖 ' + rows[i].count + ' 题';
        }
      },
      xAxis: {
        type: 'value',
        axisLabel: axisLabel,
        splitLine: splitLine,
        axisLine: { show: false },
        axisTick: { show: false }
      },
      yAxis: {
        type: 'category',
        data: rows.map(function (r) { return r.name; }),
        axisLabel: axisLabel,
        axisLine: { show: false },
        axisTick: { show: false }
      },
      series: [{
        type: 'bar',
        data: rows.map(function (r) { return r.count; }),
        barWidth: '58%',
        itemStyle: { color: accent, borderRadius: [0, 4, 4, 0] },
        emphasis: { itemStyle: { color: accent2 } }
      }]
    });
    window.addEventListener('resize', function () { chart.resize(); });
  }

  // 2) 今日题目难度分布
  var diffEl = document.getElementById('chart-difficulty');
  if (diffEl && (data.difficulty || []).length) {
    var d2 = echarts.init(diffEl, null, { renderer: 'canvas' });
    d2.setOption({
      backgroundColor: 'transparent',
      tooltip: {
        trigger: 'item',
        backgroundColor: bg2,
        borderColor: rule,
        textStyle: { color: ink },
        formatter: '{b}: {c} 题 ({d}%)'
      },
      legend: {
        bottom: 0,
        icon: 'circle',
        itemWidth: 8,
        itemHeight: 8,
        textStyle: { color: muted, fontSize: 11 }
      },
      series: [{
        type: 'pie',
        radius: ['52%', '76%'],
        center: ['50%', '45%'],
        avoidLabelOverlap: true,
        itemStyle: { borderColor: bg2, borderWidth: 2 },
        label: { show: false },
        emphasis: { scale: true, scaleSize: 6 },
        data: data.difficulty.map(function (d) {
          return { name: d.name, value: d.value };
        })
      }]
    });
    window.addEventListener('resize', function () { d2.resize(); });
  }
})();
