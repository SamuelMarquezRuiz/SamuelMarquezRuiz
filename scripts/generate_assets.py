#!/usr/bin/env python3
"""Programmatic SVG generator for Samuel Márquez Ruiz's GitHub Profile (Data Pipeline / DAG).

Generates English (`*-{dark,light}.svg`) and Spanish (`*-{dark,light}-es.svg`)
theme-adaptive SVGs into `assets/` using only the Python standard library.
"""

from __future__ import annotations

import html
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT / "assets"

THEMES: dict[str, dict[str, str]] = {
    "dark": {
        "canvas": "#090D16",
        "grid": "#162033",
        "node": "#111827",
        "node_header": "#1A2438",
        "border": "#26354D",
        "border_soft": "#1F2B3E",
        "text": "#F1F5F9",
        "muted": "#94A3B8",
        "subtle": "#78889C",
        "sky": "#38BDF8",
        "sky_soft": "#0C2D48",
        "amber": "#F59E0B",
        "amber_soft": "#3A2506",
        "emerald": "#10B981",
        "emerald_soft": "#092E23",
        "violet": "#A78BFA",
        "violet_soft": "#261B47",
        "edge": "#475569",
    },
    "light": {
        "canvas": "#F8FAFC",
        "grid": "#E2E8F0",
        "node": "#FFFFFF",
        "node_header": "#EFF4FA",
        "border": "#94A3B8",
        "border_soft": "#CBD5E1",
        "text": "#0F172A",
        "muted": "#334155",
        "subtle": "#475569",
        "sky": "#0369A1",
        "sky_soft": "#E0F2FE",
        "amber": "#B45309",
        "amber_soft": "#FEF3C7",
        "emerald": "#047857",
        "emerald_soft": "#D1FAE5",
        "violet": "#6D28D9",
        "violet_soft": "#EDE9FE",
        "edge": "#475569",
    },
}

COPY: dict[str, dict[str, Any]] = {
    "en": {
        "suffix": "",
        "availability": "OPEN TO WORK",
        "badge_w": 106,
        "header_loc": "MÁLAGA, ES · ES / EN (B2–C1)",
        "hero_title": "Data Engineering, AI & QA Automation Systems",
        "hero_sub": "Targeting Data Analyst, Data Engineer, and Junior Fullstack / QA Automation Engineer roles across EU & remote teams.",
        "hero_footer": "STREAM STATUS: HEALTHY · DUAL VET / ERASMUS COLOGNE (FEB–MAY 2026) · AI & BIG DATA SPECIALIZATION (2026–2027)",
        "hero_alt": "Event-driven career and technical architecture pipeline for Samuel Márquez Ruiz",
        "stages": [
            ("01 · INGEST", "Academic Track", "sky", [
                ("2026–2027", "Grado E: AI & Big Data"),
                ("2026", "DAM · CPIFP Alan Turing"),
                ("CORE", "Python · SQL · Java · TS"),
            ]),
            ("02 · STREAM BUS", "REWE Digital · Cologne", "amber", [
                ("topic://", "orders.online"),
                ("topic://", "orders.click_collect"),
                ("topic://", "orders.home_delivery"),
            ]),
            ("03 · QA VERIFIER", "IO Team Assertions", "emerald", [
                ("RUNNER", "Karate · Java / Groovy"),
                ("EVENT", "Kafka Payload Schema"),
                ("SINK", "SQL / DB State Check ✓"),
            ]),
            ("04 · SERVING", "Target Outputs", "violet", [
                ("BUILD 01", "BookMatch Platform"),
                ("BUILD 02", "Seismic Monitor"),
                ("BI / AI", "Power BI · Streamlit"),
            ]),
        ],
        "dag_title": "DEPENDENCY DAG // STACK & RUNTIME ECOSYSTEM",
        "dag_sub": "CLIENT → SERVICE → QA/STORAGE → ANALYTICS",
        "dag_alt": "Technology dependency graph across clients, backend streams, QA/infrastructure, and Data/AI",
        "dag_layers": [
            ("CLIENTS & UI", "violet", [
                ("Angular · TypeScript", "Web SPAs & Telemetry UI"),
                ("Kotlin · Jetpack Compose", "Native Android Clients"),
                ("C# / WPF", "Desktop Applications"),
            ]),
            ("SERVICES & STREAM", "amber", [
                ("Node.js · Express · Prisma", "REST APIs & ORM Layer"),
                ("Java · Groovy", "Backend & Test Tooling"),
                ("Apache Kafka", "Real-Time Event Streams"),
            ]),
            ("QA, DB & INFRA", "emerald", [
                ("Karate Framework", "API & Stream Assertions"),
                ("PostgreSQL · SQLite · Supabase", "Relational Persistence"),
                ("Docker · Actions · Vercel", "CI/CD & Linux/macOS"),
            ]),
            ("DATA & AI", "sky", [
                ("Python · Pandas · NumPy", "Wrangling & Pipelines"),
                ("Matplotlib · Seaborn · Streamlit", "Viz & Interactive Apps"),
                ("SQL · Excel · Power BI", "Analytics & Dashboards"),
            ]),
        ],
        "proj_header": "PRODUCTION SINKS // SELECTED SYSTEM TOPOLOGIES",
        "proj_alt": "BookMatch and Global Seismic Monitoring Web App system topologies",
        "sink1_tag": "SINK_01 // MULTIPLATFORM + BI",
        "sink1_title": "BookMatch",
        "sink1_line1": "Multiplatform book exchange & recommendation",
        "sink1_line2": "ecosystem across mobile, web, API & BI.",
        "bm_nodes": [
            ("Android + Web Clients", "Kotlin Compose · Angular", "violet"),
            ("Backend API & ORM", "Node.js · Express · Prisma", "amber"),
            ("Relational Store", "PostgreSQL Schema", "emerald"),
            ("Analytics Sink", "Power BI Dashboard", "sky"),
        ],
        "sink2_tag": "SINK_02 // GEOSPATIAL TELEMETRY",
        "sink2_title": "Global Seismic Monitoring Web App",
        "sink2_line1": "Angular telemetry app with custom Tectonic Dark",
        "sink2_line2": "UI and configurable open-source map layers.",
        "sink2_hud": "THEME: TECTONIC_DARK · LAYERS: CONFIGURABLE_OSM",
    },
    "es": {
        "suffix": "-es",
        "availability": "DISPONIBLE",
        "badge_w": 96,
        "header_loc": "MÁLAGA, ES · ES / EN (B2–C1)",
        "hero_title": "Ingeniería de Datos, IA y Automatización QA",
        "hero_sub": "Orientado a roles de Data Analyst, Data Engineer y Junior Fullstack / QA Automation en equipos europeos y remotos.",
        "hero_footer": "ESTADO: ACTIVO · FP DUAL / ERASMUS COLONIA (FEB–MAY 2026) · ESPECIALIZACIÓN IA Y BIG DATA (2026–2027)",
        "hero_alt": "Pipeline de arquitectura técnica y trayectoria profesional de Samuel Márquez Ruiz",
        "stages": [
            ("01 · INGESTA", "Trayectoria Académica", "sky", [
                ("2026–2027", "Grado E: IA y Big Data"),
                ("2026", "DAM · CPIFP Alan Turing"),
                ("BASE", "Python · SQL · Java · TS"),
            ]),
            ("02 · BUS EVENTOS", "REWE Digital · Colonia", "amber", [
                ("topic://", "orders.online"),
                ("topic://", "orders.click_collect"),
                ("topic://", "orders.home_delivery"),
            ]),
            ("03 · VERIFICADOR QA", "Aserciones Equipo IO", "emerald", [
                ("RUNNER", "Karate · Java / Groovy"),
                ("EVENTO", "Esquema Payloads Kafka"),
                ("SINK", "Validación SQL / BD ✓"),
            ]),
            ("04 · SERVICIO", "Sistemas Destino", "violet", [
                ("PROY 01", "Plataforma BookMatch"),
                ("PROY 02", "Monitor Sísmico"),
                ("BI / IA", "Power BI · Streamlit"),
            ]),
        ],
        "dag_title": "DAG DE DEPENDENCIAS // STACK Y ECOSISTEMA",
        "dag_sub": "CLIENTE → SERVICIO → QA/DATOS → ANALÍTICA",
        "dag_alt": "Grafo de dependencias tecnológicas entre clientes, backend y mensajería, QA e infraestructura y Data/IA",
        "dag_layers": [
            ("CLIENTES Y UI", "violet", [
                ("Angular · TypeScript", "SPAs Web y Telemetría"),
                ("Kotlin · Jetpack Compose", "Apps Android Nativas"),
                ("C# / WPF", "Aplicaciones Escritorio"),
            ]),
            ("SERVICIOS Y STREAM", "amber", [
                ("Node.js · Express · Prisma", "APIs REST y Capa ORM"),
                ("Java · Groovy", "Backend y Test Tooling"),
                ("Apache Kafka", "Eventos en Tiempo Real"),
            ]),
            ("QA, BD E INFRA", "emerald", [
                ("Karate Framework", "Aserciones API y Kafka"),
                ("PostgreSQL · SQLite · Supabase", "Persistencia Relacional"),
                ("Docker · Actions · Vercel", "CI/CD y Linux/macOS"),
            ]),
            ("DATA E IA", "sky", [
                ("Python · Pandas · NumPy", "Procesado y Pipelines"),
                ("Matplotlib · Seaborn · Streamlit", "Visualización y Apps"),
                ("SQL · Excel · Power BI", "Analítica y Dashboards"),
            ]),
        ],
        "proj_header": "SISTEMAS EN PRODUCCIÓN // TOPOLOGÍAS SELECCIONADAS",
        "proj_alt": "Topologías de sistema de BookMatch y Global Seismic Monitoring Web App",
        "sink1_tag": "SINK_01 // MULTIPLATAFORMA + BI",
        "sink1_title": "BookMatch",
        "sink1_line1": "Plataforma multiplataforma de intercambio y",
        "sink1_line2": "recomendación de libros en móvil, web, API y BI.",
        "bm_nodes": [
            ("Clientes Android + Web", "Kotlin Compose · Angular", "violet"),
            ("API Backend y ORM", "Node.js · Express · Prisma", "amber"),
            ("Base Relacional", "Esquema PostgreSQL", "emerald"),
            ("Capa Analítica", "Dashboard Power BI", "sky"),
        ],
        "sink2_tag": "SINK_02 // TELEMETRÍA GEOESPACIAL",
        "sink2_title": "Global Seismic Monitoring Web App",
        "sink2_line1": "App web en Angular con interfaz Tectonic Dark",
        "sink2_line2": "y capas de mapas open-source configurables.",
        "sink2_hud": "TEMA: TECTONIC_DARK · CAPAS: OSM CONFIGURABLES",
    },
}

FONT_SANS = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
FONT_MONO = "'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"


def esc(val: str) -> str:
    return html.escape(val, quote=True)


def svg_wrap(w: int, h: int, body: str, desc: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="{esc(desc)}">\n'
        f"  <title>{esc(desc)}</title>\n"
        f"{body}\n"
        f"</svg>\n"
    )


def bezier_edge(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str,
    pulse_color: str | None = None,
    duration: float = 3.2,
    begin: float = 0.0,
) -> str:
    dx = (x2 - x1) * 0.52
    d = f"M {x1:.1f} {y1:.1f} C {x1 + dx:.1f} {y1:.1f}, {x2 - dx:.1f} {y2:.1f}, {x2:.1f} {y2:.1f}"
    out = [f'  <path d="{d}" fill="none" stroke="{color}" stroke-width="1.6" stroke-dasharray="4 3"/>']
    if pulse_color:
        out.append(
            f'  <circle r="3.2" fill="{pulse_color}">'
            f'<animateMotion dur="{duration:.1f}s" begin="{begin:.1f}s" repeatCount="indefinite" path="{d}"/>'
            f"</circle>"
        )
    return "\n".join(out)


def render_pipeline_hero(t: dict[str, str], copy: dict[str, Any]) -> str:
    w, h = 880, 356
    badge_w = copy["badge_w"]
    badge_x = w - 20 - badge_w
    loc_x = badge_x - 14

    parts = [
        "  <defs>",
        '    <pattern id="pipeline-grid" width="24" height="24" patternUnits="userSpaceOnUse">',
        f'      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="{t["grid"]}" stroke-width="0.8"/>',
        "    </pattern>",
        "  </defs>",
        f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="{t["canvas"]}" stroke="{t["border"]}"/>',
        f'  <rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="11" fill="url(#pipeline-grid)"/>',
        # Top header bar
        f'  <rect x="1" y="1" width="{w - 2}" height="42" rx="11" fill="{t["node_header"]}"/>',
        f'  <line x1="1" y1="43" x2="{w - 1}" y2="43" stroke="{t["border"]}"/>',
        f'  <circle cx="20" cy="22" r="4.5" fill="{t["emerald"]}"/>',
        f'  <text x="34" y="26" font-family="{FONT_MONO}" font-size="11.5" font-weight="700" fill="{t["text"]}">PIPELINE // SAMUEL MÁRQUEZ RUIZ</text>',
        f'  <text x="{loc_x}" y="26" text-anchor="end" font-family="{FONT_MONO}" font-size="10.5" font-weight="500" fill="{t["muted"]}">{esc(copy["header_loc"])}</text>',
        # Availability pill badge with generous right margin
        f'  <rect x="{badge_x}" y="11" width="{badge_w}" height="22" rx="6" fill="{t["emerald_soft"]}" stroke="{t["emerald"]}" stroke-width="1"/>',
        f'  <text x="{badge_x + badge_w / 2:.1f}" y="25.5" text-anchor="middle" font-family="{FONT_MONO}" font-size="10" font-weight="700" fill="{t["emerald"]}">{esc(copy["availability"])}</text>',
        # Identity sub-banner
        f'  <text x="24" y="74" font-family="{FONT_SANS}" font-size="22" font-weight="700" fill="{t["text"]}" letter-spacing="-0.02em">{esc(copy["hero_title"])}</text>',
        f'  <text x="24" y="95" font-family="{FONT_SANS}" font-size="12.5" fill="{t["muted"]}">{esc(copy["hero_sub"])}</text>',
    ]

    stage_geom = [
        (24, 122, 186, 174),
        (242, 122, 198, 174),
        (472, 122, 192, 174),
        (696, 122, 160, 174),
    ]

    connectors = [
        (210, 182, 242, 172, t["sky"], 2.8, 0.0),
        (210, 224, 242, 224, t["sky"], 3.4, 0.9),
        (440, 172, 472, 172, t["amber"], 2.5, 0.3),
        (440, 214, 472, 214, t["amber"], 2.9, 1.1),
        (440, 256, 472, 256, t["amber"], 3.3, 1.7),
        (664, 192, 696, 182, t["emerald"], 2.7, 0.5),
        (664, 242, 696, 252, t["emerald"], 3.1, 1.3),
    ]
    for x1, y1, x2, y2, pulse_c, dur, beg in connectors:
        parts.append(bezier_edge(x1, y1, x2, y2, t["edge"], pulse_c, dur, beg))

    for (sx, sy, sw, sh), (stag, stitle, color_key, rows) in zip(stage_geom, copy["stages"]):
        sfg = t[color_key]
        sbg = t[f"{color_key}_soft"]
        parts.extend([
            f'  <rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="10" fill="{t["node"]}" stroke="{t["border"]}" stroke-width="1.2"/>',
            f'  <rect x="{sx}" y="{sy}" width="{sw}" height="46" rx="10" fill="{sbg}"/>',
            f'  <rect x="{sx}" y="{sy + 36}" width="{sw}" height="10" fill="{sbg}"/>',
            f'  <line x1="{sx}" y1="{sy + 46}" x2="{sx + sw}" y2="{sy + 46}" stroke="{t["border"]}"/>',
            f'  <text x="{sx + 12}" y="{sy + 19}" font-family="{FONT_MONO}" font-size="10" font-weight="700" fill="{sfg}">{esc(stag)}</text>',
            f'  <text x="{sx + 12}" y="{sy + 36}" font-family="{FONT_SANS}" font-size="12.5" font-weight="700" fill="{t["text"]}">{esc(stitle)}</text>',
        ])
        ry = sy + 64
        for rk, rv in rows:
            parts.extend([
                f'  <rect x="{sx + 10}" y="{ry}" width="{sw - 20}" height="30" rx="6" fill="{t["canvas"]}" stroke="{t["border_soft"]}" stroke-width="1"/>',
                f'  <text x="{sx + 18}" y="{ry + 12}" font-family="{FONT_MONO}" font-size="8.5" font-weight="700" fill="{sfg}">{esc(rk)}</text>',
                f'  <text x="{sx + 18}" y="{ry + 24}" font-family="{FONT_SANS}" font-size="10.8" font-weight="500" fill="{t["text"]}">{esc(rv)}</text>',
            ])
            ry += 36

    parts.append(f'  <text x="24" y="334" font-family="{FONT_MONO}" font-size="10.5" font-weight="500" fill="{t["subtle"]}">{esc(copy["hero_footer"])}</text>')
    return svg_wrap(w, h, "\n".join(parts), copy["hero_alt"])


def render_stack_dag(t: dict[str, str], copy: dict[str, Any]) -> str:
    w, h = 880, 290
    parts = [
        f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="{t["canvas"]}" stroke="{t["border"]}"/>',
        f'  <text x="24" y="30" font-family="{FONT_MONO}" font-size="11" font-weight="700" fill="{t["sky"]}">{esc(copy["dag_title"])}</text>',
        f'  <text x="{w - 24}" y="30" text-anchor="end" font-family="{FONT_MONO}" font-size="10.5" font-weight="500" fill="{t["subtle"]}">{esc(copy["dag_sub"])}</text>',
    ]

    layer_xs = [24, 240, 456, 672]
    node_w = 184
    node_h = 56
    start_y = 68
    gap_y = 14

    edges = [
        (0, 0, 1, 0),
        (0, 1, 1, 0),
        (0, 2, 2, 1),
        (1, 0, 2, 1),
        (1, 1, 2, 0),
        (1, 2, 2, 0),
        (1, 2, 3, 0),
        (2, 1, 3, 2),
        (2, 2, 3, 1),
    ]

    def node_pos(li: int, ni: int) -> tuple[float, float]:
        return layer_xs[li], start_y + ni * (node_h + gap_y)

    for l1, n1, l2, n2 in edges:
        x1, y1 = node_pos(l1, n1)
        x2, y2 = node_pos(l2, n2)
        parts.append(bezier_edge(x1 + node_w, y1 + node_h / 2, x2, y2 + node_h / 2, t["edge"], None))

    for li, (lx, (ltitle, color_key, items)) in enumerate(zip(layer_xs, copy["dag_layers"])):
        lcol = t[color_key]
        parts.append(f'  <text x="{lx}" y="56" font-family="{FONT_MONO}" font-size="10" font-weight="700" fill="{lcol}">{esc(ltitle)}</text>')
        for ni, (head, sub) in enumerate(items):
            nx, ny = node_pos(li, ni)
            parts.extend([
                f'  <rect x="{nx}" y="{ny}" width="{node_w}" height="{node_h}" rx="8" fill="{t["node"]}" stroke="{t["border"]}" stroke-width="1.1"/>',
                f'  <rect x="{nx}" y="{ny + 10}" width="3.5" height="{node_h - 20}" rx="1.5" fill="{lcol}"/>',
                f'  <text x="{nx + 13}" y="{ny + 24}" font-family="{FONT_SANS}" font-size="11" font-weight="600" fill="{t["text"]}">{esc(head)}</text>',
                f'  <text x="{nx + 13}" y="{ny + 41}" font-family="{FONT_SANS}" font-size="10.2" fill="{t["muted"]}">{esc(sub)}</text>',
                f'  <circle cx="{nx}" cy="{ny + node_h / 2}" r="2.8" fill="{t["border"]}"/>',
                f'  <circle cx="{nx + node_w}" cy="{ny + node_h / 2}" r="2.8" fill="{lcol}"/>',
            ])

    return svg_wrap(w, h, "\n".join(parts), copy["dag_alt"])


def render_projects_topology(t: dict[str, str], copy: dict[str, Any]) -> str:
    w, h = 880, 288
    parts = [
        f'  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="12" fill="{t["canvas"]}" stroke="{t["border"]}"/>',
        f'  <text x="24" y="30" font-family="{FONT_MONO}" font-size="11" font-weight="700" fill="{t["emerald"]}">{esc(copy["proj_header"])}</text>',
    ]

    # Left card: BookMatch (x=24..430, inner width=370px)
    parts.extend([
        f'  <rect x="24" y="46" width="406" height="220" rx="10" fill="{t["node"]}" stroke="{t["border"]}"/>',
        f'  <text x="42" y="70" font-family="{FONT_MONO}" font-size="10" font-weight="700" fill="{t["sky"]}">{esc(copy["sink1_tag"])}</text>',
        f'  <text x="42" y="93" font-family="{FONT_SANS}" font-size="17" font-weight="700" fill="{t["text"]}">{esc(copy["sink1_title"])}</text>',
        f'  <text x="42" y="113" font-family="{FONT_SANS}" font-size="11.5" fill="{t["muted"]}">{esc(copy["sink1_line1"])}</text>',
        f'  <text x="42" y="129" font-family="{FONT_SANS}" font-size="11.5" fill="{t["muted"]}">{esc(copy["sink1_line2"])}</text>',
    ])

    bm_geom = [
        (42, 146, 174, 44),
        (238, 146, 174, 44),
        (42, 204, 174, 44),
        (238, 204, 174, 44),
    ]
    parts.append(bezier_edge(216, 168, 238, 168, t["edge"], t["violet"], 2.4, 0.0))
    parts.append(bezier_edge(238, 180, 216, 226, t["edge"], t["amber"], 2.8, 0.7))
    parts.append(bezier_edge(216, 226, 238, 226, t["edge"], t["emerald"], 2.4, 1.2))

    for (bx, by, bw, bh), (bhead, bsub, color_key) in zip(bm_geom, copy["bm_nodes"]):
        bcol = t[color_key]
        parts.extend([
            f'  <rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="7" fill="{t["canvas"]}" stroke="{t["border_soft"]}"/>',
            f'  <circle cx="{bx + 12}" cy="{by + 16}" r="3" fill="{bcol}"/>',
            f'  <text x="{bx + 21}" y="{by + 19}" font-family="{FONT_SANS}" font-size="11" font-weight="600" fill="{t["text"]}">{esc(bhead)}</text>',
            f'  <text x="{bx + 12}" y="{by + 35}" font-family="{FONT_MONO}" font-size="9.5" fill="{t["muted"]}">{esc(bsub)}</text>',
        ])

    # Right card: Global Seismic Monitoring Web App (x=450..856, inner width=370px)
    parts.extend([
        f'  <rect x="450" y="46" width="406" height="220" rx="10" fill="{t["node"]}" stroke="{t["border"]}"/>',
        f'  <text x="468" y="70" font-family="{FONT_MONO}" font-size="10" font-weight="700" fill="{t["amber"]}">{esc(copy["sink2_tag"])}</text>',
        f'  <text x="468" y="93" font-family="{FONT_SANS}" font-size="17" font-weight="700" fill="{t["text"]}">{esc(copy["sink2_title"])}</text>',
        f'  <text x="468" y="113" font-family="{FONT_SANS}" font-size="11.5" fill="{t["muted"]}">{esc(copy["sink2_line1"])}</text>',
        f'  <text x="468" y="129" font-family="{FONT_SANS}" font-size="11.5" fill="{t["muted"]}">{esc(copy["sink2_line2"])}</text>',
    ])

    sx, sy, sw, sh = 468, 146, 370, 102
    parts.append(f'  <rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="8" fill="#070B14" stroke="{t["border"]}"/>')
    bar_count = 36
    for i in range(bar_count):
        bx = sx + 14 + i * 9.6
        norm = i / bar_count
        amp = 10 + 46 * math.exp(-((norm - 0.62) ** 2) / 0.015) + 14 * abs(math.sin(i * 0.7))
        bar_col = "#F59E0B" if amp > 38 else "#38BDF8"
        parts.append(f'  <rect x="{bx:.1f}" y="{sy + sh - 18 - amp:.1f}" width="5" height="{amp:.1f}" rx="1.5" fill="{bar_col}" opacity="0.88"/>')

    parts.append(f'  <text x="{sx + 14}" y="{sy + 20}" font-family="{FONT_MONO}" font-size="9.5" fill="#CBD5E1">{esc(copy["sink2_hud"])}</text>')
    return svg_wrap(w, h, "\n".join(parts), copy["proj_alt"])


def main() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for lang, copy in COPY.items():
        suffix = copy["suffix"]
        for theme_name, theme in THEMES.items():
            outputs = {
                f"hero-{theme_name}{suffix}.svg": render_pipeline_hero(theme, copy),
                f"stack-dag-{theme_name}{suffix}.svg": render_stack_dag(theme, copy),
                f"projects-{theme_name}{suffix}.svg": render_projects_topology(theme, copy),
            }
            for fname, content in outputs.items():
                (ASSETS_DIR / fname).write_text(content, encoding="utf-8")
                count += 1

    print(f"Generated {count} SVG assets (EN + ES, dark + light) in {ASSETS_DIR}")


if __name__ == "__main__":
    main()
