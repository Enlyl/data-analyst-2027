# -*- coding: utf-8 -*-
"""
Add 'Быстрый квиз: 5 случайных вопросов' button on the hero/home page.
Collects questions across all 18 modules, picks 5 random ones, and renders them interactively.
"""

for path in [r"d:\vibe_app\main_data_analytics\index.html", r"d:\vibe_app\main_data_analytics\course\index.html"]:
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Add button to hero section right below the paragraph
    old_hero_p = '<p>18 модулей, от Excel до AI-агентов. Каждый урок запускается в Google Colab одним кликом. Реальные датасеты, 3 портфолио-проекта, квизы для самопроверки.</p>'
    new_hero_p = '''<p>18 модулей, от Excel до AI-агентов. Каждый урок запускается в Google Colab одним кликом. Реальные датасеты, 3 портфолио-проекта, квизы для самопроверки.</p>
      <div style="margin: 0 auto 32px; display: flex; justify-content: center; gap: 12px; flex-wrap: wrap;">
        <button class="colab-btn" onclick="startRandomQuiz()" style="font-size: 15px; padding: 12px 24px; margin-bottom: 0; background: var(--foundation-primary); color: #fff;">
          🎯 Пройти быстрый квиз (5 случайных вопросов)
        </button>
      </div>'''

    if old_hero_p in html:
        html = html.replace(old_hero_p, new_hero_p, 1)

    # Add startRandomQuiz function definition to script
    random_quiz_js = '''
// ===== RANDOM COMPREHENSIVE QUIZ (5 QUESTIONS ACROSS ALL MODULES) =====
function startRandomQuiz() {
  currentModIdx = -1;
  currentTab = "quiz";
  document.getElementById("topbarTitle").textContent = "Экспресс-тестирование: 5 вопросов по всему курсу";
  
  // Deactivate sidebar items
  document.querySelectorAll(".mod-item").forEach(el => el.classList.remove("active"));
  
  // Tabs bar on topbar
  document.getElementById("tabsBar").innerHTML = `
    <div class="tab active" onclick="startRandomQuiz()">Случайный квиз</div>
    <div class="tab" onclick="showHero()">← На главную</div>
  `;

  // Aggregate all questions from all modules with module title attached
  const allQuestions = [];
  COURSE.forEach(mod => {
    if (mod.quiz) {
      const qList = parseQuiz(mod.quiz);
      qList.forEach(q => {
        allQuestions.push({
          ...q,
          moduleTitle: mod.title
        });
      });
    }
  });

  if (allQuestions.length === 0) {
    document.getElementById("content-area").innerHTML = '<div class="md-view"><p>Квизы не найдены.</p></div>';
    return;
  }

  // Shuffle array using Fisher-Yates and pick 5
  const shuffled = [...allQuestions];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  const selectedQuestions = shuffled.slice(0, 5);

  quizAnswered = {};
  const area = document.getElementById("content-area");

  let html = `
    <div style="max-width: 860px; margin: 0 auto;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
        <button class="colab-btn" onclick="showHero()" style="margin-bottom: 0; padding: 8px 14px; background: var(--foundation-secondary);">
          ← На главную
        </button>
        <button class="colab-btn" onclick="startRandomQuiz()" style="margin-bottom: 0; padding: 8px 14px; background: var(--foundation-primary);">
          🔄 Новые 5 вопросов
        </button>
      </div>

      <div class="quiz-score">
        <div class="quiz-score-num" id="quizScore">0/5</div>
        <div class="quiz-score-label">Правильных ответов</div>
      </div>
  `;

  selectedQuestions.forEach((q, qi) => {
    html += `
      <div class="quiz-question" id="q${qi}">
        <div style="font-size: 11px; font-weight: 700; color: var(--foundation-primary); text-transform: uppercase; margin-bottom: 6px; letter-spacing: 0.05em;">
          ${escapeHtml(q.moduleTitle)}
        </div>
        <h3>Вопрос ${qi + 1}: ${escapeHtml(q.question)}</h3>
    `;

    q.options.forEach((opt, oi) => {
      html += `
        <div class="quiz-option" data-q="${qi}" data-o="${oi}" data-correct="${opt.correct}" onclick="answerQuiz(this)">
          <div class="radio"></div>
          <span>${escapeHtml(opt.text)}</span>
        </div>
      `;
    });

    if (q.explanation) {
      html += `<div class="quiz-explanation" id="expl${qi}"><b>Объяснение:</b> ${escapeHtml(q.explanation)}</div>`;
    }

    html += '</div>';
  });

  html += `
      <div style="text-align: center; margin-top: 32px; margin-bottom: 48px;">
        <button class="colab-btn" onclick="startRandomQuiz()" style="font-size: 15px; padding: 12px 24px; background: var(--foundation-primary);">
          🔄 Пройти еще раз (другие 5 вопросов)
        </button>
      </div>
    </div>
  `;

  area.innerHTML = html;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
'''

    # Insert function before </script>
    if "function startRandomQuiz()" not in html:
        html = html.replace("</script>", random_quiz_js + "\n</script>", 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

print("Random quiz button and handler added.")
