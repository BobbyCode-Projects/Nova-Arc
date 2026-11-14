#!/usr/bin/env python3
"""
Nova Arc - Multi-Page Complete Website Master Generator
Builds all 54 pages across:
  - Home: index.html
  - Solutions: solutions.html, solutions/index.html, + 6 subpages
  - Services: services.html, services/index.html, 4 domain landings + 21 subpages
  - Technology: technology.html, technology/index.html, ai-platform.html, + 6 subpages
  - Industries: industries.html, industries/index.html, who-we-serve.html, + 6 subpages
  - Connect With Us: contact.html, connect.html, connect/index.html, + 4 subpages
  - 404 Error Page: 404.html
Updates sitemap.xml and searchIndex in js/main.js
"""

import os
import re
import sys
import datetime

# Add scripts directory to path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from build_pages import generate_subpage, get_shared_header, get_shared_footer
from ecg_component import get_ecg_waveform_html
from data_services import SERVICES_PAGES
from data_services_domain2 import SERVICES_DOMAIN_2
from data_services_domain3 import SERVICES_DOMAIN_3
from data_services_domain4 import SERVICES_DOMAIN_4
from data_tech_ind_connect import TECH_IND_CONNECT_PAGES

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def write_page(rel_path, content):
    full_path = os.path.join(REPO_ROOT, rel_path)
    ensure_dir(full_path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] Written: {rel_path} ({len(content):,} bytes)")

def replace_header_and_footer(html_content, root_prefix, active_section=""):
    """
    Replaces existing <header class="site-header" id="top">...</header>
    and <footer class="site-footer">...</footer> with the unified shared components.
    """
    # Clean duplicate comments
    html_content = re.sub(r'(?:<!--\s*(?:Header|Navigation|FOOTER)[^>]*-->\s*)+', '', html_content)
    # Replace header
    header_pattern = re.compile(r'<header class="site-header" id="top">.*?</header>', re.DOTALL)
    new_header = get_shared_header(root_prefix, active_section)
    if header_pattern.search(html_content):
        html_content = header_pattern.sub(new_header, html_content, count=1)
    else:
        print("    [WARN] Header pattern not found in file")

    # Replace footer
    footer_pattern = re.compile(r'<footer class="site-footer">.*?</footer>', re.DOTALL)
    new_footer = get_shared_footer(root_prefix)
    if footer_pattern.search(html_content):
        html_content = footer_pattern.sub(new_footer, html_content, count=1)
    else:
        print("    [WARN] Footer pattern not found in file")

    # Clean up any duplicate script tags and normalize main.js and style.css
    html_content = re.sub(r'<script[^>]*main\.js[^>]*></script>', '', html_content)
    html_content = re.sub(r'<!--\s*Scripts\s*-->\s*', '', html_content)
    html_content = re.sub(r'\s*</body>', f'\n\n  <!-- Scripts -->\n  <script src="{root_prefix}js/main.js?v=4.0"></script>\n</body>', html_content)

    # Normalize style.css to v=4.0
    html_content = re.sub(r'href="[^"]*css/style\.css(\?v=[^"]*)?"', f'href="{root_prefix}css/style.css?v=4.0"', html_content)

    # Normalize Favicon suite
    favicons = f'''<!-- Favicon & Brand Icons -->
  <link rel="icon" type="image/svg+xml" href="{root_prefix}images/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="{root_prefix}images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{root_prefix}images/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{root_prefix}images/apple-touch-icon.png">
  <link rel="shortcut icon" href="{root_prefix}favicon.ico">
  <link rel="manifest" href="{root_prefix}site.webmanifest">'''
    html_content = re.sub(r'<!--\s*Favicon[^-]*-->\s*<link rel="icon"[^>]*>', favicons, html_content)
    html_content = re.sub(r'<link rel="icon" type="image/png" href="[^"]*images/nova-arc-logo\.png">', favicons, html_content)

    # Ensure body has subpage-body class for root internal pages (index.html is excluded)
    if '<body class="subpage-body">' not in html_content:
        html_content = re.sub(r'<body(?:\s+class="[^"]*")?>', '<body class="subpage-body">', html_content, count=1)

    return html_content

def generate_all_subpages():
    print("\n--- Generating 41 Subpages ---")
    all_subpage_defs = (
        SERVICES_PAGES +
        SERVICES_DOMAIN_2 +
        SERVICES_DOMAIN_3 +
        SERVICES_DOMAIN_4 +
        TECH_IND_CONNECT_PAGES
    )
    
    generated_count = 0
    for page_def in all_subpage_defs:
        rel_path = page_def["rel_path"]
        html = generate_subpage(
            rel_path=rel_path,
            root_prefix="../",
            category_badge=page_def["category_badge"],
            page_title=page_def["page_title"],
            page_subtitle=page_def["page_subtitle"],
            breadcrumbs=page_def["breadcrumbs"],
            overview_paragraphs=page_def["overview_paragraphs"],
            capabilities=page_def["capabilities"],
            challenges=page_def["challenges"],
            workflow_steps=page_def["workflow_steps"],
            outcomes=page_def["outcomes"],
            related_links=page_def["related_links"],
            seo_desc=page_def["seo_desc"],
            use_cases=page_def.get("use_cases"),
            integrations=page_def.get("integrations"),
            considerations=page_def.get("considerations"),
            faqs=page_def.get("faqs"),
            what_we_deliver=page_def.get("what_we_deliver"),
            industries_served=page_def.get("industries_served"),
            why_choose_us=page_def.get("why_choose_us")
        )
        write_page(rel_path, html)
        generated_count += 1
    
    print(f"Total subpages built: {generated_count}")
    return all_subpage_defs

def generate_technology_page():
    tech_path = os.path.join(REPO_ROOT, "technology.html")
    if os.path.exists(tech_path):
        with open(tech_path, "r", encoding="utf-8") as f:
            tech_html = f.read()
        tech_html = replace_header_and_footer(tech_html, "", "technology")
        tech_html = tech_html.replace(
            "<title>Enterprise Technology &amp; Automation Platform | Nova Arc</title>",
            "<title>Technology &amp; Platform Architecture | Nova Arc</title>"
        )
        tech_html = tech_html.replace(
            "https://novaarctech.in/ai-platform.html",
            "https://novaarctech.in/technology.html"
        )
        with open(tech_path, "w", encoding="utf-8") as f:
            f.write(tech_html)
        ai_platform_path = os.path.join(REPO_ROOT, "ai-platform.html")
        with open(ai_platform_path, "w", encoding="utf-8") as f:
            f.write(tech_html)
        print("  [OK] Updated technology.html and synchronized ai-platform.html")

def update_root_pages():
    print("\n--- Updating Root Pages with Unified Header & Footer ---")

    # 1. index.html - Strictly excluded per Project Requirements
    print("  [EXCLUDED] index.html (Homepage strictly preserved and untouched)")

    # 2. services.html
    services_path = os.path.join(REPO_ROOT, "services.html")
    if os.path.exists(services_path):
        with open(services_path, "r", encoding="utf-8") as f:
            serv_html = f.read()
        serv_html = replace_header_and_footer(serv_html, "", "services")
        with open(services_path, "w", encoding="utf-8") as f:
            f.write(serv_html)
        print("  [OK] Updated services.html header & footer")

    # 4. contact.html & connect.html
    contact_path = os.path.join(REPO_ROOT, "contact.html")
    if os.path.exists(contact_path):
        with open(contact_path, "r", encoding="utf-8") as f:
            con_html = f.read()
        con_html = replace_header_and_footer(con_html, "", "connect")
        with open(contact_path, "w", encoding="utf-8") as f:
            f.write(con_html)
        print("  [OK] Updated contact.html header & footer")
        # Sync to connect.html
        with open(os.path.join(REPO_ROOT, "connect.html"), "w", encoding="utf-8") as f:
            f.write(con_html)
        print("  [OK] Synchronized connect.html")

    # 5. technology.html & ai-platform.html
    generate_technology_page()

    # 6. industries.html & who-we-serve.html
    who_we_serve_path = os.path.join(REPO_ROOT, "who-we-serve.html")
    if os.path.exists(who_we_serve_path):
        with open(who_we_serve_path, "r", encoding="utf-8") as f:
            ind_html = f.read()
        ind_html = replace_header_and_footer(ind_html, "", "industries")
        ind_html = ind_html.replace(
            "https://novaarctech.in/who-we-serve.html",
            "https://novaarctech.in/industries.html"
        )
        with open(os.path.join(REPO_ROOT, "industries.html"), "w", encoding="utf-8") as f:
            f.write(ind_html)
        with open(who_we_serve_path, "w", encoding="utf-8") as f:
            f.write(ind_html)
        print("  [OK] Created industries.html and synchronized who-we-serve.html")

def generate_directory_indexes():
    print("\n--- Generating Directory Index Aliases ---")
    mappings = [
        ("services/index.html", "services.html", "services"),
        ("technology/index.html", "technology.html", "technology"),
        ("industries/index.html", "industries.html", "industries"),
        ("connect/index.html", "contact.html", "connect")
    ]

    for rel_target, src_root_file, active_sec in mappings:
        src_path = os.path.join(REPO_ROOT, src_root_file)
        if os.path.exists(src_path):
            with open(src_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Adapt paths from root to 1 level deep:
            # 1. Replace header and footer with root_prefix="../"
            content = replace_header_and_footer(content, "../", active_sec)
            # 2. Fix CSS and JS links in head and body
            content = content.replace('href="css/', 'href="../css/')
            content = content.replace('src="js/', 'src="../js/')
            content = content.replace('href="images/', 'href="../images/')
            content = content.replace('src="images/', 'src="../images/')
            content = content.replace('href="favicon', 'href="../favicon')

            write_page(rel_target, content)

    # Ensure industries/retail.html exists as alias of industries/retail-ecommerce.html
    retail_src = os.path.join(REPO_ROOT, "industries", "retail-ecommerce.html")
    if os.path.exists(retail_src):
        with open(retail_src, "r", encoding="utf-8") as f:
            write_page("industries/retail.html", f.read())

def generate_about_page():
    print("\n--- Generating About Us Page (about.html) ---")
    header_html = get_shared_header("", "")
    footer_html = get_shared_footer("")

    about_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Nova Arc | Enterprise Technology &amp; Systems Engineering</title>
  <meta name="description" content="Nova Arc is an enterprise technology engineering firm headquartered in Hyderabad. We build connected commerce platforms, enterprise business solutions, real-time IoT monitoring, and governed AI automation.">
  <link rel="canonical" href="https://novaarctech.in/about.html">

  <!-- SEO & Social Meta Tags -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Nova Arc Technologies">
  <meta property="og:title" content="About Nova Arc | Enterprise Technology &amp; Systems Engineering">
  <meta property="og:description" content="Nova Arc is an enterprise technology engineering firm headquartered in Hyderabad. We build connected commerce platforms, enterprise business solutions, real-time IoT monitoring, and governed AI automation.">
  <meta property="og:url" content="https://novaarctech.in/about.html">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="About Nova Arc | Enterprise Technology &amp; Systems Engineering">
  <meta name="twitter:description" content="Nova Arc is an enterprise technology engineering firm headquartered in Hyderabad. We build connected commerce platforms, enterprise business solutions, real-time IoT monitoring, and governed AI automation.">

  <!-- Favicon & Brand Icons -->
  <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="images/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="manifest" href="site.webmanifest">

  <!-- Google Font: Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Core Stylesheet -->
  <link rel="stylesheet" href="css/style.css?v=4.0">

  <!-- Google tag (gtag.js) - Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-NOVAARC001"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-NOVAARC001', {{
      'anonymize_ip': true,
      'cookie_flags': 'SameSite=None;Secure'
    }});
  </script>
</head>
<body class="subpage-body">

{header_html}

  <main>
    <!-- ========================================================================
         HERO SECTION: ABOUT NOVA ARC (EXECUTIVE CENTERED WITH ECG WAVE)
         ======================================================================== -->
    <section class="solutions-hero-ags" style="min-height: 100vh; min-height: 100dvh; display: flex; flex-direction: column; justify-content: center; box-sizing: border-box; padding-top: calc(75px + clamp(16px, 2.5vw, 36px)); padding-bottom: clamp(20px, 3vw, 40px);">
      <div class="hero-orchestrated-glow-cyan"></div>
      <div class="hero-orchestrated-glow-blue"></div>
      {get_ecg_waveform_html()}

      <div class="container hero-container-ags">
        <div style="max-width: 920px; margin: 0 auto; text-align: center;">
          <nav class="breadcrumb-nav" aria-label="Breadcrumb" style="margin-bottom: var(--space-sm); justify-content: center; display: flex;">
            <ol class="breadcrumb-list" style="display: flex; gap: 8px; list-style: none; padding: 0; margin: 0; font-size: 0.85rem; color: #94A3B8;">
              <li><a href="index.html" style="color: #38BDF8; text-decoration: none;">Home</a></li>
              <li style="color: #64748B;">/</li>
              <li style="color: #FFFFFF; font-weight: 600;">About Nova Arc</li>
            </ol>
          </nav>
          
          <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; letter-spacing: 0.1em; display: inline-block; margin-bottom: 10px;">
            SYSTEMS ENGINEERING &bull; ENTERPRISE PLATFORMS
          </span>

          <h1 class="hero-title-ags" style="font-size: clamp(2.4rem, 4.2vw, 3.8rem); line-height: 1.15; font-weight: 800; color: #FFFFFF; margin-bottom: 20px;">
            Engineering Connected Systems for the Modern Enterprise
          </h1>

          <p class="hero-subtitle-ags" style="font-size: 1.18rem; line-height: 1.7; color: #CBD5E1; margin: 0 auto 32px; max-width: 780px;">
            Headquartered in Laxmi Cyber City, Hyderabad, Nova Arc designs, builds, and deploys high-performance software architectures across digital commerce, enterprise operational systems, intelligent IoT telemetry, and governed artificial intelligence.
          </p>

          <div class="hero-actions-ags" style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap; margin-bottom: var(--space-3xl);">
            <a href="contact.html" class="btn btn-consultation-ags">
              <span>Discuss Your Project</span>
              <svg class="btn-arrow-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </a>
            <a href="services.html" class="btn btn-outline-white">
              <span>Explore All Services</span>
            </a>
            <a href="tel:04046146093" class="btn btn-outline-white" style="border-color: rgba(56, 189, 248, 0.4); color: #38BDF8;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="margin-right: 6px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
              <span>040-46146093</span>
            </a>
          </div>

          <!-- Quick Executive Highlights Cards -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; text-align: left;">
            <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 18px 20px;">
              <div style="font-size: 1.8rem; font-weight: 800; color: #38BDF8; line-height: 1; margin-bottom: 6px;">04</div>
              <div style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">Technology Domains</div>
              <div style="font-size: 0.8rem; color: #94A3B8;">Commerce, ERP, IoT, AI</div>
            </div>
            <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 18px 20px;">
              <div style="font-size: 1.8rem; font-weight: 800; color: #10B981; line-height: 1; margin-bottom: 6px;">100%</div>
              <div style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">Deterministic Design</div>
              <div style="font-size: 0.8rem; color: #94A3B8;">Verifiable state machines</div>
            </div>
            <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 18px 20px;">
              <div style="font-size: 1.8rem; font-weight: 800; color: #38BDF8; line-height: 1; margin-bottom: 6px;">Zero-Trust</div>
              <div style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">Enterprise Security</div>
              <div style="font-size: 0.8rem; color: #94A3B8;">TLS 1.3 &amp; strict RBAC</div>
            </div>
            <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 18px 20px;">
              <div style="font-size: 1.8rem; font-weight: 800; color: #F59E0B; line-height: 1; margin-bottom: 6px;">Hyderabad HQ</div>
              <div style="font-size: 0.95rem; font-weight: 700; color: #FFFFFF; margin-bottom: 4px;">Laxmi Cyber City</div>
              <div style="font-size: 0.8rem; color: #94A3B8;">Kondapur Technology Hub</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 1: OUR MISSION & PURPOSE (LIGHT SLATE)
         ======================================================================== -->
    <section class="section subpage-section-light-alt" style="background: #F8FAFC; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; padding: var(--space-4xl) 0;">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: clamp(32px, 4vw, 56px); align-items: center;">
          <!-- Left Column: Narrative -->
          <div>
            <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; letter-spacing: 0.08em;">OUR MISSION</span>
            <h2 style="font-size: clamp(2rem, 3.2vw, 2.6rem); font-weight: 800; color: #0F172A; margin: 12px 0 20px; line-height: 1.25; letter-spacing: -0.02em;">
              Building Dependable Technology That Connects Every Facet of Your Enterprise
            </h2>
            <p style="color: #334155; font-size: 1.08rem; line-height: 1.7; margin-bottom: 18px;">
              Modern enterprises face an operational dilemma: inflexible legacy software that cannot keep up with digital demands, and experimental technologies that lack the reliability required for mission-critical operations.
            </p>
            <p style="color: #475569; font-size: 0.98rem; line-height: 1.7; margin-bottom: 24px;">
              At Nova Arc, we believe technology should be dependable, verifiable, and purpose-built. Rather than deploying disconnected tools, we design unified architectures where transactional databases, client-facing storefronts, and automated workflows operate seamlessly as one cohesive system.
            </p>
            <div style="display: flex; gap: 16px; flex-wrap: wrap;">
              <a href="services.html" class="btn btn-consultation-ags" style="padding: 10px 22px; font-size: 0.92rem;">
                <span>Explore Capabilities</span>
              </a>
              <a href="contact.html" class="btn btn-outline-white" style="color: #0B2545; border-color: #CBD5E1; padding: 10px 22px; font-size: 0.92rem;">
                <span>Speak with an Architect</span>
              </a>
            </div>
          </div>

          <!-- Right Column: Delivery Assurances Card -->
          <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: clamp(24px, 3vw, 36px); box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.06);">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
              <div style="width: 42px; height: 42px; border-radius: 10px; background: #E0F2FE; display: flex; align-items: center; justify-content: center; color: #0284C7;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              </div>
              <div>
                <h3 style="font-size: 1.2rem; font-weight: 700; color: #0F172A; margin: 0;">Enterprise Guarantees</h3>
                <span style="font-size: 0.82rem; color: #64748B;">Core engineering commitments to our partners</span>
              </div>
            </div>

            <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 16px;">
              <li style="display: flex; gap: 12px; align-items: flex-start;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg>
                <div>
                  <strong style="color: #0F172A; font-size: 0.95rem; display: block;">Zero Vendor Lock-In</strong>
                  <span style="color: #475569; font-size: 0.88rem;">Open standard APIs, modular microservices, and portable infrastructure deployed on your cloud of choice.</span>
                </div>
              </li>
              <li style="display: flex; gap: 12px; align-items: flex-start;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg>
                <div>
                  <strong style="color: #0F172A; font-size: 0.95rem; display: block;">Idempotent &amp; Deterministic Code</strong>
                  <span style="color: #475569; font-size: 0.88rem;">Strict state-machine logic preventing duplicate orders, phantom charges, or dropped operational messages.</span>
                </div>
              </li>
              <li style="display: flex; gap: 12px; align-items: flex-start;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg>
                <div>
                  <strong style="color: #0F172A; font-size: 0.95rem; display: block;">Sub-Second Real-Time Telemetry</strong>
                  <span style="color: #475569; font-size: 0.88rem;">IoT streaming engines and event buses providing live visibility across inventory, orders, and equipment.</span>
                </div>
              </li>
              <li style="display: flex; gap: 12px; align-items: flex-start;">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg>
                <div>
                  <strong style="color: #0F172A; font-size: 0.95rem; display: block;">Enterprise Compliance &amp; RBAC</strong>
                  <span style="color: #475569; font-size: 0.88rem;">Role-based access controls, complete audit logging, and strict data governance embedded from day one.</span>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 2: FOUR CORE ENGINEERING PRINCIPLES (DARK NAVY)
         ======================================================================== -->
    <section class="section subpage-section-dark" style="background: #08111F; border-bottom: 1px solid rgba(255,255,255,0.08); padding: var(--space-4xl) 0;">
      <div class="container">
        <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
          <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; letter-spacing: 0.08em;">FOUNDATIONAL PILLARS</span>
          <h2 style="font-size: clamp(2rem, 3.2vw, 2.6rem); font-weight: 800; color: #FFFFFF; margin: 10px 0 16px; line-height: 1.25;">Four Core Engineering Principles</h2>
          <p style="color: #CBD5E1; font-size: 1.05rem; line-height: 1.65;">
            The foundational architectural standards that guide every software component, integration pipeline, and AI workflow we engineer.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
          <!-- Principle 1 -->
          <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 28px; transition: transform 0.2s ease, border-color 0.2s ease;">
            <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(56, 189, 248, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: #38BDF8;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
            </div>
            <h3 style="font-size: 1.2rem; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Deterministic Systems Design</h3>
            <p style="font-size: 0.92rem; color: #94A3B8; line-height: 1.65; margin: 0;">
              Production systems cannot rely on guesswork. We design deterministic finite state machines, comprehensive error recovery routines, and rigorous idempotency across every data transaction.
            </p>
          </div>

          <!-- Principle 2 -->
          <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 28px; transition: transform 0.2s ease, border-color 0.2s ease;">
            <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(56, 189, 248, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: #38BDF8;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
            </div>
            <h3 style="font-size: 1.2rem; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Operational Continuity</h3>
            <p style="font-size: 0.92rem; color: #94A3B8; line-height: 1.65; margin: 0;">
              Eliminate information silos. We engineer bi-directional connectors that synchronize digital storefronts, warehouse inventory, billing ledgers, and CRM records without manual re-entry.
            </p>
          </div>

          <!-- Principle 3 -->
          <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 28px; transition: transform 0.2s ease, border-color 0.2s ease;">
            <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(56, 189, 248, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: #38BDF8;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            </div>
            <h3 style="font-size: 1.2rem; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Real-Time Observability</h3>
            <p style="font-size: 0.92rem; color: #94A3B8; line-height: 1.65; margin: 0;">
              Operational blind spots lead to costly downtime. We embed continuous telemetry, IoT sensor feeds, and automated threshold alerts directly into intuitive executive dashboards.
            </p>
          </div>

          <!-- Principle 4 -->
          <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 14px; padding: 28px; transition: transform 0.2s ease, border-color 0.2s ease;">
            <div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(56, 189, 248, 0.15); display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: #38BDF8;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
            </div>
            <h3 style="font-size: 1.2rem; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">Governed AI &amp; Oversight</h3>
            <p style="font-size: 0.92rem; color: #94A3B8; line-height: 1.65; margin: 0;">
              AI must be auditable and safe. We build intelligent agents and document processing pipelines bounded by deterministic business rules, strict RBAC, and human-in-the-loop signoffs.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 3: HOW WE DELIVER (5-STAGE METHODOLOGY) (LIGHT)
         ======================================================================== -->
    <section class="section subpage-section-light" style="background: #FFFFFF; border-bottom: 1px solid #E2E8F0; padding: var(--space-4xl) 0;">
      <div class="container">
        <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
          <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; letter-spacing: 0.08em;">STRUCTURED LIFECYCLE</span>
          <h2 style="font-size: clamp(2rem, 3.2vw, 2.6rem); font-weight: 800; color: #0F172A; margin: 10px 0 16px; line-height: 1.25;">Our Engineering &amp; Delivery Methodology</h2>
          <p style="color: #475569; font-size: 1.05rem; line-height: 1.65;">
            A disciplined, transparent delivery framework engineered to minimize operational disruption and guarantee measurable ROI.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px;">
          <!-- Stage 1 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; position: relative;">
            <div style="font-size: 0.78rem; font-weight: 800; color: #0284C7; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;">Phase 01</div>
            <h4 style="font-size: 1.1rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Discovery &amp; Systems Audit</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.55; margin: 0;">Detailed assessment of your current workflows, APIs, legacy software, and operational pain points.</p>
          </div>

          <!-- Stage 2 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; position: relative;">
            <div style="font-size: 0.78rem; font-weight: 800; color: #0284C7; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;">Phase 02</div>
            <h4 style="font-size: 1.1rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Architecture Blueprint</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.55; margin: 0;">Creation of comprehensive data schemas, state transition diagrams, interface mocks, and integration specs.</p>
          </div>

          <!-- Stage 3 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; position: relative;">
            <div style="font-size: 0.78rem; font-weight: 800; color: #0284C7; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;">Phase 03</div>
            <h4 style="font-size: 1.1rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Modular Development</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.55; margin: 0;">Agile software engineering with automated unit testing, continuous integration, and security scanning.</p>
          </div>

          <!-- Stage 4 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; position: relative;">
            <div style="font-size: 0.78rem; font-weight: 800; color: #0284C7; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;">Phase 04</div>
            <h4 style="font-size: 1.1rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Staged Integration</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.55; margin: 0;">Safe parallel testing, canary deployments, and automated validation alongside legacy systems.</p>
          </div>

          <!-- Stage 5 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; position: relative;">
            <div style="font-size: 0.78rem; font-weight: 800; color: #0284C7; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 8px;">Phase 05</div>
            <h4 style="font-size: 1.1rem; color: #0F172A; margin-bottom: 8px; font-weight: 700;">Telemetry &amp; Scaling</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.55; margin: 0;">Continuous observability, automated incident response, performance profiling, and capacity scaling.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 4: HEADQUARTERS & GLOBAL REACH (LIGHT SLATE)
         ======================================================================== -->
    <section class="section subpage-section-light-alt" style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0; padding: var(--space-4xl) 0;">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 36px; align-items: center;">
          <div>
            <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; letter-spacing: 0.08em;">HYDERABAD HEADQUARTERS</span>
            <h2 style="font-size: clamp(1.8rem, 3vw, 2.4rem); font-weight: 800; color: #0F172A; margin: 12px 0 16px; line-height: 1.3;">
              Engineered in Hyderabad’s Technology Corridor
            </h2>
            <p style="color: #475569; font-size: 1.02rem; line-height: 1.7; margin-bottom: 24px;">
              Nova Arc is located in Laxmi Cyber City, Whitefields, Kondapur &mdash; the epicenter of Hyderabad’s enterprise technology and IT innovation ecosystem.
            </p>
            <div style="display: flex; flex-direction: column; gap: 16px;">
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="width: 36px; height: 36px; border-radius: 8px; background: #E0F2FE; display: flex; align-items: center; justify-content: center; color: #0284C7; flex-shrink: 0;">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                </div>
                <div>
                  <strong style="color: #0F172A; display: block; font-size: 0.95rem;">Registered Campus Address</strong>
                  <span style="color: #64748B; font-size: 0.9rem;">BP Raju Marg, Laxmi Cyber City, Whitefields, Kondapur, Telangana &ndash; 500081</span>
                </div>
              </div>
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="width: 36px; height: 36px; border-radius: 8px; background: #E0F2FE; display: flex; align-items: center; justify-content: center; color: #0284C7; flex-shrink: 0;">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                </div>
                <div>
                  <strong style="color: #0F172A; display: block; font-size: 0.95rem;">Direct Telephone</strong>
                  <a href="tel:04046146093" style="color: #0284C7; text-decoration: none; font-size: 0.92rem; font-weight: 600;">040-46146093</a>
                </div>
              </div>
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <div style="width: 36px; height: 36px; border-radius: 8px; background: #E0F2FE; display: flex; align-items: center; justify-content: center; color: #0284C7; flex-shrink: 0;">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                </div>
                <div>
                  <strong style="color: #0F172A; display: block; font-size: 0.95rem;">Electronic Mail Directory</strong>
                  <span style="color: #64748B; font-size: 0.9rem;">info@novaarctech.in &bull; support@novaarctech.in</span>
                </div>
              </div>
            </div>
          </div>

          <div style="background: linear-gradient(135deg, #07172B 0%, #0B2545 100%); border-radius: 16px; padding: 36px; color: #FFFFFF; border: 1px solid rgba(56, 189, 248, 0.25); box-shadow: 0 12px 30px rgba(0,0,0,0.15);">
            <span style="color: #38BDF8; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">GET IN TOUCH</span>
            <h3 style="font-size: 1.6rem; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Partner with Nova Arc</h3>
            <p style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 24px;">
              Ready to modernize your operations or integrate intelligent automation into your enterprise infrastructure? Our engineering leads are ready to collaborate.
            </p>
            <div style="display: flex; flex-direction: column; gap: 12px;">
              <a href="contact.html" class="btn btn-consultation-ags" style="justify-content: center; padding: 12px 20px;">
                <span>Start a Project Discussion</span>
                <svg class="btn-arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
              </a>
              <a href="connect/project-enquiry.html" class="btn btn-outline-white" style="justify-content: center; padding: 12px 20px;">
                <span>Detailed Project RFP Form</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 5: BOTTOM CALL-TO-ACTION BANNER (DARK NAVY)
         ======================================================================== -->
    <section class="section" style="background: linear-gradient(135deg, #08111F 0%, #0B2545 100%); padding: 70px 0; text-align: center; color: #FFFFFF; border-top: 1px solid rgba(255,255,255,0.08);">
      <div class="container" style="max-width: 800px;">
        <h2 style="font-size: clamp(2rem, 3.2vw, 2.6rem); font-weight: 800; color: #FFFFFF; margin-bottom: 14px;">
          Build Smarter. Operate Better. Scale Faster.
        </h2>
        <p style="color: #CBD5E1; font-size: 1.1rem; line-height: 1.6; margin-bottom: 30px;">
          Connect with Nova Arc’s enterprise architecture leads today to design your next competitive advantage.
        </p>
        <div style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap;">
          <a href="contact.html" class="btn btn-consultation-ags" style="padding: 14px 32px;">
            <span>Schedule Architecture Consultation</span>
            <svg class="btn-arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
          <a href="connect/general-enquiries.html" class="btn btn-outline-white" style="padding: 14px 28px;">
            <span>General Enquiries</span>
          </a>
        </div>
      </div>
    </section>
  </main>

{footer_html}

  <!-- Scripts -->
  <script src="js/main.js?v=4.0"></script>
</body>
</html>"""

    write_page("about.html", about_html)

def generate_404_page():
    print("\n--- Generating 404 Error Page ---")
    header_html = get_shared_header("", "")
    footer_html = get_shared_footer("")

    page_404_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Page Not Found (404) | Nova Arc</title>
  <meta name="description" content="The page you requested could not be found. Explore Nova Arc's services, technology, and industries.">
  <meta name="robots" content="noindex, follow">

  <!-- Favicon & Brand Icons -->
  <link rel="icon" type="image/svg+xml" href="images/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="images/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="manifest" href="site.webmanifest">

  <!-- Fonts & Core Stylesheet -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v=4.0">
</head>
<body class="subpage-body">

{header_html}

  <!-- Error 404 Hero (Dark Navy) -->
  <section class="error-hero-dark" style="position: relative; overflow: hidden; background: radial-gradient(circle at 50% 30%, rgba(31, 111, 235, 0.15) 0%, transparent 70%), #08111F; color: #FFFFFF; padding: calc(75px + var(--space-4xl)) 0 var(--space-3xl); text-align: center;">
    <div class="hero-orchestrated-glow-cyan"></div>
    <div class="hero-orchestrated-glow-blue"></div>
    {get_ecg_waveform_html()}
    <div class="container" style="position: relative; z-index: 5; max-width: 860px; margin: 0 auto;">
      <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; letter-spacing: 0.1em; font-size: 0.95rem;">ERROR 404</span>
      <h1 style="font-size: clamp(2.5rem, 5vw, 4.2rem); font-weight: 900; color: #FFFFFF; margin: 12px 0 18px; letter-spacing: -0.02em;">
        Page Not Found
      </h1>
      <p style="color: #CBD5E1; font-size: 1.15rem; max-width: 620px; margin: 0 auto var(--space-2xl); line-height: 1.65;">
        The page you are looking for may have been moved, renamed, or is temporarily unavailable. Let us help you find what you need across Nova Arc’s technology suite.
      </p>

      <div style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap;">
        <a href="index.html" class="btn btn-consultation-ags" style="padding: 12px 28px;">
          <span>Return to Homepage</span>
          <svg class="btn-arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
        </a>
        <a href="services.html" class="btn btn-outline-white" style="padding: 12px 24px;">
          <span>Browse All Services</span>
        </a>
        <a href="contact.html" class="btn btn-outline-white" style="padding: 12px 24px;">
          <span>Contact Our Team</span>
        </a>
      </div>
    </div>
  </section>

  <!-- Popular Exploration Cards Grid (Light Slate) -->
  <section class="subpage-section-light-alt" style="background: #F8FAFC; border-top: 1px solid #E2E8F0; padding: var(--space-4xl) 0;">
    <div class="container" style="max-width: 960px; margin: 0 auto;">
      <div style="text-align: center; margin-bottom: var(--space-2xl);">
        <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.825rem;">NAVIGATE NOVA ARC</span>
        <h2 style="font-size: 2rem; font-weight: 800; color: #0F172A; margin: 8px 0 10px;">Popular Areas of Exploration</h2>
        <p style="color: #475569; font-size: 1.05rem;">Quick links to key enterprise platforms and service domains.</p>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: var(--space-lg);">
        <a href="services.html" class="card" style="padding: var(--space-lg); text-decoration: none; display: block; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); box-shadow: 0 4px 16px -2px rgba(11,37,69,0.05); transition: all 0.2s ease;">
          <span style="font-size: 0.72rem; color: #0284C7; background: #E0F2FE; font-weight: 700; text-transform: uppercase; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px;">Catalog</span>
          <h4 style="font-size: 1.1rem; color: #0F172A; margin: 6px 0 4px; font-weight: 700;">Services Catalog &rarr;</h4>
          <p style="color: #475569; font-size: 0.85rem; margin: 0; line-height: 1.45;">Detailed implementation capabilities across 4 technology domains.</p>
        </a>
        <a href="technology.html" class="card" style="padding: var(--space-lg); text-decoration: none; display: block; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); box-shadow: 0 4px 16px -2px rgba(11,37,69,0.05); transition: all 0.2s ease;">
          <span style="font-size: 0.72rem; color: #0284C7; background: #E0F2FE; font-weight: 700; text-transform: uppercase; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px;">Architecture</span>
          <h4 style="font-size: 1.1rem; color: #0F172A; margin: 6px 0 4px; font-weight: 700;">Technology Platform &rarr;</h4>
          <p style="color: #475569; font-size: 0.85rem; margin: 0; line-height: 1.45;">Agentic AI, real-time IoT telemetry, enterprise integration, and data analytics.</p>
        </a>
        <a href="industries.html" class="card" style="padding: var(--space-lg); text-decoration: none; display: block; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); box-shadow: 0 4px 16px -2px rgba(11,37,69,0.05); transition: all 0.2s ease;">
          <span style="font-size: 0.72rem; color: #0284C7; background: #E0F2FE; font-weight: 700; text-transform: uppercase; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px;">Sectors</span>
          <h4 style="font-size: 1.1rem; color: #0F172A; margin: 6px 0 4px; font-weight: 700;">Industries We Serve &rarr;</h4>
          <p style="color: #475569; font-size: 0.85rem; margin: 0; line-height: 1.45;">FoodTech, retail commerce, manufacturing, logistics, healthcare, and enterprise.</p>
        </a>
      </div>
          <p style="color: #475569; font-size: 0.85rem; margin: 0; line-height: 1.45;">FoodTech, retail commerce, manufacturing, logistics, healthcare, and enterprise.</p>
        </a>
      </div>
    </div>
  </section>

{footer_html}

  <!-- Scripts -->
  <script src="js/main.js?v=4.0"></script>
</body>
</html>
"""
    write_page("404.html", page_404_html)

def generate_sitemap(all_subpages):
    print("\n--- Generating sitemap.xml ---")
    urls = [
        # Root & Core Landing Pages
        ("https://novaarctech.in/", "1.0", "weekly"),
        ("https://novaarctech.in/index.html", "1.0", "weekly"),
        ("https://novaarctech.in/about.html", "0.85", "monthly"),
        ("https://novaarctech.in/services.html", "0.9", "weekly"),
        ("https://novaarctech.in/technology.html", "0.9", "weekly"),
        ("https://novaarctech.in/industries.html", "0.9", "weekly"),
        ("https://novaarctech.in/contact.html", "0.8", "monthly"),
        ("https://novaarctech.in/connect.html", "0.8", "monthly"),
        ("https://novaarctech.in/ai-platform.html", "0.8", "weekly"),
        ("https://novaarctech.in/who-we-serve.html", "0.8", "weekly"),
    ]

    for p in all_subpages:
        url = f"https://novaarctech.in/{p['rel_path']}"
        priority = "0.85" if "services/" in p['rel_path'] and p['rel_path'].count('/') == 1 else "0.8"
        urls.append((url, priority, "monthly"))

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]

    today = datetime.date.today().isoformat()
    for loc, prio, freq in urls:
        xml_lines.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>""")

    xml_lines.append('</urlset>')
    sitemap_content = "\n".join(xml_lines) + "\n"
    write_page("sitemap.xml", sitemap_content)
    print(f"Total URLs in sitemap: {len(urls)}")

def update_search_index(all_subpages):
    print("\n--- Updating searchIndex in js/main.js ---")
    main_js_path = os.path.join(REPO_ROOT, "js", "main.js")
    with open(main_js_path, "r", encoding="utf-8") as f:
        js_content = f.read()

    # Build comprehensive search index entries
    entries = []
    
    # 1. Main landing pages
    entries.append("""    {
      title: 'Nova Arc Homepage',
      category: 'Main Navigation',
      desc: 'Engineering intelligent solutions for a connected business world. Digital commerce, enterprise systems, and AI automation.',
      url: rootPrefix + 'index.html',
      tags: ['home', 'overview', 'nova arc', 'engineering', 'solutions']
    }""")
    entries.append("""    {
      title: 'Full Services Catalog',
      category: 'Services',
      desc: 'Complete engineering services across 4 core domains: Digital Commerce, Enterprise, Monitoring, and AI.',
      url: rootPrefix + 'services.html',
      tags: ['services', 'catalog', 'engineering', 'consulting', 'capabilities']
    }""")
    entries.append("""    {
      title: 'Technology Platform & Architecture',
      category: 'Technology',
      desc: 'Agentic AI, IoT telemetry, real-time analytics, and enterprise data integration architecture.',
      url: rootPrefix + 'technology.html',
      tags: ['technology', 'platform', 'ai', 'iot', 'architecture', 'data', 'analytics']
    }""")
    entries.append("""    {
      title: 'Industries We Serve',
      category: 'Industries',
      desc: 'Specialized technology solutions for FoodTech, Retail Commerce, Manufacturing, Logistics, and Healthcare.',
      url: rootPrefix + 'industries.html',
      tags: ['industries', 'foodtech', 'retail', 'manufacturing', 'logistics', 'healthcare']
    }""")
    entries.append("""    {
      title: 'About Nova Arc',
      category: 'Company',
      desc: 'Enterprise technology partner headquartered in Hyderabad. Systems engineering across commerce, enterprise systems, IoT, and AI.',
      url: rootPrefix + 'about.html',
      tags: ['about', 'company', 'hyderabad', 'engineering', 'leadership', 'principles', 'mission']
    }""")
    entries.append("""    {
      title: 'Connect With Us & Directory',
      category: 'Contact',
      desc: 'Get in touch with Nova Arc. Hyderabad headquarters, direct departmental emails, and phone contact.',
      url: rootPrefix + 'contact.html',
      tags: ['contact', 'connect', 'phone', 'email', 'hyderabad', 'support', 'sales']
    }""")

    # 2. Add all subpages
    for p in all_subpages:
        rel = p['rel_path']
        title = p['page_title'].replace("'", "\\'")
        cat = p.get('category_badge', 'Solutions & Services').title()
        if len(cat) > 28:
            cat = cat[:28]
        desc = p['page_subtitle'].replace("'", "\\'")
        if len(desc) > 130:
            desc = desc[:127] + "..."
        # Extract keywords from title and capabilities
        tags = [t.lower() for t in re.findall(r'\b[A-Za-z]{3,}\b', p['page_title'])]
        for cap in p.get('capabilities', [])[:2]:
            tags.extend([t.lower() for t in re.findall(r'\b[A-Za-z]{3,}\b', cap.get('title', ''))])
        tags_dedup = list(dict.fromkeys(tags))[:10]
        tags_str = ", ".join(f"'{t}'" for t in tags_dedup)

        entry = f"""    {{
      title: '{title}',
      category: '{cat}',
      desc: '{desc}',
      url: rootPrefix + '{rel}',
      tags: [{tags_str}]
    }}"""
        entries.append(entry)

    new_index_str = "  const searchIndex = [\n" + ",\n".join(entries) + "\n  ];"

    # Replace in js/main.js
    pattern = re.compile(r'  const (?:isServicesDir|isSubDir) =.*?;.*?const searchIndex = \[.*?\];', re.DOTALL)
    replacement = f"""  const isSubDir = window.location.pathname.includes('/services/') ||
                   window.location.pathname.includes('/technology/') ||
                   window.location.pathname.includes('/industries/') ||
                   window.location.pathname.includes('/connect/');
  const rootPrefix = isSubDir ? '../' : '';

{new_index_str}"""

    if pattern.search(js_content):
        js_content = pattern.sub(replacement, js_content, count=1)
        with open(main_js_path, "w", encoding="utf-8") as f:
            f.write(js_content)
        print(f"  [OK] Successfully updated searchIndex with {len(entries)} items")
    else:
        print("  [WARN] searchIndex pattern match failed in js/main.js")

def main():
    print("==================================================================")
    print("NOVA ARC - FULL MULTI-PAGE WEBSITE GENERATOR")
    print("==================================================================")
    all_subpages = generate_all_subpages()
    generate_about_page()
    update_root_pages()
    generate_directory_indexes()
    generate_404_page()
    generate_sitemap(all_subpages)
    update_search_index(all_subpages)
    print("\n[SUCCESS] All pages generated and synchronized successfully!")

if __name__ == "__main__":
    main()
