"""Check generated pages and internal resources using only Python's standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path('_site').resolve()
SITE = 'wupengyuan.github.io'
errors = []

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.images = []
        self.main = 0
        self.h1 = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'): self.ids.add(attrs['id'])
        if tag == 'main': self.main += 1
        if tag == 'h1': self.h1 += 1
        if tag in ('a','link') and attrs.get('href'): self.links.append(attrs['href'])
        if tag in ('img','script') and attrs.get('src'): self.links.append(attrs['src'])
        if tag == 'img' and not attrs.get('alt'): errors.append('Image has no alternative text')

pages = {}
for path in ROOT.rglob('*.html'):
    parsed = Page()
    parsed.feed(path.read_text())
    pages[path.resolve()] = parsed

for relative in ('index.html', 'publications/index.html', 'cv/index.html', '404.html'):
    path = ROOT / relative
    if path not in pages:
        errors.append(f'Missing required page: {relative}')
    elif pages[path].main != 1 or pages[path].h1 != 1:
        errors.append(f'{relative}: expected one main landmark and one h1')

for path, parsed in pages.items():
    for link in parsed.links:
        url = urlsplit(link)
        if url.scheme not in ('','https','http') or url.netloc not in ('', SITE): continue
        target = (ROOT / unquote(url.path).lstrip('/')) if url.path.startswith('/') else path.parent / unquote(url.path)
        if not url.path: target = path
        if target.is_dir(): target /= 'index.html'
        target = target.resolve()
        if not target.is_file():
            errors.append(f'{path.relative_to(ROOT)}: missing {link}')
        elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
            errors.append(f'{path.relative_to(ROOT)}: missing anchor {link}')

for text in ('Your Name', 'Red Brick University', 'none@example.org', 'Submitted to AAAI', 'Submitted to ICLR'):
    for relative in ('index.html','publications/index.html','cv/index.html'):
        if text in (ROOT / relative).read_text(): errors.append(f'{relative}: unexpected placeholder or submission information: {text}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(pages)} generated HTML pages; internal links, anchors, images, and page landmarks are valid.')
