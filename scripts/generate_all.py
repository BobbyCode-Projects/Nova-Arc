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
            seo_desc=page_def["seo_desc"]
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
  <link rel="stylesheet" href="css/style.css?v=3.1">
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
    pattern = re.compile(r'  const isServicesDir =.*?;.*?const searchIndex = \[.*?\];', re.DOTALL)
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
    update_root_pages()
    generate_directory_indexes()
    generate_404_page()
    generate_sitemap(all_subpages)
    update_search_index(all_subpages)
    print("\n[SUCCESS] All pages generated and synchronized successfully!")

if __name__ == "__main__":
    main()
