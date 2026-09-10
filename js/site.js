/* =================================================================
   ENERSAFE · Comportamiento del sitio (v3)
   ================================================================= */

/* —— Índice del buscador (editable) —— */
const SEARCH_INDEX=[
  {tag:"MIDESAFE SGM · SAT",title:"MIDESAFE SGM",snippet:"Gestión digital del SGM, con actividades, cálculos, evidencia y seguimiento técnico. Compatible con distintos controles volumétricos e integración específica con ControlGAS®.",tags:"sat sgm medicion control volumetrico controlgas anexos 21 22 23 incertidumbre balance metrologia",url:"midesafe-sgm.html"},
  {tag:"Autoconsumo · SAT",title:"MIDESAFE Autoconsumo",snippet:"Gestión digital del SGM para instalaciones de autoconsumo, con actividades, medición, cálculos, evidencia y seguimiento técnico.",tags:"autoconsumo sat sgm medicion instalacion",url:"autoconsumo.html"},
  {tag:"GASAFE Plus · ASEA",title:"GASAFE Plus",snippet:"Sistema digital para la implementación continua del SASISOPA y el seguimiento de actividades y evidencias operativas relacionadas con la NOM-005-ASEA-2016.",tags:"asea sasisopa nom-005 nom005 gasafe especialista tercero autorizado seguridad medio ambiente 18 elementos",url:"gasafe-plus.html"},
  {tag:"Cumplimiento · ASEA",title:"Auditorías SASISOPA",snippet:"Auditorías internas y externas del SASISOPA, dictaminación e informes de desempeño.",tags:"asea sasisopa auditoria interna externa dictaminacion informe desempeno semestral conclusion",url:"servicios.html"},
  {tag:"Cumplimiento · SAT",title:"Auditorías SGM",snippet:"Auditorías presenciales y remotas del Sistema de Gestión de la Medición.",tags:"sat sgm auditoria presencial remota medicion",url:"servicios.html"},
  {tag:"Cumplimiento · SEMARNAT",title:"Registros ambientales y COA",snippet:"RME, RP, Cédula de Operación Anual, análisis de riesgo, informe preventivo e impacto social.",tags:"semarnat rme rp residuos peligrosos manejo especial coa cedula operacion anual analisis de riesgo informe preventivo impacto social monitoreo ambiental pre planos",url:"servicios.html"},
  {tag:"Cumplimiento · Municipal",title:"Licencias y planos",snippet:"Licencia de funcionamiento, elaboración de planos y programa de respuesta a emergencias.",tags:"municipal licencia funcionamiento planos pre programa respuesta emergencias",url:"servicios.html"},
  {tag:"STPS",title:"NOM-035-STPS",snippet:"Cumplimiento de la normativa laboral aplicable, activable dentro de GASAFE Plus.",tags:"stps nom-035 nom035 riesgo psicosocial laboral",url:"servicios.html"},
  {tag:"Empresa",title:"Nosotros",snippet:"Especialistas en cumplimiento regulatorio para el Sector de Hidrocarburos.",tags:"nosotros empresa enersafe hidrocarburos quienes somos",url:"nosotros.html"},
  {tag:"Contacto",title:"Contacto",snippet:"Av. Homero 1422, Polanco, CDMX. Habla con un asesor ENERSAFE.",tags:"contacto homero polanco cdmx telefono correo asesor mapa whatsapp",url:"contacto.html"}
];

/* —— Testimonios (9) — edítalos aquí. ES y EN —— */
const TESTIMONIOS=[
  {ini:"SP",nom:"Servicio Pontellas",sub:"S.A. de C.V.",
   es:"Se nos hace muy práctica: está bien estructurada, completa, fácil y entendible. Agradecemos el trato y la atención que nos brindan.",
   en:"We find it very practical: well structured, complete, easy to use and understandable. We appreciate the service and attention provided."},
  {ini:"BT",nom:"BP Turpial",sub:"Estación de Servicio",
   es:"Reconocemos el apoyo oportuno en el manejo del portal y la asistencia puntual del técnico para seguir cumpliendo con este requisito.",
   en:"We recognize the timely support in managing the portal and the technician's prompt assistance in continuing to meet this requirement."},
  {ini:"BL",nom:"BP Servicio Libramiento Norte",sub:"Estación de Servicio",
   es:"La atención y asistencia han sido muy buenas, especialmente en el monitoreo.",
   en:"The attention and assistance have been very good, especially the monitoring."},
  {ini:"BQ",nom:"BP Bernardo Quintana",sub:"Estación de Servicio",
   es:"Agradecemos el apoyo, las recomendaciones y el tiempo que dedican a acompañarnos en el uso de la herramienta.",
   en:"We appreciate the support, recommendations and time dedicated to helping us use the tool."},
  {ini:"BC",nom:"BP La Calma",sub:"Estación de Servicio",
   es:"La plataforma es de mucha utilidad, junto con el apoyo y seguimiento de sus técnicos.",
   en:"The platform is very useful, together with the support and follow-up provided by the technical team."},
  {ini:"JB",nom:"BP JB Lobos",sub:"Estación de Servicio",
   es:"Llevamos el portal en orden de acuerdo con las actividades asignadas y agradecemos al técnico especialista que nos apoya y orienta.",
   en:"We keep the portal organized according to assigned activities and appreciate the specialist technician who supports and guides us."},
  {ini:"LM",nom:"BP López Mateos",sub:"Estación de Servicio",
   es:"Agradecemos el apoyo de las capacitaciones y la atención brindada.",
   en:"We appreciate the training support and the attention provided."}
];

/* —— Tema —— */
(function(){if(localStorage.getItem('enersafe-theme')==='dark')document.documentElement.setAttribute('data-theme','dark');})();
function toggleTheme(){
  const d=document.documentElement.getAttribute('data-theme')==='dark';
  if(d){document.documentElement.removeAttribute('data-theme');localStorage.setItem('enersafe-theme','light');}
  else{document.documentElement.setAttribute('data-theme','dark');localStorage.setItem('enersafe-theme','dark');}
  syncThemeIcon();
}
function syncThemeIcon(){
  const d=document.documentElement.getAttribute('data-theme')==='dark';
  const s=document.querySelector('.ic-sun'),m=document.querySelector('.ic-moon');
  if(s&&m){s.style.display=d?'none':'block';m.style.display=d?'block':'none';}
}

/* —— Idioma —— */
(function(){if(localStorage.getItem('enersafe-lang')==='en')document.documentElement.setAttribute('data-lang','en');})();
function toggleLang(){
  const en=document.documentElement.getAttribute('data-lang')==='en';
  if(en){document.documentElement.removeAttribute('data-lang');localStorage.setItem('enersafe-lang','es');}
  else{document.documentElement.setAttribute('data-lang','en');localStorage.setItem('enersafe-lang','en');}
  applyLang();renderTestimonios();
}
function applyLang(){
  const en=document.documentElement.getAttribute('data-lang')==='en';
  document.querySelectorAll('[data-es]').forEach(el=>{
    const v=en?el.getAttribute('data-en'):el.getAttribute('data-es');
    if(v===null)return;
    if(el.hasAttribute('data-attr')){el.setAttribute(el.getAttribute('data-attr'),v);return;}
    /* si el elemento empieza con un icono SVG (botones), lo preservamos
       y solo reemplazamos el texto — antes innerHTML borraba el icono */
    const firstEl=el.firstElementChild;
    if(firstEl&&firstEl.tagName&&firstEl.tagName.toLowerCase()==='svg'){
      const icon=firstEl.cloneNode(true);
      el.textContent='';
      el.appendChild(icon);
      el.appendChild(document.createTextNode(' '+v));
    } else {
      el.innerHTML=v;
    }
  });
  const lc=document.querySelector('.lang-code');if(lc)lc.textContent=en?'ES':'EN';
  document.documentElement.setAttribute('lang',en?'en':'es');
}

/* —— Testimonios carrusel —— */
let tIdx=0;
function renderTestimonios(){
  const track=document.getElementById('testiTrack');if(!track)return;
  const en=document.documentElement.getAttribute('data-lang')==='en';
  const star='<svg viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15 9 22 9 17 14 19 21 12 17 5 21 7 14 2 9 9 9"/></svg>';
  track.innerHTML=TESTIMONIOS.map(t=>`
    <div class="tslide">
      <div class="tcard-big">
        <svg class="quote-ic" viewBox="0 0 24 24" fill="currentColor"><path d="M10 7L8 11h3v6H5v-6l2-4h3zm9 0l-2 4h3v6h-6v-6l2-4h3z"/></svg>
        <div class="stars">${star.repeat(5)}</div>
        <p class="quote">${en?t.en:t.es}</p>
        <div class="who"><span class="av">${t.ini}</span><span><span class="who-t">${t.nom}</span><span class="who-d">${t.sub}</span></span></div>
      </div>
    </div>`).join('');
  const dots=document.getElementById('testiDots');
  if(dots)dots.innerHTML=TESTIMONIOS.map((_,i)=>`<button class="td-dot${i===0?' active':''}" onclick="testiGo(${i})" aria-label="${i+1}"></button>`).join('');
  testiGo(tIdx);
}
function testiGo(i){
  const track=document.getElementById('testiTrack');if(!track)return;
  tIdx=(i+TESTIMONIOS.length)%TESTIMONIOS.length;
  track.style.transform=`translateX(-${tIdx*100}%)`;
  document.querySelectorAll('.td-dot').forEach((d,k)=>d.classList.toggle('active',k===tIdx));
}
function testiNext(){testiGo(tIdx+1);restartTesti();}
function testiPrev(){testiGo(tIdx-1);restartTesti();}
let testiTimer=null;
function restartTesti(){if(testiTimer)clearInterval(testiTimer);testiTimer=setInterval(()=>testiGo(tIdx+1),9000);}

/* —— Nav móvil —— */
function toggleMobileNav(){document.querySelector('.mobile-nav').classList.toggle('open');}

/* —— Dropdown (click, con cierre al hacer click afuera) —— */
function toggleDrop(e){e.stopPropagation();document.getElementById('navDrop').classList.toggle('open');}
document.addEventListener('click',e=>{const d=document.getElementById('navDrop');if(d&&!d.contains(e.target))d.classList.remove('open');});

/* —— Buscador —— */
function openSearch(){const o=document.getElementById('searchOverlay');if(!o)return;o.classList.add('open');setTimeout(()=>document.getElementById('searchInput').focus(),50);runSearch('');}
function closeSearch(){const o=document.getElementById('searchOverlay');if(o)o.classList.remove('open');}
/* acordeón del directorio de cumplimiento (página servicios) */
function toggleAcc(btn){const item=btn.closest('.acc-item');if(!item)return;const open=item.classList.toggle('open');btn.setAttribute('aria-expanded',open?'true':'false');}
function esc(s){return s.replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function hl(t,q){const e=esc(t);if(!q)return e;return e.replace(new RegExp('('+q.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig'),'<mark>$1</mark>');}
function runSearch(q){
  const r=document.getElementById('searchResults');if(!r)return;q=q.trim().toLowerCase();
  if(!q){r.innerHTML='<div class="search-hint">Busca por dependencia (ASEA, SAT, SEMARNAT...), producto o trámite.</div>';return;}
  const m=SEARCH_INDEX.filter(i=>(i.title+' '+i.tags+' '+i.snippet).toLowerCase().includes(q)).slice(0,8);
  if(!m.length){r.innerHTML='<div class="search-empty">Sin resultados para "'+esc(q)+'".</div>';return;}
  r.innerHTML=m.map(i=>`<a class="search-result" href="${i.url}"><div class="sr-tag">${esc(i.tag)}</div><div class="sr-title">${hl(i.title,q)}</div><div class="sr-snippet">${hl(i.snippet,q)}</div></a>`).join('');
}

/* —— Slider (11s) —— */
let cur=0,timer=null;const SLIDE_MS=11000;
function show(i){const s=document.querySelectorAll('.slide'),d=document.querySelectorAll('.s-dot');if(!s.length)return;cur=(i+s.length)%s.length;s.forEach((x,k)=>x.classList.toggle('active',k===cur));d.forEach((x,k)=>x.classList.toggle('active',k===cur));}
function nextSlide(){show(cur+1);restart();}
function prevSlide(){show(cur-1);restart();}
function goSlide(i){show(i);restart();}
function restart(){if(timer)clearInterval(timer);timer=setInterval(()=>show(cur+1),SLIDE_MS);
  document.querySelectorAll('.s-dot').forEach((d,i)=>{const n=d.cloneNode(true);d.parentNode.replaceChild(n,d);});
  document.querySelectorAll('.s-dot').forEach((d,i)=>{d.classList.toggle('active',i===cur);d.onclick=()=>goSlide(i);});
}

/* —— Spotlight cards —— */
function bindSpotlight(){
  document.querySelectorAll('.pcard').forEach(card=>{
    card.addEventListener('mousemove',e=>{
      const r=card.getBoundingClientRect();const inner=card.querySelector('.pcard-inner');
      if(inner){inner.style.setProperty('--mx',(e.clientX-r.left)+'px');inner.style.setProperty('--my',(e.clientY-r.top)+'px');}
    });
  });
}

/* —— Reveal observer (global, para reusar con testimonios) —— */
const revealObserver=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');revealObserver.unobserve(e.target);}})},{threshold:.14});

/* —— Init —— */
document.addEventListener('DOMContentLoaded',()=>{
  syncThemeIcon();
  applyLang();
  renderTestimonios();
  restartTesti();
  bindSpotlight();

  document.querySelectorAll('.s-dot').forEach((d,i)=>{d.onclick=()=>goSlide(i);});

  const si=document.getElementById('searchInput');
  if(si)si.addEventListener('input',e=>runSearch(e.target.value));
  const so=document.getElementById('searchOverlay');
  if(so)so.addEventListener('click',e=>{if(e.target.id==='searchOverlay')closeSearch();});
  document.addEventListener('keydown',e=>{if(e.key==='Escape')closeSearch();if((e.ctrlKey||e.metaKey)&&e.key==='k'){e.preventDefault();openSearch();}});

  if(document.querySelector('.slide'))restart();

  document.querySelectorAll('.reveal,.reveal-l,.reveal-r,.reveal-scale').forEach(el=>revealObserver.observe(el));

  /* contadores */
  const cio=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){const el=e.target;const target=parseInt(el.dataset.count);let n=0;const step=Math.max(1,Math.round(target/32));const t=setInterval(()=>{n+=step;if(n>=target){n=target;clearInterval(t);}el.textContent=n;},26);cio.unobserve(el);}})},{threshold:.5});
  document.querySelectorAll('[data-count]').forEach(el=>cio.observe(el));

  /* header sombra al hacer scroll */
  const hd=document.getElementById('siteHeader');
  if(hd){window.addEventListener('scroll',()=>{hd.classList.toggle('scrolled',window.scrollY>10);});}

  /* formularios Formspree */
  function wireForm(formId,msgId,okEs,okEn){
    const f=document.getElementById(formId);if(!f)return;
    f.addEventListener('submit',function(e){
      e.preventDefault();const msg=document.getElementById(msgId);
      const en=document.documentElement.getAttribute('data-lang')==='en';
      fetch(f.action,{method:'POST',body:new FormData(f),headers:{'Accept':'application/json'}})
      .then(r=>{if(r.ok){msg.textContent=en?okEn:okEs;msg.style.color='var(--lime-bright)';f.reset();}else{msg.textContent=en?'There was an error. Please try again.':'Hubo un error. Intenta de nuevo.';msg.style.color='#e0b020';}})
      .catch(()=>{msg.textContent=en?'There was an error. Please try again.':'Hubo un error. Intenta de nuevo.';msg.style.color='#e0b020';});
    });
  }
  wireForm('alertsForm','alertsMsg','¡Listo! Te suscribiste a las alertas regulatorias.','Done! You subscribed to regulatory alerts.');
  wireForm('contactForm','contactMsg','¡Gracias! Tu mensaje fue enviado. Te contactaremos pronto.','Thank you! Your message was sent. We will contact you soon.');

  /* ============================================================
     EFECTOS MODERNOS (respetan prefers-reduced-motion y táctil)
     ============================================================ */
  const reduceMotion=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const isTouch=window.matchMedia('(hover: none)').matches;

  /* —— Barra de progreso de scroll (siempre activa, es liviana) —— */
  const progress=document.getElementById('scrollProgress');
  if(progress){
    const updateProgress=()=>{
      const h=document.documentElement;
      const scrolled=h.scrollTop/(h.scrollHeight-h.clientHeight);
      progress.style.width=(scrolled*100)+'%';
    };
    window.addEventListener('scroll',updateProgress,{passive:true});
    updateProgress();
  }

  if(!reduceMotion){
    /* —— Partículas del hero: motas ascendentes de marca (energía/datos) —— */
    (function heroParticles(){
      const canvas=document.getElementById('heroParticles');
      if(!canvas)return;
      /* en pantallas pequeñas reducimos o desactivamos para rendimiento */
      const small=window.innerWidth<720;
      const ctx=canvas.getContext('2d');
      let w,h,particles=[],raf=null;
      const COUNT=small?14:34;
      const COLORS=['123,204,69','143,217,87','243,217,39'];
      function resize(){
        const r=canvas.getBoundingClientRect();
        w=canvas.width=r.width*Math.min(window.devicePixelRatio||1,2);
        h=canvas.height=r.height*Math.min(window.devicePixelRatio||1,2);
      }
      function mk(){
        return{
          x:Math.random()*w,
          y:h+Math.random()*h*0.3,
          r:(Math.random()*2.4+0.8)*(Math.min(window.devicePixelRatio||1,2)),
          vy:-(Math.random()*0.5+0.18)*(Math.min(window.devicePixelRatio||1,2)),
          vx:(Math.random()-0.5)*0.25,
          a:Math.random()*0.5+0.25,
          c:COLORS[Math.floor(Math.random()*COLORS.length)]
        };
      }
      function init(){resize();particles=[];for(let i=0;i<COUNT;i++){const p=mk();p.y=Math.random()*h;particles.push(p);}}
      function frame(){
        ctx.clearRect(0,0,w,h);
        for(let i=0;i<particles.length;i++){
          const p=particles[i];
          p.y+=p.vy;p.x+=p.vx;p.x+=Math.sin(p.y*0.01)*0.15;
          if(p.y<-10){Object.assign(p,mk());p.y=h+10;}
          ctx.beginPath();ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
          ctx.fillStyle=`rgba(${p.c},${p.a})`;ctx.fill();
          /* líneas tenues entre motas cercanas (red/sistema) */
          for(let j=i+1;j<particles.length;j++){
            const q=particles[j];const dx=p.x-q.x,dy=p.y-q.y;const dist=Math.sqrt(dx*dx+dy*dy);
            const max=130*(Math.min(window.devicePixelRatio||1,2));
            if(dist<max){
              ctx.beginPath();ctx.moveTo(p.x,p.y);ctx.lineTo(q.x,q.y);
              ctx.strokeStyle=`rgba(123,204,69,${0.10*(1-dist/max)})`;
              ctx.lineWidth=1;ctx.stroke();
            }
          }
        }
        raf=requestAnimationFrame(frame);
      }
      init();frame();
      let rt=null;
      window.addEventListener('resize',()=>{clearTimeout(rt);rt=setTimeout(init,200);});
    })();

    /* —— Parallax del hero: el fondo se mueve más lento que el scroll —— */
    let ticking=false;
    function onScroll(){
      const y=window.scrollY;
      if(!ticking){
        requestAnimationFrame(()=>{
          /* fondo del slide activo (parallax suave) */
          const activeBg=document.querySelector('.slide.active .slide-bg');
          if(activeBg&&y<900){activeBg.style.transform=`scale(1.06) translateY(${y*0.18}px)`;}
          /* contenido del hero se desvanece al bajar */
          const sc=document.querySelector('.slide.active .slide-content');
          if(sc&&y<700){sc.style.opacity=Math.max(0,1-y/600);sc.style.transform=`translateY(${y*0.12}px)`;}
          /* elementos con data-parallax */
          document.querySelectorAll('[data-parallax]').forEach(el=>{
            const speed=parseFloat(el.dataset.parallax)||0.1;
            const rect=el.getBoundingClientRect();
            const center=rect.top+rect.height/2-window.innerHeight/2;
            el.style.transform=`translateY(${center*speed*-0.1}px)`;
          });
          ticking=false;
        });
        ticking=true;
      }
    }
    window.addEventListener('scroll',onScroll,{passive:true});

    /* —— Tilt 3D en tarjetas (solo con mouse, no en táctil) —— */
    if(!isTouch){
      document.querySelectorAll('[data-tilt]').forEach(card=>{
        card.addEventListener('mousemove',e=>{
          const r=card.getBoundingClientRect();
          const px=(e.clientX-r.left)/r.width-0.5;
          const py=(e.clientY-r.top)/r.height-0.5;
          card.style.transform=`perspective(900px) rotateY(${px*5}deg) rotateX(${-py*5}deg) translateY(-6px)`;
        });
        card.addEventListener('mouseleave',()=>{card.style.transform='';});
      });

      /* —— Botones magnéticos: el botón sigue sutilmente al cursor —— */
      document.querySelectorAll('.btn-primary').forEach(btn=>{
        btn.addEventListener('mousemove',e=>{
          const r=btn.getBoundingClientRect();
          const mx=e.clientX-r.left-r.width/2;
          const my=e.clientY-r.top-r.height/2;
          btn.style.transform=`translate(${mx*0.15}px,${my*0.22}px)`;
        });
        btn.addEventListener('mouseleave',()=>{btn.style.transform='';});
      });
    }
  }
});

/* —— Filtro de categorías en página FAQ —— */
function filterFaq(cat) {
  document.querySelectorAll('.faq-cat').forEach(b => {
    b.classList.toggle('active', b.getAttribute('onclick').includes("'"+cat+"'"));
  });
  document.querySelectorAll('.faq-group').forEach(g => {
    if (cat === 'todos') {
      g.style.display = '';
    } else {
      g.style.display = g.dataset.cat === cat ? '' : 'none';
    }
  });
}
