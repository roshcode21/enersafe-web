from pathlib import Path
import re

ROOT = Path('.')
HTML = ['index.html','midesafe-sgm.html','gasafe-plus.html','autoconsumo.html','servicios.html','nosotros.html','contacto.html','preguntas-frecuentes.html']
changed=[]

def get(path):
    return (ROOT/path).read_text(encoding='utf-8')

def put(path,s):
    (ROOT/path).write_text(s,encoding='utf-8')
    if path not in changed: changed.append(path)

def rep(path,old,new,required=False,count=-1):
    s=get(path); n=s.count(old)
    if required and not n: raise RuntimeError(f'{path}: target not found {old[:100]!r}')
    if n:
        s=s.replace(old,new,count)
        put(path,s)
    return n

def reg(path,pat,repl,required=False,count=1,flags=re.S):
    s=get(path); out,n=re.subn(pat,repl,s,count=count,flags=flags)
    if required and not n: raise RuntimeError(f'{path}: regex target not found {pat[:100]}')
    if n: put(path,out)
    return n

# HOME — align Spanish/English and stop mapping station environmental work to SEMARNAT by default.
rep('index.html',
    'SAT, ASEA, CNE, STPS, PROFECO, SEMARNAT y autoridades locales pueden requerir actividades, registros, permisos, información y evidencia con calendarios y responsables propios.',
    'SAT, ASEA, CNE, STPS, PROFECO y autoridades ambientales o locales pueden requerir actividades, registros, permisos, información y evidencia con calendarios y responsables propios.', True)
rep('index.html',
    'SAT, ASEA, CNE, STPS, PROFECO, SEMARNAT and local authorities may require activities, records, permits, information and evidence with their own schedules and responsible parties.',
    'SAT, ASEA, CNE, STPS, PROFECO and environmental or local authorities may require activities, records, permits, information and evidence with their own schedules and responsible parties.', True)
rep('index.html','<span class="on-code" style="font-size:.58rem">SEMARNAT</span>','<span class="on-code">CNE</span>',True)
rep('index.html',
    'MIDESAFE SGM y GASAFE Plus organizan actividades, responsables, evidencias y reportes. Los servicios especializados de ENERSAFE atienden las demás obligaciones regulatorias.',
    'MIDESAFE SGM y GASAFE Plus organizan actividades, responsables, evidencias y reportes dentro de sus respectivos alcances. Los servicios especializados de ENERSAFE atienden trámites, estudios, dictámenes y otras obligaciones regulatorias.', True)

# MIDESAFE — clean hidden English left from earlier iterations and make consultations naming consistent.
rep('midesafe-sgm.html',
    'Available for one service station or at a corporate level, from two stations up, with no need to hire specialized staff.',
    'Available for one Service Station and with a corporate view from two stations onward, with ENERSAFE technical assistance and follow-up.', True)
rep('midesafe-sgm.html',
    'Without you having to monitor the regulation yourself',
    'Adjustments to the tool and technical criteria when applicable requirements change', True)
rep('midesafe-sgm.html',
    "We'll show you live how it connects with your volumetric control and builds the file for your Annual Compliance Certificate.",
    "We'll show you how MIDESAFE manages SGM activities, works with measurement information and organizes evidence for review.", True)
rep('midesafe-sgm.html','>Preguntas frecuentes</span>','>Consultas</span>',required=False)
rep('midesafe-sgm.html','>Preguntas frecuentes</span>','>Consultas</span>',required=False)
# Safer language: ENERSAFE can review supporting documentation, not certify that it is 'correct'.
rep('midesafe-sgm.html','Verificación de que el soporte cargado sea correcto','Revisión del soporte documental registrado',required=False)
rep('midesafe-sgm.html','Verification that uploaded support is correct','Review of recorded supporting documentation',required=False)

# GASAFE — synchronize hidden EN, remove a conceptual contradiction, and attribute reporting correctly.
rep('gasafe-plus.html',
    'Many stations treat the SASISOPA as a binder you file and forget. But ASEA requires a living system, with continuous evidence, up-to-date logs and actions that are carried out and documented. When an audit arrives, what\'s reviewed is the operation, not the paper.',
    'Authorization does not end the obligation. The 18 elements must remain in operation throughout the life of the project, with activities, records and evidence aligned with the authorized Administration System and the station\'s actual operation.', True)
rep('gasafe-plus.html',
    'El valor de GASAFE Plus comienza después de la autorización: mantener los 18 elementos en operación, documentados y con seguimiento durante la vida del proyecto.',
    'Después del registro y la autorización, GASAFE Plus organiza la implementación continua del Sistema y el especialista ENERSAFE da seguimiento a la información registrada.', True)
rep('gasafe-plus.html',
    'The value of GASAFE Plus begins after authorization: keeping the 18 elements operating, documented and under follow-up throughout the life of the project.',
    'After registration and authorization, GASAFE Plus organizes continuous implementation of the System and the ENERSAFE specialist follows up on the recorded information.', True)
rep('gasafe-plus.html','Genera informes de desempeño y reportes mensuales','Integra información para informes de desempeño y reportes mensuales',True)
rep('gasafe-plus.html','Generates performance and monthly reports','Brings together information for performance reports and monthly reports',True)
rep('gasafe-plus.html',
    '12-month contract. Control and monitoring of all your service stations from a single administrator user, with continuous updates of the platform and applicable legal requirements.',
    'Continuous follow-up service. For fuel-station groups, GASAFE Plus provides a corporate view of multiple Service Stations, with updates to the tool and applicable legal requirements.', True)
rep('gasafe-plus.html','>Preguntas frecuentes</span>','>Consultas</span>',required=False)

# AUTOCONSUMO — replace the inherited generic compliance block with applicability-specific content.
s=get('autoconsumo.html')
start='<!-- ============================ CUMPLIMIENTO CONFORME A LA NORMA ============================ -->'
end='<!-- ============================ QUÉ INCLUYE ============================ -->'
if start not in s or end not in s: raise RuntimeError('autoconsumo compliance markers missing')
a,b=s.split(start,1); old,c=b.split(end,1)
new='''<!-- ============================ CUMPLIMIENTO CONFORME A LA NORMA ============================ -->
<section class="section deps">
<div class="wrap">
<div class="section-head center reveal">
<span class="eyebrow" data-en="Applicable references" data-es="Referencias aplicables">Referencias aplicables</span>
<h2 data-en="The scope depends on the self-consumption case that applies." data-es="El alcance depende del supuesto de autoconsumo que corresponda.">El alcance depende del supuesto de autoconsumo que corresponda.</h2>
<p class="lead" data-en="Rule 2.6.1.2, section VI of the 2026 RMF defines the cases in which own-use or self-consumption activities are subject to volumetric controls. Once applicability is confirmed, the SGM and the requirements for equipment/software, verification, certificates and product reports must be addressed according to their respective scope." data-es="La regla 2.6.1.2, fracción VI de la RMF 2026 define los supuestos en los que las actividades de usos propios o autoconsumo quedan sujetas a controles volumétricos. Confirmada la aplicabilidad, el SGM y los requisitos de equipos y programas, verificación, certificados y dictámenes deben atenderse conforme al alcance que corresponde a cada uno." style="margin:0 auto">La regla 2.6.1.2, fracción VI de la RMF 2026 define los supuestos en los que las actividades de usos propios o autoconsumo quedan sujetas a controles volumétricos. Confirmada la aplicabilidad, el SGM y los requisitos de equipos y programas, verificación, certificados y dictámenes deben atenderse conforme al alcance que corresponde a cada uno.</p>
</div>
<div class="seals reveal" data-delay="1">
<div class="seal"><span class="seal-ic">01</span><span class="seal-t" data-en="2026 RMF · Rule 2.6.1.2 VI" data-es="RMF 2026 · Regla 2.6.1.2 VI">RMF 2026 · Regla 2.6.1.2 VI</span><span class="seal-d" data-en="Defines the applicable own-use/self-consumption cases" data-es="Define los supuestos aplicables de usos propios y autoconsumo">Define los supuestos aplicables de usos propios y autoconsumo</span></div>
<div class="seal"><span class="seal-ic">02</span><span class="seal-t">NMX-CC-10012-IMNC-2004</span><span class="seal-d" data-en="Requirements for measurement processes and measuring equipment" data-es="Requisitos para procesos de medición y equipos de medición">Requisitos para procesos de medición y equipos de medición</span></div>
<div class="seal"><span class="seal-ic">03</span><span class="seal-t" data-en="2026 RMF · Annexes 21, 22 and 23" data-es="RMF 2026 · Anexos 21, 22 y 23">RMF 2026 · Anexos 21, 22 y 23</span><span class="seal-d" data-en="Volumetric controls, verification, certificates and product reports" data-es="Controles volumétricos, verificación, certificados y dictámenes">Controles volumétricos, verificación, certificados y dictámenes</span></div>
</div>
<div class="incl-note reveal"><span data-en="MIDESAFE Self-consumption applies SGM digital management to the facility after its regulatory case and scope have been identified. It does not replace independent verification or the certificates and reports issued by the applicable bodies." data-es="MIDESAFE Autoconsumo aplica la gestión digital del SGM a la instalación una vez identificado su supuesto regulatorio y alcance. No sustituye la verificación independiente ni los certificados y dictámenes emitidos por las figuras correspondientes.">MIDESAFE Autoconsumo aplica la gestión digital del SGM a la instalación una vez identificado su supuesto regulatorio y alcance. No sustituye la verificación independiente ni los certificados y dictámenes emitidos por las figuras correspondientes.</span></div>
</div>
</section>
'''
put('autoconsumo.html',a+new+end+c)
rep('autoconsumo.html','>Preguntas frecuentes</span>','>Consultas</span>',required=False)
# Remove old generic/absolute hidden phrases wherever they survived outside the replaced section.
rep('autoconsumo.html','The same MIDESAFE SGM management, applied to self-consumption facilities: activities, measurement, calculations, evidence and specialized technical follow-up.','MIDESAFE applies SGM digital management to self-consumption facilities that fall under the applicable volumetric-control cases.',required=False)

# SERVICES — correct environmental architecture and CNE/SENER attribution.
s=get('servicios.html')
# Move Informe Preventivo card from safety/operation into environment if it is currently in the first ASEA block.
m=re.search(r'(<a class="acc-svc-card plain" href="[^"]*Informe%20Preventivo[^"]*"[^>]*>.*?</a>)',s,re.S)
if not m: raise RuntimeError('Informe Preventivo card not found')
ip=m.group(1)
s=s[:m.start()]+s[m.end():]
marker='<!-- ASEA AMBIENTE Y RESIDUOS -->'
pos=s.find(marker)
if pos<0: raise RuntimeError('environment group marker missing')
grid=s.find('<div class="acc-svc-grid">',pos)
if grid<0: raise RuntimeError('environment grid missing')
grid_end=grid+len('<div class="acc-svc-grid">')
s=s[:grid_end]+'\n'+ip+s[grid_end:]
put('servicios.html',s)
rep('servicios.html','ASEA · Ambiente y residuos','Ambiente y residuos',True)
rep('servicios.html','Environmental matters for the hydrocarbons sector','ASEA and applicable environmental services',True)
rep('servicios.html','Materia ambiental del Sector Hidrocarburos','ASEA y servicios ambientales aplicables',True)
rep('servicios.html','Environmental impact, air-emissions filings, annual operating certificate and waste records for hydrocarbons-sector activities.','Environmental impact, air-emissions filings, annual operating certificate and waste registrations with ASEA, plus complementary environmental services.',True)
rep('servicios.html','Impacto ambiental, trámites de atmósfera, Cédula de Operación Anual y registros de residuos para actividades del Sector Hidrocarburos.','Impacto ambiental, trámites de atmósfera, Cédula de Operación Anual y registros de residuos ante la ASEA, además de servicios ambientales complementarios.',True)
# Official ASEA naming for MIA variants / notice.
rep('servicios.html','Manifestación de Impacto Ambiental (sin riesgo)','MIA Particular — sin actividad altamente riesgosa',True)
rep('servicios.html','Environmental Impact Statement (no risk)','Particular Environmental Impact Assessment — without highly hazardous activity',True)
rep('servicios.html','Manifestación de Impacto Ambiental (altamente riesgosas)','MIA Particular — con actividad altamente riesgosa',True)
rep('servicios.html','Environmental Impact Statement (highly hazardous)','Particular Environmental Impact Assessment — with highly hazardous activity',True)
rep('servicios.html','Manifestación de Impacto Ambiental Regional','MIA Regional — con actividad altamente riesgosa',True)
rep('servicios.html','Regional Environmental Impact Statement','Regional Environmental Impact Assessment — with highly hazardous activity',True)
rep('servicios.html','Aviso de no requerimiento de Impacto Ambiental','Aviso de no requerimiento de autorización en materia de impacto ambiental',True)
rep('servicios.html','Notice of non-requirement of Environmental Impact','Notice that environmental-impact authorization is not required',True)
# Update WhatsApp service labels to match the new public names.
rep('servicios.html','Manifestaci%C3%B3n%20de%20Impacto%20Ambiental%20%28sin%20riesgo%29','MIA%20Particular%20sin%20actividad%20altamente%20riesgosa',required=False)
rep('servicios.html','Manifestaci%C3%B3n%20de%20Impacto%20Ambiental%20%28altamente%20riesgosas%29','MIA%20Particular%20con%20actividad%20altamente%20riesgosa',required=False)
rep('servicios.html','Manifestaci%C3%B3n%20de%20Impacto%20Ambiental%20Regional','MIA%20Regional%20con%20actividad%20altamente%20riesgosa',required=False)
rep('servicios.html','Aviso%20de%20no%20requerimiento%20de%20Impacto%20Ambiental','Aviso%20de%20no%20requerimiento%20de%20autorizaci%C3%B3n%20en%20materia%20de%20impacto%20ambiental',required=False)
# CNE / SENER / local services: keep one useful combined accordion but tell the truth about authority.
rep('servicios.html','CNE y licencias','CNE, SENER y licencias',True)
rep('servicios.html','CNE and licenses','CNE, SENER and licenses',True)
rep('servicios.html','National Energy Commission and municipal authorities','National Energy Commission, Ministry of Energy and local authorities',True)
rep('servicios.html','Comisión Nacional de Energía y autoridades municipales','Comisión Nacional de Energía, Secretaría de Energía y autoridades locales',True)
rep('servicios.html','Permit title modifications, social impact, NOM-016 assessment, Electronic Filing Office (OPE) administration and operating licenses.','CNE permit matters and OPE administration; Social Impact Assessment before SENER; NOM-016 assessments and local operating licenses according to the applicable authority.',True)
rep('servicios.html','Modificaciones de título de permiso, impacto social, dictamen de la NOM-016, administración de la Oficialía de Partes Electrónica (OPE) y licencias de funcionamiento.','Trámites de permisos y administración de la OPE ante la CNE; Evaluación de Impacto Social ante SENER; dictámenes NOM-016 y licencias de funcionamiento conforme a la autoridad aplicable.',True)
rep('servicios.html','Impacto social (CNE)','Evaluación de Impacto Social (SENER)',True)
rep('servicios.html','Social impact (CNE)','Social Impact Assessment (SENER)',True)
rep('servicios.html','Impacto%20social%20%28CNE%29','Evaluaci%C3%B3n%20de%20Impacto%20Social%20%28SENER%29',required=False)
# Remove unsupported numeric marketing stats and convert the area to value/coverage statements.
reg('servicios.html',r'<div class="plant-stats">.*?</div>\s*</div>\s*</div>\s*</div>\s*</section>', '''<div class="plant-stats">
<div class="pstat"><span class="pstat-n" data-en="Specialized" data-es="Especializado">Especializado</span><span class="pstat-l" data-en="services focused on Service Stations" data-es="servicios enfocados en Estaciones de Servicio">servicios enfocados en Estaciones de Servicio</span></div>
<div class="pstat"><span class="pstat-n" data-en="Coordinated" data-es="Coordinado">Coordinado</span><span class="pstat-l" data-en="filings, studies and assessments within the contracted scope" data-es="trámites, estudios y dictámenes dentro del alcance contratado">trámites, estudios y dictámenes dentro del alcance contratado</span></div>
<div class="pstat"><span class="pstat-n">ENERSAFE</span><span class="pstat-l" data-en="one team to follow the contracted regulatory fronts" data-es="un equipo para dar seguimiento a los frentes contratados">un equipo para dar seguimiento a los frentes contratados</span></div>
</div>
</div>
</div>
</div>
</section>''',required=True)
# Hidden English inherited from old positioning.
rep('servicios.html','A service station doesn\'t comply before one authority, but several at once. Each asks for different things, at different times. Coordinating them separately takes time and opens the door to omissions. The alternative is having one party responsible for all of it.','SAT, ASEA, CNE, SENER, STPS, Civil Protection and environmental authorities have different scopes, filings and evidence requirements. ENERSAFE addresses the applicable services according to each obligation and authority.',True)
rep('servicios.html','Volumetric controls and a Measurement Management System that supports your Annual Compliance Certificate (Annexes 21, 22 & 23).','Measurement Management System, volumetric controls and applicable tax provisions, including Annexes 21, 22 and 23.',True)
rep('servicios.html','Tool + management','System + follow-up',required=False)
rep('servicios.html','Herramienta + gestión','Sistema + seguimiento',required=False)

# ABOUT — synchronize English with the safer Spanish version and clean accents.
rep('nosotros.html','At ENERSAFE we bring together in one place every obligation that federal authorities require from a service station. A specialized company that supports complete regulatory compliance, not an isolated procedure.','ENERSAFE develops MIDESAFE and GASAFE Plus and combines them with specialists who review activities, evidence, observations and expirations. Complementary services address other regulatory areas of the Service Station.',True)
rep('nosotros.html','ENERSAFE combines regulatory expertise, MIDESAFE, GASAFE Plus and technical follow-up to operate, document and sustain each station’s obligations.','ENERSAFE combines regulatory knowledge, MIDESAFE, GASAFE Plus and technical follow-up to operate, document and maintain continuity of each station’s obligations.',True)
rep('nosotros.html','So that no fuel retailer has to face regulation alone. Whatever the obligation or the authority, we stand on the station\'s side so it stays compliant and its owner can focus on operating.','We turn dispersed regulatory obligations into processes with responsible parties, dates, evidence and follow-up. The goal is to provide continuity and make the status of each regulatory area visible.',True)
rep('nosotros.html','data-es="Quienes somos">Quienes somos','data-es="Quiénes somos">Quiénes somos',True)
rep('nosotros.html','data-es="Como trabajamos">Como trabajamos','data-es="Cómo trabajamos">Cómo trabajamos',required=False)
rep('nosotros.html','Asistencia técnica en linea','Asistencia técnica en línea',required=False)

# CONTACT — clearer environmental category, privacy link, remove unverified support hours.
rep('contacto.html','Trámites ambientales (SEMARNAT, CONAGUA)','Trámites ambientales y residuos',True)
old='<p class="ctc-privacy" data-en="We will use your data only to respond to your request. See our Privacy Notice." data-es="Usaremos tus datos únicamente para atender tu solicitud. Consulta nuestro Aviso de Privacidad.">Usaremos tus datos únicamente para atender tu solicitud. Consulta nuestro Aviso de Privacidad.</p>'
new='<p class="ctc-privacy"><span data-en="We will use your data only to respond to your request." data-es="Usaremos tus datos únicamente para atender tu solicitud.">Usaremos tus datos únicamente para atender tu solicitud.</span> <a data-en="Privacy Notice" data-es="Aviso de Privacidad" href="https://enersafe.com.mx/aviso.html">Aviso de Privacidad</a>.</p>'
rep('contacto.html',old,new,True)
rep('contacto.html','Lunes a viernes · 8:00 am a 5:00 pm · Toda la República','Atención en línea · Cobertura en toda la República Mexicana',True)

# CONSULTATIONS — synchronize the English hidden layer with the corrected ASEA scope and simplify naming.
rep('preguntas-frecuentes.html','The annual operations report applies to regulated hydrocarbon-sector entities that fall within the cases established by the competent environmental authority, including certain federal-jurisdiction stationary sources and large hazardous-waste generators. Its scope depends on the facility’s environmental authorizations and activities.','The Hydrocarbons Sector Annual Operating Certificate is filed with ASEA when the Regulated Entity falls under the applicable cases, including certain federal-jurisdiction stationary sources and large hazardous-waste generators. Its scope depends on the facility’s environmental authorizations and activities.',True)
rep('preguntas-frecuentes.html','They are different categories and each has its own registrations and obligations. The required filing depends on the type of waste, quantity generated and generator category. ENERSAFE manages the applicable registrations and related filings within the contracted scope.','They are different categories and each has its own registrations and obligations before ASEA for Hydrocarbons Sector activities. The filing depends on the type of waste, quantity generated and generator category. ENERSAFE manages the applicable registrations and related filings within the contracted scope.',True)
rep('preguntas-frecuentes.html','Consultas frecuentes','Consultas',required=False)
rep('preguntas-frecuentes.html','Frequent consultations','Consultations',required=False)

# Remove dead social links until real company URLs are confirmed; a broken # is worse than no icon.
for path in HTML:
    reg(path,r'\n?<div class="f-social">.*?</div>','',required=False,count=1)

# Global language clean-up for legacy claims that should not survive even hidden.
for path in HTML:
    rep(path,'Sistemas propios','Soluciones digitales',required=False)
    rep(path,'sistemas propios','soluciones digitales',required=False)
    rep(path,'Proprietary systems','Digital solutions',required=False)
    rep(path,'proprietary systems','digital solutions',required=False)
    rep(path,'Proprietary digital systems','Digital solutions',required=False)
    rep(path,'proprietary digital systems','digital solutions',required=False)

# Rewrite llms.txt so machine-readable positioning matches the actual audited site.
llms='''# ENERSAFE

> Empresa mexicana especializada en cumplimiento regulatorio digital con seguimiento técnico para Estaciones de Servicio de gasolina y diésel.

ENERSAFE desarrolla MIDESAFE SGM y GASAFE Plus y complementa estas soluciones con servicios regulatorios especializados. La tecnología forma parte de un servicio continuo: especialistas ENERSAFE revisan información registrada, dan seguimiento a observaciones y vencimientos, brindan asistencia técnica y generan reportes dentro del alcance contratado.

## Soluciones principales

- [MIDESAFE SGM](https://enersafe.com.mx/midesafe-sgm.html): gestión digital del Sistema de Gestión de la Medición. Organiza actividades, registros, cálculos, evidencia y seguimiento técnico durante la operación del SGM.
- [GASAFE Plus](https://enersafe.com.mx/gasafe-plus.html): sistema digital para la conformación e implementación continua del SASISOPA y para organizar actividades y evidencias operativas relacionadas con la NOM-005-ASEA-2016.
- [MIDESAFE Autoconsumo](https://enersafe.com.mx/autoconsumo.html): gestión digital del SGM para instalaciones de autoconsumo que se encuentren en los supuestos aplicables de controles volumétricos.
- [Servicios especializados](https://enersafe.com.mx/servicios.html): trámites, estudios, dictámenes y servicios complementarios según la obligación y la autoridad aplicable.

## Criterios de alcance

- El Sistema de Gestión de la Medición y los controles volumétricos son obligaciones relacionadas, pero no equivalentes.
- MIDESAFE organiza y documenta el SGM; no sustituye el software de control volumétrico ni las verificaciones o certificados emitidos por las figuras correspondientes.
- El SASISOPA y la NOM-005-ASEA-2016 tienen alcances distintos. GASAFE Plus organiza la implementación continua del SASISOPA y actividades/evidencias operativas relacionadas con NOM-005 sin sustituir su evaluación de conformidad.
- ENERSAFE no sustituye las responsabilidades del Regulado ni las evaluaciones, verificaciones o dictámenes que correspondan a Terceros Autorizados, Unidades de Inspección u otras figuras acreditadas, aprobadas o autorizadas.

## Seguimiento técnico

Dentro del alcance contratado, el especialista ENERSAFE revisa actividades y evidencias registradas, identifica observaciones y próximos vencimientos, da seguimiento con el responsable de la estación, brinda asistencia técnica y capacitación y genera reportes periódicos.

## Marco regulatorio de referencia

- SGM y medición: NMX-CC-10012-IMNC-2004 y disposiciones de medición que resulten aplicables, incluida la RES/811/2015 según el alcance.
- Controles volumétricos: Código Fiscal de la Federación, Resolución Miscelánea Fiscal 2026 y Anexos 21, 22 y 23, entre otras disposiciones aplicables.
- SASISOPA: disposiciones de ASEA y sus 18 elementos interrelacionados durante la vida del proyecto.
- NOM-005-ASEA-2016: requisitos de diseño, construcción, operación y mantenimiento de Estaciones de Servicio para almacenamiento y expendio de diésel y gasolinas.
- Ambiente y residuos del Sector Hidrocarburos: ASEA gestiona, entre otros, trámites de impacto ambiental, Cédula de Operación Anual y registros de residuos cuando resulten aplicables.
- Permisos energéticos: CNE en el ámbito de sus atribuciones. La Evaluación de Impacto Social corresponde a la Secretaría de Energía. Las licencias y obligaciones locales corresponden a la autoridad competente en cada entidad o municipio.

## Consultas técnicas

La sección [Consultas](https://enersafe.com.mx/preguntas-frecuentes.html) reúne respuestas sobre MIDESAFE, SGM, SAT, GASAFE Plus, SASISOPA, NOM-005, ambiente, residuos y permisos. Su contenido parte de la revisión técnica de ENERSAFE y se contrasta con disposiciones oficiales vigentes.

## Contacto

- Teléfono: (55) 2155 2325
- Correo: contacto@enersafe.com.mx
- Dirección: Av. Homero 1422, Polanco, C.P. 11550, CDMX
- Web: https://enersafe.com.mx

## Páginas

- [Inicio](https://enersafe.com.mx/)
- [MIDESAFE SGM](https://enersafe.com.mx/midesafe-sgm.html)
- [GASAFE Plus](https://enersafe.com.mx/gasafe-plus.html)
- [Autoconsumo](https://enersafe.com.mx/autoconsumo.html)
- [Servicios](https://enersafe.com.mx/servicios.html)
- [Nosotros](https://enersafe.com.mx/nosotros.html)
- [Contacto](https://enersafe.com.mx/contacto.html)
- [Consultas](https://enersafe.com.mx/preguntas-frecuentes.html)
'''
put('llms.txt',llms)

# Sitemap update after the audited content revision.
s=get('sitemap.xml').replace('<lastmod>2026-09-09</lastmod>','<lastmod>2026-09-10</lastmod>')
put('sitemap.xml',s)

# VALIDATION — content, bilingual attributes and known legacy claims.
corpus='\n'.join(get(p) for p in HTML)+"\n"+get('llms.txt')
banned=[
    'ControlGAS','Sistemas propios','sistemas propios','Proprietary systems','proprietary systems',
    'El SGM que el SAT exige','sin captura manual','without manual steps','Nothing is left to interpretation',
    'No need to hire additional staff','Sin necesidad de contratar personal adicional',
    'connects with your volumetric control','one party responsible for all of it','Impacto social (CNE)',
    'SEMARNAT y autoridades locales','sostiene el servicio','sostener el servicio'
]
for x in banned:
    if x.lower() in corpus.lower(): raise RuntimeError(f'legacy/banned text remains: {x}')

must={
'index.html':['Cumplimiento digital del SGM','<span class="on-code">CNE</span>','dentro de sus respectivos alcances'],
'midesafe-sgm.html':['Configuramos el SGM','Operas y documentas','MIDESAFE calcula y da seguimiento','Preparas la verificación','Dónde se ubica el SGM dentro del cumplimiento de controles volumétricos'],
'gasafe-plus.html':['Conformación del SASISOPA','Evaluación por Tercero Autorizado','Después del registro y la autorización','Integridad física y operativa de las instalaciones','Informe periódico de desempeño'],
'autoconsumo.html':['No toda instalación de autoconsumo se encuentra en el mismo supuesto','75,714 litros','El alcance depende del supuesto de autoconsumo que corresponda.'],
'servicios.html':['Ambiente y residuos','MIA Particular — sin actividad altamente riesgosa','MIA Particular — con actividad altamente riesgosa','MIA Regional — con actividad altamente riesgosa','Evaluación de Impacto Social (SENER)','CNE, SENER y licencias','Cédula de Operación Anual del Sector Hidrocarburos'],
'preguntas-frecuentes.html':['Última actualización · 10 de septiembre de 2026','ante la ASEA para actividades del Sector Hidrocarburos'],
'contacto.html':['SGM y controles volumétricos (SAT)','href="https://enersafe.com.mx/aviso.html"'],
'llms.txt':['cumplimiento regulatorio digital','La Evaluación de Impacto Social corresponde a la Secretaría de Energía']
}
for p,items in must.items():
    s=get(p)
    for x in items:
        if x not in s: raise RuntimeError(f'{p}: required text missing: {x}')

# Informe Preventivo must occur after the environmental group begins, not in the safety block.
svc=get('servicios.html')
if svc.find('Informe Preventivo') < svc.find('<!-- ASEA AMBIENTE Y RESIDUOS -->'):
    raise RuntimeError('Informe Preventivo still appears before environmental group')

for p in HTML:
    s=get(p)
    if p!='index.html' and 'href="#alertas"' in s: raise RuntimeError(f'{p}: broken local alert link')
    if 'href="#"' in s: raise RuntimeError(f'{p}: dead # footer/social link remains')
    if len(re.findall(r'\bdata-es=',s)) != len(re.findall(r'\bdata-en=',s)):
        raise RuntimeError(f'{p}: data-es/data-en mismatch')

print('Post-audit polish OK')
print('Changed:', ', '.join(changed))
