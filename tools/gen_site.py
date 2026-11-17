#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 FileExplorer8 支持站点与 README 的全部语言版本。

文案放在 tools/pages/<code>.json，本脚本只负责套模板。
之所以生成而不是手写 14 份页面，是为了让结构、样式、语言切换条永远一致。

用法：
    python3 tools/gen_site.py

产物（写在仓库根目录）：
    index.html / index.<code>.html
    privacy.html / privacy.<code>.html
    README.md / README.<code>.md
"""

from __future__ import annotations

import json
import pathlib
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ROOT / "tools" / "pages"

# 顺序与应用菜单「语言 ▸」一致：先中文，再英文，其余按使用广度。
# 这里只保留 code / nativeName，改语言集合要同步源工程的 scripts/l10n/languages.json。
LANGS = [
    ("zh-Hans", "简体中文"),
    ("zh-Hant", "繁體中文"),
    ("en", "English"),
    ("ja", "日本語"),
    ("ko", "한국어"),
    ("de", "Deutsch"),
    ("fr", "Français"),
    ("es", "Español"),
    ("pt-BR", "Português (Brasil)"),
    ("ru", "Русский"),
    ("vi", "Tiếng Việt"),
    ("id", "Bahasa Indonesia"),
    ("ms", "Bahasa Melayu"),
    ("th", "ไทย"),
]

ISSUES = "https://github.com/rosesmall2010/FileExplorer8/issues"
SITE = "https://rosesmall2010.github.io/FileExplorer8/"
VERSION = "1.1.6"


def html_name(base: str, code: str) -> str:
    """中文是默认语言，占不带后缀的文件名。"""
    return f"{base}.html" if code == "zh-Hans" else f"{base}.{code}.html"


def readme_name(code: str) -> str:
    return "README.md" if code == "zh-Hans" else f"README.{code}.md"


def langbar(code: str, base: str) -> str:
    """语言切换条。当前语言是不能点的 span。"""
    parts = []
    for other, label in LANGS:
        if other == code:
            parts.append(f'<span aria-current="page">{label}</span>')
        else:
            parts.append(f'<a href="{html_name(base, other)}" hreflang="{other}" lang="{other}">{label}</a>')
    return '<div class="lang">' + "".join(parts) + "</div>"


def render_blocks(blocks) -> str:
    """按顺序渲染正文块。支持 h3 / p / ul / table。"""
    out = []
    for b in blocks:
        if "h3" in b:
            out.append(f'<h3>{b["h3"]}</h3>')
        if "p" in b:
            out.append(f"<p>{b['p']}</p>")
        if "ul" in b:
            items = "".join(f"<li>{x}</li>" for x in b["ul"])
            out.append(f"<ul>{items}</ul>")
        if "table" in b:
            t = b["table"]
            head = "".join(f"<th>{c}</th>" for c in t["head"])
            rows = "".join(
                "<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in t["rows"]
            )
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>")
    return "\n".join(out)


def page_shell(code: str, html_lang: str, title: str, desc: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<div class="wrap">
{body}
</div>
</body>
</html>
"""


def render_index(code: str, d: dict) -> str:
    idx = d["index"]
    nav = idx["nav"]
    faq = "\n".join(
        f"<p><strong>{q}</strong><br>{a}</p>" for q, a in idx["faq"]
    )
    feats = "\n".join(
        f"  <li><strong>{t}</strong>: {x}</li>" for t, x in idx["features"]
    )
    shots = "\n".join(
        f"""  <a href="images/{src}" target="_blank" rel="noopener">
    <img src="images/readme/{src}" alt="{cap}" loading="lazy">
  </a>"""
        for src, cap in idx["shots"]
    )
    body = f"""<header>
  <h1>{d["appName"]}</h1>
  <p class="lead">{idx["lead"]}</p>
</header>

{langbar(code, "index")}

<nav class="main">
  <a href="#support">{nav[0]}</a>
  <a href="#features">{nav[1]}</a>
  <a href="{html_name("privacy", code)}">{nav[2]}</a>
  <a href="{ISSUES}">{nav[3]}</a>
</nav>

<h2 id="support">{idx["supportH"]}</h2>

<div class="card">
{idx["supportCard"]}
</div>

<h3>{idx["faqH"]}</h3>

{faq}

<h2 id="features">{idx["featuresH"]}</h2>

<p>{idx["featuresIntro"]}</p>

<ul>
{feats}
</ul>

<div class="shots">
{shots}
</div>
<p class="caption">{idx["shotHint"]}</p>

<footer>
  <p>{d["appName"]} · <a href="{html_name("privacy", code)}">{nav[2]}</a> ·
     <a href="{ISSUES}">{nav[3]}</a></p>
  <p>{idx["trademark"]}</p>
</footer>"""
    return page_shell(code, d["htmlLang"], idx["title"], idx["desc"], body)


def render_privacy(code: str, d: dict) -> str:
    prv = d["privacy"]
    nav = d["index"]["nav"]
    sections = "\n\n".join(
        f'<h2>{s["h2"]}</h2>\n\n' + render_blocks(s["blocks"]) for s in prv["sections"]
    )
    summary = ""
    if "summary" in prv:
        sm = prv["summary"]
        summary = f"""
<details>
<summary>{sm["h"]}</summary>

{render_blocks(sm["blocks"])}

</details>"""
    body = f"""<h1>{prv["h1"]}</h1>
<p class="meta">
  {d["appName"]}<br>
  {prv["updated"]} · {prv["version"]} · {prv["platform"]}
</p>

{langbar(code, "privacy")}

<nav class="main"><a href="{html_name("index", code)}">{prv["back"]}</a></nav>

<div class="tldr">
  <p>{prv["tldr"]}</p>
</div>

{sections}{summary}

<footer>
  <p>{d["appName"]} · <a href="{html_name("index", code)}">{nav[0]}</a> ·
     <a href="{ISSUES}">{nav[3]}</a></p>
</footer>"""
    return page_shell(code, d["htmlLang"], prv["title"], prv["desc"], body)


def render_readme(code: str, d: dict) -> str:
    r = d["readme"]
    idx = d["index"]

    others = " · ".join(
        f"<a href=\"{readme_name(other)}\" hreflang=\"{other}\" lang=\"{other}\">{label}</a>"
        if other != code else f"<strong>{label}</strong>"
        for other, label in LANGS
    )

    about = "\n\n".join(r["about"])
    feature_groups = ""
    for g in r["featureGroups"]:
        body = "\n\n".join(g.get("p", []))
        if "ul" in g:
            ul = "\n".join(f"- {x}" for x in g["ul"])
            body = f"{body}\n\n{ul}" if body else ul
        feature_groups += f"\n### {g['h3']}\n\n{body}\n"

    shots = "\n".join(
        f"### {cap}\n\n![{cap}](images/readme/{src})\n" for src, cap in idx["shots"]
    )
    faq = "\n".join(f"**{q}**\n{a}\n" for q, a in idx["faq"])
    reqs = "\n".join(f"- {x}" for x in r["req"])

    return f"""<p align="center">
  <img src="images/icon-1024.png" width="128" alt="{d['appName']}">
</p>

<h1 align="center">{d["appName"]}</h1>

<p align="center"><strong>{r["tagline"]}</strong></p>

<p align="center">{r["subtitle"]}</p>

<p align="center">
  <a href="{SITE}"><img src="https://img.shields.io/badge/{quote(r["badgeSite"])}-blue" alt="Site"></a>
  <a href="{html_name("privacy", code)}"><img src="https://img.shields.io/badge/{quote(r["badgePrivacy"])}-green" alt="Privacy"></a>
  <img src="https://img.shields.io/badge/version-{VERSION}-lightgrey" alt="Version">
</p>

<p align="center">{others}</p>

---

## {r["aboutH"]}

{about}

---

## {r["shotsH"]}

{shots}
---

## {r["featuresH"]}
{feature_groups}
---

## {r["privacyH"]}

{r["privacyP"]}

[{r["seePrivacy"]}]({html_name("privacy", code)})

---

## {r["supportH"]}

{r["supportP"]}

### {r["faqH"]}

{faq}
---

## {r["reqH"]}

{reqs}

---

<p align="center"><sub>{r["trademark"]}</sub></p>
"""


def main() -> int:
    written = 0
    for code, label in LANGS:
        src = PAGES / f"{code}.json"
        if not src.exists():
            print(f"  缺文案：{src.relative_to(ROOT)}")
            return 1
        d = json.loads(src.read_text(encoding="utf-8"))
        d.setdefault("appName", label if code != "zh-Hans" else "文件8")

        outputs = {
            html_name("index", code): render_index(code, d),
            html_name("privacy", code): render_privacy(code, d),
            readme_name(code): render_readme(code, d),
        }
        for name, text in outputs.items():
            (ROOT / name).write_text(text, encoding="utf-8")
            written += 1
        print(f"  {code:<8} → {', '.join(outputs)}")

    print(f"共写出 {written} 个文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
