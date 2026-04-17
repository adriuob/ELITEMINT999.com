import re

def minify_css(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([{};:])\s*', r'\1', css)
    return css.strip()

def minify_js(js):
    # Very basic JS minifier (removes comments and extra whitespace)
    js = re.sub(r'//.*?\n', '\n', js)
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    js = re.sub(r'\s+', ' ', js)
    # This is a bit risky for JS without a proper parser, but for this script it should be okay
    # as long as we don't break logic. Let's be conservative.
    return js.strip()

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(minify_css(css))

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(minify_js(js))

def minify_html(html):
    html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
    html = re.sub(r'>\s+<', '><', html)
    return html.strip()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(minify_html(html))
