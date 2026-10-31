# -*- coding: utf-8 -*-
"""Inject lieflat-charts animations into index.html"""
import re

HTML_PATH = r"d:\vibe_app\main_data_analytics\index.html"
COURSE_PATH = r"d:\vibe_app\main_data_analytics\course\index.html"

with open(HTML_PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1) Insert lieflat CSS before </style>
lf_css = '''
    /* ===== LIEFLAT CHARTS ANIMATIONS (dark-adapted) ===== */
    .lf-charts-row {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 16px;
      max-width: 900px;
      margin: 48px auto 0;
    }
    .lf-card {
      background: var(--bg-card);
      border-radius: 16px;
      padding: 20px 20px 14px;
      cursor: pointer;
      border: 1px solid var(--border);
      transition: border-color 300ms var(--ease);
    }
    .lf-card:hover { border-color: var(--border-focus); }
    .lf-card h3 {
      font-size: 14px;
      font-weight: 600;
      letter-spacing: -0.02em;
      margin-bottom: 2px;
      color: var(--text-main);
    }
    .lf-card .lf-sub {
      font-size: 11px;
      color: var(--text-muted);
      margin-bottom: 12px;
    }
    .lf-card svg { width: 100%; display: block; }
    .lf-card .lf-src {
      font-size: 9px;
      color: var(--text-dim);
      margin-top: 8px;
      letter-spacing: 0.08em;
      font-weight: 500;
      font-family: var(--font-mono);
    }
    .lf-pop { transform-box: fill-box; transform-origin: center bottom; animation: lfPop 0.5s cubic-bezier(0.2,0.7,0.3,1.3) both; }
    @keyframes lfPop { from { transform: scaleY(0); } to { transform: none; } }
    .lf-fade { animation: lfFade 0.9s ease both; }
    @keyframes lfFade { from { opacity: 0; } }
    .lf-draw { stroke-dasharray: 1; stroke-dashoffset: 1; animation: lfDraw 1.2s cubic-bezier(0.4,0,0.2,1) both; }
    @keyframes lfDraw { to { stroke-dashoffset: 0; } }
    .lf-dot-pop { transform-box: fill-box; transform-origin: center; animation: lfDotPop 0.4s cubic-bezier(0.2,0.7,0.3,1.3) both; }
    @keyframes lfDotPop { from { transform: scale(0); } to { transform: none; } }
    @media (max-width: 768px) {
      .lf-charts-row { grid-template-columns: 1fr; max-width: 320px; }
    }
'''
html = html.replace('  </style>', lf_css + '  </style>', 1)

# 2) Replace the showHero function to include animated charts
old_hero = '''function showHero() {
  currentModIdx = -1;
  currentTab = "readme";
  document.getElementById("topbarTitle").textContent = "Data Analyst 2027";
  document.getElementById("tabsBar").innerHTML = "";

  // deactivate sidebar
  document.querySelectorAll(".mod-item").forEach(el => el.classList.remove("active"));

  const totalNb = COURSE.reduce((s, m) => s + m.notebooks.length, 0);

  document.getElementById("content-area").innerHTML = `
    <div class="hero">
      <div class="hero-badge">\u0418\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u043a\u0443\u0440\u0441 2027</div>
      <h1>\u0421\u0442\u0430\u043d\u044c Data Analyst<br>\u0432 \u044d\u043f\u043e\u0445\u0443 AI</h1>
      <p>18 \u043c\u043e\u0434\u0443\u043b\u0435\u0439, \u043e\u0442 Excel \u0434\u043e AI-\u0430\u0433\u0435\u043d\u0442\u043e\u0432. \u041a\u0430\u0436\u0434\u044b\u0439 \u0443\u0440\u043e\u043a \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0435\u0442\u0441\u044f \u0432 Google Colab \u043e\u0434\u043d\u0438\u043c \u043a\u043b\u0438\u043a\u043e\u043c. \u0420\u0435\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u0442\u0430\u0441\u0435\u0442\u044b, 3 \u043f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e-\u043f\u0440\u043e\u0435\u043a\u0442\u0430, \u043a\u0432\u0438\u0437\u044b \u0434\u043b\u044f \u0441\u0430\u043c\u043e\u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438.</p>
      <div class="hero-stats">
        <div class="hero-stat">
          <div class="hero-stat-num">${COURSE.length}</div>
          <div class="hero-stat-label">\u043c\u043e\u0434\u0443\u043b\u0435\u0439</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num">${totalNb}</div>
          <div class="hero-stat-label">Colab \u043d\u043e\u0443\u0442\u0431\u0443\u043a\u043e\u0432</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num">3</div>
          <div class="hero-stat-label">\u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u043f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e</div>
        </div>
      </div>
    </div>
  `;
}'''

new_hero = '''function showHero() {
  currentModIdx = -1;
  currentTab = "readme";
  document.getElementById("topbarTitle").textContent = "Data Analyst 2027";
  document.getElementById("tabsBar").innerHTML = "";

  document.querySelectorAll(".mod-item").forEach(el => el.classList.remove("active"));

  const totalNb = COURSE.reduce((s, m) => s + m.notebooks.length, 0);

  document.getElementById("content-area").innerHTML = `
    <div class="hero">
      <div class="hero-badge">\u0418\u043d\u0442\u0435\u0440\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439 \u043a\u0443\u0440\u0441 2027</div>
      <h1>\u0421\u0442\u0430\u043d\u044c Data Analyst<br>\u0432 \u044d\u043f\u043e\u0445\u0443 AI</h1>
      <p>18 \u043c\u043e\u0434\u0443\u043b\u0435\u0439, \u043e\u0442 Excel \u0434\u043e AI-\u0430\u0433\u0435\u043d\u0442\u043e\u0432. \u041a\u0430\u0436\u0434\u044b\u0439 \u0443\u0440\u043e\u043a \u0437\u0430\u043f\u0443\u0441\u043a\u0430\u0435\u0442\u0441\u044f \u0432 Google Colab \u043e\u0434\u043d\u0438\u043c \u043a\u043b\u0438\u043a\u043e\u043c. \u0420\u0435\u0430\u043b\u044c\u043d\u044b\u0435 \u0434\u0430\u0442\u0430\u0441\u0435\u0442\u044b, 3 \u043f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e-\u043f\u0440\u043e\u0435\u043a\u0442\u0430, \u043a\u0432\u0438\u0437\u044b \u0434\u043b\u044f \u0441\u0430\u043c\u043e\u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438.</p>
      <div class="hero-stats">
        <div class="hero-stat">
          <div class="hero-stat-num">${COURSE.length}</div>
          <div class="hero-stat-label">\u043c\u043e\u0434\u0443\u043b\u0435\u0439</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num">${totalNb}</div>
          <div class="hero-stat-label">Colab \u043d\u043e\u0443\u0442\u0431\u0443\u043a\u043e\u0432</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num">3</div>
          <div class="hero-stat-label">\u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u043f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e</div>
        </div>
      </div>

      <!-- Lieflat Charts: animated SVG data viz -->
      <div class="lf-charts-row">
        <div class="lf-card" onclick="replayChart('lfRungs')">
          <h3>\u041d\u0430\u0432\u044b\u043a\u0438 \u043a\u0443\u0440\u0441\u0430, \u043f\u043e \u0447\u0430\u0441\u0442\u044f\u043c</h3>
          <div class="lf-sub">\u043e\u0434\u043d\u0430 \u0441\u0442\u0443\u043f\u0435\u043d\u044c\u043a\u0430 = 1 \u043c\u043e\u0434\u0443\u043b\u044c \u00b7 \u043a\u043b\u0438\u043a \u2014 \u043f\u0435\u0440\u0435\u0438\u0433\u0440\u0430\u0442\u044c</div>
          <svg id="lfRungs" viewBox="0 0 260 200" preserveAspectRatio="xMidYMid meet" role="img" aria-label="\u0420\u0430\u0441\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u043c\u043e\u0434\u0443\u043b\u0435\u0439 \u043f\u043e \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f\u043c: \u0425\u0430\u0440\u0434 5, AI 5, \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 2, \u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e 3, \u0421\u043e\u0444\u0442 3"></svg>
          <div class="lf-src">RUNG BARS \u00b7 \u041a\u0423\u0420\u0421 2027</div>
        </div>
        <div class="lf-card" onclick="replayChart('lfWaffle')">
          <h3>\u0421\u043e\u0441\u0442\u0430\u0432 \u043a\u0443\u0440\u0441\u0430</h3>
          <div class="lf-sub">\u043e\u0434\u043d\u0430 \u0442\u043e\u0447\u043a\u0430 = 1 \u043d\u043e\u0443\u0442\u0431\u0443\u043a \u00b7 67 \u0443\u0440\u043e\u043a\u043e\u0432</div>
          <svg id="lfWaffle" viewBox="0 0 260 200" preserveAspectRatio="xMidYMid meet" role="img" aria-label="\u0421\u043e\u0441\u0442\u0430\u0432 \u043a\u0443\u0440\u0441\u0430: 67 \u043d\u043e\u0443\u0442\u0431\u0443\u043a\u043e\u0432 \u043f\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043c"></svg>
          <div class="lf-src">DOT WAFFLE \u00b7 \u041a\u0423\u0420\u0421 2027</div>
        </div>
        <div class="lf-card" onclick="replayChart('lfLine')">
          <h3>\u041a\u0440\u0438\u0432\u0430\u044f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f</h3>
          <div class="lf-sub">\u043d\u0435\u0434\u0435\u043b\u044f \u0437\u0430 \u043d\u0435\u0434\u0435\u043b\u0435\u0439 \u00b7 \u043a\u0443\u043c\u0443\u043b\u044f\u0442\u0438\u0432\u043d\u044b\u0435 \u043d\u0430\u0432\u044b\u043a\u0438</div>
          <svg id="lfLine" viewBox="0 0 260 200" preserveAspectRatio="xMidYMid meet" role="img" aria-label="\u041a\u0440\u0438\u0432\u0430\u044f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f: \u0440\u043e\u0441\u0442 \u043d\u0430\u0432\u044b\u043a\u043e\u0432 \u0437\u0430 18 \u043d\u0435\u0434\u0435\u043b\u044c"></svg>
          <div class="lf-src">HAIRLINE LINE \u00b7 \u041a\u0423\u0420\u0421 2027</div>
        </div>
      </div>
    </div>
  `;
  renderLieflatCharts();
}

// ===== LIEFLAT CHARTS ENGINE (dark-adapted mono tokens) =====
const LF = {
  INK: '#FFFFFF', PAPER: '#272727', MUTED: '#9B9B9B', FAINT: '#666666',
  GRID: '#313131', ACCENT: '#F97316',
  L: ['#FFFFFF','#E0E0E0','#C0C0C0','#9B9B9B','#777777','#666666','#555555'],
  rnd: (i,k) => Math.abs(((i*73856093)^(k*19349663))%1000)/1000,
  el: (p,t,a) => { const n=document.createElementNS('http://www.w3.org/2000/svg',t); for(const k in a) n.setAttribute(k,a[k]); p.appendChild(n); return n; },
  txt: (p,a,s) => { const n=LF.el(p,'text',a); n.textContent=s; return n; },
};

function renderLieflatCharts() {
  drawRungs();
  drawWaffle();
  drawLine();
}

function replayChart(id) {
  const svg = document.getElementById(id);
  if (!svg) return;
  svg.innerHTML = '';
  if (id === 'lfRungs') drawRungs();
  else if (id === 'lfWaffle') drawWaffle();
  else if (id === 'lfLine') drawLine();
}

// ---- F1 Rung Bars: course skills breakdown ----
function drawRungs() {
  const svg = document.getElementById('lfRungs');
  if (!svg) return;
  svg.innerHTML = '';

  const data = [
    {label: '\u0425\u0430\u0440\u0434', v: 5, shade: LF.L[0]},
    {label: 'AI',   v: 5, shade: LF.L[1]},
    {label: '\u041f\u043e\u0440\u0442\u0444.', v: 3, shade: LF.L[2]},
    {label: '\u0421\u0442\u0430\u0442\u044b', v: 2, shade: LF.L[3]},
    {label: '\u0421\u043e\u0444\u0442', v: 2, shade: LF.L[4]},
    {label: '\u041a\u0430\u0440\u044c\u0435\u0440\u0430', v: 1, shade: LF.L[5]},
  ];
  const maxV = Math.max(...data.map(d=>d.v));
  const barW = 28, gap = 12, startX = 50, startY = 175;
  const rungH = 6, rungGap = 3;

  data.forEach((d, i) => {
    const x = startX + i * (barW + gap);
    // Draw rungs (each rung = 1 module)
    for (let r = 0; r < d.v; r++) {
      const ry = startY - (r+1) * (rungH + rungGap);
      const rect = LF.el(svg, 'rect', {
        x: x, y: ry, width: barW, height: rungH,
        rx: 3, fill: d.shade,
        class: 'lf-pop',
        style: `animation-delay: ${(i * 100 + r * 30)}ms`
      });
    }
    // Value on top
    const topY = startY - d.v * (rungH + rungGap) - 6;
    LF.txt(svg, {x: x + barW/2, y: topY, 'text-anchor': 'middle', fill: LF.INK,
      'font-size': '11', 'font-weight': '700', 'font-family': "'Geist','Inter',sans-serif",
      class: 'lf-fade', style: `animation-delay: ${i * 100 + 200}ms`
    }, d.v);
    // Label below
    LF.txt(svg, {x: x + barW/2, y: startY + 14, 'text-anchor': 'middle', fill: LF.MUTED,
      'font-size': '9', 'font-weight': '600', 'font-family': "'Geist','Inter',sans-serif",
      class: 'lf-fade', style: `animation-delay: ${i * 100 + 100}ms`
    }, d.label);
  });

  // Baseline
  LF.el(svg, 'line', {x1: startX-8, y1: startY+1, x2: startX + data.length*(barW+gap)-gap+8, y2: startY+1,
    stroke: LF.GRID, 'stroke-width': '0.7'});
}

// ---- G4 Dot Waffle: course composition ----
function drawWaffle() {
  const svg = document.getElementById('lfWaffle');
  if (!svg) return;
  svg.innerHTML = '';

  // Category dot counts (total ~67 notebooks)
  const cats = [
    {n: 24, color: '#FFFFFF', label: '\u0425\u0430\u0440\u0434 \u0431\u0430\u0437\u0430'},
    {n: 19, color: '#C0C0C0', label: 'AI \u0441\u0442\u0435\u043a'},
    {n:  8, color: '#F97316', label: '\u041f\u043e\u0440\u0442\u0444\u043e\u043b\u0438\u043e'},
    {n: 10, color: '#9B9B9B', label: '\u0421\u0442\u0430\u0442\u044b & A/B'},
    {n:  6, color: '#666666', label: '\u041e\u0441\u0442\u0430\u043b\u044c\u043d\u043e\u0435'},
  ];

  const cols = 10, r = 7, gap = 18, startX = 22, startY = 16;
  let idx = 0;
  cats.forEach((cat) => {
    for (let d = 0; d < cat.n; d++) {
      const col = idx % cols;
      const row = Math.floor(idx / cols);
      LF.el(svg, 'circle', {
        cx: startX + col * gap, cy: startY + row * gap,
        r: r, fill: cat.color,
        class: 'lf-dot-pop',
        style: `animation-delay: ${idx * 12}ms`
      });
      idx++;
    }
  });

  // Legend
  let lx = 10, ly = 186;
  cats.forEach((cat, i) => {
    LF.el(svg, 'circle', {cx: lx, cy: ly, r: 3.5, fill: cat.color});
    LF.txt(svg, {x: lx + 7, y: ly + 3, fill: LF.MUTED,
      'font-size': '8', 'font-weight': '500', 'font-family': "'Geist','Inter',sans-serif"
    }, cat.label);
    lx += 52;
  });
}

// ---- F2 Hairline Line: learning curve ----
function drawLine() {
  const svg = document.getElementById('lfLine');
  if (!svg) return;
  svg.innerHTML = '';

  // Cumulative skills growth over 18 weeks (sigmoid-like)
  const weeks = 18;
  const vals = [];
  for (let w = 0; w < weeks; w++) {
    vals.push(Math.round(100 / (1 + Math.exp(-0.45 * (w - 9)))));
  }
  const maxV = 100;
  const px = 240, py = 170, ox = 24, oy = 16;
  const sx = (px - ox) / (weeks - 1);

  // Grid lines
  for (let g = 0; g <= 4; g++) {
    const gy = oy + (py - oy) * (1 - g/4);
    LF.el(svg, 'line', {x1: ox, y1: gy, x2: px, y2: gy, stroke: LF.GRID, 'stroke-width': '0.5'});
    LF.txt(svg, {x: ox - 4, y: gy + 3, 'text-anchor': 'end', fill: LF.FAINT,
      'font-size': '8', 'font-family': "'Geist Mono',monospace"
    }, Math.round(g * 25) + '%');
  }

  // Area fill
  let areaD = `M${ox} ${py}`;
  vals.forEach((v, i) => {
    const x = ox + i * sx;
    const y = oy + (py - oy) * (1 - v / maxV);
    areaD += ` L${x} ${y}`;
  });
  areaD += ` L${ox + (weeks-1)*sx} ${py} Z`;
  LF.el(svg, 'path', {d: areaD, fill: LF.INK, opacity: '0.06', class: 'lf-fade'});

  // Line with draw animation
  let lineD = '';
  vals.forEach((v, i) => {
    const x = ox + i * sx;
    const y = oy + (py - oy) * (1 - v / maxV);
    lineD += (i === 0 ? 'M' : ' L') + x.toFixed(1) + ' ' + y.toFixed(1);
  });
  const line = LF.el(svg, 'polyline', {
    points: lineD.replace(/[ML]/g,'').trim().replace(/ L/g, ' '),
    fill: 'none', stroke: LF.INK, 'stroke-width': '2',
    'stroke-linecap': 'round', 'stroke-linejoin': 'round',
    'pathLength': '1', class: 'lf-draw'
  });
  // Fix: polyline needs points not d. Redo with path:
  svg.removeChild(line);
  LF.el(svg, 'path', {
    d: lineD, fill: 'none', stroke: LF.INK, 'stroke-width': '2',
    'stroke-linecap': 'round', 'stroke-linejoin': 'round',
    'pathLength': '1', class: 'lf-draw'
  });

  // Dots at each week
  vals.forEach((v, i) => {
    const x = ox + i * sx;
    const y = oy + (py - oy) * (1 - v / maxV);
    LF.el(svg, 'circle', {
      cx: x, cy: y, r: 2.5,
      fill: (i === weeks - 1) ? LF.ACCENT : LF.INK,
      class: 'lf-dot-pop',
      style: `animation-delay: ${600 + i * 40}ms`
    });
  });

  // End value label
  const lastX = ox + (weeks-1) * sx;
  const lastY = oy + (py - oy) * (1 - vals[weeks-1] / maxV);
  LF.txt(svg, {x: lastX + 1, y: lastY - 8, 'text-anchor': 'middle', fill: LF.ACCENT,
    'font-size': '12', 'font-weight': '700', 'font-family': "'Geist Mono',monospace",
    class: 'lf-fade', style: 'animation-delay: 1200ms'
  }, vals[weeks-1] + '%');

  // Week labels
  LF.txt(svg, {x: ox, y: py + 14, 'text-anchor': 'middle', fill: LF.FAINT,
    'font-size': '8', 'font-family': "'Geist',sans-serif"
  }, '\u041d\u04351');
  LF.txt(svg, {x: ox + Math.floor(weeks/2)*sx, y: py + 14, 'text-anchor': 'middle', fill: LF.FAINT,
    'font-size': '8', 'font-family': "'Geist',sans-serif"
  }, '\u041d\u04359');
  LF.txt(svg, {x: px, y: py + 14, 'text-anchor': 'middle', fill: LF.FAINT,
    'font-size': '8', 'font-family': "'Geist',sans-serif"
  }, '\u041d\u043518');
}'''

# Do the replacement
if old_hero in html:
    html = html.replace(old_hero, new_hero, 1)
    print("Hero function replaced successfully")
else:
    # Try a regex approach in case of whitespace differences
    pattern = r'function showHero\(\) \{[^}]+\n  `;\n\}'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        html = html[:match.start()] + new_hero + html[match.end():]
        print("Hero replaced via regex")
    else:
        print("WARNING: Could not find showHero function to replace")
        # Fallback: find it by line and replace
        lines = html.split('\n')
        start_idx = None
        end_idx = None
        brace_count = 0
        for i, line in enumerate(lines):
            if 'function showHero()' in line:
                start_idx = i
                brace_count = 0
            if start_idx is not None:
                brace_count += line.count('{') - line.count('}')
                if brace_count == 0 and i > start_idx:
                    end_idx = i
                    break
        if start_idx is not None and end_idx is not None:
            lines = lines[:start_idx] + new_hero.split('\n') + lines[end_idx+1:]
            html = '\n'.join(lines)
            print(f"Hero replaced by line range {start_idx}-{end_idx}")
        else:
            print("FAILED: Could not locate showHero at all")

with open(HTML_PATH, "w", encoding="utf-8") as f:
    f.write(html)
with open(COURSE_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Done. File size: {len(html)} bytes")
