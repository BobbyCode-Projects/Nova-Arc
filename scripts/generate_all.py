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

# Add scripts directory to path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from build_pages import generate_subpage, get_shared_header, get_shared_footer
from data_solutions import SOLUTIONS_PAGES
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
    html_content = re.sub(r'\s*</body>', f'\n\n  <!-- Scripts -->\n  <script src="{root_prefix}js/main.js?v=3.5"></script>\n</body>', html_content)

    # Normalize style.css to v=3.5
    html_content = re.sub(r'href="[^"]*css/style\.css(\?v=[^"]*)?"', f'href="{root_prefix}css/style.css?v=3.5"', html_content)

    return html_content

def generate_all_subpages():
    print("\n--- Generating 47 Subpages ---")
    all_subpage_defs = (
        SOLUTIONS_PAGES +
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
            faqs=page_def.get("faqs")
        )
        write_page(rel_path, html)
        generated_count += 1
    
    print(f"Total subpages built: {generated_count}")
    return all_subpage_defs

def update_root_pages():
    print("\n--- Updating Root Pages with Unified Header & Footer ---")

    # 1. index.html
    index_path = os.path.join(REPO_ROOT, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            idx_html = f.read()
        idx_html = replace_header_and_footer(idx_html, "", "")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(idx_html)
        print("  [OK] Updated index.html header & footer")

    # 2. solutions.html
    solutions_path = os.path.join(REPO_ROOT, "solutions.html")
    if os.path.exists(solutions_path):
        with open(solutions_path, "r", encoding="utf-8") as f:
            sol_html = f.read()
        sol_html = replace_header_and_footer(sol_html, "", "solutions")
        with open(solutions_path, "w", encoding="utf-8") as f:
            f.write(sol_html)
        print("  [OK] Updated solutions.html header & footer")

    # 3. services.html
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
    ai_platform_path = os.path.join(REPO_ROOT, "ai-platform.html")
    if os.path.exists(ai_platform_path):
        with open(ai_platform_path, "r", encoding="utf-8") as f:
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
        with open(os.path.join(REPO_ROOT, "technology.html"), "w", encoding="utf-8") as f:
            f.write(tech_html)
        with open(ai_platform_path, "w", encoding="utf-8") as f:
            f.write(tech_html)
        print("  [OK] Created technology.html and synchronized ai-platform.html")

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
        ("solutions/index.html", "solutions.html", "solutions"),
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

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="images/nova-arc-logo.png">

  <!-- Google Font: Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Core Stylesheet -->
  <link rel="stylesheet" href="css/style.css?v=3.5">

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
<body>

{header_html}

  <main>
    <!-- ========================================================================
         HERO SECTION: ABOUT NOVA ARC (2-COLUMN BALANCED)
         ======================================================================== -->
    <section class="solutions-hero-ags" style="padding-top: calc(70px + var(--space-3xl)); padding-bottom: var(--space-4xl);">
      <div class="container">
        <div class="hero-subpage-grid">
          <!-- Left Column -->
          <div class="hero-left-col">
            <div class="hero-category-badge">
              <span class="badge-dot"></span>
              COMPANY OVERVIEW &bull; ENTERPRISE SYSTEMS ENGINEERING
            </div>

            <h1 class="hero-title">
              Engineering Connected Systems for the Modern Enterprise
            </h1>

            <p class="hero-description">
              Nova Arc is an enterprise technology engineering firm headquartered in Laxmi Cyber City, Hyderabad. We design, build, and deploy high-performance software platforms across digital commerce, enterprise operational systems, intelligent IoT telemetry, and governed artificial intelligence.
            </p>

            <div class="hero-cta-group">
              <a href="contact.html" class="btn btn-consultation-ags">
                <span>Discuss Your Project</span>
                <svg class="btn-arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
              </a>
              <a href="services.html" class="btn btn-outline-white">
                <span>Explore Services</span>
              </a>
              <a href="tel:04046146093" class="btn btn-outline-white" style="border-color: rgba(56, 189, 248, 0.4); color: #38BDF8;">
                <span>Call 040-46146093</span>
              </a>
            </div>

            <div class="hero-highlights-strip">
              <span class="hero-highlight-pill">&bull; 4 Integrated Technology Domains</span>
              <span class="hero-highlight-pill">&bull; Deterministic Architecture</span>
              <span class="hero-highlight-pill">&bull; Human-in-the-Loop Governance</span>
              <span class="hero-highlight-pill">&bull; Hyderabad HQ &bull; Kondapur</span>
            </div>
          </div>

          <!-- Right Column: Enterprise Telemetry & Architectural Profile -->
          <div class="hero-visual-col">
            <div class="hero-arch-window">
              <div class="arch-window-topbar">
                <div class="arch-window-dots">
                  <span class="arch-dot red"></span>
                  <span class="arch-dot yellow"></span>
                  <span class="arch-dot green"></span>
                </div>
                <div class="arch-window-title">Nova Arc &bull; Enterprise Profile</div>
                <div class="arch-window-status">
                  <span class="arch-pulse-dot"></span>
                  OPERATIONAL
                </div>
              </div>

              <div class="arch-window-body">
                <div class="arch-stage-card">
                  <div class="arch-stage-header">
                    <span class="arch-stage-num">01</span>
                    <span class="arch-stage-name">Digital Commerce &amp; Supply Chain</span>
                    <span class="arch-stage-tag tag-ready">Integrated</span>
                  </div>
                  <div class="arch-stage-desc">High-performance B2B/B2C storefronts, dynamic ordering, and inventory orchestration.</div>
                </div>

                <div class="arch-stage-card">
                  <div class="arch-stage-header">
                    <span class="arch-stage-num">02</span>
                    <span class="arch-stage-name">Enterprise Business Solutions</span>
                    <span class="arch-stage-tag tag-active">Connected</span>
                  </div>
                  <div class="arch-stage-desc">Unified CRM, modern HRMS, approval hierarchies, and cross-departmental data sync.</div>
                </div>

                <div class="arch-stage-card">
                  <div class="arch-stage-header">
                    <span class="arch-stage-num">03</span>
                    <span class="arch-stage-name">Intelligent Monitoring &amp; IoT</span>
                    <span class="arch-stage-tag tag-ready">Live Stream</span>
                  </div>
                  <div class="arch-stage-desc">Sub-second telemetry ingestion, operational dashboards, and event-based alerts.</div>
                </div>

                <div class="arch-stage-card">
                  <div class="arch-stage-header">
                    <span class="arch-stage-num">04</span>
                    <span class="arch-stage-name">AI &amp; Governed Automation</span>
                    <span class="arch-stage-tag tag-active">Governed</span>
                  </div>
                  <div class="arch-stage-desc">Autonomous task orchestration, document processing, and strict human approvals.</div>
                </div>

                <div class="arch-telemetry-strip">
                  <div class="arch-telemetry-cell">
                    <div class="telemetry-label">Architecture</div>
                    <div class="telemetry-val">Deterministic</div>
                  </div>
                  <div class="arch-telemetry-cell">
                    <div class="telemetry-label">Security</div>
                    <div class="telemetry-val">Role-Based RBAC</div>
                  </div>
                  <div class="arch-telemetry-cell">
                    <div class="telemetry-label">Availability</div>
                    <div class="telemetry-val">99.9% Target</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 1: MISSION & PHILOSOPHY
         ======================================================================== -->
    <section class="section" style="background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
      <div class="container">
        <div style="max-width: 860px; margin: 0 auto; text-align: center;">
          <span class="eyebrow-ags" style="color: #1F6FEB; font-weight: 700; letter-spacing: 0.1em; font-size: 0.85rem;">OUR MISSION</span>
          <h2 style="font-size: clamp(2rem, 3.5vw, 2.8rem); font-weight: 800; color: #0B2545; margin: 12px 0 20px; letter-spacing: -0.02em;">
            Building Deterministic Technology That Connects Every Facet of Your Enterprise
          </h2>
          <p style="color: #475569; font-size: 1.12rem; line-height: 1.7; margin-bottom: 24px;">
            Modern enterprises face an operational dilemma: inflexible legacy systems that cannot keep up with digital demands, and experimental technologies that lack the reliability required for mission-critical operations.
          </p>
          <p style="color: #64748B; font-size: 1.02rem; line-height: 1.7;">
            At Nova Arc, we believe technology should be dependable, verifiable, and purpose-built. We bridge front-end customer touchpoints directly with backend transactional systems, creating seamless operational continuity that scales with your business.
          </p>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 2: CORE ENGINEERING PRINCIPLES
         ======================================================================== -->
    <section class="section" style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
      <div class="container">
        <div class="section-header-centered">
          <span class="eyebrow-ags">OUR PHILOSOPHY</span>
          <h2 class="section-heading-ags">Four Core Engineering Principles</h2>
          <p class="section-desc-ags">
            The foundational architectural standards that guide every software system, integration connector, and AI workflow we engineer.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 28px; margin-top: 40px;">
          <!-- Principle 1 -->
          <div class="card" style="padding: 32px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
            <div style="width: 48px; height: 48px; border-radius: 10px; background: rgba(31, 111, 235, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1F6FEB" stroke-width="2.5"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; font-weight: 700; color: #0B2545; margin-bottom: 12px;">Deterministic Design</h3>
            <p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin: 0;">
              Production systems cannot rely on guesswork. We design deterministic finite state machines, comprehensive error recovery routines, and rigorous idempotency across every data transaction.
            </p>
          </div>

          <!-- Principle 2 -->
          <div class="card" style="padding: 32px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
            <div style="width: 48px; height: 48px; border-radius: 10px; background: rgba(31, 111, 235, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1F6FEB" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; font-weight: 700; color: #0B2545; margin-bottom: 12px;">Operational Continuity</h3>
            <p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin: 0;">
              Eliminate information silos. We engineer bi-directional connectors that synchronize digital storefronts, warehouse inventory, billing ledgers, and CRM records without manual re-entry.
            </p>
          </div>

          <!-- Principle 3 -->
          <div class="card" style="padding: 32px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
            <div style="width: 48px; height: 48px; border-radius: 10px; background: rgba(31, 111, 235, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1F6FEB" stroke-width="2.5"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; font-weight: 700; color: #0B2545; margin-bottom: 12px;">Real-Time Observability</h3>
            <p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin: 0;">
              Operational blind spots lead to costly downtime. We embed continuous telemetry, IoT sensor feeds, and automated threshold alerts directly into intuitive executive dashboards.
            </p>
          </div>

          <!-- Principle 4 -->
          <div class="card" style="padding: 32px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
            <div style="width: 48px; height: 48px; border-radius: 10px; background: rgba(31, 111, 235, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 20px;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1F6FEB" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
            </div>
            <h3 style="font-size: 1.25rem; font-weight: 700; color: #0B2545; margin-bottom: 12px;">Governed AI &amp; Oversight</h3>
            <p style="font-size: 0.92rem; color: #475569; line-height: 1.6; margin: 0;">
              AI must be auditable and safe. We build intelligent agents and document processing pipelines bounded by deterministic business rules, strict RBAC, and human-in-the-loop signoffs.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 3: HOW WE DELIVER (5-STAGE METHODOLOGY)
         ======================================================================== -->
    <section class="section" style="background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
      <div class="container">
        <div class="section-header-centered">
          <span class="eyebrow-ags">STRUCTURED LIFECYCLE</span>
          <h2 class="section-heading-ags">Our Engineering &amp; Delivery Methodology</h2>
          <p class="section-desc-ags">
            A disciplined, transparent delivery framework engineered to minimize operational disruption and guarantee measurable ROI.
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-top: 40px;">
          <!-- Stage 1 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 24px;">
            <div style="font-size: 0.8rem; font-weight: 800; color: #1F6FEB; text-transform: uppercase; margin-bottom: 8px;">Phase 01</div>
            <h4 style="font-size: 1.1rem; color: #0B2545; margin-bottom: 8px;">Discovery &amp; Systems Audit</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.5; margin: 0;">Detailed assessment of your current workflows, APIs, legacy software, and operational pain points.</p>
          </div>

          <!-- Stage 2 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 24px;">
            <div style="font-size: 0.8rem; font-weight: 800; color: #1F6FEB; text-transform: uppercase; margin-bottom: 8px;">Phase 02</div>
            <h4 style="font-size: 1.1rem; color: #0B2545; margin-bottom: 8px;">Architecture Blueprint</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.5; margin: 0;">Creation of comprehensive data schemas, state transition diagrams, interface mocks, and integration specs.</p>
          </div>

          <!-- Stage 3 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 24px;">
            <div style="font-size: 0.8rem; font-weight: 800; color: #1F6FEB; text-transform: uppercase; margin-bottom: 8px;">Phase 03</div>
            <h4 style="font-size: 1.1rem; color: #0B2545; margin-bottom: 8px;">Modular Development</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.5; margin: 0;">Agile software engineering with automated unit testing, continuous integration, and security scanning.</p>
          </div>

          <!-- Stage 4 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 24px;">
            <div style="font-size: 0.8rem; font-weight: 800; color: #1F6FEB; text-transform: uppercase; margin-bottom: 8px;">Phase 04</div>
            <h4 style="font-size: 1.1rem; color: #0B2545; margin-bottom: 8px;">Staged Integration</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.5; margin: 0;">Safe parallel testing, canary deployments, and automated validation alongside legacy systems.</p>
          </div>

          <!-- Stage 5 -->
          <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 24px;">
            <div style="font-size: 0.8rem; font-weight: 800; color: #1F6FEB; text-transform: uppercase; margin-bottom: 8px;">Phase 05</div>
            <h4 style="font-size: 1.1rem; color: #0B2545; margin-bottom: 8px;">Telemetry &amp; Scaling</h4>
            <p style="font-size: 0.88rem; color: #64748B; line-height: 1.5; margin: 0;">Continuous observability, automated incident response, performance profiling, and capacity scaling.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================================================
         SECTION 4: HEADQUARTERS & GLOBAL REACH
         ======================================================================== -->
    <section class="section" style="background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
      <div class="container">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 36px; align-items: center;">
          <div>
            <span class="eyebrow-ags">HYDERABAD HEADQUARTERS</span>
            <h2 class="section-heading-ags" style="margin-bottom: 16px;">Engineered in Hyderabad’s Technology Corridor</h2>
            <p style="color: #475569; font-size: 1.05rem; line-height: 1.7; margin-bottom: 20px;">
              Nova Arc is located in Laxmi Cyber City, Whitefields, Kondapur &mdash; the heart of Hyderabad’s enterprise technology and innovation ecosystem.
            </p>
            <div style="display: flex; flex-direction: column; gap: 16px; margin-top: 24px;">
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#1F6FEB" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <div>
                  <strong style="color: #0B2545; display: block;">Office Address</strong>
                  <span style="color: #64748B; font-size: 0.92rem;">BP Raju Marg, Laxmi Cyber City, Whitefields, Kondapur, Telangana &ndash; 500081</span>
                </div>
              </div>
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#1F6FEB" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                <div>
                  <strong style="color: #0B2545; display: block;">Direct Telephone</strong>
                  <a href="tel:04046146093" style="color: #1F6FEB; text-decoration: none; font-size: 0.92rem; font-weight: 600;">040-46146093</a>
                </div>
              </div>
              <div style="display: flex; gap: 12px; align-items: flex-start;">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#1F6FEB" stroke-width="2.5" style="flex-shrink: 0; margin-top: 2px;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                <div>
                  <strong style="color: #0B2545; display: block;">Electronic Mail</strong>
                  <span style="color: #64748B; font-size: 0.92rem;">info@novaarctech.in &bull; support@novaarctech.in</span>
                </div>
              </div>
            </div>
          </div>

          <div style="background: linear-gradient(135deg, #0B2545 0%, #0F172A 100%); border-radius: 16px; padding: 36px; color: #FFFFFF; border: 1px solid rgba(56, 189, 248, 0.3);">
            <span style="color: #38BDF8; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-bottom: 8px;">GET IN TOUCH</span>
            <h3 style="font-size: 1.6rem; font-weight: 800; color: #FFFFFF; margin-bottom: 12px;">Partner with Nova Arc</h3>
            <p style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 24px;">
              Ready to modernize your operations or integrate intelligent automation into your tech stack? Our engineering leads are ready to collaborate.
            </p>
            <div style="display: flex; flex-direction: column; gap: 12px;">
              <a href="contact.html" class="btn btn-primary" style="justify-content: center; padding: 12px 20px;">
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
         SECTION 5: BOTTOM CALL-TO-ACTION BANNER
         ======================================================================== -->
    <section class="section" style="background: linear-gradient(135deg, #0B2545 0%, #0284C7 100%); padding: 60px 0; text-align: center; color: #FFFFFF;">
      <div class="container" style="max-width: 800px;">
        <h2 style="font-size: clamp(2rem, 3.2vw, 2.6rem); font-weight: 800; color: #FFFFFF; margin-bottom: 14px;">
          Build Smarter. Operate Better. Scale Faster.
        </h2>
        <p style="color: rgba(255, 255, 255, 0.9); font-size: 1.1rem; line-height: 1.6; margin-bottom: 30px;">
          Join forward-thinking enterprises that trust Nova Arc to power their digital commerce, enterprise systems, and intelligent automation.
        </p>
        <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
          <a href="contact.html" class="btn btn-consultation-ags" style="background: #FFFFFF; color: #0B2545;">
            <span>Connect With Our Team</span>
            <svg class="btn-arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg>
          </a>
          <a href="solutions.html" class="btn btn-outline-white" style="border-color: #FFFFFF; color: #FFFFFF;">
            <span>Explore Solutions</span>
          </a>
        </div>
      </div>
    </section>
  </main>

{footer_html}

  <!-- Scripts -->
  <script src="js/main.js?v=3.5"></script>
</body>
</html>
"""
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
  <meta name="description" content="The page you requested could not be found. Explore Nova Arc's solutions, services, technology, and industries.">
  <meta name="robots" content="noindex, follow">

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="images/nova-arc-logo.png">

  <!-- Fonts & Core Stylesheet -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css?v=3.5">
</head>
<body>

{header_html}

  <main style="padding-top: calc(70px + var(--space-4xl)); padding-bottom: var(--space-4xl); min-height: 80vh; display: flex; align-items: center;">
    <div class="container" style="max-width: 860px; text-align: center; margin: 0 auto;">
      <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; letter-spacing: 0.1em; font-size: 0.95rem;">ERROR 404</span>
      <h1 style="font-size: clamp(2.5rem, 5vw, 4.2rem); font-weight: 900; color: #FFFFFF; margin: 12px 0 18px; letter-spacing: -0.02em;">
        Page Not Found
      </h1>
      <p style="color: #CBD5E1; font-size: 1.15rem; max-width: 620px; margin: 0 auto var(--space-2xl); line-height: 1.65;">
        The page you are looking for may have been moved, renamed, or is temporarily unavailable. Let us help you find what you need across Nova Arc’s technology suite.
      </p>

      <div style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap; margin-bottom: var(--space-3xl);">
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

      <!-- Quick Navigation Cards Grid -->
      <div style="text-align: left; margin-top: var(--space-2xl);">
        <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: var(--space-lg); text-align: center;">Popular Areas of Exploration:</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: var(--space-lg);">
          <a href="solutions.html" class="card" style="padding: var(--space-lg); text-decoration: none; display: block;">
            <span style="font-size: 0.75rem; color: #38BDF8; font-weight: 700; text-transform: uppercase;">Overview</span>
            <h4 style="font-size: 1.1rem; color: #FFFFFF; margin: 6px 0 4px;">Solutions Suite &rarr;</h4>
            <p style="color: #94A3B8; font-size: 0.85rem; margin: 0; line-height: 1.4;">Comprehensive digital commerce, supply chain, monitoring, and AI platforms.</p>
          </a>
          <a href="services.html" class="card" style="padding: var(--space-lg); text-decoration: none; display: block;">
            <span style="font-size: 0.75rem; color: #38BDF8; font-weight: 700; text-transform: uppercase;">Catalog</span>
            <h4 style="font-size: 1.1rem; color: #FFFFFF; margin: 6px 0 4px;">Services Catalog &rarr;</h4>
            <p style="color: #94A3B8; font-size: 0.85rem; margin: 0; line-height: 1.4;">Detailed implementation capabilities across 4 technology domains.</p>
          </a>
          <a href="technology.html" class="card" style="padding: var(--space-lg); text-decoration: none; display: block;">
            <span style="font-size: 0.75rem; color: #38BDF8; font-weight: 700; text-transform: uppercase;">Architecture</span>
            <h4 style="font-size: 1.1rem; color: #FFFFFF; margin: 6px 0 4px;">Technology Platform &rarr;</h4>
            <p style="color: #94A3B8; font-size: 0.85rem; margin: 0; line-height: 1.4;">Agentic AI, real-time IoT telemetry, enterprise integration, and data analytics.</p>
          </a>
          <a href="industries.html" class="card" style="padding: var(--space-lg); text-decoration: none; display: block;">
            <span style="font-size: 0.75rem; color: #38BDF8; font-weight: 700; text-transform: uppercase;">Sectors</span>
            <h4 style="font-size: 1.1rem; color: #FFFFFF; margin: 6px 0 4px;">Industries We Serve &rarr;</h4>
            <p style="color: #94A3B8; font-size: 0.85rem; margin: 0; line-height: 1.4;">FoodTech, retail commerce, manufacturing, logistics, healthcare, and enterprise.</p>
          </a>
        </div>
      </div>
    </div>
  </main>

{footer_html}

  <!-- Scripts -->
  <script src="js/main.js?v=3.5"></script>
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
        ("https://novaarctech.in/solutions.html", "0.9", "weekly"),
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

    today = "2026-10-27"
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
      title: 'All Solutions Overview',
      category: 'Solutions',
      desc: 'Unified architecture combining commerce, enterprise systems, intelligent monitoring, and AI automation.',
      url: rootPrefix + 'solutions.html',
      tags: ['solutions', 'overview', 'enterprise solutions', 'digital commerce', 'supply chain', 'monitoring']
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
                   window.location.pathname.includes('/solutions/') ||
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
