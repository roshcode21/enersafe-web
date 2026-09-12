from pathlib import Path
from html.parser import HTMLParser
from html import unescape
import re

ROOT = Path('.')
HTML_FILES = [
    'index.html','midesafe-sgm.html','gasafe-plus.html','autoconsumo.html',
    'servicios.html','nosotros.html','contacto.html','preguntas-frecuentes.html'
]


def read(path):
    return Path(path).read_text(encoding='utf-8')

def write(path, text):
    Path(path).write_text(text, encoding='utf-8')

def must_replace(path, old, new, count=None):
    s = read(path)
    n = s.count(old)
    if n == 0:
        raise RuntimeError(f'{path}: target not found: {old[:120]!r}')
    if count is not None and n != count:
        raise RuntimeError(f'{path}: expected {count} occurrences, found {n}: {old[:120]!r}')
    s = s.replace(old, new)
    write(path, s)
    print(f'{path}: replaced {n} occurrence(s)')

# ------------------------------------------------------------------
# 1) NOSOTROS — remove visible editorial defects and inherited copy
# ------------------------------------------------------------------
s = read('nosotros.html')
s = s.replace('Quienes somos', 'Quiénes somos')
s = s.replace(
    'data-en="We support you all year, not just at handover" data-es="Seguimiento durante la operación, no sólo en la entrega">Seguimiento durante la operación, no sólo en la entrega</h3>\n<p data-en="Building and registering a system is only the start. We sustain it throughout the year, with daily review of scheduled activities." data-es="Conformar y registrar un sistema es solo el arranque. Lo sostenemos a lo largo del ano, con revisión diaria de las actividades programadas.">Conformar y registrar un sistema es solo el arranque. Lo sostenemos a lo largo del ano, con revisión diaria de las actividades programadas.</p>',
    'data-en="Follow-up throughout operation" data-es="Seguimiento durante toda la operación">Seguimiento durante toda la operación</h3>\n<p data-en="Registration is one stage of the process. ENERSAFE follows up on scheduled activities and recorded evidence throughout operation." data-es="El registro es una etapa del proceso. ENERSAFE da seguimiento a las actividades programadas y a la evidencia registrada durante la operación.">El registro es una etapa del proceso. ENERSAFE da seguimiento a las actividades programadas y a la evidencia registrada durante la operación.</p>'
)
s = s.replace(
    'ENERSAFE desarrolla, conforma e implementa Sistemas de Administración en Seguridad Industrial, Seguridad Operativa y Protección al Medio Ambiente para Estaciones de Servicio del Sector de Hidrocarburos. Acompañamiento técnico especializado, todos los días.',
    'ENERSAFE desarrolla MIDESAFE SGM y GASAFE Plus y brinda seguimiento técnico y servicios regulatorios para Estaciones de Servicio en México.'
)
s = s.replace(
    'Especialistas en cumplimiento ante SAT, ASEA, STPS, PROFECO y SEMARNAT para el Sector de Hidrocarburos. Acompañamiento técnico especializado, todos los días.',
    'Tecnología aplicada, especialistas técnicos y servicios regulatorios para Estaciones de Servicio en México.'
)
write('nosotros.html', s)

# ------------------------------------------------------------------
# 2) HOME — make Autoconsumo a different proposition, not MIDESAFE clone
# ------------------------------------------------------------------
idx = read('index.html')
pattern = re.compile(r'<!-- SLIDE 3 — Autoconsumo -->.*?<!-- SLIDE 4 — Cumplimiento integral -->', re.S)
match = pattern.search(idx)
if not match:
    raise RuntimeError('index.html: Autoconsumo slide block not found')
new_slide = '''<!-- SLIDE 3 — Autoconsumo -->
<div class="slide autoconsumo-slide">
<!-- IMAGEN DE FONDO slide 3 -->
<div class="slide-bg slide-bg-3"></div>
<div class="slide-mesh"></div>
<div class="slide-inner"><div class="slide-content">
<div class="slide-logo"><img alt="ENERSAFE" src="assets/enersafe-logo.png"/><span class="sub">MIDESAFE AUTOCONSUMO</span></div>
<div class="slide-badge"><span class="pulse"></span> SAT · Aplicabilidad RMF 2026</div>
<h1 data-en='Is your self-consumption facility &lt;span class="hl"&gt;subject to volumetric controls?&lt;/span&gt;' data-es='¿Tu instalación de autoconsumo &lt;span class="hl"&gt;está sujeta a controles volumétricos?&lt;/span&gt;'>¿Tu instalación de autoconsumo <span class="hl">está sujeta a controles volumétricos?</span></h1>
<p class="lead" data-en="Not every self-consumption facility falls under the same fiscal assumption. ENERSAFE reviews applicability and, when required, MIDESAFE manages the facility’s SGM, records, calculations and evidence." data-es="No todas las instalaciones de autoconsumo se encuentran en el mismo supuesto fiscal. ENERSAFE revisa la aplicabilidad y, cuando corresponde, MIDESAFE gestiona el SGM, los registros, cálculos y evidencia de la instalación.">No todas las instalaciones de autoconsumo se encuentran en el mismo supuesto fiscal. ENERSAFE revisa la aplicabilidad y, cuando corresponde, MIDESAFE gestiona el SGM, los registros, cálculos y evidencia de la instalación.</p>
<div class="slide-diagnostic" aria-label="Aspectos que se revisan para determinar la aplicabilidad">
<span data-en="Permit" data-es="Permiso">Permiso</span>
<span data-en="Product" data-es="Producto">Producto</span>
<span data-en="Storage" data-es="Almacenamiento">Almacenamiento</span>
<span data-en="Volume / consumption" data-es="Volumen / consumo">Volumen / consumo</span>
</div>
<div class="slide-actions">
<a class="btn btn-primary" data-en="Review my case" data-es="Revisar mi caso" href="autoconsumo.html"><svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><path d="M14 16V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"></path><path d="M14 9h4l4 4v3a1 1 0 0 1-1 1h-1"></path><circle cx="7.5" cy="17.5" r="2.5"></circle><circle cx="17.5" cy="17.5" r="2.5"></circle></svg> Revisar mi caso</a>
<a class="btn btn-secondary" data-en="Talk to an advisor" data-es="Hablar con un asesor" href="https://wa.me/525610360614" rel="noopener" target="_blank"><svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg> Hablar con un asesor</a>
</div>
</div></div>
</div>
<!-- SLIDE 4 — Cumplimiento integral -->'''
idx = idx[:match.start()] + new_slide + idx[match.end():]
write('index.html', idx)

# ------------------------------------------------------------------
# 3) Small visual distinction for the diagnostic Autoconsumo slide
# ------------------------------------------------------------------
css = read('css/styles.css')
marker = '/* PUBLIC QA · AUTOCONSUMO SLIDE DIFFERENTIATION · 2026-09-11 */'
if marker not in css:
    css += '''\n\n/* PUBLIC QA · AUTOCONSUMO SLIDE DIFFERENTIATION · 2026-09-11 */\n.autoconsumo-slide .slide-content{max-width:760px}\n.autoconsumo-slide .slide-badge{border-color:rgba(243,217,39,.42);background:rgba(243,217,39,.10)}\n.autoconsumo-slide .slide-badge .pulse{background:var(--yellow)}\n.slide-diagnostic{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 2px}\n.slide-diagnostic span{display:inline-flex;align-items:center;padding:7px 12px;border-radius:999px;border:1px solid rgba(255,255,255,.18);background:rgba(7,12,8,.34);backdrop-filter:blur(8px);color:#eef4ea;font-size:.76rem;font-weight:600;letter-spacing:.01em}\n@media(max-width:720px){.slide-diagnostic{margin-top:16px}.slide-diagnostic span{font-size:.7rem;padding:6px 10px}}\n'''
write('css/styles.css', css)

# Keep sitemap fresh after public-facing changes
sm = read('sitemap.xml')
sm = re.sub(r'<lastmod>\d{4}-\d{2}-\d{2}</lastmod>', '<lastmod>2026-09-11</lastmod>', sm)
write('sitemap.xml', sm)

# ------------------------------------------------------------------
# 4) Editorial / structural QA gate
# ------------------------------------------------------------------
class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.parts = []
        self.ids = []
        self.hrefs = []
        self.srcs = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag in ('script','style'):
            self.skip += 1
        if 'data-es' in d and d['data-es']:
            self.parts.append(d['data-es'])
        if tag == 'meta' and d.get('content'):
            key = d.get('name') or d.get('property') or ''
            if key in ('description','twitter:title','twitter:description','og:title','og:description'):
                self.parts.append(d['content'])
        if d.get('id'):
            self.ids.append(d['id'])
        if d.get('href'):
            self.hrefs.append(d['href'])
        if d.get('src'):
            self.srcs.append(d['src'])
    def handle_endtag(self, tag):
        if tag in ('script','style') and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data)

common_unaccented = {
    'ano':'año','anos':'años','Mexico':'México','Republica':'República',
    'medicion':'medición','gestion':'gestión','operacion':'operación',
    'administracion':'administración','verificacion':'verificación',
    'capacitacion':'capacitación','implementacion':'implementación',
    'autorizacion':'autorización','informacion':'información','estacion':'estación',
    'estaciones':'estaciones', # valid as written; retained only to document exclusion below
    'regulacion':'regulación','evaluacion':'evaluación','aplicacion':'aplicación',
    'tecnico':'técnico','tecnica':'técnica','tecnicos':'técnicos','tecnicas':'técnicas',
    'pagina':'página','electronica':'electrónica','calculo':'cálculo','calculos':'cálculos',
    'documentacion':'documentación','revision':'revisión','emision':'emisión',
    'integracion':'integración','configuracion':'configuración','actualizacion':'actualización'
}
# 'estaciones' does not carry an accent. Do not scan it.
common_unaccented.pop('estaciones')

errors = []
all_visible = []
page_ids = {}
for name in HTML_FILES:
    raw = read(name)
    if any(x in raw for x in ('Ã','Â','�')):
        errors.append(f'{name}: possible mojibake / replacement character')
    p = Collector(); p.feed(raw)
    visible = ' '.join(p.parts)
    all_visible.append(visible)
    page_ids[name] = set(p.ids)
    if len(p.ids) != len(set(p.ids)):
        dup = sorted({x for x in p.ids if p.ids.count(x)>1})
        errors.append(f'{name}: duplicate ids {dup}')
    for bad, good in common_unaccented.items():
        if re.search(rf'(?<![A-Za-zÁÉÍÓÚÜÑáéíóúüñ]){re.escape(bad)}(?![A-Za-zÁÉÍÓÚÜÑáéíóúüñ])', visible):
            errors.append(f'{name}: suspicious unaccented Spanish word {bad!r} (expected {good!r})')
    if re.search(r'\bQuienes somos\b', visible):
        errors.append(f'{name}: "Quienes somos" should be "Quiénes somos"')

    # local href and anchor checks
    for href in p.hrefs:
        if not href or href.startswith(('http://','https://','mailto:','tel:','javascript:')):
            continue
        if href == '#':
            continue
        target, _, frag = href.partition('#')
        target = target.split('?',1)[0]
        target_file = target or name
        if target_file.endswith('.html') and not Path(target_file).exists():
            errors.append(f'{name}: missing local href target {href}')
        if frag and target_file.endswith('.html') and Path(target_file).exists():
            if target_file not in page_ids:
                q = Collector(); q.feed(read(target_file)); page_ids[target_file]=set(q.ids)
            if frag not in page_ids[target_file]:
                errors.append(f'{name}: href {href} points to missing id #{frag}')
    for src in p.srcs:
        if src.startswith(('http://','https://','data:')):
            continue
        f = src.split('?',1)[0]
        if f and not Path(f).exists():
            errors.append(f'{name}: missing local src {src}')

corpus = '\n'.join(all_visible)
for banned in [
    r'\bControlGAS\b', r'\bano\b', r'\banos\b',
    r'\bsostenemos\b', r'\bsostiene\b', r'\bsostener\b',
    r'distintos controles volumétricos'
]:
    if re.search(banned, corpus, re.I):
        errors.append(f'public copy still contains banned/suspicious pattern: {banned}')

# Slider integrity: four slides and four dots.
idx = read('index.html')
slide_count = len(re.findall(r'<div class="slide(?: [^"]*)?">', idx))
dot_count = len(re.findall(r'class="s-dot(?: active)?"', idx))
if slide_count != 4 or dot_count != 4:
    errors.append(f'index.html: slider integrity error: {slide_count} slides / {dot_count} dots')

if errors:
    print('\nPUBLIC QA FAILED')
    for e in errors:
        print(' -', e)
    raise SystemExit(1)

print('PUBLIC QA PASSED')
print('Checked:', ', '.join(HTML_FILES))
print('Slider:', slide_count, 'slides /', dot_count, 'dots')
