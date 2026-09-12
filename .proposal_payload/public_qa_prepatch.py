from pathlib import Path

p = Path('nosotros.html')
s = p.read_text(encoding='utf-8')

repls = {
    'data-en="Why ENERSAFE" data-es="Por que ENERSAFE">Por que ENERSAFE':
        'data-en="ENERSAFE follow-up" data-es="Seguimiento ENERSAFE">Seguimiento ENERSAFE',
    'data-en="National and international standards" data-es="Estándares nacionales e internacionales">Estándares nacionales e internacionales':
        'data-en="Technical and regulatory criteria" data-es="Criterio técnico y regulatorio">Criterio técnico y regulatorio',
    'data-en="Our systems are developed under the standards that apply to the sector, ensuring process standardization and continuous improvement." data-es="Nuestros sistemas se desarrollan bajo los estándares que aplican al sector, asegurando la estandarización del proceso y la mejora continua.">Nuestros sistemas se desarrollan bajo los estándares que aplican al sector, asegurando la estandarización del proceso y la mejora continua.':
        'data-en="Systems and services consider the provisions, standards and criteria applicable to each scope." data-es="Los sistemas y servicios consideran las disposiciones, normas y criterios aplicables a cada alcance.">Los sistemas y servicios consideran las disposiciones, normas y criterios aplicables a cada alcance.',
    'data-en="Support every day" data-es="Acompañamiento todos los días">Acompañamiento todos los días':
        'data-en="Review and follow-up" data-es="Revisión y seguimiento">Revisión y seguimiento',
    'data-en="Daily review of scheduled activities and verification that each uploaded record is correct, with help to fix it." data-es="Revisión diaria de las actividades programadas y verificacion de que cada soporte cargado sea correcto, con apoyo para corregir.">Revisión diaria de las actividades programadas y verificacion de que cada soporte cargado sea correcto, con apoyo para corregir.':
        'data-en="The technical team reviews scheduled activities and recorded evidence and follows up on observations and pending items." data-es="El equipo técnico revisa las actividades programadas y la evidencia registrada, y da seguimiento a observaciones y pendientes.">El equipo técnico revisa las actividades programadas y la evidencia registrada, y da seguimiento a observaciones y pendientes.',
    'data-en="One sector, no distractions" data-es="Un solo sector, sin distracciones">Un solo sector, sin distracciones':
        'data-en="Sector specialization" data-es="Especialización sectorial">Especialización sectorial',
    'data-en="We work exclusively with gasoline and diesel service stations in the Hydrocarbons Sector." data-es="Nos dedicamos exclusivamente a las Estaciones de Servicio de gasolina y diésel del Sector de Hidrocarburos.">Nos dedicamos exclusivamente a las Estaciones de Servicio de gasolina y diésel del Sector de Hidrocarburos.':
        'data-en="Our work focuses on regulatory obligations for Service Stations and other applicable hydrocarbon-sector facilities." data-es="Nuestro trabajo se concentra en las obligaciones regulatorias de Estaciones de Servicio y otras instalaciones aplicables del Sector de Hidrocarburos.">Nuestro trabajo se concentra en las obligaciones regulatorias de Estaciones de Servicio y otras instalaciones aplicables del Sector de Hidrocarburos.'
}

for old, new in repls.items():
    if old not in s:
        raise RuntimeError(f'Nosotros prepatch target not found: {old[:100]}')
    s = s.replace(old, new)

p.write_text(s, encoding='utf-8')
print('Nosotros editorial prepatch applied')
