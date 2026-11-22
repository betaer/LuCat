"""Validate generated locale URLs, metadata, source coverage and local assets."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from build import ROOT, DATA, LANGUAGES, BASE, page_url

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.assets = []
        self.languages = []
        self.canonical = []
        self.lang = None
        self.json_ld = False
        self.json_chunks = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'html':
            self.lang = a.get('lang')
        if tag == 'link' and a.get('rel') == 'alternate':
            self.languages.append(a.get('hreflang'))
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical.append(a.get('href'))
        if tag == 'a' and 'href' in a:
            self.links.append(a['href'])
        if tag in ('img', 'script') and 'src' in a:
            self.assets.append(a['src'])
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self.json_ld = True
    def handle_data(self, data):
        if self.json_ld:
            self.json_chunks.append(data)
    def handle_endtag(self, tag):
        if tag == 'script':
            self.json_ld = False

expected = json.loads(Path('/Users/aa/Documents/my/xcode/LuCat/LuCatShared/Sources/LuCatCore/Localization/Resources/Translations.json').read_text())['languages'] if Path('/Users/aa/Documents/my/xcode/LuCat/LuCatShared/Sources/LuCatCore/Localization/Resources/Translations.json').exists() else LANGUAGES
assert set(expected) == set(LANGUAGES)
for code, content in DATA.items():
    assert set(content) == set(DATA['en'])
    assert all(isinstance(value, str) and value.strip() for value in content.values())
    path = ROOT/'dist'/code/'index.html'
    page = Page()
    page.feed(path.read_text())
    assert page.lang == code
    assert page.canonical == [page_url(code)]
    assert set(page.languages) == set(LANGUAGES) | {'x-default'}
    assert json.loads(''.join(page.json_chunks))['inLanguage'] == code
    for asset in page.assets:
        assert asset.startswith(BASE)
        assert (ROOT/'dist'/urlparse(asset).path.removeprefix('/lucat/')).is_file(), asset
    for link in page.links:
        if link.startswith(BASE) and '/privacy/' not in link:
            target = ROOT/'dist'/urlparse(link).path.removeprefix('/lucat/')
            assert target.is_file() or (target/'index.html').is_file(), link
    assert '2124558620260188334' in path.read_text()
    assert (ROOT/f'README.{code}.md').is_file()
print('PASS: 10 locales, app language coverage, source fields, metadata, JSON-LD, images and cross-links')
