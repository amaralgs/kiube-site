#!/usr/bin/env python3
"""Generates the Kiube site (EN at the root, PT-BR under /pt/) from one set of texts.

Run from anywhere:  python3 tools/build.py
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://kiube.werker.com.br"
UPDATED = {"en": "November 17, 2026", "pt": "17 de novembro de 2026"}

STAGES = ["stage_1_white_cross", "stage_2_white_corners", "stage_3_middle_layer", "stage_4_yellow_cross",
          "stage_5_yellow_edges", "stage_6_corners_position", "stage_7_corners_orient"]
BADGES = ["stage_white_cross", "stage_white_corners", "stage_middle_layer", "stage_yellow_cross",
          "stage_yellow_edges", "stage_corners_pos", "stage_corners_ori", "all_stages", "streak_3_days",
          "first_challenge", "challenge_easy", "challenge_medium", "challenge_hard", "fundamentals"]

T = {
 "en": {
  "html_lang": "en", "name": "Kiube",
  "title": "Kiube – Learn to solve the 3×3 puzzle cube, step by step",
  "desc": "Kiube teaches you to solve the 3×3 puzzle cube with a clear 7-step method: a flat view of the cube, animated 3D moves, badges and surprise challenges. Portuguese and English. Private, no account.",
  "og": "Learn to solve the cube, one move at a time.",
  "nav_features": "Features", "nav_method": "The method", "nav_privacy": "Privacy", "nav_get": "Get the app",
  "home": "Home", "about": "About", "privacy": "Privacy", "contact": "Contact", "other_lang": "Português",
  "other_lang_short": "PT",
  "kicker": "Step by step · no account",
  "h1": "Learn the cube. <em>One move</em> at a time.",
  "sub": "Kiube teaches the classic 3×3 puzzle cube with a clear 7-step method. Follow the flat view, watch each move turn in 3D, and earn badges as it clicks.",
  "cta_soon": "Coming soon to the App Store", "cta_read": "Read the privacy policy",
  "f_eyebrow": "Features", "f_h2": "Clear, calm, at your pace.",
  "f_lead": "Kiube shows what each step builds, how the moves turn, and keeps the pressure off.",
  "features": [
    ("🧩", "Seven steps", "From the white cross to the last yellow corners, one small goal at a time."),
    ("🎞️", "Flat view + 3D moves", "See the state on a flat face and watch every move animate on a 3D cube."),
    ("🎓", "Fundamentals first", "Learn the pieces, the six faces and how to read moves before the first step."),
    ("🏅", "Badges and challenges", "Earn medals as you finish stages, and take surprise timed challenges, from easy to hard."),
    ("🌐", "Portuguese and English", "The whole app and every lesson in both languages, more to come."),
    ("🔒", "Private by default", "No account, no ads in this version, and your progress stays on your device."),
  ],
  "m_eyebrow": "The method", "m_h2": "Seven steps to solved.",
  "m_lead": "A layer-by-layer method that beginners can follow without memorising everything at once.",
  "stages": ["White cross", "White corners", "Middle layer", "Yellow cross", "Yellow edges", "Position the corners", "Orient the corners"],
  "stage_word": "Step",
  "n_eyebrow": "Learn the language of moves", "n_h2": "Moves you can read.",
  "n_lead": "Every move is a turn of one face. Kiube teaches them with animations before you use them, so a sequence like this stops looking like code:",
  "n_moves": ["R", "U", "R'", "U'"], "n_caption": "Right, Up, Right back, Up back: one of the first sequences you will learn.",
  "b_eyebrow": "Keep going", "b_h2": "Badges worth collecting.",
  "b_lead": "One for each stage, plus streaks, challenges and the fundamentals.",
  "p_eyebrow": "Privacy", "p_h2": "We collect none of your information.",
  "p_lead": "The developer of Kiube does not collect your data: no account, no sign-up, no data server, no tracking. Your progress stays on your device.",
  "p_cards": [("No account", "Nothing to create, nothing to sign in to."), ("Everything on your device", "Progress, badges and times never leave it."),
              ("No tracking", "No analytics in this version."), ("You are in control", "Uninstall the app and everything is gone.")],
  "p_note": "This version has no ads. A free version with ads and a paid ad-free version are planned; if ads arrive, this policy will be updated first and consent will be asked where the law requires.",
  "g_eyebrow": "Get Kiube", "g_h2": "In testing on TestFlight.",
  "g_lead": "iPhone and iPad. Available in Portuguese and English.",
  "g_small": "Kiube keeps your data on your device.",
  "r_eyebrow": "On the roadmap", "r_h2": "What comes next.",
  "r_lead": "Planned, not promised: help from the camera when you get stuck, and other puzzles after the 3×3 — 2×2, pyramid, 4×4 and 5×5.",
  "about_title": "About Kiube – Learn to solve the puzzle cube", "about_desc": "About Kiube, an app that teaches the 3×3 puzzle cube step by step, and the developer behind it.",
  "about_h1": "About Kiube",
  "about_p": [
    "Kiube is an app that teaches you to solve the classic 3×3 puzzle cube, step by step. It started from a simple frustration: most tutorials show a long list of moves without explaining what each step is trying to build.",
    "The lessons use a clear method in seven steps. Each one shows a flat view of the cube for the state you want, and a 3D cube that animates every move. Before the first step there is a short Fundamentals chapter on the pieces, the faces and how to read moves.",
    "Along the way you earn badges and can take surprise timed challenges, from easy to hard, so the moves start to become automatic.",
    "Kiube runs on your device. Your progress stays with you.",
  ],
  "about_dev_h": "The developer", "about_dev_p": "Kiube is an independent app made by Gilberto Amaral.",
  "about_contact_h": "Contact", "about_more_h": "More",
  "priv_title": "Kiube – Privacy Policy", "priv_h1": "Kiube – Privacy Policy",
  "priv_meta": "Last updated: {d} · Developer: Gilberto Amaral · Draft, pending legal review",
  "promise_h": "The developer does not collect any information about you.",
  "promise_p": "No account, no data server, no tracking. Everything stays on your device.",
  "priv": [
    ("In short", "Kiube keeps your progress on your device. There is no account, and the developer does not receive your data."),
    ("What the app stores", "Your progress in the lessons (stages completed, badges and the dates you earned them, best challenge times, days in a row), your answer to “is your cube solved or scrambled”, and your language and display choices. All of it is stored only on your device."),
    ("No account, no data collection", "Kiube has no sign-up and no server that receives your information. We cannot see your progress, and nothing is sold or shared."),
    ("Camera", "This version does not use the camera. A future version may offer camera help to recognise which step your cube is at. If it does, the plan is for the images to be processed on your device and not sent anywhere, and this policy will be updated before it ships."),
    ("Advertising and tracking", "This version has no advertising and no analytics, and does not track you. A free version with ads and a paid ad-free version are planned. If ads are added, the ad provider (for example Google AdMob) may use device identifiers under its own policy; Kiube will ask for your consent where the law requires, and this policy will be updated before that version is released."),
    ("Children", "Kiube is not directed to children under 13."),
    ("Your rights", "Because the data stays on your device, you control it: uninstall the app and everything is removed."),
    ("Changes", "If this policy changes, the date above is updated."),
    ("Contact", "Questions: contato@amaral.pro"),
  ],
 },
 "pt": {
  "html_lang": "pt-BR", "name": "Kiube",
  "title": "Kiube – Aprenda a resolver o cubo mágico 3×3, passo a passo",
  "desc": "O Kiube ensina a resolver o cubo mágico 3×3 com um método claro em 7 etapas: vista plana do cubo, movimentos animados em 3D, medalhas e desafios surpresa. Em português e inglês. Privado, sem conta.",
  "og": "Aprenda a resolver o cubo mágico, um movimento por vez.",
  "nav_features": "Recursos", "nav_method": "O método", "nav_privacy": "Privacidade", "nav_get": "Baixar o app",
  "home": "Início", "about": "Sobre", "privacy": "Privacidade", "contact": "Contato", "other_lang": "English",
  "other_lang_short": "EN",
  "kicker": "Passo a passo · sem conta",
  "h1": "Aprenda o cubo. <em>Um movimento</em> por vez.",
  "sub": "O Kiube ensina o cubo mágico 3×3 com um método claro em 7 etapas. Siga a vista plana, veja cada movimento girar em 3D e ganhe medalhas conforme for pegando o jeito.",
  "cta_soon": "Em breve na App Store", "cta_read": "Ler a política de privacidade",
  "f_eyebrow": "Recursos", "f_h2": "Claro, calmo, no seu ritmo.",
  "f_lead": "O Kiube mostra o que cada etapa constrói, como os movimentos giram e tira a pressão de cima de você.",
  "features": [
    ("🧩", "Sete etapas", "Da cruz branca aos últimos cantos amarelos, um objetivo pequeno de cada vez."),
    ("🎞️", "Vista plana + movimentos em 3D", "Veja o estado numa face plana e assista a cada movimento animado num cubo 3D."),
    ("🎓", "Primeiro os fundamentos", "Conheça as peças, as seis faces e como ler os movimentos antes da primeira etapa."),
    ("🏅", "Medalhas e desafios", "Ganhe medalhas ao concluir etapas e encare desafios surpresa com tempo, do fácil ao difícil."),
    ("🌐", "Português e inglês", "O app inteiro e todas as lições nos dois idiomas, e mais a caminho."),
    ("🔒", "Privado por padrão", "Sem conta, sem anúncios nesta versão, e seu progresso fica no seu aparelho."),
  ],
  "m_eyebrow": "O método", "m_h2": "Sete etapas até montar.",
  "m_lead": "Um método por camadas que o iniciante consegue seguir sem decorar tudo de uma vez.",
  "stages": ["Cruz branca", "Cantos brancos", "Camada do meio", "Cruz amarela", "Arestas amarelas", "Posicionar os cantos", "Orientar os cantos"],
  "stage_word": "Etapa",
  "n_eyebrow": "Aprenda a linguagem dos movimentos", "n_h2": "Movimentos que você sabe ler.",
  "n_lead": "Cada movimento é o giro de uma face. O Kiube ensina com animações antes de você usá-los, e uma sequência como esta deixa de parecer código:",
  "n_moves": ["R", "U", "R'", "U'"], "n_caption": "Direita, Cima, Direita de volta, Cima de volta: uma das primeiras sequências que você vai aprender.",
  "b_eyebrow": "Continue", "b_h2": "Medalhas que valem a coleção.",
  "b_lead": "Uma para cada etapa, mais sequência de dias, desafios e os fundamentos.",
  "p_eyebrow": "Privacidade", "p_h2": "Não coletamos nenhuma informação sua.",
  "p_lead": "O desenvolvedor do Kiube não coleta seus dados: sem conta, sem cadastro, sem servidor de dados, sem rastreamento. Seu progresso fica no seu aparelho.",
  "p_cards": [("Sem conta", "Nada para criar, nada para entrar."), ("Tudo no seu aparelho", "Progresso, medalhas e tempos nunca saem dele."),
              ("Sem rastreamento", "Nenhuma análise de uso nesta versão."), ("Você no controle", "Desinstale o app e tudo desaparece.")],
  "p_note": "Esta versão não tem anúncios. Estão planejadas uma versão gratuita com anúncios e uma paga sem anúncios; se os anúncios chegarem, esta política será atualizada antes e o consentimento será pedido onde a lei exigir.",
  "g_eyebrow": "Baixe o Kiube", "g_h2": "Em teste no TestFlight.",
  "g_lead": "iPhone e iPad. Disponível em português e inglês.",
  "g_small": "O Kiube mantém seus dados no seu aparelho.",
  "r_eyebrow": "No roteiro", "r_h2": "O que vem depois.",
  "r_lead": "Planejado, não prometido: ajuda da câmera quando você travar, e outros cubos depois do 3×3 — 2×2, pirâmide, 4×4 e 5×5.",
  "about_title": "Sobre o Kiube – Aprenda a resolver o cubo mágico", "about_desc": "Sobre o Kiube, um app que ensina o cubo mágico 3×3 passo a passo, e o desenvolvedor por trás dele.",
  "about_h1": "Sobre o Kiube",
  "about_p": [
    "O Kiube é um app que ensina a resolver o clássico cubo mágico 3×3, passo a passo. Ele nasceu de uma frustração simples: a maioria dos tutoriais mostra uma lista longa de movimentos sem explicar o que cada etapa está tentando construir.",
    "As lições usam um método claro em sete etapas. Cada uma mostra uma vista plana do cubo com o estado que você quer alcançar, e um cubo 3D que anima cada movimento. Antes da primeira etapa há um capítulo curto de Fundamentos sobre as peças, as faces e como ler os movimentos.",
    "No caminho você ganha medalhas e pode encarar desafios surpresa com tempo, do fácil ao difícil, até os movimentos ficarem automáticos.",
    "O Kiube roda no seu aparelho. Seu progresso fica com você.",
  ],
  "about_dev_h": "O desenvolvedor", "about_dev_p": "O Kiube é um app independente feito por Gilberto Amaral.",
  "about_contact_h": "Contato", "about_more_h": "Mais",
  "priv_title": "Kiube – Política de Privacidade", "priv_h1": "Kiube – Política de Privacidade",
  "priv_meta": "Última atualização: {d} · Desenvolvedor: Gilberto Amaral · Rascunho, pendente de revisão jurídica",
  "promise_h": "O desenvolvedor não coleta nenhuma informação sobre você.",
  "promise_p": "Sem conta, sem servidor de dados, sem rastreamento. Tudo fica no seu aparelho.",
  "priv": [
    ("Em resumo", "O Kiube guarda seu progresso no seu aparelho. Não existe conta, e o desenvolvedor não recebe seus dados."),
    ("O que o app guarda", "Seu progresso nas lições (etapas concluídas, medalhas e as datas em que foram conquistadas, melhores tempos dos desafios, dias seguidos), sua resposta a “seu cubo está montado ou embaralhado” e suas escolhas de idioma e de exibição. Tudo é guardado apenas no seu aparelho."),
    ("Sem conta, sem coleta de dados", "O Kiube não tem cadastro nem servidor que receba suas informações. Não conseguimos ver seu progresso, e nada é vendido ou compartilhado."),
    ("Câmera", "Esta versão não usa a câmera. Uma versão futura poderá oferecer ajuda da câmera para reconhecer em que etapa está o seu cubo. Se isso acontecer, a intenção é que as imagens sejam processadas no seu aparelho e não sejam enviadas a lugar nenhum, e esta política será atualizada antes do lançamento."),
    ("Publicidade e rastreamento", "Esta versão não tem publicidade nem análise de uso, e não rastreia você. Estão planejadas uma versão gratuita com anúncios e uma paga sem anúncios. Se anúncios forem adicionados, o provedor de anúncios (por exemplo, o Google AdMob) poderá usar identificadores do aparelho conforme a política dele; o Kiube pedirá seu consentimento onde a lei exigir, e esta política será atualizada antes do lançamento dessa versão."),
    ("Crianças", "O Kiube não é direcionado a crianças menores de 13 anos."),
    ("Seus direitos", "Como os dados ficam no seu aparelho, você os controla: desinstale o app e tudo é removido."),
    ("Alterações", "Se esta política mudar, a data acima será atualizada."),
    ("Contato", "Dúvidas: contato@amaral.pro"),
  ],
 },
}

PAGES = {"index": "index.html", "about": "about.html", "privacy": "privacy.html"}


def urls(lang, page):
    """(path-for-this-lang, en-url, pt-url) for a page key."""
    f = PAGES[page]
    path_en = "" if page == "index" else f
    path_pt = "pt/" + ("" if page == "index" else f)
    return (path_en if lang == "en" else path_pt), f"{BASE}/{path_en}", f"{BASE}/{path_pt}"


def head(lang, page, title, desc):
    t = T[lang]
    own, en, pt = urls(lang, page)
    canon = en if lang == "en" else pt
    pre = "" if lang == "en" else "../"
    ld = ""
    if page == "index":
        ld = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareApplication",'
              '"name":"Kiube","applicationCategory":"EducationalApplication","operatingSystem":"iOS, iPadOS",'
              f'"description":"{t["desc"]}","inLanguage":["en","pt-BR"],"author":{{"@type":"Person","name":"Gilberto Amaral"}}}}</script>')
    return f'''<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#0a0f24">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{en}">
<link rel="alternate" hreflang="pt-BR" href="{pt}">
<link rel="alternate" hreflang="x-default" href="{en}">
<link rel="icon" href="{pre}icon.png">
<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{BASE}/icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{t['og']}">
<meta name="twitter:card" content="summary">
<link rel="stylesheet" href="{pre}assets/style.css">
{ld}
</head>
<body>
'''


def topbar(lang, page, full):
    t = T[lang]
    pre = "" if lang == "en" else "../"
    other = "pt/" + PAGES[page] if lang == "en" else "../" + PAGES[page]
    other = other.replace("index.html", "")
    other_lang = "pt-BR" if lang == "en" else "en"
    nav = (f'<a class="hide-sm" href="#features">{t["nav_features"]}</a>'
           f'<a class="hide-sm" href="#method">{t["nav_method"]}</a>'
           f'<a class="hide-sm" href="#privacy">{t["nav_privacy"]}</a>'
           f'<a href="#get">{t["nav_get"]}</a>') if full else f'<a href="./">{t["home"]}</a>'
    home = "./"
    return f'''<header class="topbar"><div class="in">
  <a class="brand" href="{home}"><img src="{pre}icon.png" alt="" width="28" height="28">Kiube</a>
  <nav aria-label="Main">
    {nav}
    <a class="lang" href="{other}" hreflang="{other_lang}" lang="{other_lang}">{t['other_lang_short']}</a>
  </nav>
</div></header>
'''


def footer(lang, page):
    t = T[lang]
    other = "pt/" + PAGES[page] if lang == "en" else "../" + PAGES[page]
    other = other.replace("index.html", "")
    other_lang = "pt-BR" if lang == "en" else "en"
    return f'''<footer><div class="wrap">
  <span class="grow">© 2026 Gilberto Amaral</span>
  <a href="about.html">{t['about']}</a>
  <a href="privacy.html">{t['privacy']}</a>
  <a href="mailto:contato@amaral.pro">{t['contact']}</a>
  <a href="{other}" hreflang="{other_lang}" lang="{other_lang}">{t['other_lang']}</a>
</div></footer>
</body>
</html>
'''


def cube():
    def face(cls, cells):
        return f'<div class="face {cls}">' + "".join(f'<i class="{c}"></i>' for c in cells) + "</div>"
    return ('<div class="stage3d" aria-hidden="true"><div class="cube">'
            + face("f", "GGGGGGGGG") + face("k", "BBBBBBBBB") + face("r", "RRRRRRRRR")
            + face("l", "OOOOOOOOO") + face("u", "YWYWWWYWY") + face("d", "YYYYYYYYY")
            + '</div></div>')


def index(lang):
    t = T[lang]
    pre = "" if lang == "en" else "../"
    out = [head(lang, "index", t["title"], t["desc"]), topbar(lang, "index", True)]
    out.append(f'''<main>
<section class="hero">
  <div class="floor" aria-hidden="true"></div>
  <div class="wrap">
    <p class="kicker">{t['kicker']}</p>
    {cube()}
    <h1>{t['h1']}</h1>
    <p class="sub">{t['sub']}</p>
    <div class="row">
      <!-- Troque pelo link da App Store/TestFlight quando estiver publicado -->
      <a class="btn soon" href="#get" aria-disabled="true">{t['cta_soon']}</a>
      <a class="btn ghost" href="privacy.html">{t['cta_read']}</a>
    </div>
  </div>
</section>

<section class="block" id="features">
  <div class="wrap">
    <p class="eyebrow">{t['f_eyebrow']}</p>
    <h2>{t['f_h2']}</h2>
    <p class="lead">{t['f_lead']}</p>
    <div class="grid">
''')
    for ico, h, p in t["features"]:
        out.append(f'      <div class="card"><span class="ico" aria-hidden="true">{ico}</span><h3>{h}</h3><p>{p}</p></div>\n')
    out.append(f'''    </div>
  </div>
</section>

<section class="block alt" id="method">
  <div class="wrap">
    <p class="eyebrow">{t['m_eyebrow']}</p>
    <h2>{t['m_h2']}</h2>
    <p class="lead">{t['m_lead']}</p>
    <ol class="stages">
''')
    for i, (key, name) in enumerate(zip(STAGES, t["stages"]), 1):
        out.append(f'      <li><img src="{pre}assets/stages/{key}.svg" alt="" width="92" height="92" loading="lazy"><strong>{t["stage_word"]} {i}</strong>{name}</li>\n')
    out.append(f'''    </ol>
  </div>
</section>

<section class="block">
  <div class="wrap split">
    <div>
      <p class="eyebrow">{t['n_eyebrow']}</p>
      <h2>{t['n_h2']}</h2>
      <p class="lead" style="margin-bottom:0">{t['n_lead']}</p>
    </div>
    <div class="moves" role="img" aria-label="{' '.join(t['n_moves'])}">
      {''.join(f'<span>{m}</span>' for m in t['n_moves'])}
      <small>{t['n_caption']}</small>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <p class="eyebrow">{t['b_eyebrow']}</p>
    <h2>{t['b_h2']}</h2>
    <p class="lead">{t['b_lead']}</p>
    <ul class="badges" aria-hidden="true">
''')
    for b in BADGES:
        out.append(f'      <li><img src="{pre}assets/badges/{b}.svg" alt="" width="68" height="68" loading="lazy"></li>\n')
    out.append(f'''    </ul>
  </div>
</section>

<section class="block" id="privacy">
  <div class="wrap">
    <p class="eyebrow">{t['p_eyebrow']}</p>
    <h2>{t['p_h2']}</h2>
    <p class="lead">{t['p_lead']}</p>
    <div class="pgrid">
''')
    for h, p in t["p_cards"]:
        out.append(f'      <div class="card"><h3>{h}</h3><p>{p}</p></div>\n')
    out.append(f'''    </div>
    <p class="priv-note">{t['p_note']}</p>
    <p><a class="btn ghost" href="privacy.html">{t['cta_read']}</a></p>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <div class="card note"><h3>{t['r_eyebrow']} · {t['r_h2']}</h3><p>{t['r_lead']}</p></div>
  </div>
</section>

<section class="block cta" id="get">
  <div class="wrap">
    <p class="eyebrow">{t['g_eyebrow']}</p>
    <h2>{t['g_h2']}</h2>
    <p class="lead">{t['g_lead']}</p>
    <div class="row">
      <a class="btn soon" href="#get" aria-disabled="true">{t['cta_soon']}</a>
    </div>
    <p class="small" style="margin-top:18px">{t['g_small']} <a href="privacy.html">{t['privacy']}</a></p>
  </div>
</section>
</main>
''')
    out.append(footer(lang, "index"))
    return "".join(out)


def about(lang):
    t = T[lang]
    body = "".join(f"  <p>{p}</p>\n" for p in t["about_p"])
    return (head(lang, "about", t["about_title"], t["about_desc"]) + topbar(lang, "about", False)
            + f'''<main class="page">
  <h1>{t['about_h1']}</h1>
{body}  <h2>{t['about_dev_h']}</h2>
  <p>{t['about_dev_p']}</p>
  <h2>{t['about_contact_h']}</h2>
  <p><a href="mailto:contato@amaral.pro">contato@amaral.pro</a></p>
  <h2>{t['about_more_h']}</h2>
  <p><a href="privacy.html">{t['privacy']}</a></p>
</main>
''' + footer(lang, "about"))


def privacy(lang):
    t = T[lang]
    body = "".join(f"  <h2>{h}</h2>\n  <p>{p}</p>\n" for h, p in t["priv"])
    return (head(lang, "privacy", t["priv_title"], t["desc"]) + topbar(lang, "privacy", False)
            + f'''<main class="page">
  <h1>{t['priv_h1']}</h1>
  <p class="small">{t['priv_meta'].format(d=UPDATED[lang])}</p>
  <div class="promise"><strong>{t['promise_h']}</strong><p>{t['promise_p']}</p></div>
{body}</main>
''' + footer(lang, "privacy"))


def sitemap():
    rows = []
    for page in PAGES:
        for lang in ("en", "pt"):
            own, en, pt = urls(lang, page)
            loc = en if lang == "en" else pt
            rows.append(f'  <url><loc>{loc}</loc><xhtml:link rel="alternate" hreflang="en" href="{en}"/>'
                        f'<xhtml:link rel="alternate" hreflang="pt-BR" href="{pt}"/></url>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")


def main():
    for lang in ("en", "pt"):
        d = ROOT if lang == "en" else ROOT / "pt"
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(index(lang))
        (d / "about.html").write_text(about(lang))
        (d / "privacy.html").write_text(privacy(lang))
    (ROOT / "sitemap.xml").write_text(sitemap())
    print("site generated")


main()
