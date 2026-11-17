"""
Nova Arc - Dedicated Healthcare RCM Main Domain Page Generator
Generates: services/healthcare-rcm.html

Strictly satisfies all PART 1 requirements:
- Page Title & Headline: Transforming Healthcare Operations Through Intelligence, Automation & Precision.
- Introduction (2 paragraphs)
- Section 1: Our Core RCM Services (5 cards linking to subpages)
- Section 2: Intelligent Technology & Automation (Beyond Traditional RCM. Powered by Intelligence - Agentic AI, NovaChron, Revenue Leakage Dashboard, BPMS)
- Section 3: Business Outcomes (Measurable Performance. Meaningful Results - Benchmark Table + Disclaimer)
- Section 4: Industries & Healthcare Organizations Served
- Section 5: Why Nova Arc for Healthcare RCM?
- Section 6: Final CTA
"""

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from build_pages import get_shared_header, get_shared_footer
from ecg_component import get_ecg_waveform_html

def generate_rcm_domain_page():
    root_prefix = "../"
    page_title = "Intelligent Healthcare Technology & Revenue Cycle Management"
    seo_desc = "Transform healthcare operations with NovaArc's end-to-end Revenue Cycle Management (RCM) solutions powered by Agentic AI, NovaChron real-time monitoring, and leakage intelligence."
    canonical_url = "https://novaarctech.in/services/healthcare-rcm.html"

    # Navigation pills in hero
    pills = [
        ("Patient Access & Front-End RCM", "services/rcm-patient-access.html"),
        ("Medical Coding & Charge Management", "services/rcm-medical-coding.html"),
        ("Medical Billing & Payment Management", "services/rcm-billing-payment.html"),
        ("Accounts Receivable & Denial Management", "services/rcm-ar-denial.html"),
        ("Target Benchmarks & Outcomes", "services/rcm-target-benchmarks.html")
    ]
    pills_html = "".join([
        f'<a href="{root_prefix}{link}" class="category-pill-link category-pill-cta" style="padding: 9px 18px; font-size: 0.88rem; display: inline-flex; align-items: center; gap: 8px;">'
        f'<span>{title}</span>'
        f'<svg class="pill-arrow-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#1F6FEB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        f'<line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline>'
        f'</svg>'
        f'</a>'
        for title, link in pills
    ])

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title} | Nova Arc</title>
  <meta name="description" content="{seo_desc}">
  <link rel="canonical" href="{canonical_url}">

  <!-- SEO & Social Meta Tags -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Nova Arc Technologies">
  <meta property="og:title" content="{page_title} | Nova Arc">
  <meta property="og:description" content="{seo_desc}">
  <meta property="og:url" content="{canonical_url}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{page_title} | Nova Arc">
  <meta name="twitter:description" content="{seo_desc}">

  <!-- Favicon & Brand Icons -->
  <link rel="icon" type="image/svg+xml" href="{root_prefix}images/favicon.svg">
  <link rel="icon" type="image/png" sizes="32x32" href="{root_prefix}images/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="{root_prefix}images/favicon-16x16.png">
  <link rel="apple-touch-icon" sizes="180x180" href="{root_prefix}images/apple-touch-icon.png">
  <link rel="shortcut icon" href="{root_prefix}favicon.ico">
  <link rel="manifest" href="{root_prefix}site.webmanifest">

  <!-- Fonts & Core Stylesheet -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{root_prefix}css/style.css?v=4.0">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{page_title}",
    "description": "{seo_desc}",
    "url": "{canonical_url}"
  }}
  </script>
</head>
<body class="subpage-body">

{get_shared_header(root_prefix, "services")}

  <!-- Hero Section -->
  <section class="page-hero page-hero-dark" style="min-height: calc(100vh - 75px); min-height: calc(100dvh - 75px); display: flex; flex-direction: column; justify-content: center; box-sizing: border-box; padding-top: calc(75px + clamp(16px, 2.5vw, 36px)); padding-bottom: clamp(28px, 4vw, 52px); position: relative; overflow: hidden;">
    <div class="hero-orchestrated-glow-cyan"></div>
    <div class="hero-orchestrated-glow-blue"></div>
    {get_ecg_waveform_html()}

    <div class="container hero-container-ags" style="position: relative; z-index: 5;">
      <nav class="breadcrumb-nav" aria-label="Breadcrumb" style="margin-bottom: 14px;">
        <ol class="breadcrumb-list" style="display: flex; gap: 8px; list-style: none; padding: 0; margin: 0; font-size: 0.82rem; color: #94A3B8;">
          <li><a href="{root_prefix}index.html">Home</a></li>
          <span class="breadcrumb-separator">/</span>
          <li><a href="{root_prefix}services.html">Services</a></li>
          <span class="breadcrumb-separator">/</span>
          <li aria-current="page">Healthcare Revenue Cycle Management</li>
        </ol>
      </nav>

      <div class="page-hero-content" style="max-width: 920px;">
        <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; font-size: 0.82rem; letter-spacing: 0.08em; display: inline-block; margin-bottom: 12px;">INTELLIGENT HEALTHCARE TECHNOLOGY &amp; REVENUE CYCLE MANAGEMENT</span>
        <h1 class="page-hero-title" style="font-size: clamp(1.85rem, 3.8vw, 3.2rem); line-height: 1.18; color: #FFFFFF; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.02em;">Transforming Healthcare Operations Through Intelligence, Automation &amp; Precision.</h1>
        <p class="hero-tagline-ags" style="font-size: clamp(1.02rem, 1.3vw, 1.2rem); font-weight: 600; color: #38BDF8; line-height: 1.5; margin-bottom: 14px;">
          End-to-End Enterprise Healthcare Revenue Cycle Management
        </p>
        <p class="hero-intro-text" style="font-size: 1.02rem; line-height: 1.65; color: #E2E8F0; margin-bottom: 14px;">
          NovaArc delivers end-to-end healthcare Revenue Cycle Management (RCM) services powered by intelligent automation, real-time operational monitoring, and AI-driven insights.
        </p>
        <p class="hero-intro-text" style="font-size: 1.02rem; line-height: 1.65; color: #CBD5E1; margin-bottom: 24px;">
          We combine healthcare expertise, advanced technology, and automated workflows to help healthcare organizations optimize revenue performance, reduce operational inefficiencies, minimize revenue leakage, and achieve greater financial visibility.
        </p>
      </div>

      <div class="hero-actions-ags" style="display: flex; gap: 16px; flex-wrap: wrap; align-items: center;">
        <a href="{root_prefix}contact.html" class="btn btn-consultation-ags" style="padding: 12px 28px; font-size: 0.98rem;">
          <span>Discuss Your Project</span>
          <svg class="btn-arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </a>
        <a href="#core-services" class="btn btn-outline-white" style="padding: 12px 24px; font-size: 0.98rem;">
          <span>Explore Core Services</span>
        </a>
      </div>

      <div class="hero-highlights-strip" style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 24px;">
        {pills_html}
      </div>
    </div>
  </section>

  <!-- SECTION 1: Our Core RCM Services (LIGHT SLATE) -->
  <section id="core-services" class="subpage-section-light" style="padding: clamp(52px, 6vw, 84px) 0; background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="text-align: center; max-width: 820px; margin: 0 auto clamp(36px, 4vw, 54px);">
        <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; letter-spacing: 0.08em; display: inline-block; margin-bottom: 8px;">OUR CORE RCM SERVICES</span>
        <h2 style="font-size: clamp(1.85rem, 2.8vw, 2.5rem); font-weight: 800; color: #0F172A; margin: 0 0 14px; letter-spacing: -0.02em;">Comprehensive Revenue Cycle Architecture</h2>
        <p style="color: #475569; font-size: 1.05rem; line-height: 1.65; margin: 0;">Specialized domain modules delivering structured workflows, certified operational precision, and seamless data continuity across the patient journey.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
        <!-- Card 1: Patient Access -->
        <div class="rcm-service-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);">
          <div>
            <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(2, 132, 199, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; color: #0284C7;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="8.5" cy="7.5" r="4"></circle><polyline points="17 11 19 13 23 9"></polyline></svg>
            </div>
            <span class="rcm-badge-num">DOMAIN 01</span>
            <h3 class="rcm-service-title" style="margin-top: 4px;"><a href="{root_prefix}services/rcm-patient-access.html" style="color: #0F172A; text-decoration: none;">Patient Access &amp; Front-End RCM</a></h3>
            <p style="color: #0284C7; font-weight: 600; font-size: 0.92rem; margin-bottom: 12px;">Accurate Patient Data. Stronger Financial Clearance.</p>
            <p class="rcm-service-desc">Streamline front-end intake to minimize data entry errors, prevent avoidable claim denials, and guarantee financial readiness before care is delivered.</p>
            <div class="rcm-includes-title">Core Capabilities:</div>
            <ul class="rcm-checklist">
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Patient Registration &amp; Master Index Validation</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Real-Time 270/271 Eligibility &amp; Benefit Inquiries</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Prior Authorization Tracking &amp; Clinical Submissions</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Good Faith Estimates &amp; Point-of-Service Collections</li>
            </ul>
          </div>
          <div style="margin-top: 20px; padding-top: 14px; border-top: 1px solid #E2E8F0;">
            <a href="{root_prefix}services/rcm-patient-access.html" style="color: #0284C7; font-weight: 700; text-decoration: none; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 6px;">
              <span>Explore Subpage &amp; Capabilities</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>
        </div>

        <!-- Card 2: Medical Coding -->
        <div class="rcm-service-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);">
          <div>
            <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(2, 132, 199, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; color: #0284C7;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            </div>
            <span class="rcm-badge-num">DOMAIN 02</span>
            <h3 class="rcm-service-title" style="margin-top: 4px;"><a href="{root_prefix}services/rcm-medical-coding.html" style="color: #0F172A; text-decoration: none;">Medical Coding &amp; Charge Management</a></h3>
            <p style="color: #0284C7; font-weight: 600; font-size: 0.92rem; margin-bottom: 12px;">Precision in Every Code. Revenue in Every Encounter.</p>
            <p class="rcm-service-desc">Certified AAPC/AHIMA medical coding ensuring clinical accuracy, compliant documentation, and total charge capture integrity across all specialties.</p>
            <div class="rcm-includes-title">Core Capabilities:</div>
            <ul class="rcm-checklist">
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Professional Multi-Specialty &amp; Surgical Coding</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Inpatient MS-DRG &amp; Outpatient Facility Coding</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Hierarchical Condition Category (HCC) Risk Optimization</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Surgical Implant &amp; Infusion Charge Reconciliation</li>
            </ul>
          </div>
          <div style="margin-top: 20px; padding-top: 14px; border-top: 1px solid #E2E8F0;">
            <a href="{root_prefix}services/rcm-medical-coding.html" style="color: #0284C7; font-weight: 700; text-decoration: none; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 6px;">
              <span>Explore Subpage &amp; Capabilities</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>
        </div>

        <!-- Card 3: Medical Billing -->
        <div class="rcm-service-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);">
          <div>
            <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(2, 132, 199, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; color: #0284C7;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="2"></rect><line x1="2" y1="10" x2="22" y2="10"></line></svg>
            </div>
            <span class="rcm-badge-num">DOMAIN 03</span>
            <h3 class="rcm-service-title" style="margin-top: 4px;"><a href="{root_prefix}services/rcm-billing-payment.html" style="color: #0F172A; text-decoration: none;">Medical Billing &amp; Payment Management</a></h3>
            <p style="color: #0284C7; font-weight: 600; font-size: 0.92rem; margin-bottom: 12px;">Smarter Billing. Faster Reimbursements.</p>
            <p class="rcm-service-desc">Complete billing lifecycle management through triple-tier claim scrubbing, clearinghouse rejection resolution, and automated remittance reconciliation.</p>
            <div class="rcm-includes-title">Core Capabilities:</div>
            <ul class="rcm-checklist">
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Electronic 837P / 837I Claims Submission &amp; Scrubbing</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> 24-Hour Clearinghouse Gateway Rejection Resolution</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Automated Secondary Crossover Claim Generation</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Daily ERA 835 Auto-Posting &amp; Bank Cash Balancing</li>
            </ul>
          </div>
          <div style="margin-top: 20px; padding-top: 14px; border-top: 1px solid #E2E8F0;">
            <a href="{root_prefix}services/rcm-billing-payment.html" style="color: #0284C7; font-weight: 700; text-decoration: none; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 6px;">
              <span>Explore Subpage &amp; Capabilities</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>
        </div>

        <!-- Card 4: A/R & Denial -->
        <div class="rcm-service-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);">
          <div>
            <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(2, 132, 199, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; color: #0284C7;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>
            </div>
            <span class="rcm-badge-num">DOMAIN 04</span>
            <h3 class="rcm-service-title" style="margin-top: 4px;"><a href="{root_prefix}services/rcm-ar-denial.html" style="color: #0F172A; text-decoration: none;">Accounts Receivable &amp; Denial Management</a></h3>
            <p style="color: #0284C7; font-weight: 600; font-size: 0.92rem; margin-bottom: 12px;">Recover Revenue. Reduce Denials. Maximize Collections.</p>
            <p class="rcm-service-desc">Algorithmic aging prioritization, root-cause denial analysis, and clinical appeal packages that recover trapped cash and eliminate write-offs.</p>
            <div class="rcm-includes-title">Core Capabilities:</div>
            <ul class="rcm-checklist">
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Automated Aging Work Queues (30, 60, 90, 120+ Days)</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Root-Cause CARC/RARC Denial Categorization</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Multi-Tier Clinical &amp; Administrative Appeal Packages</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Payer Contract Underpayment Identification &amp; Recovery</li>
            </ul>
          </div>
          <div style="margin-top: 20px; padding-top: 14px; border-top: 1px solid #E2E8F0;">
            <a href="{root_prefix}services/rcm-ar-denial.html" style="color: #0284C7; font-weight: 700; text-decoration: none; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 6px;">
              <span>Explore Subpage &amp; Capabilities</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>
        </div>

        <!-- Card 5: Target Benchmarks -->
        <div class="rcm-service-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 28px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);">
          <div>
            <div style="width: 44px; height: 44px; border-radius: 10px; background: rgba(2, 132, 199, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 16px; color: #0284C7;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            </div>
            <span class="rcm-badge-num">DOMAIN 05</span>
            <h3 class="rcm-service-title" style="margin-top: 4px;"><a href="{root_prefix}services/rcm-target-benchmarks.html" style="color: #0F172A; text-decoration: none;">Target Benchmarks &amp; Outcomes</a></h3>
            <p style="color: #0284C7; font-weight: 600; font-size: 0.92rem; margin-bottom: 12px;">Measurable Performance. Meaningful Results.</p>
            <p class="rcm-service-desc">Transparent performance benchmarks, continuous SLA governance, and executive financial analytics aligned with HFMA and MGMA industry standards.</p>
            <div class="rcm-includes-title">Core Capabilities:</div>
            <ul class="rcm-checklist">
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Clean Claim Rate Optimization (&ge; 95%)</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Denial Rate Minimization (&lt; 5%)</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Days in A/R Acceleration (&lt; 40 Days)</li>
              <li class="rcm-check-item"><svg class="rcm-check-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Net Collection Yield Maximization (&ge; 95%)</li>
            </ul>
          </div>
          <div style="margin-top: 20px; padding-top: 14px; border-top: 1px solid #E2E8F0;">
            <a href="{root_prefix}services/rcm-target-benchmarks.html" style="color: #0284C7; font-weight: 700; text-decoration: none; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 6px;">
              <span>Explore Subpage &amp; Capabilities</span>
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 2: Intelligent Technology & Automation (DARK NAVY) -->
  <section id="rcm-technology" class="subpage-section-dark" style="padding: clamp(52px, 6vw, 84px) 0; background: #08111F; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 820px; margin: 0 auto clamp(36px, 4vw, 54px);">
        <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; letter-spacing: 0.08em; display: inline-block; margin-bottom: 8px;">INTELLIGENT TECHNOLOGY &amp; AUTOMATION</span>
        <h2 style="font-size: clamp(1.85rem, 2.8vw, 2.5rem); font-weight: 800; color: #FFFFFF; margin: 0 0 14px; letter-spacing: -0.02em;">Beyond Traditional RCM. Powered by Intelligence.</h2>
        <p style="color: #94A3B8; font-size: 1.05rem; line-height: 1.65; margin: 0;">Our technology ecosystem connects healthcare operations, intelligent automation, and real-time business intelligence into one unified operating model.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 24px;">
        <!-- Module A: Agentic AI -->
        <div class="rcm-tech-card" style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 12px; padding: 28px; display: flex; flex-direction: column;">
          <div class="rcm-tech-card-header">
            <div class="rcm-tech-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 2a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2 2 2 0 0 1-2-2V4a2 2 0 0 1 2-2z"></path><rect x="4" y="8" width="16" height="12" rx="2"></rect><path d="M9 13v2"></path><path d="M15 13v2"></path></svg></div>
            <div>
              <span style="font-size: 0.72rem; font-weight: 700; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.08em;">MODULE A</span>
              <h3 class="rcm-tech-title">Agentic AI &amp; Intelligent Automation</h3>
            </div>
          </div>
          <p class="rcm-tech-desc">Autonomous intelligent agents designed to execute, support, and accelerate complex healthcare revenue cycle workflows without human bottlenecks.</p>
          <div style="margin-top: auto;">
            <ul class="rcm-tech-caps-list" style="margin-bottom: 20px;">
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Automated Eligibility Verification</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Intelligent Claims Processing</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> AI-Assisted Medical Coding</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Denial Prediction &amp; Prevention</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Automated Payment Posting</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Intelligent Appeals Assistance</li>
            </ul>
            <div style="padding: 12px 14px; background: rgba(56, 189, 248, 0.08); border-left: 3px solid #38BDF8; border-radius: 6px; font-size: 0.85rem; color: #CBD5E1; line-height: 1.5;">
              <strong style="color: #38BDF8; display: block; font-size: 0.75rem; text-transform: uppercase;">Operational Use Case:</strong>
              Autonomous agents execute batch 270/271 queries 24 hours prior to surgery, predicting authorization gaps before encounters occur.
            </div>
          </div>
        </div>

        <!-- Module B: NovaChron -->
        <div class="rcm-tech-card" style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 12px; padding: 28px; display: flex; flex-direction: column;">
          <div class="rcm-tech-card-header">
            <div class="rcm-tech-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
            <div>
              <span style="font-size: 0.72rem; font-weight: 700; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.08em;">MODULE B</span>
              <h3 class="rcm-tech-title">NovaChron &ndash; Real-Time Operations Monitoring</h3>
            </div>
          </div>
          <p class="rcm-tech-desc">Monitor every transaction, claim touch, and operational workflow through a centralized telemetric monitoring platform.</p>
          <div style="margin-top: auto;">
            <ul class="rcm-tech-caps-list" style="margin-bottom: 20px;">
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Live Productivity Tracking</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Employee Performance Monitoring</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Transaction-Level Visibility</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> SLA &amp; Turnaround Monitoring</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Quality &amp; Accuracy Tracking</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Operational Performance Dashboards</li>
            </ul>
            <div style="padding: 12px 14px; background: rgba(56, 189, 248, 0.08); border-left: 3px solid #38BDF8; border-radius: 6px; font-size: 0.85rem; color: #CBD5E1; line-height: 1.5;">
              <strong style="color: #38BDF8; display: block; font-size: 0.75rem; text-transform: uppercase;">Operational Use Case:</strong>
              Real-time alerts trigger when biller touch times deviate from SLA benchmarks or when claim hold queues approach timely filing thresholds.
            </div>
          </div>
        </div>

        <!-- Module C: Revenue Leakage Dashboard -->
        <div class="rcm-tech-card" style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 12px; padding: 28px; display: flex; flex-direction: column;">
          <div class="rcm-tech-card-header">
            <div class="rcm-tech-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg></div>
            <div>
              <span style="font-size: 0.72rem; font-weight: 700; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.08em;">MODULE C</span>
              <h3 class="rcm-tech-title">Revenue Leakage Intelligence Dashboard</h3>
            </div>
          </div>
          <p class="rcm-tech-desc">Identify exactly where earned revenue is being lost and quantify its financial impact through deep predictive analytics.</p>
          <div style="margin-top: auto;">
            <ul class="rcm-tech-caps-list" style="margin-bottom: 20px;">
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Multi-Dimensional Denial Analysis</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Missed Surgical &amp; Drug Charge Detection</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Coding-Related Revenue Loss Auditing</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Payer Contract Underpayment Identification</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> A/R Aging Velocity &amp; Drift Analysis</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Timely Filing Risk Window Monitoring</li>
            </ul>
            <div style="padding: 12px 14px; background: rgba(56, 189, 248, 0.08); border-left: 3px solid #38BDF8; border-radius: 6px; font-size: 0.85rem; color: #CBD5E1; line-height: 1.5;">
              <strong style="color: #38BDF8; display: block; font-size: 0.75rem; text-transform: uppercase;">Operational Use Case:</strong>
              Automated auditing cross-references paid ERA 835s against contracted fee schedules to detect systematic $50-$200 short-payments on surgical implants.
            </div>
          </div>
        </div>

        <!-- Module D: BPMS -->
        <div class="rcm-tech-card" style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 12px; padding: 28px; display: flex; flex-direction: column;">
          <div class="rcm-tech-card-header">
            <div class="rcm-tech-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M16 16v1a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h11a2 2 0 0 1 2 2v1"></path><path d="M18 8h4a2 2 0 0 1 2 2v7a2 2 0 0 1-2 2h-4"></path><circle cx="8" cy="12" r="2"></circle></svg></div>
            <div>
              <span style="font-size: 0.72rem; font-weight: 700; color: #38BDF8; text-transform: uppercase; letter-spacing: 0.08em;">MODULE D</span>
              <h3 class="rcm-tech-title">BPMS &ndash; Business Process Management System</h3>
            </div>
          </div>
          <p class="rcm-tech-desc">A centralized workflow automation engine connecting clinical people, business processes, and intelligent technology.</p>
          <div style="margin-top: auto;">
            <ul class="rcm-tech-caps-list" style="margin-bottom: 20px;">
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Automated Workflow Orchestration</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Intelligent Task Allocation by Specialty</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Rule-Based Straight-Through Processing</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> AI-Driven Task Automation Routing</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Human Review &amp; Executive Approval Gates</li>
              <li class="rcm-tech-cap-item"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Complete Audit Tracking &amp; Compliance Logs</li>
            </ul>
            <div style="padding: 12px 14px; background: rgba(56, 189, 248, 0.08); border-left: 3px solid #38BDF8; border-radius: 6px; font-size: 0.85rem; color: #CBD5E1; line-height: 1.5;">
              <strong style="color: #38BDF8; display: block; font-size: 0.75rem; text-transform: uppercase;">Operational Use Case:</strong>
              High-dollar inpatient claims over $25,000 route automatically to senior certified auditors, while routine resubmissions clear autonomously via rule scripts.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 3: Business Outcomes (LIGHT WHITE) -->
  <section id="rcm-outcomes" class="subpage-section-light" style="padding: clamp(52px, 6vw, 84px) 0; background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="text-align: center; max-width: 820px; margin: 0 auto clamp(36px, 4vw, 54px);">
        <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; letter-spacing: 0.08em; display: inline-block; margin-bottom: 8px;">BUSINESS OUTCOMES &amp; TARGET BENCHMARKS</span>
        <h2 style="font-size: clamp(1.85rem, 2.8vw, 2.5rem); font-weight: 800; color: #0F172A; margin: 0 0 14px; letter-spacing: -0.02em;">Measurable Performance. Meaningful Results.</h2>
        <p style="color: #475569; font-size: 1.05rem; line-height: 1.65; margin: 0;">We hold our operational workflows to strict performance standards designed to compress accounts receivable aging, eliminate preventable denials, and maximize net collection yield.</p>
      </div>

      <!-- Benchmark Table Container -->
      <div class="rcm-outcomes-container" style="max-width: 960px; margin: 0 auto;">
        <div class="rcm-table-wrap">
          <table class="rcm-benchmark-table">
            <thead>
              <tr>
                <th>Performance Area</th>
                <th>Target Benchmark</th>
                <th>Operational Focus &amp; Impact</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="font-weight: 700; color: #0B2545;">Clean Claim Rate</td>
                <td><span class="rcm-benchmark-val">95% or higher</span></td>
                <td>Triple-pass pre-submission scrubbing and automated demographic validation preventing upstream clearinghouse rejections.</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #0B2545;">Denial Rate</td>
                <td><span class="rcm-benchmark-val">Under 5%</span></td>
                <td>Predictive denial algorithms, proactive eligibility verification, and 24-hour root-cause CARC/RARC resolution.</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #0B2545;">Days in A/R (DAR)</td>
                <td><span class="rcm-benchmark-val">Under 40 days</span></td>
                <td>High-velocity 24-48 hr charge entry, automated ERA posting, and early outreach starting at Day 21.</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #0B2545;">A/R Over 90 Days</td>
                <td><span class="rcm-benchmark-val">Under 15%</span></td>
                <td>Disciplined aging queue follow-up, dedicated senior appeal strike teams, and prompt-pay statutory enforcement.</td>
              </tr>
              <tr>
                <td style="font-weight: 700; color: #0B2545;">Net Collection Rate</td>
                <td><span class="rcm-benchmark-val">95% or higher</span></td>
                <td>Fee schedule allowable modeling, surgical charge reconciliation, and systematic recovery of payer underpayments.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="rcm-disclaimer-note" style="border-left: 3px solid #0284C7;">
          <strong style="color: #0F172A;">Important Benchmark Disclaimer:</strong> These figures represent target benchmarks, not guaranteed results. Actual performance targets depend on the client's existing baseline, operational requirements, and mutually agreed service levels.
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 4: Industries & Healthcare Organizations Served (LIGHT SLATE) -->
  <section id="healthcare-segments" class="subpage-section-light-alt" style="padding: clamp(52px, 6vw, 84px) 0; background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="text-align: center; max-width: 820px; margin: 0 auto clamp(36px, 4vw, 54px);">
        <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; letter-spacing: 0.08em; display: inline-block; margin-bottom: 8px;">ORGANIZATIONS SERVED</span>
        <h2 style="font-size: clamp(1.85rem, 2.8vw, 2.5rem); font-weight: 800; color: #0F172A; margin: 0 0 14px; letter-spacing: -0.02em;">Industries &amp; Healthcare Organizations Served</h2>
        <p style="color: #475569; font-size: 1.05rem; line-height: 1.65; margin: 0;">Tailored revenue cycle solutions engineered for diverse healthcare delivery models, compliance environments, and specialty workflows.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
          <div style="font-size: 0.72rem; font-weight: 700; color: #0284C7; text-transform: uppercase; margin-bottom: 6px;">ENTERPRISE CARE</div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">Hospitals &amp; Multi-Hospital Systems</h3>
          <p style="font-size: 0.90rem; color: #475569; line-height: 1.55; margin: 0;">Inpatient DRG validation, complex observation stay billing, CDI query integration, and high-volume trauma billing operations.</p>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
          <div style="font-size: 0.72rem; font-weight: 700; color: #0284C7; text-transform: uppercase; margin-bottom: 6px;">AMBULATORY SURGERY</div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">Ambulatory Surgical Centers (ASCs)</h3>
          <p style="font-size: 0.90rem; color: #475569; line-height: 1.55; margin: 0;">Same-day surgical packaging rules, implant and prosthetic fee ticket reconciliation, and pre-admission financial clearance.</p>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
          <div style="font-size: 0.72rem; font-weight: 700; color: #0284C7; text-transform: uppercase; margin-bottom: 6px;">PHYSICIAN GROUPS</div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">Multi-Specialty Physician Networks</h3>
          <p style="font-size: 0.90rem; color: #475569; line-height: 1.55; margin: 0;">Multi-provider credentialing, shared EMR charge capture, centralized billing queues, and specialty-specific modifier compliance.</p>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
          <div style="font-size: 0.72rem; font-weight: 700; color: #0284C7; text-transform: uppercase; margin-bottom: 6px;">DIAGNOSTICS &amp; LABS</div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">Diagnostic, Pathology &amp; Imaging Centers</h3>
          <p style="font-size: 0.90rem; color: #475569; line-height: 1.55; margin: 0;">Professional and technical component splitting (-26/TC), CLIA-certified billing, and high-throughput electronic requisition parsing.</p>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
          <div style="font-size: 0.72rem; font-weight: 700; color: #0284C7; text-transform: uppercase; margin-bottom: 6px;">DIGITAL HEALTH</div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">Telehealth &amp; Virtual Care Providers</h3>
          <p style="font-size: 0.90rem; color: #475569; line-height: 1.55; margin: 0;">Multi-state provider licensure, cross-state Medicaid enrollment, place of service 02/10 billing, and automated patient copay capture.</p>
        </div>

        <div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.03);">
          <div style="font-size: 0.72rem; font-weight: 700; color: #0284C7; text-transform: uppercase; margin-bottom: 6px;">SPECIALTY CARE</div>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">Independent Specialty Practices</h3>
          <p style="font-size: 0.90rem; color: #475569; line-height: 1.55; margin: 0;">Cardiology, orthopedics, oncology, and neurology practices requiring complex prior authorizations and buy-and-bill drug recovery.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 5: Why Nova Arc for Healthcare RCM? (DARK NAVY) -->
  <section id="why-nova-arc" class="subpage-section-dark-alt" style="padding: clamp(52px, 6vw, 84px) 0; background: #0A1628; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 820px; margin: 0 auto clamp(36px, 4vw, 54px);">
        <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; letter-spacing: 0.08em; display: inline-block; margin-bottom: 8px;">OUR ADVANTAGE</span>
        <h2 style="font-size: clamp(1.85rem, 2.8vw, 2.5rem); font-weight: 800; color: #FFFFFF; margin: 0 0 14px; letter-spacing: -0.02em;">Why Nova Arc for Healthcare RCM?</h2>
        <p style="color: #94A3B8; font-size: 1.05rem; line-height: 1.65; margin: 0;">We unite certified clinical expertise with intelligent enterprise systems to deliver complete operational visibility, minimized revenue leakage, and predictable cash flow.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
        <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 22px;">
          <h4 style="color: #38BDF8; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;">Healthcare RCM Expertise</h4>
          <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.55; margin: 0;">AAPC and AHIMA certified coders and billing specialists covering 35+ clinical specialties with rigorous compliance standards.</p>
        </div>

        <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 22px;">
          <h4 style="color: #38BDF8; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;">Intelligent Automation</h4>
          <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.55; margin: 0;">Autonomous agentic workflows across clearinghouse and payer endpoints eliminating manual data entry bottlenecks.</p>
        </div>

        <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 22px;">
          <h4 style="color: #38BDF8; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;">AI-Driven Operational Assistance</h4>
          <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.55; margin: 0;">Predictive denial scoring and natural language clinical chart parsing resolving documentation ambiguities proactively.</p>
        </div>

        <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 22px;">
          <h4 style="color: #38BDF8; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;">Real-Time NovaChron Monitoring</h4>
          <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.55; margin: 0;">Second-by-second telemetric visibility into team touch times, queue volumes, and claim status adherence.</p>
        </div>

        <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 22px;">
          <h4 style="color: #38BDF8; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;">Revenue Leakage Visibility</h4>
          <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.55; margin: 0;">Continuous allowable modeling detecting payer contract variances, implant underpayments, and uncaptured clinical charges.</p>
        </div>

        <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 22px;">
          <h4 style="color: #38BDF8; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;">Enterprise BPMS Orchestration</h4>
          <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.55; margin: 0;">Structured work distribution, automated escalation triggers, and comprehensive audit trails protecting ledger integrity.</p>
        </div>

        <div style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 22px;">
          <h4 style="color: #38BDF8; font-size: 1.05rem; font-weight: 700; margin-bottom: 8px;">Performance-Focused Workflows</h4>
          <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.55; margin: 0;">Strict alignment with HFMA MAP Keys targeting &ge;95% clean claim rates, &lt;5% denial rates, and accelerated cash recovery.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SECTION 6: Final CTA (Dark Gradient) -->
  <section class="cta-strip-ags subpage-section-dark" style="padding: clamp(56px, 7vw, 84px) 0; background: linear-gradient(135deg, #07172B 0%, #0B2545 60%, #0E2E56 100%); text-align: center; border-top: 1px solid rgba(255,255,255,0.08);">
    <div class="container" style="max-width: 820px; margin: 0 auto;">
      <h2 style="font-size: clamp(2rem, 3.5vw, 2.8rem); font-weight: 800; color: #FFFFFF; margin-bottom: 16px; letter-spacing: -0.02em;">
        Build a Smarter, More Efficient Healthcare Revenue Cycle.
      </h2>
      <p style="font-size: 1.1rem; color: #CBD5E1; line-height: 1.65; margin-bottom: 32px;">
        Combine healthcare expertise, intelligent automation, and operational visibility to strengthen financial performance and streamline healthcare operations.
      </p>
      <div style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap;">
        <a href="{root_prefix}contact.html" class="btn btn-consultation-ags" style="font-size: 1.02rem; padding: 14px 32px;">
          <span>Contact NovaArc</span>
          <svg class="btn-arrow-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </a>
        <a href="tel:04046146093" class="btn btn-outline-white" style="font-size: 1.02rem; padding: 14px 28px;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="margin-right: 6px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>040-46146093</span>
        </a>
      </div>
    </div>
  </section>

{get_shared_footer(root_prefix)}

  <!-- Scripts -->
  <script src="{root_prefix}js/main.js?v=4.0"></script>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    content = generate_rcm_domain_page()
    out_path = os.path.join(REPO_ROOT, "services", "healthcare-rcm.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {out_path} ({len(content):,} bytes)")
