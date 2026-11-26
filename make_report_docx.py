"""Создаёт отчёт по практической работе №7 в стиле отчётов по графикам/математике."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn
from docx.shared import Cm, Pt

ROOT = Path(r"F:\labagit")
FIG_DIR = ROOT / "report_figures"
TEMPLATE = Path(r"F:\graphs1var\Отчет по Математическим.docx")
OUTPUT = ROOT / "Отчет по Git и GitHub.docx"

FIG_DIR.mkdir(exist_ok=True)


def save_fig(fig, name):
    path = FIG_DIR / name
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return path


# Рисунок 1 — история коммитов
fig, ax = plt.subplots(figsize=(10, 3.6))
ax.set_xlim(0, 6)
ax.set_ylim(-0.8, 1.8)
ax.axis("off")
commits = [
    (0.5, 0, "7182816\nreport"),
    (2.0, 0, "abd3755\nmerge"),
    (3.5, 1, "a73a3b7\nreport-branch"),
    (5.0, 0, "1b4eec9\nsites"),
]
for (x1, y1, _), (x2, y2, _) in zip(commits, commits[1:]):
    ax.plot([x1, x2], [y1, y2], color="#2563eb", lw=2)
ax.plot([0.5, 2.0, 5.0], [0, 0, 0], "o", color="#2563eb", ms=12)
ax.plot([3.5], [1], "o", color="#f59e0b", ms=12)
ax.plot([2.0, 3.5], [0, 1], color="#f59e0b", lw=2)
for x, y, label in commits:
    ax.text(x, y - 0.42, label, ha="center", va="top", fontsize=8)
ax.text(0.5, 0.32, "main", ha="center", fontsize=9, color="#1d4ed8")
ax.text(3.5, 1.32, "report-branch", ha="center", fontsize=9, color="#b45309")
fig1 = save_fig(fig, "01_git_history.png")

# Рисунок 2 — структура репозитория
fig, ax = plt.subplots(figsize=(9, 5.2))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")
tree = """homework-IIT/
├── .gitignore
├── README.md
├── Отчет_по_практической_работе_7.md
├── docs/                      <- статический сайт (GitHub Pages)
│   ├── index.html
│   ├── css/style.css
│   ├── js/script.js
│   └── README.md
└── dynamic-site/              <- динамический сайт (Flask)
    ├── app.py
    ├── templates/index.html
    ├── static/style.css
    ├── requirements.txt
    ├── render.yaml
    └── README.md"""
ax.text(0.2, 9.6, tree, va="top", ha="left", family="Consolas", fontsize=11,
        bbox=dict(boxstyle="round,pad=0.5", fc="#f8fafc", ec="#94a3b8"))
fig2 = save_fig(fig, "02_repo_structure.png")

# Рисунок 3 — схема публикации
fig, ax = plt.subplots(figsize=(10, 3.2))
ax.set_xlim(0, 12)
ax.set_ylim(0, 4)
ax.axis("off")
boxes = [
    (0.5, "Локальный\nрепозиторий\nF:\\labagit", "#dbeafe"),
    (4.5, "GitHub\n homework-IIT\nsayusayusayu1337", "#dcfce7"),
    (8.5, "GitHub Pages\nsayusayusayu1337.\ngithub.io/homework-IIT", "#fef3c7"),
]
for x, text, color in boxes:
    ax.add_patch(FancyBboxPatch((x, 1.0), 3.0, 2.0, boxstyle="round,pad=0.15",
                                fc=color, ec="#475569", lw=1.5))
    ax.text(x + 1.5, 2.0, text, ha="center", va="center", fontsize=10)
for x in (3.6, 7.6):
    ax.add_patch(FancyArrowPatch((x, 2.0), (x + 0.8, 2.0), arrowstyle="-|>",
                                 mutation_scale=18, lw=2, color="#2563eb"))
ax.text(4.0, 3.4, "git push", ha="center", fontsize=9, color="#1d4ed8")
ax.text(8.0, 3.4, "Deploy from a branch: main / docs", ha="center", fontsize=9, color="#1d4ed8")
fig3 = save_fig(fig, "03_github_publishing.png")

# Документ на основе существующего шаблона
doc = Document(TEMPLATE)
body = doc.element.body
for child in list(body):
    if child.tag != qn("w:sectPr"):
        body.remove(child)


def add(text="", size=14, bold=False, align=None, style="Normal (Web)", font="Calibri"):
    p = doc.add_paragraph(style=style)
    if align is not None:
        p.alignment = align
    if text:
        run = p.add_run(text)
        run.font.name = font
        run.font.size = Pt(size)
        run.bold = bold
    return p


def heading(text):
    add(text, size=26, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, style="Normal")


def body_line(text):
    add(text, size=14)


# Титульная страница
title = add("", size=22, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, style="Normal")
title.add_run("Практическая работа\n")
title.add_run("по дисциплине «Введение в информационные технологии»\n")
title.add_run("на тему «Git и GitHub»")
for line in [
    "Выполнил: студент группы БИК2611",
    "Звалинский Олег Евгеньевич",
    "Проверили:",
    "старший преподаватель кафедры ТиЗВ",
    "Егоров Дмитрий Аркадьевич",
    "старший преподаватель кафедры ТиЗВ",
    "Федоров Владимир Дмитриевич",
]:
    add(line, size=14, align=WD_ALIGN_PARAGRAPH.RIGHT, style="Normal")
add(style="Normal")
add(style="Normal")
for _ in range(7):
    add(style="Normal", align=WD_ALIGN_PARAGRAPH.CENTER)
add("Москва 2026", size=14, align=WD_ALIGN_PARAGRAPH.RIGHT, style="Normal")
add(style="Normal").add_run().add_break(WD_BREAK.PAGE)

# Цели
heading("Цели работы:")
for line in [
    "— Установить Git и создать локальный репозиторий",
    "— Научиться фиксировать версии отчёта в Git",
    "— Создать ветку отчёта и слить её в основную ветку",
    "— Зарегистрироваться на GitHub и загрузить проект «homework IIT»",
    "— Разместить статический сайт и подготовить динамический сайт",
]:
    add(line, size=16.5)

# Задание
heading("Задание")
add(
    "1. Установить GIT. 2. Создать локальный репозиторий. 3. Создать файл отчёта по выполнению "
    "практической работы, поместить его в репозиторий и зафиксировать версию в Git. 4. Создать ветку "
    "отчёта в Git, добавить описания шагов в отчёт и создать версию отчёта в новой ветке. 5. Слить "
    "последнее изменение отчёта в основную ветку. 6. Зарегистрироваться на GitHub, создать проект "
    "«homework IIT» и залить содержимое локального репозитория в проект. 7. Разместить на GitHub "
    "статический сайт. 8. Дополнительное задание — разместить на GitHub динамический сайт. "
    "9. Завершить отчёт, добавив описание всех пунктов.",
    size=16.5,
)

# Ход работы
heading("Ход работы")
steps = [
    "1. Я создал папку F:\\labagit и скачал установщик Git for Windows F:\\Git-2.56.0.4-64-bit.exe. "
    "Установку выполнил в тихом режиме с параметром /DIR=F:\\Git, чтобы не изменять диск C. Проверка: "
    "git version 2.56.0.windows.4.",
    "2. В папке F:\\labagit выполнил git init -b main и локально настроил имя, e-mail и core.autocrlf "
    "командами git config. Глобальный конфиг на диске C не трогал.",
    "3. Создал файл Отчет_по_практической_работе_7.md с описанием первых шагов, добавил его командой "
    "git add . и зафиксировал первую версию коммитом 7182816.",
    "4. Создал ветку report-branch командой git checkout -b report-branch, дописал в отчёт подробные "
    "описания команд git add, git commit, git log и назначения веток. Новую версию зафиксировал "
    "коммитом a73a3b7 уже в этой ветке.",
    "5. Вернулся в main и выполнил git merge --no-ff report-branch -m \"Merge report-branch into main\". "
    "Коммит слияния получил хеш abd3755; история коммитов показана на рисунке 1.",
    "6. Создал статический сайт в папке docs/ (index.html, css/style.css, js/script.js) и динамический "
    "сайт на Flask в папке dynamic-site/ (app.py, шаблон, стили, requirements.txt, render.yaml). "
    "Динамический сайт проверил тестовым клиентом Flask: GET / вернул 200, POST с именем — приветствие "
    "«Привет, Олег!». Структура проекта показана на рисунке 2.",
    "7. Зарегистрировал аккаунт GitHub с логином sayusayusayu1337, авторизовал GitHub CLI по коду "
    "устройства через https://github.com/login/device, создал репозиторий homework-IIT и загрузил ветки "
    "командой git push -u origin main report-branch.",
    "8. Через API GitHub включил публикацию Pages из ветки main, папки /docs. Сайт доступен по адресу "
    "https://sayusayusayu1337.github.io/homework-IIT/ и отвечает кодом 200. Схема публикации — рисунок 3.",
    "9. Добавил README.md, дописал в отчёт все пункты задания и ссылки. Финальный коммит 35729fe "
    "отправлен в GitHub; рабочее дерево чистое.",
]
for step in steps:
    body_line(step)

for image, caption in [
    (fig1, "Рисунок 1 — История коммитов и слияние ветки report-branch"),
    (fig2, "Рисунок 2 — Структура репозитория homework-IIT"),
    (fig3, "Рисунок 3 — Публикация проекта на GitHub и GitHub Pages"),
]:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(image), width=Cm(15))
    add(caption, size=12, align=WD_ALIGN_PARAGRAPH.CENTER, style="Normal")

# Вывод
heading("Вывод")
add(
    "В ходе практики установлен Git 2.56.0, создан локальный репозиторий в папке F:\\labagit и освоена "
    "работа с версиями документа. Отчёт прошёл несколько версий: начальный коммит, коммит в ветке "
    "report-branch и коммит слияния в основную ветку. Проект загружен в репозиторий GitHub "
    "https://github.com/sayusayusayu1337/homework-IIT. Статический сайт опубликован через GitHub Pages "
    "по адресу https://sayusayusayu1337.github.io/homework-IIT/, динамический сайт на Flask размещён "
    "в репозитории с готовой конфигурацией и инструкцией по запуску. Все пункты задания выполнены.",
    size=16.5,
)

doc.save(OUTPUT)
print(OUTPUT)
