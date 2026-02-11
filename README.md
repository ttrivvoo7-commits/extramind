# =====================================================================
# HIKI / LEGEND MATRIX — MODULE SPEC + ASSEMBLY GUIDE
# MOOTTORITILA → PAKOPUTKI
# (DOKUMENTOIVA BASH, EI AJETTAVAKSI)
# =====================================================================

# =====================================================================
# 0️⃣ FILOSOFIA: MITEN TÄMÄ KASATAAN
# =====================================================================
"""
Moottoritila (ENGINE):
- Ei renderiä
- Ei audioa
- Vain LOGIIKKAA ja AIKAA

Pakoputki (EXHAUST):
- Ei päätöksiä
- Ei tunnetta
- Vain VIRTAUS ulos (audio + mesh)

Kaikki virtaa YHTEEN SUUNTAAN.
Ei takaisinkytkentää frontendistä backend-logiikkaan.
"""

# =====================================================================
# 1️⃣ KANSIORAKENNE (LOPULLINEN)
# =====================================================================
backend/
├─ core/                     # 🧠 moottoritila
│  ├─ fsm/
│  │  ├─ machine.py
│  │  └─ __init__.py
│  ├─ emotion/
│  │  ├─ state.py
│  │  └─ __init__.py
│  └─ __init__.py
│
├─ tts/
│  ├─ timeline.py
│  ├─ phoneme_map.py
│  └─ __init__.py
│
├─ avatar/
│  ├─ blendshape_map.py
│  ├─ driver.py
│  ├─ frame.py
│  ├─ stream.py
│  └─ __init__.py
│
├─ assets/
│  ├─ visemes.json
│  ├─ blendshapes/
│  │  └─ humanoid_v1.json
│  └─ voices/
│     └─ piper_harri.json
│
├─ index.py                  # 🔗 backend ENTRY
│
frontend/
├─ avatar/
│  ├─ applyBlendshapes.js
│  ├─ driver.js
│  └─ index.js               # 🔗 frontend ENTRY
│
└─ assets/
   ├─ models/
   │  └─ avatar.glb
   └─ audio/
      └─ speech.wav

# =====================================================================
# 2️⃣ MODULEIDEN SISÄLTÖ (MITÄ NE TEKEE)
# =====================================================================

# -----------------------------------------------------
# core/fsm/machine.py
# -----------------------------------------------------
"""
VASTUU:
- Ajan yli kehittyvä tila
- Stressin kertymä ja vuoto
- CRACK-logiikka

EI SAA:
- Tietää TTS:stä
- Tietää avatarista
- Tietää frontendistä

INPUT:
- text (string)
OUTPUT:
- state (enum)
- stress (float)
"""

# -----------------------------------------------------
# core/emotion/state.py
# -----------------------------------------------------
"""
VASTUU:
- FSM → puheparametrit

MUUNTAA:
state + stress
→ latency_ms
→ timing_drift
→ intensity
→ micro_fail

EI SAA:
- Generoida audioa
- Koskea blendshapeihin
"""

# -----------------------------------------------------
# tts/timeline.py
# -----------------------------------------------------
"""
VASTUU:
- Teksti → phoneme-sekvenssi
- Phoneme → viseme
- Aikajanan laskenta

SAAT:
- emotion-state (timing_drift, micro_fail)

EI SAA:
- Tietää rigistä
- Tietää frontendistä
"""

# -----------------------------------------------------
# avatar/blendshape_map.py
# -----------------------------------------------------
"""
VASTUU:
- Abstrahoida viseme → rig

SISÄLTÖ:
- Dictionary tai JSON
- Ei logiikkaa

HYÖTY:
- Avatar vaihdettavissa
"""

# -----------------------------------------------------
# avatar/driver.py
# -----------------------------------------------------
"""
VASTUU:
- emotion-state → blendshape painot
- intensity + micro_fail

EI SAA:
- Tietää ajasta
- Tietää audiosta
"""

# -----------------------------------------------------
# avatar/frame.py
# -----------------------------------------------------
"""
VASTUU:
- Yksi frame = yksi hetki

SISÄLTÄÄ:
- time
- duration
- blendshape snapshot
"""

# -----------------------------------------------------
# avatar/stream.py
# -----------------------------------------------------
"""
VASTUU:
- Koko puhe kehon näkökulmasta

OUTPUT:
- frames[] (lineaarinen, ajettava)
"""

# -----------------------------------------------------
# backend/index.py
# -----------------------------------------------------
"""
PIPELINE ENTRYPOINT

KUTSUJÄRJESTYS:
text
→ FSM
→ emotion
→ TTS timeline
→ avatar stream

OUTPUT:
- audio (wav)
- frames (json)
"""

# =====================================================================
# 3️⃣ ASSETS & INDEXIT
# =====================================================================

# -----------------------------------------------------
# assets/visemes.json
# -----------------------------------------------------
"""
Yleinen viseme-setti:
A, E, O, M, F, L, rest

HYÖTY:
- Sama timeline toimii kaikille avatareille
"""

# -----------------------------------------------------
# assets/blendshapes/humanoid_v1.json
# -----------------------------------------------------
"""
Rig-kohtainen kartta:
viseme → blendshape-nimet

HYÖTY:
- Yksi FSM, monta kehoa
"""

# -----------------------------------------------------
# assets/voices/piper_harri.json
# -----------------------------------------------------
"""
Ääniassetti:
- pitch
- speed
- formant

HYÖTY:
- Ääni vaihdettavissa ilman animaatiomuutoksia
"""

# =====================================================================
# 4️⃣ FRONTEND-MODUULIT
# =====================================================================

# -----------------------------------------------------
# frontend/avatar/applyBlendshapes.js
# -----------------------------------------------------
"""
VASTUU:
- Ottaa numerot
- Asettaa ne meshiin

EI SAA:
- Päättää MITÄÄN
"""

# -----------------------------------------------------
# frontend/avatar/driver.js
# -----------------------------------------------------
"""
VASTUU:
- audio.currentTime
- frame lookup
- requestAnimationFrame

EI SAA:
- Säätää timingia
- Muuttaa tunnetta
"""

# -----------------------------------------------------
# frontend/avatar/index.js
# -----------------------------------------------------
"""
ENTRY:
- Lataa audio
- Lataa frames.json
- Käynnistää driverin
"""

# =====================================================================
# 5️⃣ KASAAMISMETODI (ENGINE → EXHAUST)
# =====================================================================

"""
1️⃣ RAKENNA FSM ENSIN
- Testaa stressi + CRACK ilman audioa

2️⃣ LISÄÄ EMOTION
- Tarkista latency + timing_drift numeroina

3️⃣ RAKENNA TTS TIMELINE
- Tulosta phoneme/viseme/aika konsoliin

4️⃣ LIITÄ AVATAR STREAM
- Varmista että frames[] on lineaarinen

5️⃣ VASTA LOPUKSI FRONTEND
- Frontend EI SAA vaikuttaa logiikkaan

SÄÄNTÖ:
Jos jokin tuntuu väärältä frontendissä,
vika on backendissä.
"""

# =====================================================================
# 6️⃣ LOPULLINEN TOTUUS
# =====================================================================
"""
Tämä järjestelmä on:
- deterministinen YLHÄÄLTÄ
- epätäydellinen ALHAALLA
- laajennettava sivusuunnassa
- PROD-KESTÄVÄ

Moottoritila on rauhallinen.
Pakoputki saa paukkua.
"""
# =====================================================================
