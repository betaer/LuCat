"""Generate public introductions and static pages from content/*.json."""
import argparse
import html
import json
import shutil
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://betaer.github.io/lucat/'
REPO = 'https://github.com/betaer/LuCat'
APP = 'https://apps.apple.com/us/app/lucat-cat-petting-timer/id6835910184'
POST = 'https://x.com/Betaer/status/2124558620260188334'
CHAT = 'https://x.com/i/chat/group_join/g2122385444969349533/55EEg15kcr'
FEEDBACK = 'https://docs.qq.com/doc/DVmpqSXpBYmVsdnZK'
LANGUAGES = ['en', 'zh-Hans', 'zh-Hant-HK', 'ru', 'pt-BR', 'es-MX', 'fr', 'de', 'it', 'ja']
DATA = {code: json.loads((ROOT / 'content' / f'{code}.json').read_text()) for code in LANGUAGES}
e = html.escape

def page_url(code):
    return BASE + code + '/'

def section(title, body):
    return f'<section class="story-block"><h2>{e(title)}</h2><p>{e(body)}</p></section>'

def build_page(code):
    t = DATA[code]
    assets = BASE + 'assets/'
    alternates = ''.join(f'<link rel="alternate" hreflang="{c}" href="{page_url(c)}">' for c in LANGUAGES)
    alternates += f'<link rel="alternate" hreflang="x-default" href="{BASE}">'
    options = ''.join(f'<option value="{page_url(c)}" {"selected" if c == code else ""}>{e(DATA[c]["name"])}</option>' for c in LANGUAGES)
    language_links = ' · '.join(f'<a href="{page_url(c)}" hreflang="{c}" lang="{c}">{e(DATA[c]["name"])}</a>' for c in LANGUAGES)
    title = 'LuCat · ' + t['tagline']
    description = t['intro']
    def image(name, alt, extra=''):
        return f'<img src="{assets}images/{name}" alt="{e(alt)}" {extra}>'
    def feature(title_key, body_key, name, width, height):
        return f'<article class="feature"><a class="feature-shot" href="{assets}images/{name}">{image(name,t[title_key],f"width={width} height={height} loading=lazy")}</a><h3>{e(t[title_key])}</h3><p>{e(t[body_key])}</p></article>'
    return f'''<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#fffaef">
<title>{e(title)}</title><meta name="description" content="{e(description)}">
<link rel="canonical" href="{page_url(code)}">{alternates}
<link rel="icon" href="{assets}images/lucat-icon.webp">
<link rel="stylesheet" href="{assets}css/landing.css?v=multilingual1">
<script defer src="{assets}js/support-email.js"></script>
<meta property="og:type" content="website"><meta property="og:site_name" content="LuCat">
<meta property="og:locale" content="{code.replace('-', '_')}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{page_url(code)}"><meta property="og:image" content="{assets}images/lucat-social.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"SoftwareApplication","name":"LuCat","url":page_url(code),"inLanguage":code,"operatingSystem":"iOS, iPadOS, watchOS","applicationCategory":"LifestyleApplication","downloadUrl":APP,"description":description,"offers":{"@type":"Offer","price":"0","priceCurrency":"USD"}},ensure_ascii=False)}</script>
</head><body>
<header class="site-header wrap">
<a class="brand" href="{page_url(code)}">{image('lucat-icon.webp','', 'width=44 height=44')}<span>LuCat</span></a>
<nav aria-label="LuCat"><a href="#features">{e(t['featuresLabel'])}</a><a href="#story">{e(t['storyLabel'])}</a><a href="#support">{e(t['communityLabel'])}</a>
<label class="language-control"><span>{e(t['languageLabel'])}</span><select id="language" aria-label="{e(t['languageLabel'])}">{options}</select></label></nav>
</header>
<main id="main" class="wrap">
<section class="hero">
<div class="hero-copy"><p class="devices">{e(t['devices'])}</p><h1>{e(t['headline'])}</h1><p class="hero-intro">{e(t['intro'])}</p>
<a class="download-link" href="{APP}">{e(t['download'])}</a></div>
<figure class="hero-visual">
<div class="phone-frame">{image('session-timeline.webp',t['motionTitle'],'width=690 height=1500 fetchpriority=high')}</div>
<div class="watch-frame">{image('watch-start.webp',t['howTitle'],'width=416 height=496')}</div>
</figure></section>
<section id="features" class="features"><div class="section-heading"><h2>{e(t['featuresLabel'])}</h2><p>{e(t['how'])}</p></div>
<div class="feature-grid">
{feature('remindersTitle','reminders','daily-progress.webp',780,1696)}
{feature('catsTitle','cats','time-by-cat.webp',780,1696)}
<div class="feature-stack">{feature('weightTitle','weight','duo-weight-trends.webp',1160,816)}
<article class="feature"><div class="watch-gallery">{''.join(f'<a href="{assets}images/{name}">{image(name,t["howTitle"],"width=416 height=496 loading=lazy")}</a>' for name in ['watch-start.webp','watch-switch-cat.webp','watch-time-with-luna.webp'])}</div><h3>{e(t['motionTitle'])}</h3><p>{e(t['motion'])}</p></article></div></div></section>
<article id="story" class="article-copy">
{section(t['headline'],t['origin'])}{section(t['storyTitle'],t['story'])}{section(t['roadmapTitle'],t['roadmap'])}
<p>{e(t['thanks'])}</p><p><a href="{POST}">{e(t['postLabel'])}</a> · <a href="{REPO}/blob/main/README.{code}.md">{e(t['repoLabel'])}</a></p></article>
<section class="support" id="support"><div><h2>{e(t['communityLabel'])}</h2><p>{e(t['thanks'])}</p></div>
<ul class="contact-links">
<li><a data-support-email><strong>{e(t['emailLabel'])}</strong><span data-email-label="{e(t['emailLabel'])}">{image('support-address.png',t['emailLabel'],'width=140 height=24')}</span></a></li>
<li><a href="{CHAT}">{e(t['chatLabel'])}</a></li><li><a href="{FEEDBACK}">{e(t['otherLabel'])} · {e(t['feedbackLabel'])}</a></li></ul></section>
</main><footer class="site-footer wrap"><span>LuCat</span><nav><a href="{APP}">{e(t['download'])}</a><a href="{BASE}privacy/?lang={code}">{e(t['privacyLabel'])}</a><a href="{REPO}">GitHub</a><a href="{POST}">𝕏 @Betaer</a></nav></footer>
<nav class="language-links wrap" aria-label="{e(t['languageLabel'])}">{language_links}</nav>
<script>document.getElementById('language').addEventListener('change',function(){{window.location.assign(this.value);}});</script>
</body></html>'''

def readme(code):
    t = DATA[code]
    language_links = ' | '.join(f'[{DATA[c]["name"]}](README.{c}.md)' for c in LANGUAGES)
    lines = [f'# 🐾 LuCat · {t["tagline"]}', language_links,
             f'**[{t["download"]}]({APP})** · [{t["repoLabel"]}]({page_url(code)}) · [{t["postLabel"]}]({POST})',
             '![LuCat](site/assets/images/lucat-social.jpg)',
             f'## {t["headline"]}', t['origin'], t['intro']]
    for title, body in [('howTitle','how'),('catsTitle','cats'),('weightTitle','weight'),('remindersTitle','reminders'),('motionTitle','motion'),('storyTitle','story'),('roadmapTitle','roadmap')]:
        lines += [f'## {t[title]}', t[body]]
    lines += [f'## {t["communityLabel"]}', t['thanks'], f'[{t["chatLabel"]}]({CHAT}) · [{t["otherLabel"]}]({FEEDBACK})',
              f'[{t["privacyLabel"]}]({BASE}privacy/?lang={code})']
    if code == 'en':
        lines += ['## Maintaining this introduction',
                  'Edit the matching file in `content/`. Run `python3 scripts/build.py` to regenerate the README files and the website in `dist/`. English artwork lives in `site/assets/`. These public files contain the product introduction, website, and publishing tools.',
                  'GitHub Actions regenerates README files after content changes. The betaer.github.io workflow fetches this repository every 15 minutes and publishes the generated pages at /lucat/. Each language has its own static URL, canonical link, hreflang links, and sitemap entry. You can also run that workflow manually to publish immediately.']
    return '\n\n'.join(lines) + '\n'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT/'dist')
    parser.add_argument('--site-only', action='store_true')
    args = parser.parse_args()
    output = args.output.resolve()
    if output == ROOT or output in ROOT.parents:
        raise SystemExit('Output must be a dedicated website directory')
    output.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT/'site', output, dirs_exist_ok=True)
    for code in LANGUAGES:
        (output/code).mkdir(exist_ok=True)
        (output/code/'index.html').write_text(build_page(code))
        if not args.site_only:
            (ROOT/f'README.{code}.md').write_text(readme(code))
    # English remains available at the existing URL, with the locale page as canonical.
    (output/'index.html').write_text(build_page('en'))
    # Preserve the current privacy URL and make its return link follow the selected locale.
    privacy = output/'privacy'/'index.html'
    privacy.write_text(privacy.read_text().replace("'../?lang='+encodeURIComponent(lang)", "'../'+encodeURIComponent(lang)+'/'"))
    ns = 'http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('', ns)
    sitemap = ET.Element(f'{{{ns}}}urlset')
    for url in [BASE, *map(page_url, LANGUAGES)]:
        node = ET.SubElement(sitemap, f'{{{ns}}}url')
        ET.SubElement(node, f'{{{ns}}}loc').text = url
    ET.ElementTree(sitemap).write(output/'sitemap.xml', encoding='utf-8', xml_declaration=True)
    if not args.site_only:
        (ROOT/'README.md').write_text(readme('en'))
    print(f'Built {len(LANGUAGES)} locales in {output}')

if __name__ == '__main__':
    main()
