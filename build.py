"""Gera o site estático da Vanessa Kreitchmann (substitui o Lovable).
Uso: python3 build.py   → escreve os HTML na própria pasta.
"""
from pathlib import Path

ROOT = Path(__file__).parent
WA = "555189418635"
GROUP_URL = "https://chat.whatsapp.com/CVVTLax1o7lLS6nhViTWq8?s=cl&p=i&iam=2"
OG_IMG = "https://vanessakreitchmann.com.br/img/vanessa-hero.jpg"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">')

def tracking(pixel_id: str) -> str:
    return f"""
<!-- Google Ads -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-16849738415"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','AW-16849738415');</script>
<!-- Meta Pixel -->
<script>!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','{pixel_id}');fbq('track','PageView');</script>
<!-- TikTok Pixel -->
<script>!function(w,d,t){{w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie","holdConsent","revokeConsent","grantConsent"],ttq.setAndDefer=function(t,e){{t[e]=function(){{t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){{for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e}},ttq.load=function(e,n){{var r="https://analytics.tiktok.com/i18n/pixel/events.js",o=n&&n.partner;ttq._i=ttq._i||{{}},ttq._i[e]=[],ttq._i[e]._u=r,ttq._t=ttq._t||{{}},ttq._t[e]=+new Date,ttq._o=ttq._o||{{}},ttq._o[e]=n||{{}};n=document.createElement("script");n.type="text/javascript",n.async=!0,n.src=r+"?sdkid="+e+"&lib="+t;e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(n,e)}};ttq.load('D9UTL13C77UE58FDAIK0');ttq.page();}}(window,document,'ttq');</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-5PMSVCMT');</script>
"""

GTM_NOSCRIPT = '<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5PMSVCMT" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'

def page(title, desc, body, css="", pixel="905228488881016", robots=None, extra_head=""):
    rob = f'<meta name="robots" content="{robots}">' if robots else ""
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Vanessa Kreitchmann">
{rob}
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="{OG_IMG}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#121212">
<link rel="icon" href="/favicon.ico">
{FONTS}
{tracking(pixel)}
{extra_head}
<style>{BASE_CSS}{css}</style>
</head>
<body>
{GTM_NOSCRIPT}
{body}
</body>
</html>
"""

BASE_CSS = """
:root{--gold:#e8d94a;--gold-d:#d1c12a;--dark:#121212;--card:#1c1c1c;--muted:#262626;--wa:#25d366}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:Inter,system-ui,sans-serif;background:var(--dark);color:#fff;line-height:1.55;-webkit-font-smoothing:antialiased}
h1,h2,h3,.disp{font-family:Montserrat,system-ui,sans-serif;line-height:1.12;letter-spacing:-.01em}
a{color:inherit}
img{max-width:100%;display:block}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;background:var(--gold);color:var(--dark);font-weight:700;font-family:Montserrat,sans-serif;text-decoration:none;padding:16px 26px;border-radius:12px;font-size:16px;border:0;cursor:pointer;transition:background .2s}
.btn:hover{background:var(--gold-d)}
.wa-float{position:fixed;right:18px;bottom:18px;width:58px;height:58px;border-radius:50%;background:var(--wa);display:grid;place-items:center;box-shadow:0 6px 20px #0006;z-index:40}
.wa-float svg{width:30px;height:30px}
"""

WA_SVG = '<svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm4.5 12.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c0-.1-.2-.2-.4-.3z"/></svg>'
ARROW = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#e8d94a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg>'

# ---------------------------------------------------------------- HOME
HOME_CSS = """
header.top{position:sticky;top:0;z-index:30;background:#121212e6;backdrop-filter:blur(8px);border-bottom:1px solid #ffffff12}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;height:64px}
.brand{font-family:Montserrat,sans-serif;font-weight:700;font-size:14px;letter-spacing:.06em;text-transform:uppercase;line-height:1.2}
.brand small{display:block;font-weight:500;letter-spacing:0;text-transform:none;opacity:.6;font-family:Inter,sans-serif}
header .btn{padding:10px 16px;font-size:14px;white-space:nowrap}
.hero{padding:56px 0 40px}
.hero .grid{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
.pill{display:inline-block;border:1px solid #e8d94a55;color:var(--gold);font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;padding:8px 14px;border-radius:30px}
.hero h1{font-size:clamp(38px,6vw,62px);font-weight:800;margin:20px 0 18px}
.hero h1 em{font-style:normal;color:var(--gold)}
.hero p.lead{font-size:18px;color:#ffffffc4;max-width:560px}
.hero p.lead b{color:#fff}
.hero .note{font-size:13px;color:#ffffff73;margin-top:14px}
.hero .cta{margin-top:28px}
.video{position:relative;width:100%;aspect-ratio:9/16;max-width:360px;margin:0 auto;border-radius:20px;overflow:hidden;background:#000;box-shadow:0 20px 60px #0008}
.video img,.video iframe{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border:0}
.video button{position:absolute;inset:0;margin:auto;width:76px;height:76px;border-radius:50%;background:var(--gold);border:0;cursor:pointer;display:grid;place-items:center;box-shadow:0 8px 30px #0008}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:36px;max-width:560px}
.stats div{background:var(--card);border:1px solid #ffffff10;border-radius:14px;padding:14px}
.stats b{display:block;font-family:Montserrat,sans-serif;font-size:24px;color:var(--gold)}
.stats span{font-size:12.5px;color:#ffffff99}
section.s{padding:72px 0}
section.alt{background:#181818}
.eyebrow{color:var(--gold);font-size:12px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;margin-bottom:12px}
h2{font-size:clamp(28px,4vw,40px);font-weight:800;margin-bottom:18px}
h2 em{font-style:normal;color:var(--gold)}
.lst{list-style:none;display:grid;gap:12px;margin-top:22px}
.lst li{display:flex;gap:12px;align-items:flex-start;background:var(--card);border:1px solid #ffffff10;border-radius:12px;padding:14px 16px;font-size:16px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:center}
.box{background:var(--card);border:1px solid #e8d94a33;border-radius:16px;padding:22px;margin-top:22px}
.box b{color:var(--gold)}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px}
.steps div{background:var(--card);border:1px solid #ffffff10;border-radius:16px;padding:24px}
.steps i{font-style:normal;display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;background:var(--gold);color:var(--dark);font-weight:800;font-family:Montserrat,sans-serif;margin-bottom:14px}
.steps h3{font-size:19px;margin-bottom:8px}
.steps p{color:#ffffffb0;font-size:15px}
.photo{border-radius:20px;overflow:hidden;aspect-ratio:4/5}
.photo img{width:100%;height:100%;object-fit:cover}
p.body{color:#ffffffc4;font-size:16.5px;margin-bottom:14px}
.quote{font-family:Montserrat,sans-serif;font-weight:700;font-size:20px;color:var(--gold);margin-top:10px}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.gallery img{border-radius:16px;aspect-ratio:3/4;object-fit:cover;width:100%;height:100%}
.ben{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:26px}
.ben div{display:flex;gap:12px;align-items:center;background:var(--card);border:1px solid #ffffff10;border-radius:14px;padding:18px;font-weight:500}
details{background:var(--card);border:1px solid #ffffff10;border-radius:14px;padding:18px 20px;margin-top:10px}
summary{cursor:pointer;font-weight:600;font-size:16.5px;list-style:none;display:flex;justify-content:space-between;gap:12px}
summary::after{content:"+";color:var(--gold);font-size:22px;line-height:1}
details[open] summary::after{content:"–"}
details p{color:#ffffffb0;margin-top:10px}
.final{text-align:center}
.final .strip{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin:30px 0}
.final .strip img{border-radius:14px;aspect-ratio:9/14;object-fit:cover;width:100%}
footer{padding:30px 0 90px;color:#ffffff66;font-size:13px;text-align:center;border-top:1px solid #ffffff10}
@media(max-width:860px){.hero .grid,.two{grid-template-columns:1fr;gap:28px}.steps,.ben{grid-template-columns:1fr}.hero{padding-top:32px}.final .strip{grid-template-columns:repeat(3,1fr)}.final .strip img:nth-child(n+4){display:none}.gallery{grid-template-columns:1fr 1fr}.gallery img:nth-child(3){display:none}}
"""

def li(items):
    return "".join(f"<li>{CHECK}<span>{t}</span></li>" for t in items)

FAQ = [
 ("A Vanessa vende raquetes?","Não. A Vanessa oferece uma consultoria técnica e independente para ajudar você a escolher uma raquete mais adequada antes de comprar em uma loja."),
 ("A consultoria é gratuita?","Não. Trata-se de um atendimento profissional, individual e pago. O investimento e os horários disponíveis são informados ao final da pré-avaliação e no WhatsApp."),
 ("Como funciona a consultoria?","O atendimento acontece por videochamada e dura entre 30 e 45 minutos. Durante a conversa, a Vanessa analisa seu nível, estilo de jogo, objetivos, dificuldades e preferências."),
 ("Preciso já ter algum modelo em mente?","Não. A consultoria é indicada tanto para quem já está comparando modelos quanto para quem ainda não sabe por onde começar."),
 ("A consultoria serve para iniciantes?","Sim. Ela pode ajudar quem está escolhendo a primeira raquete e também jogadores que querem trocar de modelo."),
 ("Receberei indicação de marcas e modelos?","Após analisar o seu perfil, a Vanessa poderá orientar características e modelos compatíveis com suas necessidades e faixa de investimento."),
 ("A consultoria substitui avaliação médica?","Não. A consultoria considera os desconfortos relatados para orientar a escolha da raquete, mas não substitui avaliação médica ou fisioterapêutica."),
 ("Como conheço o investimento e os horários?","Faça a pré-avaliação rápida: o investimento aparece no final e você continua pelo WhatsApp para ver os horários disponíveis."),
]

HOME_BODY = f"""
<header class="top"><div class="wrap">
  <div class="brand">Vanessa Kreitchmann<small>Consultoria personalizada de raquetes</small></div>
  <a class="btn" href="/diagnostico/" data-cta="header">Pré-avaliação</a>
</div></header>

<section class="hero"><div class="wrap grid">
  <div>
    <span class="pill">Especialista em raquetes de Beach Tennis</span>
    <h1>Escolha a raquete certa. <em>Jogue com mais conforto.</em> Evolua de verdade.</h1>
    <p class="lead"><b>Consultoria individual</b> por <b>videochamada com duração entre 30 e 45 minutos</b> para ajudar você a escolher uma raquete adequada ao seu nível, estilo de jogo e objetivos — antes de investir no modelo errado. A Vanessa não vende raquetes: a recomendação é técnica, personalizada e independente.</p>
    <div class="cta"><a class="btn" href="/diagnostico/" data-cta="hero">Fazer pré-avaliação {ARROW}</a></div>
    <p class="note">Leva menos de 1 minuto • Investimento informado ao final da pré-avaliação • Horários pelo WhatsApp</p>
    <div class="stats"><div><b>80.000+</b><span>Consultorias realizadas</span></div><div><b>12+</b><span>Anos de experiência</span></div><div><b>50+</b><span>Marcas atendidas</span></div></div>
  </div>
  <div class="video" id="video"><img src="/img/vanessa-hero-2.jpg" alt="Vanessa Kreitchmann com raquetes de beach tennis" loading="eager"><button aria-label="Assistir vídeo"><svg width="30" height="30" viewBox="0 0 24 24" fill="#121212"><path d="M8 5v14l11-7z"/></svg></button></div>
</div></section>

<section class="s alt"><div class="wrap two">
  <div>
    <h2>Você sente que poderia estar jogando melhor, mas algo parece <em>travar?</em></h2>
    <ul class="lst">{li(['Está treinando, mas sente que não evolui','Precisa forçar os golpes para a bola passar','Sente desconforto no braço, ombro ou cotovelo','Está em dúvida entre vários modelos e marcas','Já comprou uma raquete e não se adaptou'])}</ul>
    <p class="body" style="margin-top:20px">Você não está sozinho! A maioria dos jogadores passa por isso, e o problema pode estar na <b style="color:var(--gold)">raquete errada</b>.</p>
  </div>
  <div class="photo"><img src="/img/vanessa-photo-5.jpg" alt="Vanessa analisando raquete" loading="lazy"></div>
</div></section>

<section class="s"><div class="wrap">
  <p class="eyebrow">Para quem é</p>
  <h2>Para quem é a consultoria?</h2>
  <ul class="lst" style="grid-template-columns:repeat(auto-fit,minmax(300px,1fr))">{li(['Vai comprar sua primeira raquete','Quer trocar de modelo, mas está em dúvida','Já comprou uma raquete e não se adaptou','Está comparando marcas e modelos','Busca mais conforto, controle ou potência','Quer evitar investir em uma escolha inadequada'])}</ul>
  <div class="box">Esta consultoria <b>não é uma loja.</b> A Vanessa não vende equipamentos e não indica modelos gratuitamente pelo WhatsApp. A recomendação é realizada após uma análise individual durante a consultoria.</div>
</div></section>

<section class="s alt"><div class="wrap">
  <p class="eyebrow">Como funciona</p>
  <h2>Passo a passo</h2>
  <div class="steps">
    <div><i>1</i><h3>Análise individual</h3><p>Videochamada com duração entre 30 e 45 minutos para entender seu nível, experiência, estilo de jogo, dificuldades, objetivos e possíveis desconfortos.</p></div>
    <div><i>2</i><h3>Orientação técnica</h3><p>Análise de peso, balance, formato, materiais e demais características que fazem sentido para o seu perfil.</p></div>
    <div><i>3</i><h3>Decisão mais segura</h3><p>Orientação sobre modelos compatíveis com sua necessidade, preferências e faixa de investimento antes de concluir a compra.</p></div>
  </div>
</div></section>

<section class="s"><div class="wrap two">
  <div class="photo"><img src="/img/vanessa-authority-1.jpg" alt="Vanessa Kreitchmann" loading="lazy"></div>
  <div>
    <p class="eyebrow">Por que fazer a consultoria</p>
    <p class="body">Na minha consultoria personalizada, analiso o seu perfil de jogo, suas características físicas e seus objetivos para indicar a raquete ideal para você.</p>
    <p class="body">Esse cuidado é fundamental, porque o uso de uma raquete inadequada pode gerar uma série de problemas, especialmente desconfortos como a epicondilite (conhecida como "cotovelo de tenista"), que atendo com frequência. Muitos desses casos surgem por indicações baseadas apenas em tendências de mercado ou em informações genéricas, sem considerar as reais necessidades do atleta.</p>
    <p class="body">Meu trabalho é justamente evitar que isso aconteça: com uma orientação técnica e personalizada, você ganha rendimento, precisão e conforto, preservando a sua saúde a longo prazo.</p>
    <p class="quote">A raquete certa transforma seu jogo e protege seu futuro nas quadras.</p>
  </div>
</div></section>

<section class="s alt"><div class="wrap">
  <p class="eyebrow">Quem vai te ajudar</p>
  <h2>A maior <em>especialista</em> em raquetes do Brasil</h2>
  <div class="two" style="align-items:start">
    <div>
      <p class="body">Vanessa Kreitchmann é referência em raquetes de Beach Tennis no Brasil e atua diretamente no desenvolvimento de projetos para marcas, sendo peça-chave na criação e evolução de novos modelos.</p>
      <p class="body">Está conectada com as principais indústrias do setor, acompanha de perto o processo de fabricação e investe no desenvolvimento de novos materiais, sempre buscando inovação e performance para os atletas.</p>
      <div class="stats" style="margin-top:22px"><div><b>+80 mil</b><span>Consultorias realizadas</span></div><div><b>+50</b><span>Marcas lançadas no mercado</span></div><div><b>+12</b><span>Países atendidos</span></div></div>
    </div>
    <div class="gallery"><img src="/img/vanessa-photo-2.jpg" alt="" loading="lazy"><img src="/img/vanessa-photo-3.jpg" alt="" loading="lazy"><img src="/img/vanessa-authority-2.jpg" alt="" loading="lazy"></div>
  </div>
</div></section>

<section class="s"><div class="wrap">
  <h2>Com a consultoria você ganha:</h2>
  <div class="ben">{''.join(f'<div>{CHECK}<span>{t}</span></div>' for t in ['Segurança na escolha da raquete','Prevenção de dores e desconfortos','Evolução técnica com mais conforto','Análise personalizada do seu jogo','Critérios técnicos claros e aplicados','Mais confiança antes de comprar'])}</div>
</div></section>

<section class="s alt"><div class="wrap" style="max-width:820px">
  <p class="eyebrow">Perguntas frequentes</p>
  <h2>Ainda tem dúvidas?</h2>
  {''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)}
</div></section>

<section class="s final"><div class="wrap">
  <h2>Você pode continuar tentando acertar sozinho…</h2>
  <p class="body">Ou garantir agora a orientação de quem mais entende do assunto no Brasil.</p>
  <div class="strip">{''.join(f'<img src="/img/vanessa-social-{i}.jpg" alt="" loading="lazy">' for i in range(1,6))}</div>
  <a class="btn" href="/diagnostico/" data-cta="final">Fazer minha pré-avaliação {ARROW}</a>
  <p class="note" style="color:#ffffff73;font-size:13px;margin-top:14px">Consultoria individual e paga por videochamada • Investimento informado ao final da pré-avaliação • Atendimento com horários limitados por semana</p>
</div></section>

<footer><div class="wrap">© Vanessa Kreitchmann · Consultoria de raquetes de Beach Tennis · <a href="https://www.instagram.com/vankreitchmann/" target="_blank" rel="noopener">@vankreitchmann</a></div></footer>

<a class="wa-float" href="/diagnostico/" aria-label="Falar com a Vanessa" data-cta="flutuante">{WA_SVG}</a>

<script>
// Leva as UTMs da página para a pré-avaliação
(function(){{var q=location.search;if(!q)return;document.querySelectorAll('a[href^="/diagnostico"]').forEach(function(a){{a.href=a.getAttribute('href')+q}})}})();
// Vídeo: carrega o YouTube só ao clicar
document.querySelector('#video button').onclick=function(){{var v=document.getElementById('video');v.innerHTML='<iframe src="https://www.youtube-nocookie.com/embed/yCP5Tn0pbfE?autoplay=1&playsinline=1&rel=0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen title="Vídeo da Vanessa"></iframe>'}};
</script>
"""

# ---------------------------------------------------------------- GRUPO (idêntico ao Lovable)
GRUPO_CSS = """
body{min-height:100svh;display:flex;align-items:center;justify-content:center;padding:20px}
.box{width:100%;max-width:380px;text-align:center}
.k{color:var(--gold);font-size:12px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;margin-bottom:16px}
h1{font-size:24px;margin-bottom:12px}
p{color:#ffffff99;font-size:14px;margin-bottom:24px}
.btn{width:100%;text-transform:uppercase;letter-spacing:.06em;font-size:14px}
small{display:block;margin-top:16px;color:#ffffff4d;font-size:12px}
"""
GRUPO_BODY = f"""
<main class="box">
  <p class="k">Vanessa Kreitchmann</p>
  <h1>Entrando no grupo do WhatsApp…</h1>
  <p>Se a janela não abrir automaticamente, toque no botão abaixo.</p>
  <a class="btn" href="{GROUP_URL}">Entrar no grupo</a>
  <small id="w">Redirecionando…</small>
</main>
<script>
// Mesmo comportamento da página antiga: Lead no pixel de Grupos e redirecionamento após 0,8 s
try{{fbq('track','Lead')}}catch(e){{}}
setTimeout(function(){{location.replace({GROUP_URL!r})}},800);
setTimeout(function(){{var w=document.getElementById('w');if(w)w.remove()}},1200);
</script>
"""

# ---------------------------------------------------------------- PAGAMENTO CONFIRMADO
PAG_MSG = "Olá, Vanessa! Meu pagamento da Consultoria Personalizada de Raquetes foi confirmado. Gostaria de escolher o dia e horário da minha videochamada."
PAG_BODY = f"""
<main class="box">
  <p class="k">Vanessa Kreitchmann</p>
  <h1>Pagamento confirmado! 🎾</h1>
  <p>Obrigada pela confiança. Agora é só me chamar no WhatsApp para escolher o dia e o horário da sua videochamada.</p>
  <a class="btn" style="background:var(--wa);color:#fff" href="https://wa.me/{WA}?text={PAG_MSG.replace(' ','%20').replace('!','%21').replace(',','%2C')}" target="_blank" rel="noopener">{WA_SVG.replace('aria-hidden','width="22" height="22" aria-hidden')} Agendar no WhatsApp</a>
</main>
"""

# ---------------------------------------------------------------- 404 → home (mantém UTMs)
NF_BODY = """
<main class="box"><p class="k">Vanessa Kreitchmann</p><h1>Redirecionando…</h1><p><a href="/">Ir para a página inicial</a></p></main>
<script>location.replace('/'+location.search+location.hash)</script>
"""

def write(rel, html):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf-8")
    print("ok", rel, len(html))

if __name__ == "__main__":
    write("index.html", page("Consultoria de Raquetes | Vanessa Kreitchmann",
        "Consultoria personalizada para escolha da raquete ideal de beach tennis. Análise técnica, acompanhamento completo e mais performance em quadra.",
        HOME_BODY, HOME_CSS))
    write("grupo/index.html", page("Grupo do WhatsApp | Vanessa Kreitchmann", "Grupo do WhatsApp da Vanessa Kreitchmann.",
        GRUPO_BODY, GRUPO_CSS, pixel="1116193634600220", robots="noindex, nofollow"))
    write("pagamento-confirmado/index.html", page("Pagamento confirmado | Vanessa Kreitchmann", "Agende sua videochamada.",
        PAG_BODY, GRUPO_CSS, robots="noindex, nofollow"))
    write("404.html", page("Vanessa Kreitchmann", "Consultoria de raquetes.", NF_BODY, GRUPO_CSS, robots="noindex"))
    chat = (ROOT / "diagnostico" / "chat.html").read_text(encoding="utf-8")
    write("diagnostico/index.html", page("Pré-avaliação da sua raquete | Vanessa Kreitchmann",
        "Responda 5 perguntas rápidas e receba a sua pré-avaliação no WhatsApp.",
        chat, "", robots="noindex"))
    quiz = (ROOT / "quiz" / "quiz.html").read_text(encoding="utf-8")
    write("quiz/index.html", page("Sua raquete combina com o seu jogo? | Vanessa Kreitchmann",
        "Teste rápido de 1 minuto: descubra seu perfil de jogo e o que pode estar te travando em quadra.",
        quiz, "", robots="noindex"))
