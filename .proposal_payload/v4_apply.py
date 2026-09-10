from pathlib import Path
import re

ROOT = Path('.')
changed = []

def load(path):
    p = ROOT / path
    return p, p.read_text(encoding='utf-8')

def save(path, text):
    p = ROOT / path
    p.write_text(text, encoding='utf-8')
    if path not in changed:
        changed.append(path)

def replace(path, old, new, required=True, count=-1):
    p, s = load(path)
    n = s.count(old)
    if required and n == 0:
        raise RuntimeError(f'{path}: missing replacement target: {old[:120]!r}')
    if n:
        s = s.replace(old, new, count)
        save(path, s)
    return n

def sub(path, pattern, repl, required=True, flags=re.S, count=1):
    p, s = load(path)
    out, n = re.subn(pattern, repl, s, count=count, flags=flags)
    if required and n == 0:
        raise RuntimeError(f'{path}: regex target not found: {pattern[:120]}')
    if n:
        save(path, out)
    return n

def section(path, start_marker, end_marker, new_html):
    p, s = load(path)
    pattern = re.escape(start_marker) + r'.*?(?=' + re.escape(end_marker) + r')'
    block = start_marker + '\n' + new_html.rstrip() + '\n'
    out, n = re.subn(pattern, lambda m: block, s, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError(f'{path}: section not found {start_marker}')
    save(path, out)

# -----------------------------------------------------------------------------
# GLOBAL NAVIGATION: internal pages must return to Home for regulatory alerts.
# -----------------------------------------------------------------------------
for path in ['midesafe-sgm.html','gasafe-plus.html','autoconsumo.html','servicios.html','nosotros.html','contacto.html','preguntas-frecuentes.html']:
    replace(path, 'href="#alertas"', 'href="index.html#alertas"', required=False)

# -----------------------------------------------------------------------------
# MIDESAFE SGM — rebuild the commercial story around the SGM, not data transfer.
# -----------------------------------------------------------------------------
section('midesafe-sgm.html',
'<!-- ============================ ENCABEZADO DE PÁGINA ============================ -->',
'<!-- ============================ EL PROBLEMA QUE RESUELVE ============================ -->',
'''<section class="page-hero">
<div class="ph-mesh"></div>
<div class="wrap">
<div class="crumbs">
<a data-en="Home" data-es="Inicio" href="index.html">Inicio</a> <span>/</span>
<a data-en="Solutions" data-es="Soluciones" href="servicios.html">Soluciones</a> <span>/</span>
<span>MIDESAFE SGM</span>
</div>
<span class="eyebrow light">MIDESAFE SGM</span>
<h1 data-en="Digital SGM compliance &lt;span class='hl'&gt;with MIDESAFE.&lt;/span&gt;" data-es="Cumplimiento digital del SGM &lt;span class='hl'&gt;con MIDESAFE.&lt;/span&gt;">Cumplimiento digital del SGM <span class="hl">con MIDESAFE.</span></h1>
<p data-en="MIDESAFE brings together SGM activities, records, calculations and evidence in one digital environment, with specialized technical follow-up throughout operation." data-es="MIDESAFE concentra actividades, registros, cálculos y evidencia del Sistema de Gestión de la Medición en un entorno digital, con seguimiento técnico especializado durante su operación.">MIDESAFE concentra actividades, registros, cálculos y evidencia del Sistema de Gestión de la Medición en un entorno digital, con seguimiento técnico especializado durante su operación.</p>
<div class="ph-norm"><svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><path d="M9 11l3 3L22 4"></path><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg> <span data-en="NMX-CC-10012-IMNC-2004 · 2026 RMF · Reviewed by accredited Inspection Units" data-es="NMX-CC-10012-IMNC-2004 · RMF 2026 · Revisado por Unidades de Inspección acreditadas">NMX-CC-10012-IMNC-2004 · RMF 2026 · Revisado por Unidades de Inspección acreditadas</span></div>
<div class="ph-actions">
<a class="btn btn-primary" data-en="Request a demo" data-es="Solicitar demostración" href="https://wa.me/525610360614" rel="noopener" target="_blank"><svg fill="currentColor" style="width:16px;height:16px" viewbox="0 0 24 24"><path d="M17.5 14.4c-.3-.1-1.7-.8-2-.9-.3-.1-.5-.1-.7.1-.2.3-.7.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6.1-.1.3-.3.4-.5.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.7-.7 1.9-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3z"></path></svg> Solicitar demostración</a>
<a class="btn btn-secondary" data-en="See how it works" data-es="Ver cómo funciona" href="#como"><svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg> Ver cómo funciona</a>
</div>
</div>
</section>''')

section('midesafe-sgm.html',
'<!-- ============================ EL PROBLEMA QUE RESUELVE ============================ -->',
'<!-- ============================ CÓMO FUNCIONA (flujo de 4 pasos) ============================ -->',
'''<section class="section sols">
<div class="wrap">
<div class="prob-layout">
<div class="reveal-l">
<span class="eyebrow" data-en="What the SGM requires" data-es="Lo que exige el SGM">Lo que exige el SGM</span>
<h2 data-en="The SGM is more than measurement: it also requires processes, responsible parties and evidence." data-es="El SGM es más que medición: también requiere procesos, responsables y evidencia.">El SGM es más que medición: también requiere procesos, responsables y evidencia.</h2>
<p class="lead" data-en="A Measurement Management System controls measurement processes and equipment, but also responsibilities, activities, records and documented evidence. When these pieces are managed separately, follow-up becomes harder and the annual review requires more rework." data-es="Un Sistema de Gestión de la Medición controla procesos y equipos de medición, pero también responsabilidades, actividades, registros y evidencia documental. Cuando esas piezas se administran por separado, el seguimiento se vuelve más complejo y la revisión anual exige más trabajo de preparación.">Un Sistema de Gestión de la Medición controla procesos y equipos de medición, pero también responsabilidades, actividades, registros y evidencia documental. Cuando esas piezas se administran por separado, el seguimiento se vuelve más complejo y la revisión anual exige más trabajo de preparación.</p>
</div>
<div class="reveal-r" data-delay="1">
<span class="prob-label" data-en="Without a centralized SGM" data-es="Sin una gestión centralizada">Sin una gestión centralizada</span>
<div class="prob-list">
<div class="prob-item"><span class="pi-x">×</span><span data-en="Activities and responsible parties are followed up in separate files" data-es="Las actividades y responsables se siguen en archivos separados">Las actividades y responsables se siguen en archivos separados</span></div>
<div class="prob-item"><span class="pi-x">×</span><span data-en="Balance and uncertainty calculations are performed manually" data-es="Los cálculos de balance e incertidumbre se realizan manualmente">Los cálculos de balance e incertidumbre se realizan manualmente</span></div>
<div class="prob-item"><span class="pi-x">×</span><span data-en="Evidence and validities are dispersed in different folders" data-es="La evidencia y las vigencias quedan dispersas en distintas carpetas">La evidencia y las vigencias quedan dispersas en distintas carpetas</span></div>
<div class="prob-item"><span class="pi-x">×</span><span data-en="The annual review begins with pending items still to organize" data-es="La revisión anual comienza con pendientes todavía por ordenar">La revisión anual comienza con pendientes todavía por ordenar</span></div>
</div>
</div>
</div>
</div>
</section>''')

section('midesafe-sgm.html',
'<!-- ============================ CÓMO FUNCIONA (flujo de 4 pasos) ============================ -->',
'<!-- ============================ CONEXIÓN CON CONTROL VOLUMÉTRICO ============================ -->',
'''<section class="section how" id="como">
<div class="wrap">
<div class="section-head center reveal">
<span class="eyebrow" data-en="How the service works" data-es="Cómo funciona el servicio">Cómo funciona el servicio</span>
<h2 data-en="From SGM setup to annual verification." data-es="De la configuración del SGM a la verificación anual.">De la configuración del SGM a la verificación anual.</h2>
<p class="lead" data-en="MIDESAFE is not just a repository. The service combines configuration, daily operation, automated calculations, evidence management and technical follow-up." data-es="MIDESAFE no es sólo un repositorio. El servicio combina configuración, operación, cálculos automatizados, gestión de evidencia y seguimiento técnico." style="margin:0 auto">MIDESAFE no es sólo un repositorio. El servicio combina configuración, operación, cálculos automatizados, gestión de evidencia y seguimiento técnico.</p>
</div>
<div class="flow">
<div class="flow-line"></div>
<div class="flow-step reveal">
<div class="fs-ic"><svg fill="none" stroke="currentColor" stroke-width="1.8" viewbox="0 0 24 24"><path d="M4 4h16v16H4z"></path><path d="M8 8h8M8 12h8M8 16h5"></path></svg></div>
<span class="fs-step" data-en="Step 1" data-es="Paso 1">Paso 1</span>
<h3 data-en="We configure the SGM" data-es="Configuramos el SGM">Configuramos el SGM</h3>
<p data-en="We integrate station information, measurement equipment, users, responsible parties, procedures and the activities that apply to its operation." data-es="Integramos la información de la estación, equipos de medición, usuarios, responsables, procedimientos y las actividades que aplican a su operación.">Integramos la información de la estación, equipos de medición, usuarios, responsables, procedimientos y las actividades que aplican a su operación.</p>
</div>
<div class="flow-step reveal" data-delay="1">
<div class="fs-ic"><svg fill="none" stroke="currentColor" stroke-width="1.8" viewbox="0 0 24 24"><path d="M5 4h14v16H5z"></path><path d="M8 9l2 2 5-5M8 15h8"></path></svg></div>
<span class="fs-step" data-en="Step 2" data-es="Paso 2">Paso 2</span>
<h3 data-en="You operate and document" data-es="Operas y documentas">Operas y documentas</h3>
<p data-en="MIDESAFE schedules SGM activities and brings together the forms, records, supporting documents and evidence generated during operation." data-es="MIDESAFE programa las actividades del SGM y concentra los formatos, registros, soportes y evidencias que se generan durante la operación.">MIDESAFE programa las actividades del SGM y concentra los formatos, registros, soportes y evidencias que se generan durante la operación.</p>
</div>
<div class="flow-step reveal" data-delay="2">
<div class="fs-ic"><svg fill="none" stroke="currentColor" stroke-width="1.8" viewbox="0 0 24 24"><path d="M3 19h18M5 16l4-5 4 3 6-8"></path></svg></div>
<span class="fs-step" data-en="Step 3" data-es="Paso 3">Paso 3</span>
<h3 data-en="MIDESAFE calculates and follows up" data-es="MIDESAFE calcula y da seguimiento">MIDESAFE calcula y da seguimiento</h3>
<p data-en="The tool performs calculations such as product balance and uncertainty, controls validities and keeps the history. The ENERSAFE specialist reviews activities, supporting documents and observations." data-es="La herramienta realiza cálculos como balance de producto e incertidumbre, controla vigencias y conserva el historial. El especialista ENERSAFE revisa actividades, soportes y observaciones.">La herramienta realiza cálculos como balance de producto e incertidumbre, controla vigencias y conserva el historial. El especialista ENERSAFE revisa actividades, soportes y observaciones.</p>
</div>
<div class="flow-step reveal" data-delay="3">
<div class="fs-ic"><svg fill="none" stroke="currentColor" stroke-width="1.8" viewbox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16h16V8z"></path><path d="M14 2v6h6M8 14h8M8 18h5"></path></svg></div>
<span class="fs-step" data-en="Step 4" data-es="Paso 4">Paso 4</span>
<h3 data-en="You prepare the verification" data-es="Preparas la verificación">Preparas la verificación</h3>
<p data-en="Procedures, forms, records, calculations and supporting documents are organized in an exportable digital file to facilitate review. Verification and certificate issuance correspond to the applicable accredited body." data-es="Procedimientos, formatos, registros, cálculos y soportes quedan organizados en un expediente digital exportable para facilitar la revisión. La verificación y la emisión de certificados corresponden a la figura acreditada aplicable.">Procedimientos, formatos, registros, cálculos y soportes quedan organizados en un expediente digital exportable para facilitar la revisión. La verificación y la emisión de certificados corresponden a la figura acreditada aplicable.</p>
</div>
</div>
</div>
</section>''')

section('midesafe-sgm.html',
'<!-- ============================ CONEXIÓN CON CONTROL VOLUMÉTRICO ============================ -->',
'<!-- ============================ CUMPLIMIENTO CONFORME A LA NORMA ============================ -->',
'''<section class="spec">
<div class="spec-mesh"></div><div class="spec-grid-bg"></div>
<div class="wrap"><div class="spec-inner">
<div class="reveal-l">
<span class="eyebrow light" data-en="MIDESAFE in operation" data-es="MIDESAFE en operación">MIDESAFE en operación</span>
<h2 data-en="What MIDESAFE manages throughout SGM operation." data-es="Lo que MIDESAFE administra durante la operación del SGM.">Lo que MIDESAFE administra durante la operación del SGM.</h2>
<p class="lead" data-en="Activities, measurement information, calculations, documentation and technical follow-up are organized in MIDESAFE to maintain traceability and make the status of the SGM visible." data-es="Actividades, información de medición, cálculos, documentación y seguimiento técnico se organizan en MIDESAFE para mantener la trazabilidad y hacer visible el estado del SGM.">Actividades, información de medición, cálculos, documentación y seguimiento técnico se organizan en MIDESAFE para mantener la trazabilidad y hacer visible el estado del SGM.</p>
<div class="spec-list">
<div class="spec-item"><span class="ic">01</span><span class="tx"><b data-en="Activities and responsible parties" data-es="Actividades y responsables">Actividades y responsables</b><span data-en="Schedules activities, assigns responsible parties and notifies pending work." data-es="Programa actividades, asigna responsables y notifica pendientes.">Programa actividades, asigna responsables y notifica pendientes.</span></span></div>
<div class="spec-item"><span class="ic">02</span><span class="tx"><b data-en="Measurement and calculations" data-es="Medición y cálculos">Medición y cálculos</b><span data-en="Manages measurement information and calculations such as product balance and uncertainty." data-es="Administra información de medición y cálculos como balance de producto e incertidumbre.">Administra información de medición y cálculos como balance de producto e incertidumbre.</span></span></div>
<div class="spec-item"><span class="ic">03</span><span class="tx"><b data-en="Evidence and history" data-es="Evidencia e historial">Evidencia e historial</b><span data-en="Keeps procedures, forms, supporting documents, validities and documentary history together." data-es="Concentra procedimientos, formatos, soportes, vigencias e historial documental.">Concentra procedimientos, formatos, soportes, vigencias e historial documental.</span></span></div>
<div class="spec-item"><span class="ic">04</span><span class="tx"><b data-en="Technical follow-up" data-es="Seguimiento técnico">Seguimiento técnico</b><span data-en="The ENERSAFE specialist reviews recorded information and reports observations, pending items and progress." data-es="El especialista ENERSAFE revisa la información registrada y reporta observaciones, pendientes y avance.">El especialista ENERSAFE revisa la información registrada y reporta observaciones, pendientes y avance.</span></span></div>
</div>
</div>
<div class="reveal-r" data-delay="1"><div class="spec-panel">
<p class="spec-panel-intro" data-en="A practical view of follow-up in MIDESAFE:" data-es="Una vista práctica del seguimiento en MIDESAFE:">Una vista práctica del seguimiento en MIDESAFE:</p>
<div class="sp-head"><span class="t" data-en="SGM follow-up" data-es="Seguimiento del SGM">Seguimiento del SGM</span><span class="sp-live"><span class="pulse"></span> <span data-en="Active" data-es="Activo">Activo</span></span></div>
<div class="sp-body">
<div class="sp-row"><span class="sp-check ok">✓</span><span class="lbl" data-en="Scheduled activity" data-es="Actividad programada">Actividad programada</span><span class="val val-ok" data-en="In follow-up" data-es="En seguimiento">En seguimiento</span></div>
<div class="sp-row"><span class="sp-check ok">✓</span><span class="lbl" data-en="Supporting document" data-es="Soporte documental">Soporte documental</span><span class="val val-ok" data-en="Reviewed" data-es="Revisado">Revisado</span></div>
<div class="sp-row"><span class="sp-check warn">!</span><span class="lbl" data-en="Upcoming expiration" data-es="Próximo vencimiento">Próximo vencimiento</span><span class="val val-warn" data-en="Alert" data-es="Alerta">Alerta</span></div>
<div class="sp-row"><span class="sp-check warn">!</span><span class="lbl" data-en="Observation" data-es="Observación">Observación</span><span class="val val-warn" data-en="Pending attention" data-es="Por atender">Por atender</span></div>
</div>
<div class="sp-foot"><span data-en="Status is updated with the information recorded in the platform and the specialist's review." data-es="El estado se actualiza con la información registrada en la plataforma y la revisión del especialista.">El estado se actualiza con la información registrada en la plataforma y la revisión del especialista.</span></div>
</div></div>
</div></div></section>''')

section('midesafe-sgm.html',
'<!-- ============================ CUMPLIMIENTO CONFORME A LA NORMA ============================ -->',
'<!-- ============================ QUÉ INCLUYE ============================ -->',
'''<section class="section deps">
<div class="wrap">
<div class="section-head center reveal">
<span class="eyebrow" data-en="Technical and tax references" data-es="Referencias técnicas y fiscales">Referencias técnicas y fiscales</span>
<h2 data-en="Where the SGM fits within volumetric-control compliance." data-es="Dónde se ubica el SGM dentro del cumplimiento de controles volumétricos.">Dónde se ubica el SGM dentro del cumplimiento de controles volumétricos.</h2>
<p class="lead" data-en="NMX-CC-10012-IMNC-2004 establishes requirements for measurement processes and measurement equipment. The 2026 RMF separately regulates technical specifications for volumetric-control equipment and software, verification and certificates, and product-related reports. MIDESAFE focuses on operating and documenting the SGM and does not replace those independent assessments." data-es="La NMX-CC-10012-IMNC-2004 establece requisitos para los procesos de medición y los equipos de medición. La RMF 2026 regula por separado las especificaciones de equipos y programas de controles volumétricos, su verificación y certificados, y los dictámenes sobre el producto. MIDESAFE se enfoca en operar y documentar el SGM y no sustituye esas evaluaciones independientes." style="margin:0 auto">La NMX-CC-10012-IMNC-2004 establece requisitos para los procesos de medición y los equipos de medición. La RMF 2026 regula por separado las especificaciones de equipos y programas de controles volumétricos, su verificación y certificados, y los dictámenes sobre el producto. MIDESAFE se enfoca en operar y documentar el SGM y no sustituye esas evaluaciones independientes.</p>
</div>
<div class="seals reveal" data-delay="1">
<div class="seal"><span class="seal-ic">01</span><span class="seal-t">NMX-CC-10012-IMNC-2004</span><span class="seal-d" data-en="Measurement processes and measurement equipment" data-es="Procesos de medición y equipos de medición">Procesos de medición y equipos de medición</span></div>
<div class="seal"><span class="seal-ic">02</span><span class="seal-t">RES/811/2015</span><span class="seal-d" data-en="Measurement provisions applicable according to the activity" data-es="Disposiciones de medición aplicables según la actividad">Disposiciones de medición aplicables según la actividad</span></div>
<div class="seal"><span class="seal-ic">03</span><span class="seal-t" data-en="2026 RMF · Annexes 21, 22 and 23" data-es="RMF 2026 · Anexos 21, 22 y 23">RMF 2026 · Anexos 21, 22 y 23</span><span class="seal-d" data-en="Volumetric controls, verification, certificates and reports" data-es="Controles volumétricos, verificación, certificados y dictámenes">Controles volumétricos, verificación, certificados y dictámenes</span></div>
</div>
<div class="incl-note reveal"><span data-en="MIDESAFE has been reviewed by accredited Inspection Units in verification processes. This experience does not replace the assessment that corresponds to each regulated entity." data-es="MIDESAFE ha sido revisado por Unidades de Inspección acreditadas en procesos de verificación. Esta experiencia no sustituye la evaluación que corresponda a cada Regulado.">MIDESAFE ha sido revisado por Unidades de Inspección acreditadas en procesos de verificación. Esta experiencia no sustituye la evaluación que corresponda a cada Regulado.</span></div>
<div class="req-block reveal" data-delay="2">
<h3 class="req-title" data-en="SGM components managed in MIDESAFE" data-es="Componentes del SGM gestionados en MIDESAFE">Componentes del SGM gestionados en MIDESAFE</h3>
<div class="req-grid">
<div class="req"><span class="req-n">01</span><span data-en="Policy" data-es="Política">Política</span></div>
<div class="req"><span class="req-n">02</span><span data-en="Risk identification and evaluation matrix" data-es="Matriz para identificar y evaluar riesgos">Matriz para identificar y evaluar riesgos</span></div>
<div class="req"><span class="req-n">03</span><span data-en="Legal requirements matrix" data-es="Matriz de requisitos legales">Matriz de requisitos legales</span></div>
<div class="req"><span class="req-n">04</span><span data-en="Objectives" data-es="Objetivos">Objetivos</span></div>
<div class="req"><span class="req-n">05</span><span data-en="Roles and responsibilities matrix" data-es="Matriz de funciones y responsabilidades">Matriz de funciones y responsabilidades</span></div>
<div class="req"><span class="req-n">06</span><span data-en="Staff competence and training" data-es="Competencia y capacitación del personal">Competencia y capacitación del personal</span></div>
<div class="req"><span class="req-n">07</span><span data-en="Communication" data-es="Comunicación">Comunicación</span></div>
<div class="req"><span class="req-n">08</span><span data-en="Document control" data-es="Control de documentos">Control de documentos</span></div>
<div class="req"><span class="req-n">09</span><span data-en="Product unloads" data-es="Descargas de producto">Descargas de producto</span></div>
<div class="req"><span class="req-n">10</span><span data-en="Product balances" data-es="Balances de producto">Balances de producto</span></div>
<div class="req"><span class="req-n">11</span><span data-en="Preventive and corrective maintenance" data-es="Mantenimiento preventivo y correctivo">Mantenimiento preventivo y correctivo</span></div>
<div class="req"><span class="req-n">12</span><span data-en="Measurement uncertainty" data-es="Incertidumbre de medición">Incertidumbre de medición</span></div>
<div class="req"><span class="req-n">13</span><span data-en="Metrological confirmation" data-es="Confirmación metrológica">Confirmación metrológica</span></div>
<div class="req"><span class="req-n">14</span><span data-en="Measurement-equipment calibration" data-es="Calibración de equipos de medición">Calibración de equipos de medición</span></div>
<div class="req"><span class="req-n">15</span><span data-en="Corrective-action follow-up and closure" data-es="Seguimiento y cierre de acciones correctivas">Seguimiento y cierre de acciones correctivas</span></div>
<div class="req"><span class="req-n">16</span><span data-en="SGM equipment list" data-es="Listado de equipos del SGM">Listado de equipos del SGM</span></div>
<div class="req"><span class="req-n">17</span><span data-en="SGM audits" data-es="Auditorías al SGM">Auditorías al SGM</span></div>
<div class="req"><span class="req-n">18</span><span data-en="Incident and accident matrix" data-es="Matriz de incidentes y accidentes">Matriz de incidentes y accidentes</span></div>
<div class="req"><span class="req-n">19</span><span data-en="Results review" data-es="Revisión de resultados">Revisión de resultados</span></div>
</div></div>
</div></section>''')

# MIDESAFE inclusions: preserve layout but improve claims and remove conflicting hours.
replace('midesafe-sgm.html','Qué incluye MIDESAFE SGM.','Qué incluye el servicio MIDESAFE SGM.', required=False)
replace('midesafe-sgm.html','What MIDESAFE SGM includes.','What the MIDESAFE SGM service includes.', required=False)
replace('midesafe-sgm.html','El sistema digital','Plataforma MIDESAFE', required=False)
replace('midesafe-sgm.html','The digital system','MIDESAFE platform', required=False)
replace('midesafe-sgm.html','Registro y validación de la información del control volumétrico requerida para el SGM','Gestión de actividades, formatos, registros y evidencia del SGM', required=False)
replace('midesafe-sgm.html','Recording and validation of volumetric-control information required for the SGM','Management of SGM activities, forms, records and evidence', required=False)
replace('midesafe-sgm.html','De 9:00 a 17:00, de lunes a viernes','Asistencia en línea durante el horario de atención ENERSAFE', required=False)
replace('midesafe-sgm.html','From 9:00 to 17:00, Monday to Friday','Online assistance during ENERSAFE service hours', required=False)
replace('midesafe-sgm.html','Verificación de que el soporte cargado sea correcto, con apoyo para corregir','Revisión del soporte documental y seguimiento de observaciones', required=False)
replace('midesafe-sgm.html','Verification that uploaded support is correct, with help to fix it','Review of supporting documentation and follow-up on observations', required=False)
replace('midesafe-sgm.html','Verificación mensual de usuarios, firmas y permisos','Revisión periódica de usuarios, firmas y permisos registrados', required=False)
replace('midesafe-sgm.html','Monthly check of users, signatures and permits','Periodic review of recorded users, signatures and permits', required=False)
replace('midesafe-sgm.html','Sin costo adicional','Incluido', required=False)
replace('midesafe-sgm.html','No extra cost','Included', required=False)
replace('midesafe-sgm.html','Consultas técnicas sobre MIDESAFE, SGM y Control Volumétrico.','Consultas sobre MIDESAFE y el Sistema de Gestión de la Medición.', required=False)
replace('midesafe-sgm.html','Technical questions about MIDESAFE, SGM and volumetric control.','Questions about MIDESAFE and the Measurement Management System.', required=False)

# Metadata / structured data for MIDESAFE.
replace('midesafe-sgm.html','MIDESAFE administra actividades, registros, cálculos y evidencia del Sistema de Gestión de la Medición, con seguimiento técnico especializado.','MIDESAFE concentra actividades, registros, cálculos y evidencia del Sistema de Gestión de la Medición, con seguimiento técnico especializado durante su operación.', required=False)
replace('midesafe-sgm.html','Sistema digital para administrar actividades, registros, cálculos y evidencia del SGM, con seguimiento técnico especializado.','Sistema digital para operar y documentar actividades, registros, cálculos y evidencia del SGM, con seguimiento técnico especializado.', required=False)

# -----------------------------------------------------------------------------
# GASAFE PLUS — correct the SASISOPA sequence and official commercial 18 elements.
# -----------------------------------------------------------------------------
section('gasafe-plus.html',
'<!-- ============================ EL CAMINO DEL SASISOPA ============================ -->',
'<!-- ============================ OPERACIÓN DIARIA / NOM-005 (oscuro) ============================ -->',
'''<section class="section how" id="camino">
<div class="wrap">
<div class="section-head center reveal">
<span class="eyebrow" data-en="SASISOPA process" data-es="Proceso SASISOPA">Proceso SASISOPA</span>
<h2 data-en="Setup, third-party assessment, registration/authorization and continuous implementation." data-es="Conformación, evaluación, registro/autorización e implementación continua.">Conformación, evaluación, registro/autorización e implementación continua.</h2>
<p class="lead" data-en="These are related stages, but they are not equivalent. Having registration or authorization does not, by itself, mean the SASISOPA is implemented." data-es="Son etapas relacionadas, pero no equivalentes. Contar con el registro o la autorización no significa, por sí solo, que el SASISOPA esté implementado." style="margin:0 auto">Son etapas relacionadas, pero no equivalentes. Contar con el registro o la autorización no significa, por sí solo, que el SASISOPA esté implementado.</p>
</div>
<div class="flow"><div class="flow-line"></div>
<div class="flow-step reveal"><div class="fs-ic">01</div><span class="fs-step" data-en="Step 1" data-es="Paso 1">Paso 1</span><h3 data-en="SASISOPA setup" data-es="Conformación del SASISOPA">Conformación del SASISOPA</h3><p data-en="We integrate the System Administration documentation, its 18 elements and the implementation program applicable to the project." data-es="Integramos la documentación del Sistema de Administración, sus 18 elementos y el programa de implementación aplicable al proyecto.">Integramos la documentación del Sistema de Administración, sus 18 elementos y el programa de implementación aplicable al proyecto.</p></div>
<div class="flow-step reveal" data-delay="1"><div class="fs-ic">02</div><span class="fs-step" data-en="Step 2" data-es="Paso 2">Paso 2</span><h3 data-en="Assessment by an Authorized Third Party" data-es="Evaluación por Tercero Autorizado">Evaluación por Tercero Autorizado</h3><p data-en="The Authorized Third Party performs the corresponding assessment and issues the required approving assessment(s) for the registration and authorization process." data-es="El Tercero Autorizado realiza la evaluación correspondiente y emite el o los dictámenes aprobatorios requeridos para el proceso de registro y autorización.">El Tercero Autorizado realiza la evaluación correspondiente y emite el o los dictámenes aprobatorios requeridos para el proceso de registro y autorización.</p></div>
<div class="flow-step reveal" data-delay="2"><div class="fs-ic">03</div><span class="fs-step" data-en="Step 3" data-es="Paso 3">Paso 3</span><h3 data-en="Registration and authorization with ASEA" data-es="Registro y autorización ante la ASEA">Registro y autorización ante la ASEA</h3><p data-en="ENERSAFE supports the documentary process. ASEA grants the System Administration conformity registration and the authorization of the System to be implemented, according to the applicable case." data-es="ENERSAFE acompaña la gestión documental. La ASEA otorga el Registro de la Conformación del Sistema de Administración y la Autorización del Sistema a implementar, según el caso aplicable.">ENERSAFE acompaña la gestión documental. La ASEA otorga el Registro de la Conformación del Sistema de Administración y la Autorización del Sistema a implementar, según el caso aplicable.</p></div>
<div class="flow-step continuous reveal" data-delay="3"><div class="fs-ic">04</div><span class="fs-step cont" data-en="During operation" data-es="Durante la operación">Durante la operación</span><h3 data-en="Continuous implementation with GASAFE Plus" data-es="Implementación continua con GASAFE Plus">Implementación continua con GASAFE Plus</h3><p data-en="GASAFE Plus schedules activities, assigns responsible parties and brings together logs, records, evidence, permits, training, incidents and corrective actions. The ENERSAFE specialist follows up on the recorded information." data-es="GASAFE Plus calendariza actividades, asigna responsables y concentra bitácoras, registros, evidencias, permisos, capacitación, incidentes y acciones correctivas. El especialista ENERSAFE da seguimiento a la información registrada.">GASAFE Plus calendariza actividades, asigna responsables y concentra bitácoras, registros, evidencias, permisos, capacitación, incidentes y acciones correctivas. El especialista ENERSAFE da seguimiento a la información registrada.</p></div>
</div>
<div class="flow-closing reveal"><span data-en="The value of GASAFE Plus begins after authorization: keeping the 18 elements operating, documented and under follow-up throughout the life of the project." data-es="El valor de GASAFE Plus comienza después de la autorización: mantener los 18 elementos en operación, documentados y con seguimiento durante la vida del proyecto.">El valor de GASAFE Plus comienza después de la autorización: mantener los 18 elementos en operación, documentados y con seguimiento durante la vida del proyecto.</span></div>
</div></section>''')

section('gasafe-plus.html',
'<!-- ============================ CUMPLIMIENTO (sellos + 18 elementos) ============================ -->',
'<!-- ============================ QUÉ INCLUYE ============================ -->',
'''<section class="section deps">
<div class="wrap">
<div class="section-head center reveal">
<span class="eyebrow" data-en="Scope" data-es="Alcance">Alcance</span>
<h2 data-en="SASISOPA and NOM-005 are related in operation, but they are different obligations." data-es="SASISOPA y NOM-005 se relacionan en la operación, pero son obligaciones diferentes.">SASISOPA y NOM-005 se relacionan en la operación, pero son obligaciones diferentes.</h2>
<p class="lead" data-en="GASAFE Plus supports SASISOPA setup and continuous implementation, and organizes operational activities and evidence related to NOM-005-ASEA-2016. The NOM retains its own technical scope and annual conformity assessment." data-es="GASAFE Plus apoya la conformación e implementación continua del SASISOPA y organiza actividades y evidencias operativas relacionadas con la NOM-005-ASEA-2016. La NOM conserva su alcance técnico propio y su evaluación anual de conformidad." style="margin:0 auto">GASAFE Plus apoya la conformación e implementación continua del SASISOPA y organiza actividades y evidencias operativas relacionadas con la NOM-005-ASEA-2016. La NOM conserva su alcance técnico propio y su evaluación anual de conformidad.</p>
</div>
<div class="seals reveal" data-delay="1">
<div class="seal"><span class="seal-ic">01</span><span class="seal-t" data-en="SASISOPA" data-es="SASISOPA">SASISOPA</span><span class="seal-d" data-en="18 interrelated elements implemented throughout the life of the project" data-es="18 elementos interrelacionados durante la vida del proyecto">18 elementos interrelacionados durante la vida del proyecto</span></div>
<div class="seal"><span class="seal-ic">02</span><span class="seal-t">NOM-005-ASEA-2016</span><span class="seal-d" data-en="Design, construction, operation and maintenance of service stations" data-es="Diseño, construcción, operación y mantenimiento de Estaciones de Servicio">Diseño, construcción, operación y mantenimiento de Estaciones de Servicio</span></div>
<div class="seal"><span class="seal-ic">03</span><span class="seal-t" data-en="Independent assessments" data-es="Evaluaciones independientes">Evaluaciones independientes</span><span class="seal-d" data-en="Authorized Third Parties and approved verification bodies perform the assessments that correspond" data-es="Terceros Autorizados y figuras aprobadas realizan las evaluaciones que corresponden">Terceros Autorizados y figuras aprobadas realizan las evaluaciones que corresponden</span></div>
</div>
<div class="req-block reveal" data-delay="2">
<h3 class="req-title" data-en="The 18 SASISOPA elements" data-es="Los 18 elementos del SASISOPA">Los 18 elementos del SASISOPA</h3>
<div class="req-grid">
<div class="req"><span class="req-n">01</span><span data-en="Safety and environmental policy" data-es="Política de Seguridad Industrial, Operativa y Protección al Medio Ambiente">Política de Seguridad Industrial, Operativa y Protección al Medio Ambiente</span></div>
<div class="req"><span class="req-n">02</span><span data-en="Physical and operational integrity of facilities" data-es="Integridad física y operativa de las instalaciones">Integridad física y operativa de las instalaciones</span></div>
<div class="req"><span class="req-n">03</span><span data-en="Risk identification and analysis" data-es="Identificación, análisis y evaluación de riesgos">Identificación, análisis y evaluación de riesgos</span></div>
<div class="req"><span class="req-n">04</span><span data-en="Best practices and standards" data-es="Mejores prácticas y estándares">Mejores prácticas y estándares</span></div>
<div class="req"><span class="req-n">05</span><span data-en="Objectives, goals and indicators" data-es="Objetivos, metas e indicadores">Objetivos, metas e indicadores</span></div>
<div class="req"><span class="req-n">06</span><span data-en="Roles and responsibilities" data-es="Funciones y responsabilidades">Funciones y responsabilidades</span></div>
<div class="req"><span class="req-n">07</span><span data-en="Training and instruction" data-es="Capacitación y entrenamiento">Capacitación y entrenamiento</span></div>
<div class="req"><span class="req-n">08</span><span data-en="Control of activities and processes" data-es="Control de actividades y procesos">Control de actividades y procesos</span></div>
<div class="req"><span class="req-n">09</span><span data-en="Communication, dissemination and consultation" data-es="Comunicación, difusión y consulta">Comunicación, difusión y consulta</span></div>
<div class="req"><span class="req-n">10</span><span data-en="Document control" data-es="Control de documentos">Control de documentos</span></div>
<div class="req"><span class="req-n">11</span><span data-en="Contractor provisions" data-es="Disposiciones para contratistas">Disposiciones para contratistas</span></div>
<div class="req"><span class="req-n">12</span><span data-en="Accident prevention and emergency response" data-es="Prevención de accidentes y respuesta a emergencias">Prevención de accidentes y respuesta a emergencias</span></div>
<div class="req"><span class="req-n">13</span><span data-en="Incident and accident registration and investigation" data-es="Registro, investigación y análisis de incidentes y accidentes">Registro, investigación y análisis de incidentes y accidentes</span></div>
<div class="req"><span class="req-n">14</span><span data-en="Monitoring, verification and evaluation" data-es="Monitoreo, verificación y evaluación">Monitoreo, verificación y evaluación</span></div>
<div class="req"><span class="req-n">15</span><span data-en="Audits and follow-up on nonconformities" data-es="Auditorías y seguimiento de incumplimientos">Auditorías y seguimiento de incumplimientos</span></div>
<div class="req"><span class="req-n">16</span><span data-en="Legal and regulatory requirements" data-es="Requisitos legales y normativos">Requisitos legales y normativos</span></div>
<div class="req"><span class="req-n">17</span><span data-en="Results review" data-es="Revisión de resultados">Revisión de resultados</span></div>
<div class="req"><span class="req-n">18</span><span data-en="Periodic performance report" data-es="Informe periódico de desempeño">Informe periódico de desempeño</span></div>
</div></div>
</div></section>''')

replace('gasafe-plus.html','Entrega digital de las carpetas y del dictamen autorizado','Entrega organizada de la documentación y de los dictámenes emitidos', required=False)
replace('gasafe-plus.html','Digital delivery of the files and the authorized assessment','Organized delivery of documentation and issued assessments', required=False)
replace('gasafe-plus.html','Registro y reporte de incidentes y accidentes conforme a la ASEA','Registro y seguimiento de incidentes, accidentes y acciones correctivas', required=False)
replace('gasafe-plus.html','Recording and reporting of incidents and accidents per ASEA','Recording and follow-up of incidents, accidents and corrective actions', required=False)
replace('gasafe-plus.html','Monitoreo constante de tu sistema por nuestro equipo técnico','Revisión de actividades y evidencias registradas por el equipo técnico', required=False)
replace('gasafe-plus.html','Constant monitoring of your system by our technical team','Review of recorded activities and evidence by the technical team', required=False)
replace('gasafe-plus.html','Sin necesidad de contratar personal adicional','Acompañamiento del especialista ENERSAFE durante la implementación', required=False)
replace('gasafe-plus.html','No need to hire additional staff','ENERSAFE specialist support during implementation', required=False)
replace('gasafe-plus.html','Ejemplo ilustrativo','Vista de seguimiento', required=False)
replace('gasafe-plus.html','Illustrative example','Follow-up view', required=False)

# -----------------------------------------------------------------------------
# AUTOCONSUMO — applicability first, then the same SGM service logic.
# -----------------------------------------------------------------------------
section('autoconsumo.html',
'<!-- ============================ ENCABEZADO DE PÁGINA ============================ -->',
'<!-- ============================ EL PROBLEMA QUE RESUELVE ============================ -->',
'''<section class="page-hero">
<div class="ph-mesh"></div><div class="wrap">
<div class="crumbs"><a data-en="Home" data-es="Inicio" href="index.html">Inicio</a> <span>/</span><a data-en="Solutions" data-es="Soluciones" href="servicios.html">Soluciones</a> <span>/</span><span data-en="Self-consumption" data-es="Autoconsumo">Autoconsumo</span></div>
<span class="eyebrow light">MIDESAFE Autoconsumo</span>
<h1 data-en="Digital SGM management &lt;span class='hl'&gt;for self-consumption facilities.&lt;/span&gt;" data-es="Gestión digital del SGM &lt;span class='hl'&gt;para instalaciones de autoconsumo.&lt;/span&gt;">Gestión digital del SGM <span class="hl">para instalaciones de autoconsumo.</span></h1>
<p data-en="For facilities subject to volumetric-control obligations, MIDESAFE organizes SGM activities, measurement information, calculations, evidence and technical follow-up." data-es="Para instalaciones sujetas a obligaciones de controles volumétricos, MIDESAFE organiza las actividades del SGM, información de medición, cálculos, evidencia y seguimiento técnico.">Para instalaciones sujetas a obligaciones de controles volumétricos, MIDESAFE organiza las actividades del SGM, información de medición, cálculos, evidencia y seguimiento técnico.</p>
<div class="ph-norm"><span data-en="Applicability: 2026 RMF rule 2.6.1.2, section VI" data-es="Aplicabilidad: regla 2.6.1.2, fracción VI de la RMF 2026">Aplicabilidad: regla 2.6.1.2, fracción VI de la RMF 2026</span></div>
<div class="ph-actions"><a class="btn btn-primary" data-en="Review my case" data-es="Revisar mi caso" href="https://wa.me/525610360614" rel="noopener" target="_blank">Revisar mi caso</a><a class="btn btn-secondary" data-en="See how MIDESAFE works" data-es="Ver cómo funciona MIDESAFE" href="#como">Ver cómo funciona MIDESAFE</a></div>
</div></section>''')

section('autoconsumo.html',
'<!-- ============================ EL PROBLEMA QUE RESUELVE ============================ -->',
'<!-- ============================ CÓMO FUNCIONA (flujo de 4 pasos) ============================ -->',
'''<section class="section sols">
<div class="wrap"><div class="prob-layout">
<div class="reveal-l"><span class="eyebrow" data-en="Applicability" data-es="Aplicabilidad">Aplicabilidad</span><h2 data-en="Not every self-consumption facility falls under the same assumption." data-es="No toda instalación de autoconsumo se encuentra en el mismo supuesto.">No toda instalación de autoconsumo se encuentra en el mismo supuesto.</h2><p class="lead" data-en="The obligation to keep volumetric controls depends on the permits, type of product, storage and consumption thresholds established in the applicable tax rules. ENERSAFE first reviews whether the facility falls under rule 2.6.1.2, section VI, and from there determines the scope of the SGM." data-es="La obligación de llevar controles volumétricos depende de los permisos, el tipo de producto, el almacenamiento y los umbrales de consumo previstos en las disposiciones fiscales aplicables. ENERSAFE revisa primero si la instalación se encuentra en los supuestos de la regla 2.6.1.2, fracción VI, y a partir de ahí determina el alcance del SGM.">La obligación de llevar controles volumétricos depende de los permisos, el tipo de producto, el almacenamiento y los umbrales de consumo previstos en las disposiciones fiscales aplicables. ENERSAFE revisa primero si la instalación se encuentra en los supuestos de la regla 2.6.1.2, fracción VI, y a partir de ahí determina el alcance del SGM.</p></div>
<div class="reveal-r" data-delay="1"><span class="prob-label" data-en="Cases contemplated by the SAT" data-es="Supuestos que contempla el SAT">Supuestos que contempla el SAT</span><div class="prob-list">
<div class="prob-item"><span class="pi-x">✓</span><span data-en="Facilities operating under an applicable own-use storage or import permit" data-es="Instalaciones que operan al amparo de un permiso aplicable para almacenamiento de usos propios o importación">Instalaciones que operan al amparo de un permiso aplicable para almacenamiento de usos propios o importación</span></div>
<div class="prob-item"><span class="pi-x">✓</span><span data-en="Without such a permit, own-use storage that reaches at least 75,714 liters of petroleum products in one month" data-es="Sin ese permiso, almacenamiento para usos propios que alcance al menos 75,714 litros de petrolíferos en un mes">Sin ese permiso, almacenamiento para usos propios que alcance al menos 75,714 litros de petrolíferos en un mes</span></div>
<div class="prob-item"><span class="pi-x">✓</span><span data-en="Fixed natural-gas reception facilities subject to the annual energy thresholds established in the rule" data-es="Instalaciones fijas para recepción de gas natural sujetas a los umbrales anuales de energía previstos en la regla">Instalaciones fijas para recepción de gas natural sujetas a los umbrales anuales de energía previstos en la regla</span></div>
<div class="prob-item"><span class="pi-x">i</span><span data-en="The specific case must be reviewed before assuming the obligation" data-es="El caso concreto debe revisarse antes de asumir que la obligación aplica">El caso concreto debe revisarse antes de asumir que la obligación aplica</span></div>
</div></div>
</div></div></section>''')

section('autoconsumo.html',
'<!-- ============================ CÓMO FUNCIONA (flujo de 4 pasos) ============================ -->',
'<!-- ============================ CONEXIÓN CON CONTROL VOLUMÉTRICO ============================ -->',
'''<section class="section how" id="como">
<div class="wrap"><div class="section-head center reveal"><span class="eyebrow" data-en="Once applicability is confirmed" data-es="Una vez confirmada la aplicabilidad">Una vez confirmada la aplicabilidad</span><h2 data-en="MIDESAFE applies the SGM service cycle to your self-consumption facility." data-es="MIDESAFE aplica el ciclo de gestión del SGM a tu instalación de autoconsumo.">MIDESAFE aplica el ciclo de gestión del SGM a tu instalación de autoconsumo.</h2></div>
<div class="flow"><div class="flow-line"></div>
<div class="flow-step reveal"><div class="fs-ic">01</div><span class="fs-step" data-en="Step 1" data-es="Paso 1">Paso 1</span><h3 data-en="We configure the facility" data-es="Configuramos la instalación">Configuramos la instalación</h3><p data-en="We integrate the facility, measurement equipment, users, responsible parties, procedures and SGM activities that apply." data-es="Integramos la instalación, equipos de medición, usuarios, responsables, procedimientos y actividades del SGM que correspondan.">Integramos la instalación, equipos de medición, usuarios, responsables, procedimientos y actividades del SGM que correspondan.</p></div>
<div class="flow-step reveal" data-delay="1"><div class="fs-ic">02</div><span class="fs-step" data-en="Step 2" data-es="Paso 2">Paso 2</span><h3 data-en="You operate and document" data-es="Operas y documentas">Operas y documentas</h3><p data-en="MIDESAFE schedules activities and brings together measurement records, forms, supporting documents and evidence generated during operation." data-es="MIDESAFE programa actividades y concentra registros de medición, formatos, soportes y evidencia generados durante la operación.">MIDESAFE programa actividades y concentra registros de medición, formatos, soportes y evidencia generados durante la operación.</p></div>
<div class="flow-step reveal" data-delay="2"><div class="fs-ic">03</div><span class="fs-step" data-en="Step 3" data-es="Paso 3">Paso 3</span><h3 data-en="It calculates and follows up" data-es="Calcula y da seguimiento">Calcula y da seguimiento</h3><p data-en="The tool performs the applicable calculations, controls validities and keeps the documentary history. The ENERSAFE specialist reviews recorded information and observations." data-es="La herramienta realiza los cálculos aplicables, controla vigencias y conserva el historial documental. El especialista ENERSAFE revisa la información registrada y las observaciones.">La herramienta realiza los cálculos aplicables, controla vigencias y conserva el historial documental. El especialista ENERSAFE revisa la información registrada y las observaciones.</p></div>
<div class="flow-step reveal" data-delay="3"><div class="fs-ic">04</div><span class="fs-step" data-en="Step 4" data-es="Paso 4">Paso 4</span><h3 data-en="You prepare the verification" data-es="Preparas la verificación">Preparas la verificación</h3><p data-en="The SGM evidence is organized in an exportable digital file. The independent verification and certificates correspond to the applicable accredited body." data-es="La evidencia del SGM queda organizada en un expediente digital exportable. La verificación independiente y los certificados corresponden a la figura acreditada aplicable.">La evidencia del SGM queda organizada en un expediente digital exportable. La verificación independiente y los certificados corresponden a la figura acreditada aplicable.</p></div>
</div></div></section>''')

section('autoconsumo.html',
'<!-- ============================ CONEXIÓN CON CONTROL VOLUMÉTRICO ============================ -->',
'<!-- ============================ CUMPLIMIENTO CONFORME A LA NORMA ============================ -->',
'''<section class="spec"><div class="spec-mesh"></div><div class="spec-grid-bg"></div><div class="wrap"><div class="spec-inner">
<div class="reveal-l"><span class="eyebrow light" data-en="MIDESAFE Self-consumption" data-es="MIDESAFE Autoconsumo">MIDESAFE Autoconsumo</span><h2 data-en="The same SGM capabilities, adapted to the facility's operation." data-es="Las capacidades del SGM, adaptadas a la operación de la instalación.">Las capacidades del SGM, adaptadas a la operación de la instalación.</h2><p class="lead" data-en="MIDESAFE organizes activities, measurement information, calculations, evidence and follow-up according to the scope that applies to each self-consumption facility." data-es="MIDESAFE organiza actividades, información de medición, cálculos, evidencia y seguimiento de acuerdo con el alcance que aplica a cada instalación de autoconsumo.">MIDESAFE organiza actividades, información de medición, cálculos, evidencia y seguimiento de acuerdo con el alcance que aplica a cada instalación de autoconsumo.</p>
<div class="spec-list"><div class="spec-item"><span class="ic">01</span><span class="tx"><b data-en="Activities and responsible parties" data-es="Actividades y responsables">Actividades y responsables</b><span data-en="Scheduling, evidence and follow-up." data-es="Programación, evidencia y seguimiento.">Programación, evidencia y seguimiento.</span></span></div><div class="spec-item"><span class="ic">02</span><span class="tx"><b data-en="Measurement and calculations" data-es="Medición y cálculos">Medición y cálculos</b><span data-en="Records, balances, uncertainty and metrological control according to scope." data-es="Registros, balances, incertidumbre y control metrológico según el alcance.">Registros, balances, incertidumbre y control metrológico según el alcance.</span></span></div><div class="spec-item"><span class="ic">03</span><span class="tx"><b data-en="Digital evidence" data-es="Evidencia digital">Evidencia digital</b><span data-en="Documentary history and exportable file for review." data-es="Historial documental y expediente exportable para revisión.">Historial documental y expediente exportable para revisión.</span></span></div></div></div>
<div class="reveal-r" data-delay="1"><div class="spec-panel"><p class="spec-panel-intro" data-en="Before implementation:" data-es="Antes de implementar:">Antes de implementar:</p><div class="sp-body"><div class="sp-row"><span class="sp-check ok">1</span><span class="lbl" data-en="Applicability" data-es="Aplicabilidad">Aplicabilidad</span><span class="val val-ok" data-en="Reviewed" data-es="Revisada">Revisada</span></div><div class="sp-row"><span class="sp-check ok">2</span><span class="lbl" data-en="Facility scope" data-es="Alcance de la instalación">Alcance de la instalación</span><span class="val val-ok" data-en="Defined" data-es="Definido">Definido</span></div><div class="sp-row"><span class="sp-check warn">3</span><span class="lbl" data-en="SGM setup" data-es="Configuración SGM">Configuración SGM</span><span class="val val-warn" data-en="Starts" data-es="Inicia">Inicia</span></div></div><div class="sp-foot"><span data-en="The service starts by confirming the facility's regulatory assumption, not by assuming that every self-consumption case is identical." data-es="El servicio comienza confirmando el supuesto regulatorio de la instalación, no asumiendo que todos los casos de autoconsumo son iguales.">El servicio comienza confirmando el supuesto regulatorio de la instalación, no asumiendo que todos los casos de autoconsumo son iguales.</span></div></div></div>
</div></div></section>''')

# -----------------------------------------------------------------------------
# SERVICES — authority map and claims.
# -----------------------------------------------------------------------------
replace('servicios.html','Your service station answers to several federal authorities, each with its own obligations, dates and formats. ENERSAFE manages them in a single relationship, with the tools and engineers that sustain them.','MIDESAFE and GASAFE Plus address recurring SGM and SASISOPA obligations; ENERSAFE complements them with assessments, studies, filings and specialized regulatory services.', required=False)
replace('servicios.html','MIDESAFE y GASAFE Plus cubren obligaciones recurrentes de medición y SASISOPA; el equipo de ENERSAFE complementa ese trabajo con gestiones, dictámenes, estudios y servicios ante otras autoridades.','MIDESAFE y GASAFE Plus atienden obligaciones recurrentes del SGM y SASISOPA; ENERSAFE complementa ese trabajo con dictámenes, estudios, trámites y servicios regulatorios especializados.', required=False)
replace('servicios.html','<div class="pstat"><span class="pstat-n">0</span><span class="pstat-l" data-en="specialized staff you need to hire" data-es="personal especializado que necesitas contratar">personal especializado que necesitas contratar</span></div>','<div class="pstat"><span class="pstat-n">1</span><span class="pstat-l" data-en="ENERSAFE team to coordinate the contracted scope" data-es="equipo ENERSAFE para coordinar el alcance contratado">equipo ENERSAFE para coordinar el alcance contratado</span></div>', required=False)
replace('servicios.html','Services by authority and obligation.','Services by regulatory area and authority.', required=False)
replace('servicios.html','Servicios por autoridad y obligación.','Servicios por frente regulatorio y autoridad.', required=False)
replace('servicios.html','<!-- ASEA -->','<!-- ASEA SEGURIDAD Y OPERACION -->', required=False)
replace('servicios.html','<span class="acc-titles"><span class="acc-name">ASEA</span><span class="acc-sub" data-en="Agency for Safety, Energy and Environment" data-es="Agencia de Seguridad, Energía y Ambiente">Agencia de Seguridad, Energía y Ambiente</span></span>','<span class="acc-titles"><span class="acc-name">ASEA · Seguridad y operación</span><span class="acc-sub" data-en="Agency for Safety, Energy and Environment" data-es="Agencia de Seguridad, Energía y Ambiente">Agencia de Seguridad, Energía y Ambiente</span></span>', required=False, count=1)
replace('servicios.html','<!-- SEMARNAT -->','<!-- ASEA AMBIENTE Y RESIDUOS -->', required=False)
replace('servicios.html','<span class="acc-titles"><span class="acc-name">SEMARNAT</span><span class="acc-sub" data-en="Ministry of Environment and Natural Resources" data-es="Secretaría de Medio Ambiente y Recursos Naturales">Secretaría de Medio Ambiente y Recursos Naturales</span></span>','<span class="acc-titles"><span class="acc-name">ASEA · Ambiente y residuos</span><span class="acc-sub" data-en="Environmental matters for the hydrocarbons sector" data-es="Materia ambiental del Sector Hidrocarburos">Materia ambiental del Sector Hidrocarburos</span></span>', required=False)
replace('servicios.html','Environmental impacts, waste records, operating certificates and change procedures with the environmental authority.','Environmental impact, air-emissions filings, annual operating certificate and waste records for hydrocarbons-sector activities.', required=False)
replace('servicios.html','Impactos ambientales, registros de residuos, cédulas de operación y gestiones de cambio ante la autoridad ambiental.','Impacto ambiental, trámites de atmósfera, Cédula de Operación Anual y registros de residuos para actividades del Sector Hidrocarburos.', required=False)
replace('servicios.html','Cédula de Operación Anual (ordinaria y extraordinaria)','Cédula de Operación Anual del Sector Hidrocarburos', required=False)
replace('servicios.html','Annual Operating Certificate (ordinary and extraordinary)','Annual Operating Certificate for the Hydrocarbons Sector', required=False)

# -----------------------------------------------------------------------------
# ABOUT — remove unsupported counters and vague certification language.
# -----------------------------------------------------------------------------
replace('nosotros.html','Sistemas desarrollados bajo estándares nacionales e internacionales aplicables al sector','Tecnología aplicada, especialistas técnicos y servicios regulatorios', required=False)
replace('nosotros.html','Systems developed under applicable national and international standards for the sector','Applied technology, technical specialists and regulatory services', required=False)
replace('nosotros.html','Sistemas digitales propios, especialistas técnicos y servicios regulatorios.','Tecnología aplicada, especialistas técnicos y servicios regulatorios.', required=False)
replace('nosotros.html','Proprietary digital systems, technical specialists and regulatory services.','Applied technology, technical specialists and regulatory services.', required=False)
replace('nosotros.html','<div class="ab-stat"><span class="ab-n">32</span><span class="ab-l" data-en="States with stations served" data-es="Estados de la República con estaciones atendidas">Estados de la República con estaciones atendidas</span></div>','<div class="ab-stat"><span class="ab-n" data-en="National" data-es="Nacional">Nacional</span><span class="ab-l" data-en="Service for stations in Mexico" data-es="Atención a Estaciones de Servicio en México">Atención a Estaciones de Servicio en México</span></div>', required=False)
replace('nosotros.html','<div class="ab-stat"><span class="ab-n" data-en="Daily" data-es="A diario">A diario</span><span class="ab-l" data-en="Follow-up of recorded activities and evidence" data-es="Seguimiento de actividades y evidencias registradas">Seguimiento de actividades y evidencias registradas</span></div>','<div class="ab-stat"><span class="ab-n" data-en="Follow-up" data-es="Seguimiento">Seguimiento</span><span class="ab-l" data-en="Review of recorded activities and evidence" data-es="Revisión de actividades y evidencias registradas">Revisión de actividades y evidencias registradas</span></div>', required=False)
replace('nosotros.html','<div class="ab-stat"><span class="ab-n">8–17 h</span><span class="ab-l" data-en="Online technical assistance, Monday to Friday" data-es="Asistencia técnica en linea, de lunes a viernes">Asistencia técnica en linea, de lunes a viernes</span></div>','<div class="ab-stat"><span class="ab-n" data-en="Online" data-es="En línea">En línea</span><span class="ab-l" data-en="Technical assistance during the service" data-es="Asistencia técnica durante el servicio">Asistencia técnica durante el servicio</span></div>', required=False)
replace('nosotros.html','<div class="ab-stat"><span class="ab-n" data-en="8 authorities" data-es="8 autoridades">8 autoridades</span><span class="ab-l" data-en="SAT, ASEA, CNE, STPS, PROFECO, environmental authorities and more" data-es="SAT, ASEA, CNE, STPS, PROFECO, autoridades ambientales y más">SAT, ASEA, CNE, STPS, PROFECO, autoridades ambientales y más</span></div>','<div class="ab-stat"><span class="ab-n" data-en="Regulatory" data-es="Regulatorio">Regulatorio</span><span class="ab-l" data-en="SAT, ASEA, CNE, STPS and other applicable fronts" data-es="SAT, ASEA, CNE, STPS y otros frentes aplicables">SAT, ASEA, CNE, STPS y otros frentes aplicables</span></div>', required=False)

# -----------------------------------------------------------------------------
# CONTACT — use technically clearer lead qualification.
# -----------------------------------------------------------------------------
replace('contacto.html','¿Qué te preocupa más en este momento?','¿Qué necesitas revisar?', required=False)
replace('contacto.html','What concerns you most right now?','What do you need to review?', required=False)
replace('contacto.html','Mi Certificado Anual de Cumplimiento (SAT)','SGM y controles volumétricos (SAT)', required=False)
replace('contacto.html','Tus datos se usan solo para responderte. Sin spam.','Usaremos tus datos únicamente para atender tu solicitud. Consulta nuestro Aviso de Privacidad.', required=False)
replace('contacto.html','Your data is used only to reply to you. No spam.','We will use your data only to respond to your request. See our Privacy Notice.', required=False)

# -----------------------------------------------------------------------------
# CONSULTATIONS — make LA + official-source corrections visible and dated.
# -----------------------------------------------------------------------------
replace('preguntas-frecuentes.html','MIDESAFE, SGM y SAT; GASAFE Plus, SASISOPA y NOM-005; además de temas ambientales, residuos y permisos. Organizado por tema para localizar rápido la consulta que necesitas.','MIDESAFE, SGM y SAT; GASAFE Plus, SASISOPA y NOM-005; además de temas ambientales, residuos y permisos. Las respuestas parten de la revisión técnica de ENERSAFE y se contrastan con las disposiciones oficiales vigentes.', required=False)
replace('preguntas-frecuentes.html','Answers about MIDESAFE, GASAFE Plus and other regulatory fronts, using the terminology applied by ENERSAFE\'s technical team.','Answers about MIDESAFE, GASAFE Plus and other regulatory fronts, based on ENERSAFE technical review and checked against current official provisions.', required=False)
# Insert update stamp after hero paragraph if not already present.
p, s = load('preguntas-frecuentes.html')
if 'Última actualización · 10 de septiembre de 2026' not in s:
    needle = 'Las respuestas parten de la revisión técnica de ENERSAFE y se contrastan con las disposiciones oficiales vigentes.</p>'
    if needle not in s:
        raise RuntimeError('preguntas-frecuentes.html: hero paragraph target missing')
    s = s.replace(needle, needle + '\n<div class="ph-norm"><span data-en="Last updated · September 10, 2026" data-es="Última actualización · 10 de septiembre de 2026">Última actualización · 10 de septiembre de 2026</span></div>', 1)
    save('preguntas-frecuentes.html', s)
replace('preguntas-frecuentes.html','La COA aplica a los Regulados del Sector Hidrocarburos que se encuentren en los supuestos establecidos por la autoridad ambiental competente','La COA del Sector Hidrocarburos se presenta ante la ASEA cuando el Regulado se encuentra en los supuestos aplicables', required=False)
replace('preguntas-frecuentes.html','The COA applies to Hydrocarbons Sector regulated entities that fall under the assumptions established by the competent environmental authority','The Hydrocarbons Sector COA is filed with ASEA when the regulated entity falls under the applicable assumptions', required=False)
replace('preguntas-frecuentes.html','Son categorías distintas y cada una tiene registros y obligaciones propios. El trámite depende del tipo de residuo, la cantidad generada y la categoría del generador. ENERSAFE gestiona los registros y trámites relacionados que correspondan dentro del alcance contratado.','Son categorías distintas y cada una tiene registros y obligaciones propios ante la ASEA para actividades del Sector Hidrocarburos. El trámite depende del tipo de residuo, la cantidad generada y la categoría del generador. ENERSAFE gestiona los registros y trámites relacionados que correspondan dentro del alcance contratado.', required=False)
replace('preguntas-frecuentes.html','They are different categories and each has its own registrations and obligations. The filing depends on the type of waste, the amount generated and the generator category. ENERSAFE manages the applicable registrations and related filings within the contracted scope.','They are different categories and each has its own registrations and obligations with ASEA for Hydrocarbons Sector activities. The filing depends on the type of waste, the amount generated and the generator category. ENERSAFE manages the applicable registrations and related filings within the contracted scope.', required=False)

# -----------------------------------------------------------------------------
# HOME — small consistency fixes based on the audited internal pages.
# -----------------------------------------------------------------------------
replace('index.html','Control de la medición','SGM y controles volumétricos', required=False)
replace('index.html','Measurement control','SGM and volumetric controls', required=False)
replace('index.html','MIDESAFE y GASAFE Plus organizan actividades, responsables, evidencias y reportes. Los servicios especializados de ENERSAFE atienden las demás obligaciones regulatorias.','MIDESAFE y GASAFE Plus organizan actividades, responsables, evidencias y reportes en sus respectivos alcances. Los servicios especializados de ENERSAFE atienden trámites, estudios, dictámenes y otras obligaciones regulatorias.', required=False)
replace('index.html','MIDESAFE SGM and GASAFE Plus organize activities, responsible parties, evidence and reports. ENERSAFE specialized services address the remaining regulatory obligations.','MIDESAFE SGM and GASAFE Plus organize activities, responsible parties, evidence and reports within their respective scopes. ENERSAFE specialized services address filings, studies, assessments and other regulatory obligations.', required=False)

# -----------------------------------------------------------------------------
# Clean legacy English/Spanish claims that must not survive hidden in data attrs.
# -----------------------------------------------------------------------------
for path in ['index.html','midesafe-sgm.html','gasafe-plus.html','autoconsumo.html','servicios.html','nosotros.html','contacto.html','preguntas-frecuentes.html']:
    replace(path,'Nothing is left to interpretation.','The applicable scope must be reviewed for each case.', required=False)
    replace(path,'sin captura manual','con gestión digital', required=False)
    replace(path,'without manual steps','with digital management', required=False)
    replace(path,'No need to hire additional staff','Specialized ENERSAFE follow-up included', required=False)
    replace(path,'Sin necesidad de contratar personal adicional','Seguimiento especializado ENERSAFE incluido', required=False)

# -----------------------------------------------------------------------------
# Validation.
# -----------------------------------------------------------------------------
all_html = '\n'.join((ROOT / f).read_text(encoding='utf-8') for f in ['index.html','midesafe-sgm.html','gasafe-plus.html','autoconsumo.html','servicios.html','nosotros.html','contacto.html','preguntas-frecuentes.html'])
for banned in ['ControlGAS','sostiene el servicio','Sistemas propios','El SGM que el SAT exige','sin captura manual','Nothing is left to interpretation','No need to hire additional staff','Sin necesidad de contratar personal adicional']:
    if banned.lower() in all_html.lower():
        raise RuntimeError(f'Banned legacy phrase remains: {banned}')

checks = {
    'midesafe-sgm.html': ['Cumplimiento digital del SGM','Configuramos el SGM','Operas y documentas','Preparas la verificación','Lo que MIDESAFE administra durante la operación del SGM','Dónde se ubica el SGM dentro del cumplimiento de controles volumétricos'],
    'gasafe-plus.html': ['Conformación del SASISOPA','Evaluación por Tercero Autorizado','Registro y autorización ante la ASEA','Integridad física y operativa de las instalaciones','Mejores prácticas y estándares','Informe periódico de desempeño'],
    'autoconsumo.html': ['No toda instalación de autoconsumo se encuentra en el mismo supuesto','75,714 litros','regla 2.6.1.2, fracción VI'],
    'servicios.html': ['ASEA · Seguridad y operación','ASEA · Ambiente y residuos','Cédula de Operación Anual del Sector Hidrocarburos'],
    'preguntas-frecuentes.html': ['Última actualización · 10 de septiembre de 2026'],
}
for path, needles in checks.items():
    s = (ROOT / path).read_text(encoding='utf-8')
    for needle in needles:
        if needle not in s:
            raise RuntimeError(f'{path}: validation missing {needle}')

for path in ['midesafe-sgm.html','gasafe-plus.html','autoconsumo.html','servicios.html','nosotros.html','contacto.html','preguntas-frecuentes.html']:
    if 'href="#alertas"' in (ROOT/path).read_text(encoding='utf-8'):
        raise RuntimeError(f'{path}: broken #alertas link remains')

print('Changed:', ', '.join(changed))
print('V4 audit validation OK')
