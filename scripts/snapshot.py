from pathlib import Path
import re
import shutil

source = Path('build')
output = Path('rendered')
shutil.copytree(source, output, dirs_exist_ok=True)
p = source / 'kb/incidents/4471-reassessment/index.html'
html = p.read_text()
def inline_css(match):
    return '<style>' + (p.parent / match.group(1)).read_text() + '</style>'
html = re.sub(r'<link href="([^"]+\.css)" rel="stylesheet">', inline_css, html)
html = re.sub(r'<script\b[^>]*>.*?</script>', '', html, flags=re.S)
html = html.replace('<select ', '<select disabled ').replace('<input ', '<input disabled ')
html = html.replace('<main>', '<main><p>Static snapshot. For the interactive controls, serve the rendered directory and open /kb/incidents/4471-reassessment/.</p>', 1)
(output / '4471-reassessment.html').write_text(html)
assert 'DR-' in html and '379' in html and '33' in html
print('Rendered snapshot includes cause counts and generated signature stamp.')
