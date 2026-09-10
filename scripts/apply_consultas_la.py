from pathlib import Path
import re, json, html

ROOT = Path('.')
FAQ = ROOT / 'preguntas-frecuentes.html'
HOME = ROOT / 'index.html'
JS = ROOT / 'js/site.js'


def esc(s):
    return html.escape(s, quote=True)


def item(es_q, es_p, en_q, en_p, open_first=False):
    if isinstance(es_p, str): es_p = [es_p]
    if isinstance(en_p, str): en_p = [en_p]
    op = ' open=""' if open_first else ''
    paras = []
    for ep, np in zip(es_p, en_p):
        paras.append(f'<p data-es="{esc(ep)}" data-en="{esc(np)}">{ep}</p>')
    return f'''<details class="faq-item"{op}>
<summary class="faq-q">
<span data-es="{esc(es_q)}" data-en="{esc(en_q)}">{es_q}</span>
<svg class="faq-chev" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" viewbox="0 0 24 24"><polyline points="6 9 12 15 18 9"></polyline></svg>
</summary>
<div class="faq-a">
{''.join(paras)}
</div>
</details>'''


def group(cat, label_es, label_en, color, entries):
    return f'''<div class="faq-group" data-cat="{cat}">
<div class="faq-group-label">
<span class="faq-group-dot" style="background:{color}"></span>
<span data-es="{esc(label_es)}" data-en="{esc(label_en)}">{label_es}</span>
</div>
{''.join(entries)}
</div>'''

questions = []

def q(cat, es_q, es_p, en_q, en_p):
    questions.append((cat, es_q, es_p if isinstance(es_p, list) else [es_p], en_q, en_p if isinstance(en_p, list) else [en_p]))

# MIDESAFE SGM — contenido derivado de la revisión de L.A., editado para lectura web.
q('sgm',
  '¿Qué actividades del SGM se administran desde MIDESAFE?',
  [
    'MIDESAFE administra, programa, notifica y da seguimiento a las actividades del SGM, concentrando procedimientos, registros, evidencias y soporte documental.',
    'Desde la plataforma se gestionan requisitos de medición, inventario y control de equipos, calibraciones y verificaciones, confirmación metrológica, incertidumbre, descargas y balances de producto, mantenimiento, control de equipos no conformes, función metrológica, control documental, auditorías y revisión de resultados.',
    'Cada actividad conserva su soporte documental e historial para facilitar la trazabilidad y la disponibilidad de evidencias.'
  ],
  'Which SGM activities are managed in MIDESAFE?',
  [
    'MIDESAFE manages, schedules, notifies and follows up on SGM activities, bringing together procedures, records, evidence and supporting documentation.',
    'The platform covers measurement requirements, equipment inventory and control, calibrations and verifications, metrological confirmation, uncertainty, product unloads and balances, maintenance, nonconforming equipment control, the metrology function, document control, audits and results review.',
    'Each activity keeps its supporting documentation and history to facilitate traceability and evidence availability.'
  ])
q('sgm',
  '¿Qué seguimiento realiza ENERSAFE durante la operación de MIDESAFE?',
  [
    'Los técnicos de ENERSAFE revisan las actividades programadas, su ejecución y los soportes documentales registrados en MIDESAFE. Cuando detectan observaciones, desviaciones o acciones correctivas pendientes, dan seguimiento con el responsable de la estación.',
    'Dentro del alcance contratado también se revisan usuarios, firmas, permisos y responsables de actividades. Con esta información se generan reportes periódicos por estación con avance, actividades, desempeño, hallazgos, pendientes y oportunidades de mejora.'
  ],
  'What follow-up does ENERSAFE provide while MIDESAFE is operating?',
  [
    'ENERSAFE technicians review scheduled activities, their execution and the supporting documentation recorded in MIDESAFE. When observations, deviations or pending corrective actions are identified, they follow up with the station manager.',
    'Within the contracted scope, users, signatures, permits and activity owners are also reviewed. This information is used to issue periodic station reports covering progress, activities, performance, findings, pending items and improvement opportunities.'
  ])
q('sgm',
  '¿Cómo prepara MIDESAFE la información para la verificación anual?',
  [
    'MIDESAFE concentra en un expediente digital los procedimientos, formatos, registros, cálculos y soportes documentales del SGM que deben mantenerse disponibles para revisión. La información puede exportarse de forma ordenada para facilitar la evaluación.',
    'La verificación y la emisión del certificado corresponden a la figura acreditada que resulte aplicable. MIDESAFE facilita la organización, disponibilidad y presentación de la evidencia; no sustituye esa evaluación.'
  ],
  'How does MIDESAFE prepare information for annual verification?',
  [
    'MIDESAFE brings together the SGM procedures, forms, records, calculations and supporting documentation that must remain available for review in a digital file. The information can be exported in an organized way to facilitate assessment.',
    'Verification and certificate issuance correspond to the applicable accredited body. MIDESAFE facilitates the organization, availability and presentation of evidence; it does not replace that assessment.'
  ])
q('sgm',
  '¿MIDESAFE permite administrar varias Estaciones de Servicio a nivel corporativo?',
  'Sí. A partir de dos estaciones, MIDESAFE puede operar con una vista corporativa para dar seguimiento a usuarios, responsables, actividades y desempeño por estación, conservando el expediente y la información individual de cada instalación.',
  'Can MIDESAFE manage multiple Service Stations at corporate level?',
  'Yes. From two stations onward, MIDESAFE can provide a corporate view to follow users, responsible persons, activities and performance by station while preserving each facility’s individual file and information.')

# SGM, SAT y controles volumétricos — el bloque extenso de L.A. se divide para evitar una respuesta interminable.
q('sat',
  '¿Qué relación existe entre el Sistema de Gestión de la Medición y los controles volumétricos?',
  'El control volumétrico registra las operaciones de entrada, salida e inventario de producto. El SGM establece cómo se controlan los procesos de medición, los equipos, las responsabilidades y la documentación asociada. Son obligaciones relacionadas, pero no equivalentes. MIDESAFE organiza la operación y la evidencia del SGM a partir de la información de medición de la estación.',
  'How are the Measurement Management System and volumetric controls related?',
  'Volumetric control records product receipts, deliveries and inventory. The SGM establishes how measurement processes, equipment, responsibilities and related documentation are controlled. They are related obligations, but they are not equivalent. MIDESAFE organizes SGM operation and evidence using the station’s measurement information.')
q('sat',
  '¿Qué marco normativo debe considerar el SGM en 2026?',
  [
    'Entre las principales referencias se encuentran la NMX-CC-10012-IMNC-2004, las disposiciones aplicables de la RES/811/2015, el artículo 28, fracción I, apartado B del Código Fiscal de la Federación y la Resolución Miscelánea Fiscal 2026.',
    'La NOM-016-CRE-2016 continúa vigente para las especificaciones de calidad de los petrolíferos. El alcance concreto de cada disposición debe revisarse de acuerdo con la actividad y las características de la estación.'
  ],
  'Which regulatory framework should the SGM consider in 2026?',
  [
    'Key references include NMX-CC-10012-IMNC-2004, the applicable provisions of RES/811/2015, Article 28, section I, subsection B of the Federal Tax Code and the 2026 Tax Miscellaneous Resolution.',
    'NOM-016-CRE-2016 remains in force for petroleum-product quality specifications. The specific scope of each provision should be reviewed according to the station’s activity and characteristics.'
  ])
q('sat',
  '¿Qué regulan los Anexos 21, 22 y 23 de la RMF 2026?',
  [
    'El Anexo 21 establece las especificaciones técnicas de funcionalidad y seguridad de los equipos y programas informáticos para llevar controles volumétricos de hidrocarburos y petrolíferos.',
    'El Anexo 22 regula los servicios de verificación de la correcta operación y funcionamiento de esos equipos y programas, así como los certificados que se emitan. El Anexo 23 establece las características de los dictámenes que determinan el tipo de hidrocarburo o petrolífero y, cuando corresponde, otros parámetros como el octanaje de la gasolina.',
    'En 2026, los Anexos 21 y 22 tuvieron una Primera Modificación publicada el 17 de julio.'
  ],
  'What do Annexes 21, 22 and 23 of the 2026 Tax Miscellaneous Resolution regulate?',
  [
    'Annex 21 establishes the technical functionality and security specifications for equipment and software used to keep volumetric controls of hydrocarbons and petroleum products.',
    'Annex 22 regulates services for verifying the correct operation and functioning of that equipment and software, as well as the certificates issued. Annex 23 establishes the characteristics of reports that determine the type of hydrocarbon or petroleum product and, where applicable, other parameters such as gasoline octane.',
    'In 2026, Annexes 21 and 22 received a First Amendment published on July 17.'
  ])
q('sat',
  '¿Qué establecen las reglas 2.6.1.1 a 2.6.1.6 de la RMF 2026?',
  [
    'En conjunto, estas reglas delimitan el régimen de controles volumétricos. La 2.6.1.1 identifica los hidrocarburos y petrolíferos objeto de control; la 2.6.1.2 define a los contribuyentes obligados; la 2.6.1.3 establece características para equipos y programas informáticos; y la 2.6.1.4 reúne los requerimientos para llevar los controles volumétricos.',
    'Las reglas 2.6.1.5 y 2.6.1.6 se relacionan, respectivamente, con los certificados de correcta operación y funcionamiento y con los dictámenes que determinan el tipo de hidrocarburo o petrolífero y otros parámetros aplicables.'
  ],
  'What do rules 2.6.1.1 through 2.6.1.6 of the 2026 Tax Miscellaneous Resolution establish?',
  [
    'Together, these rules define the volumetric-control framework. Rule 2.6.1.1 identifies the hydrocarbons and petroleum products subject to control; 2.6.1.2 defines the taxpayers required to keep such controls; 2.6.1.3 establishes characteristics for equipment and software; and 2.6.1.4 sets the requirements for keeping volumetric controls.',
    'Rules 2.6.1.5 and 2.6.1.6 relate, respectively, to certificates of correct operation and functioning and to reports that determine the type of hydrocarbon or petroleum product and other applicable parameters.'
  ])
q('sat',
  '¿Cómo se relaciona MIDESAFE con el control volumétrico de la estación?',
  'MIDESAFE administra el SGM utilizando la información de medición y control volumétrico que corresponde a la estación. Los datos requeridos se registran y validan en MIDESAFE para mantener los registros, cálculos y evidencia del sistema. MIDESAFE no sustituye al software de control volumétrico.',
  'How does MIDESAFE relate to the station’s volumetric control?',
  'MIDESAFE manages the SGM using the station’s applicable measurement and volumetric-control information. Required data is recorded and validated in MIDESAFE to maintain the system’s records, calculations and evidence. MIDESAFE does not replace volumetric-control software.')

# GASAFE PLUS / SASISOPA / NOM-005
q('sasisopa',
  '¿Qué implica mantener el SASISOPA implementado durante la operación?',
  [
    'La autorización del SASISOPA no concluye la obligación. Durante la vida del proyecto, los 18 elementos deben permanecer operativos, actualizados y alineados con las condiciones reales de la estación.',
    'Esto implica ejecutar y documentar actividades programadas, mantener procedimientos, registros y evidencias, gestionar cambios en instalaciones, procesos, equipos, personal o requisitos legales y dar seguimiento a capacitación, mantenimiento, inspecciones, riesgos, emergencias, contratistas, auditorías, acciones correctivas e indicadores.',
    'El seguimiento debe identificar desviaciones, responsables y fechas compromiso, verificar la atención de las acciones y conservar la evidencia correspondiente. Cuando aplique, también deben realizarse las gestiones y notificaciones ante la autoridad.'
  ],
  'What does keeping SASISOPA implemented during operation involve?',
  [
    'SASISOPA authorization does not end the obligation. Throughout the life of the project, all 18 elements must remain operational, updated and aligned with the station’s actual conditions.',
    'This includes performing and documenting scheduled activities, maintaining procedures, records and evidence, managing changes in facilities, processes, equipment, personnel or legal requirements, and following up on training, maintenance, inspections, risks, emergencies, contractors, audits, corrective actions and indicators.',
    'Follow-up should identify deviations, owners and target dates, verify that actions are addressed and retain the corresponding evidence. Where applicable, filings and notifications to the authority must also be made.'
  ])
q('sasisopa',
  '¿Qué diferencia existe entre la conformación y el registro del SASISOPA?',
  'La conformación consiste en diseñar, desarrollar e integrar el Sistema de Administración conforme a sus 18 elementos, incluyendo políticas, procedimientos, responsabilidades, controles y mecanismos de seguimiento. El Registro de la Conformación corresponde al trámite mediante el cual esa documentación se presenta ante la ASEA para su revisión y registro.',
  'What is the difference between SASISOPA setup and registration?',
  'Setup consists of designing, developing and integrating the Management System according to its 18 elements, including policies, procedures, responsibilities, controls and follow-up mechanisms. Registration of conformity is the filing through which that documentation is submitted to ASEA for review and registration.')
q('sasisopa',
  '¿Qué diferencia existe entre la autorización y la implementación del SASISOPA?',
  'La autorización permite implementar el Sistema de Administración en una instalación conforme al alcance y condiciones autorizadas. La implementación es llevar ese sistema a la operación real y mantenerlo funcionando durante la vida del proyecto. Contar con registro o autorización no significa, por sí solo, que el SASISOPA esté implementado.',
  'What is the difference between SASISOPA authorization and implementation?',
  'Authorization allows the Management System to be implemented at a facility under the authorized scope and conditions. Implementation means putting that system into actual operation and keeping it functioning throughout the life of the project. Registration or authorization alone does not mean that SASISOPA is implemented.')
q('sasisopa',
  '¿Cómo administra GASAFE Plus los 18 elementos del SASISOPA?',
  'GASAFE Plus calendariza las actividades del sistema, asigna responsables y concentra bitácoras, registros y evidencias. También permite controlar autorizaciones y permisos, registrar incidentes, dar seguimiento a acciones correctivas y mantener disponible la información de los 18 elementos para su revisión.',
  'How does GASAFE Plus manage the 18 SASISOPA elements?',
  'GASAFE Plus schedules system activities, assigns responsible persons and brings together logs, records and evidence. It also supports authorization and permit tracking, incident recording, corrective-action follow-up and keeps information from all 18 elements available for review.')
q('sasisopa',
  '¿Qué seguimiento realiza el especialista asignado a la estación?',
  [
    'El especialista revisa las actividades programadas y las evidencias registradas en GASAFE Plus, y verifica su vigencia y correspondencia con la operación de la estación. Cuando detecta observaciones o desviaciones, da seguimiento con el responsable hasta su atención y cierre.',
    'El servicio también contempla capacitación, asistencia técnica, apoyo en la aplicación de requisitos y reportes periódicos sobre avance, pendientes, hallazgos y oportunidades de mejora.'
  ],
  'What follow-up does the specialist assigned to the station provide?',
  [
    'The specialist reviews scheduled activities and evidence recorded in GASAFE Plus and verifies their validity and correspondence with station operations. When observations or deviations are identified, the specialist follows up with the responsible person until they are addressed and closed.',
    'The service also includes training, technical assistance, support in applying requirements and periodic reports on progress, pending items, findings and improvement opportunities.'
  ])
q('sasisopa',
  '¿Qué relación existe entre GASAFE Plus y la NOM-005-ASEA-2016?',
  'GASAFE Plus ayuda a organizar actividades y evidencias de operación relacionadas con la NOM-005-ASEA-2016, como mantenimiento, bitácoras y permisos de trabajo. La NOM-005 tiene un alcance técnico propio para diseño, construcción, operación y mantenimiento de Estaciones de Servicio y su evaluación de conformidad se realiza de manera independiente. GASAFE Plus no sustituye el dictamen correspondiente.',
  'How does GASAFE Plus relate to NOM-005-ASEA-2016?',
  'GASAFE Plus helps organize operational activities and evidence related to NOM-005-ASEA-2016, such as maintenance, logs and work permits. NOM-005 has its own technical scope for the design, construction, operation and maintenance of Service Stations, and conformity assessment is performed independently. GASAFE Plus does not replace the corresponding assessment report.')
q('sasisopa',
  '¿Qué participación tiene el Tercero Autorizado y qué parte corresponde a ENERSAFE?',
  'Dentro del alcance contratado, ENERSAFE puede conformar la documentación, desarrollar el programa de implementación, acompañar la operación y gestionar el proceso de dictaminación. El Tercero Autorizado realiza la evaluación y emite los dictámenes que correspondan conforme a las disposiciones de la ASEA. Son funciones distintas dentro del mismo proceso de cumplimiento.',
  'What role does the Authorized Third Party play and what corresponds to ENERSAFE?',
  'Within the contracted scope, ENERSAFE can prepare documentation, develop the implementation program, support operation and manage the assessment process. The Authorized Third Party performs the evaluation and issues the applicable reports under ASEA provisions. These are separate functions within the same compliance process.')
q('sasisopa',
  '¿Cómo se documenta la capacitación del personal en GASAFE Plus?',
  'GASAFE Plus incorpora cursos y registros de capacitación asociados a las funciones del personal. La plataforma permite asignar contenidos, dar seguimiento y conservar la evidencia correspondiente, de manera que la competencia y capacitación del personal formen parte del expediente del SASISOPA.',
  'How is staff training documented in GASAFE Plus?',
  'GASAFE Plus includes training courses and records associated with staff functions. The platform allows content to be assigned, followed up and documented so that personnel competence and training form part of the SASISOPA file.')

# AMBIENTAL Y RESIDUOS
q('ambiental',
  '¿Cuándo corresponde presentar la Cédula de Operación Anual del Sector Hidrocarburos?',
  'La COA aplica a los Regulados del Sector Hidrocarburos que se encuentren en los supuestos establecidos por la autoridad ambiental competente, entre ellos determinadas fuentes fijas de jurisdicción federal y grandes generadores de residuos peligrosos. Su alcance depende de las autorizaciones ambientales y de las actividades de la instalación.',
  'When is the Hydrocarbon Sector Annual Operations Report required?',
  'The annual operations report applies to regulated hydrocarbon-sector entities that fall within the cases established by the competent environmental authority, including certain federal-jurisdiction stationary sources and large hazardous-waste generators. Its scope depends on the facility’s environmental authorizations and activities.')
q('ambiental',
  '¿Qué diferencia existe entre un Informe Preventivo y una Manifestación de Impacto Ambiental?',
  [
    'Ambos son instrumentos de evaluación de impacto ambiental, pero no aplican a los mismos proyectos. Para Estaciones de Servicio, la ASEA contempla el Informe Preventivo en determinados proyectos ubicados en áreas urbanas, suburbanas, industriales, de equipamiento urbano o de servicios y en otros supuestos previstos por la autoridad.',
    'La Manifestación de Impacto Ambiental Particular corresponde a proyectos que, por ubicación, características o alcance, se encuentran en supuestos de mayor sensibilidad ambiental. El instrumento aplicable debe determinarse antes de iniciar el trámite.'
  ],
  'What is the difference between a Preventive Report and an Environmental Impact Assessment?',
  [
    'Both are environmental-impact assessment instruments, but they do not apply to the same projects. For Service Stations, ASEA provides for the Preventive Report in certain projects located in urban, suburban, industrial, urban-equipment or service areas and in other cases established by the authority.',
    'The Particular Environmental Impact Assessment applies to projects that, because of their location, characteristics or scope, fall within cases of greater environmental sensitivity. The applicable instrument should be determined before filing.'
  ])
q('ambiental',
  '¿Qué trámites aplican a los residuos peligrosos y a los residuos de manejo especial?',
  'Son categorías distintas y cada una tiene registros y obligaciones propios. El trámite depende del tipo de residuo, la cantidad generada y la categoría del generador. ENERSAFE gestiona los registros y trámites relacionados que correspondan dentro del alcance contratado.',
  'Which filings apply to hazardous waste and special-management waste?',
  'They are different categories and each has its own registrations and obligations. The required filing depends on the type of waste, quantity generated and generator category. ENERSAFE manages the applicable registrations and related filings within the contracted scope.')

# PERMISOS Y REGULACIÓN SECTORIAL
q('permisos',
  '¿Cuándo corresponde actualizar o modificar un permiso de expendio?',
  'Una actualización atiende cambios que no alteran las condiciones esenciales bajo las que se otorgó el permiso. Una modificación aplica cuando cambian condiciones relevantes del servicio, por ejemplo una cesión, fusión, cambio de control o una modificación técnica de la infraestructura. La CNE distingue ambos trámites, por lo que el supuesto debe revisarse antes de ingresar la solicitud.',
  'When should a retail permit be updated or modified?',
  'An update addresses changes that do not alter the essential conditions under which the permit was granted. A modification applies when relevant service conditions change, such as an assignment, merger, change of control or a technical infrastructure modification. CNE distinguishes between the two procedures, so the applicable case should be reviewed before filing.')

by_cat = {c: [] for c in ['sgm','sat','sasisopa','ambiental','permisos']}
for cat, eq, ep, nq, np in questions:
    by_cat[cat].append(item(eq, ep, nq, np, open_first=(cat == 'sgm' and len(by_cat[cat]) == 0)))

main = f'''<!-- NAVEGACIÓN POR TEMA -->
<section class="section faq-page-main">
<div class="wrap">
<div class="faq-cats reveal">
<button class="faq-cat active" data-en="All" data-es="Todo" onclick="filterFaq('todos')">Todo</button>
<button class="faq-cat" data-en="MIDESAFE SGM" data-es="MIDESAFE SGM" onclick="filterFaq('sgm')">MIDESAFE SGM</button>
<button class="faq-cat" data-en="SGM · SAT" data-es="SGM · SAT" onclick="filterFaq('sat')">SGM · SAT</button>
<button class="faq-cat" data-en="GASAFE Plus" data-es="GASAFE Plus" onclick="filterFaq('sasisopa')">GASAFE Plus</button>
<button class="faq-cat" data-en="Environmental" data-es="Ambiental" onclick="filterFaq('ambiental')">Ambiental</button>
<button class="faq-cat" data-en="Permits" data-es="Permisos" onclick="filterFaq('permisos')">Permisos</button>
</div>
<div class="faq-page-grid reveal" data-delay="1">
{group('sgm','MIDESAFE SGM','MIDESAFE SGM','var(--yellow)',by_cat['sgm'])}
{group('sat','SGM · SAT y controles volumétricos','SGM · SAT and volumetric controls','var(--lime)',by_cat['sat'])}
{group('sasisopa','GASAFE Plus · SASISOPA + NOM-005','GASAFE Plus · SASISOPA + NOM-005','var(--lime-deep)',by_cat['sasisopa'])}
{group('ambiental','Ambiental y residuos','Environmental and waste','var(--gray-brand)',by_cat['ambiental'])}
{group('permisos','Permisos y regulación sectorial','Permits and sector regulation','var(--yellow-deep)',by_cat['permisos'])}
</div>
<div class="faq-cta reveal">
<div class="faq-cta-inner">
<svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" viewbox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
<div>
<p class="faq-cta-title" data-en="Does your case require a specific review?" data-es="¿Tu caso requiere una revisión específica?">¿Tu caso requiere una revisión específica?</p>
<p class="faq-cta-sub" data-en="Tell us about your station and we will review the applicable scope with you." data-es="Cuéntanos sobre tu estación y revisamos contigo el alcance que corresponde.">Cuéntanos sobre tu estación y revisamos contigo el alcance que corresponde.</p>
</div>
<a class="btn btn-primary" data-en="Ask an advisor" data-es="Consultar con un asesor" href="https://wa.me/525610360614" rel="noopener" target="_blank">Consultar con un asesor</a>
</div>
</div>
</div>
</section>'''

faq_text = FAQ.read_text(encoding='utf-8')
faq_text = re.sub(
    r'<!-- NAVEGACIÓN POR TEMA -->.*?</section>\s*<footer>',
    main + '\n<footer>',
    faq_text,
    count=1,
    flags=re.S
)

# Hero editorial: el Word de L.A. es la base; la navegación web se organiza por tema.
faq_text = faq_text.replace(
    'Consultas sobre SGM, SASISOPA, NOM-005 <span class="hl">y cumplimiento regulatorio.</span>',
    'Respuestas técnicas <span class="hl">para las obligaciones de tu estación.</span>'
).replace(
    'data-es="Consultas sobre SGM, SASISOPA, NOM-005 &lt;span class=\'hl\'&gt;y cumplimiento regulatorio.&lt;/span&gt;"',
    'data-es="Respuestas técnicas &lt;span class=\'hl\'&gt;para las obligaciones de tu estación.&lt;/span&gt;"'
).replace(
    'Respuestas sobre el alcance de MIDESAFE, GASAFE Plus y otros frentes regulatorios, con la terminología que utiliza el equipo técnico de ENERSAFE.',
    'MIDESAFE, SGM y SAT; GASAFE Plus, SASISOPA y NOM-005; además de temas ambientales, residuos y permisos. Organizado por tema para localizar rápido la consulta que necesitas.'
)

# Schema FAQPage sincronizado con la nueva base.
schema = {
    '@context': 'https://schema.org',
    '@graph': [
        {'@type':'Organization','@id':'https://enersafe.com.mx/#organization','name':'ENERSAFE','url':'https://enersafe.com.mx'},
        {'@type':'WebPage','@id':'https://enersafe.com.mx/preguntas-frecuentes.html','url':'https://enersafe.com.mx/preguntas-frecuentes.html','name':'Consultas ENERSAFE — MIDESAFE, SGM, SAT, GASAFE Plus y SASISOPA','description':'Consultas técnicas sobre MIDESAFE SGM, controles volumétricos, RMF 2026, GASAFE Plus, SASISOPA, NOM-005, temas ambientales y permisos para Estaciones de Servicio.'},
        {'@type':'FAQPage','mainEntity':[
            {'@type':'Question','name':eq,'acceptedAnswer':{'@type':'Answer','text':' '.join(ep)}}
            for _,eq,ep,_,_ in questions
        ]}
    ]
}
faq_text = re.sub(
    r'<script type="application/ld\+json">.*?</script>',
    '<script type="application/ld+json">\n' + json.dumps(schema, ensure_ascii=False, separators=(',',':')) + '\n</script>',
    faq_text,
    count=1,
    flags=re.S
)
faq_text = re.sub(r'<title>.*?</title>', '<title>Consultas ENERSAFE — MIDESAFE, SGM, SAT, SASISOPA y NOM-005</title>', faq_text, count=1, flags=re.S)
faq_text = re.sub(r'<meta content="[^"]*" name="description"/>', '<meta content="Consultas técnicas sobre MIDESAFE SGM, controles volumétricos, RMF 2026, GASAFE Plus, SASISOPA, NOM-005, temas ambientales y permisos para Estaciones de Servicio." name="description"/>', faq_text, count=1)
FAQ.write_text(faq_text, encoding='utf-8')

# HOME: muestra sólo cuatro consultas representativas y manda a la base completa.
home_items = [
    item(
        '¿Qué relación existe entre el SGM y los controles volumétricos?',
        'El control volumétrico registra entradas, salidas e inventarios. El SGM controla los procesos de medición, los equipos, las responsabilidades y la documentación asociada. Son obligaciones relacionadas, pero no equivalentes.',
        'How are the SGM and volumetric controls related?',
        'Volumetric control records receipts, deliveries and inventory. The SGM controls measurement processes, equipment, responsibilities and related documentation. They are related obligations, but not equivalent.',
        True
    ),
    item(
        '¿Qué actividades del SGM se administran desde MIDESAFE?',
        'MIDESAFE programa, notifica y da seguimiento a las actividades del SGM y concentra procedimientos, registros, cálculos, evidencias y soporte documental.',
        'Which SGM activities are managed in MIDESAFE?',
        'MIDESAFE schedules, notifies and follows up on SGM activities while bringing together procedures, records, calculations, evidence and supporting documentation.'
    ),
    item(
        '¿Qué implica mantener el SASISOPA implementado durante la operación?',
        'La autorización no concluye la obligación. Los 18 elementos deben permanecer operativos, actualizados y documentados durante la vida del proyecto, de acuerdo con las condiciones reales de la estación.',
        'What does keeping SASISOPA implemented during operation involve?',
        'Authorization does not end the obligation. All 18 elements must remain operational, updated and documented throughout the life of the project according to the station’s actual conditions.'
    ),
    item(
        '¿Qué relación existe entre GASAFE Plus y la NOM-005-ASEA-2016?',
        'GASAFE Plus organiza actividades y evidencias operativas relacionadas con la NOM-005. La norma tiene un alcance técnico propio y su evaluación de conformidad se realiza de manera independiente.',
        'How does GASAFE Plus relate to NOM-005-ASEA-2016?',
        'GASAFE Plus organizes operational activities and evidence related to NOM-005. The standard has its own technical scope and conformity assessment is performed independently.'
    )
]
home_section = f'''<!-- ============================ CONSULTAS ============================ -->
<section aria-label="Consultas ENERSAFE" class="section faq-sec" id="faq">
<div class="wrap">
<div class="section-head center reveal">
<span class="eyebrow" data-en="ENERSAFE consultations" data-es="Consultas ENERSAFE">Consultas ENERSAFE</span>
<h2 data-en="Clear answers about the obligations we manage." data-es="Respuestas claras sobre las obligaciones que atendemos.">Respuestas claras sobre las obligaciones que atendemos.</h2>
<p class="lead" data-en="SGM, SAT, volumetric controls, SASISOPA and NOM-005. The full consultation center also includes environmental matters, waste and permits." data-es="SGM, SAT, controles volumétricos, SASISOPA y NOM-005. El centro de consultas completo también incluye temas ambientales, residuos y permisos." style="margin:0 auto">SGM, SAT, controles volumétricos, SASISOPA y NOM-005. El centro de consultas completo también incluye temas ambientales, residuos y permisos.</p>
</div>
<div class="faq-list reveal" data-delay="1">
{''.join(home_items)}
</div>
<div class="reveal" style="text-align:center;margin-top:10px;">
<a class="faq-more-link" data-en="View all consultations" data-es="Ver todas las consultas" href="preguntas-frecuentes.html">Ver todas las consultas <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><line x1="5" x2="19" y1="12" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></a>
</div>
</div>
</section>'''

home_text = HOME.read_text(encoding='utf-8')
home_text = re.sub(
    r'<!-- ============================ PREGUNTAS FRECUENTES.*?</section>\s*<!-- ============================ CTA',
    home_section + '\n<!-- ============================ CTA',
    home_text,
    count=1,
    flags=re.S
)
HOME.write_text(home_text, encoding='utf-8')

# Normalizar el nombre del recurso en footers y navegación: Consultas, no FAQ/Preguntas frecuentes.
for p in ROOT.glob('*.html'):
    txt = p.read_text(encoding='utf-8')
    txt = txt.replace('data-es="Preguntas frecuentes"', 'data-es="Consultas"')
    txt = txt.replace('>Preguntas frecuentes</a>', '>Consultas</a>')
    p.write_text(txt, encoding='utf-8')

# Añadir Consultas al buscador del sitio si aún no existe.
js = JS.read_text(encoding='utf-8')
if 'title:"Consultas ENERSAFE"' not in js:
    needle = 'const SEARCH_INDEX=[\n'
    entry = '  {tag:"Consultas",title:"Consultas ENERSAFE",snippet:"SGM, SAT, controles volumétricos, SASISOPA, NOM-005, ambiente, residuos y permisos.",tags:"consultas preguntas sgm sat controles volumetricos sasisopa nom-005 ambiental residuos permisos cne",url:"preguntas-frecuentes.html"},\n'
    js = js.replace(needle, needle + entry, 1)
JS.write_text(js, encoding='utf-8')

# Validaciones de publicación.
faq_check = FAQ.read_text(encoding='utf-8')
assert 'CONTROLGAS' not in faq_check.upper()
assert '¿Cómo se documenta la capacitación del personal en GASAFE Plus?' in faq_check
assert '¿Qué regulan los Anexos 21, 22 y 23 de la RMF 2026?' in faq_check
assert '¿Qué establecen las reglas 2.6.1.1 a 2.6.1.6 de la RMF 2026?' in faq_check
assert faq_check.count('class="faq-item"') >= 21
assert 'data-cat="ambiental"' in faq_check and 'data-cat="permisos"' in faq_check
assert 'FAQPage' in faq_check
assert 'Consultas ENERSAFE' in HOME.read_text(encoding='utf-8')
print(f'Consultas integradas: {len(questions)} preguntas en 5 bloques temáticos.')
