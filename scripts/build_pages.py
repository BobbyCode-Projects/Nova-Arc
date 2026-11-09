#!/usr/bin/env python3
"""
Nova Arc - Multi-Page Complete Website Builder
Builds all 54 pages across Home, Solutions, Services, Technology, Industries, and Connect.
Preserves existing visual design, CSS styling, components, responsive layouts, and branding.
"""

import os
import sys
from ecg_component import get_ecg_waveform_html
from hero_visuals import get_hero_svg_for_page
from page_enhancer import get_industries_for_page, get_supplemental_capabilities, INDUSTRY_ICON_MAP

def get_shared_header(root_prefix, active_section=""):
    serv_active = ' active' if active_section == 'services' else ''
    tech_active = ' active' if active_section == 'technology' else ''
    ind_active = ' active' if active_section == 'industries' else ''
    con_active = ' active' if active_section == 'connect' else ''

    return f"""  <header class="site-header" id="top">
    <div class="container navbar">
      <!-- Logo -->
      <a href="{root_prefix}index.html" class="logo" aria-label="Nova Arc Homepage">
        <img src="{root_prefix}images/nova-arc-logo.png" alt="Nova Arc Logo" class="logo-img" width="38" height="33">
        <span class="logo-text">Nova<span class="logo-highlight">Arc</span></span>
      </a>

      <!-- Desktop Navigation Menu -->
      <nav class="desktop-nav" aria-label="Main Navigation">
        <ul class="nav-menu">
          <!-- Item 1: Services Mega-Menu -->
          <li class="nav-item-dropdown nav-item-services">
            <a href="{root_prefix}services.html" class="nav-dropdown-link nav-pill-services{serv_active}" id="servicesDropdownToggle" aria-haspopup="true" aria-expanded="false">
              <span>Services</span>
              <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <div class="mega-menu-panel" id="servicesMegaMenu" role="menu" aria-labelledby="servicesDropdownToggle" aria-hidden="true">
              <div class="mega-menu-inner container">
                <div class="mega-menu-grid">
                  <!-- Col 1: Digital Commerce & Supply Chain -->
                  <div class="mega-col" role="none">
                    <h3 class="mega-col-heading" id="menu-col-1-heading"><a href="{root_prefix}services/digital-commerce.html" class="mega-heading-link">Digital Commerce &amp; Supply Chain</a></h3>
                    <ul class="mega-menu-list" role="none" aria-labelledby="menu-col-1-heading">
                      <li role="none"><a href="{root_prefix}services/digital-commerce-platforms.html" class="mega-item standalone" role="menuitem">Digital Commerce Platforms</a></li>
                      <li role="none"><a href="{root_prefix}services/foodtech.html" class="mega-item standalone" role="menuitem">FoodTech Solutions</a></li>
                      <li role="none"><a href="{root_prefix}services/supply-chain-management.html" class="mega-item standalone" role="menuitem">Supply Chain Management</a></li>
                      <li role="none"><a href="{root_prefix}services/procurement.html" class="mega-item standalone" role="menuitem">Procurement &amp; Vendor Management</a></li>
                      <li role="none"><a href="{root_prefix}services/logistics.html" class="mega-item standalone" role="menuitem">Logistics &amp; Distribution</a></li>
                    </ul>
                  </div>

                  <!-- Col 2: Enterprise Business Solutions -->
                  <div class="mega-col" role="none">
                    <h3 class="mega-col-heading" id="menu-col-2-heading"><a href="{root_prefix}services/enterprise-business.html" class="mega-heading-link">Enterprise Business Solutions</a></h3>
                    <ul class="mega-menu-list" role="none" aria-labelledby="menu-col-2-heading">
                      <li role="none"><a href="{root_prefix}services/crm.html" class="mega-item standalone" role="menuitem">CRM</a></li>
                      <li role="none"><a href="{root_prefix}services/hrms.html" class="mega-item standalone" role="menuitem">HRMS</a></li>
                      <li role="none"><a href="{root_prefix}services/business-process-automation.html" class="mega-item standalone" role="menuitem">Business Process Automation</a></li>
                      <li role="none"><a href="{root_prefix}services/enterprise-applications.html" class="mega-item standalone" role="menuitem">Custom Enterprise Applications</a></li>
                      <li role="none"><a href="{root_prefix}services/enterprise-integration.html" class="mega-item standalone" role="menuitem">Enterprise Integration &amp; BI</a></li>
                    </ul>
                  </div>

                  <!-- Col 3: Intelligent Monitoring & Automation -->
                  <div class="mega-col" role="none">
                    <h3 class="mega-col-heading" id="menu-col-3-heading"><a href="{root_prefix}services/intelligent-monitoring.html" class="mega-heading-link">Intelligent Monitoring &amp; Automation</a></h3>
                    <ul class="mega-menu-list" role="none" aria-labelledby="menu-col-3-heading">
                      <li role="none"><a href="{root_prefix}services/real-time-monitoring.html" class="mega-item standalone" role="menuitem">Real-Time Monitoring &amp; Dashboards</a></li>
                      <li role="none"><a href="{root_prefix}services/iot-integration.html" class="mega-item standalone" role="menuitem">IoT &amp; Device Integration</a></li>
                      <li role="none"><a href="{root_prefix}services/operational-analytics.html" class="mega-item standalone" role="menuitem">Operational Analytics</a></li>
                      <li role="none"><a href="{root_prefix}services/workflow-automation.html" class="mega-item standalone" role="menuitem">Workflow &amp; Process Automation</a></li>
                      <li role="none"><a href="{root_prefix}services/infrastructure-monitoring.html" class="mega-item standalone" role="menuitem">System &amp; Infrastructure Monitoring</a></li>
                    </ul>
                  </div>

                  <!-- Col 4: AI & Healthcare Technology -->
                  <div class="mega-col" role="none">
                    <h3 class="mega-col-heading" id="menu-col-4-heading"><a href="{root_prefix}services/ai-healthcare.html" class="mega-heading-link">AI &amp; Healthcare Technology</a></h3>
                    <ul class="mega-menu-list" role="none" aria-labelledby="menu-col-4-heading">
                      <li role="none"><a href="{root_prefix}services/agentic-ai.html" class="mega-item standalone" role="menuitem">Agentic AI &amp; Intelligent Agents</a></li>
                      <li role="none"><a href="{root_prefix}services/generative-ai.html" class="mega-item standalone" role="menuitem">Generative AI &amp; Enterprise Assistants</a></li>
                      <li role="none"><a href="{root_prefix}services/document-processing.html" class="mega-item standalone" role="menuitem">Intelligent Document Processing</a></li>
                      <li role="none"><a href="{root_prefix}services/ai-workflow-automation.html" class="mega-item standalone" role="menuitem">AI-Powered Workflow Automation</a></li>
                      <li role="none"><a href="{root_prefix}services/healthcare-automation.html" class="mega-item standalone" role="menuitem">Healthcare Technology &amp; Automation</a></li>
                      <li role="none"><a href="{root_prefix}services/healthcare-data-analytics.html" class="mega-item standalone" role="menuitem">Healthcare Data Integration &amp; Analytics</a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </li>

          <!-- Item 3: Technology Dropdown -->
          <li class="nav-item-dropdown nav-item-tech">
            <a href="{root_prefix}technology.html" class="nav-dropdown-link{tech_active}" id="techDropdownToggle" aria-haspopup="true" aria-expanded="false">
              <span>Technology</span>
              <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <div class="nav-simple-dropdown" aria-labelledby="techDropdownToggle" role="menu">
              <a href="{root_prefix}technology.html" class="nav-simple-item" role="menuitem">
                <strong>Technology Platform Overview</strong>
                <span>Intelligent Technology, Connected Systems &amp; Practical Outcomes</span>
              </a>
              <a href="{root_prefix}technology/agentic-ai.html" class="nav-simple-item" role="menuitem">
                <strong>Agentic AI</strong>
                <span>Autonomous multi-step task orchestration &amp; API-connected reasoning</span>
              </a>
              <a href="{root_prefix}technology/generative-ai.html" class="nav-simple-item" role="menuitem">
                <strong>Generative AI</strong>
                <span>Enterprise knowledge assistants, document search &amp; summarization</span>
              </a>
              <a href="{root_prefix}technology/intelligent-automation.html" class="nav-simple-item" role="menuitem">
                <strong>Intelligent Automation</strong>
                <span>Cross-system rules, automated document extraction &amp; exception routing</span>
              </a>
              <a href="{root_prefix}technology/iot.html" class="nav-simple-item" role="menuitem">
                <strong>Internet of Things (IoT)</strong>
                <span>Connected sensors, device telemetry ingestion &amp; edge synchronization</span>
              </a>
              <a href="{root_prefix}technology/enterprise-integration.html" class="nav-simple-item" role="menuitem">
                <strong>Enterprise Integration</strong>
                <span>REST/GraphQL connectors, ERP/CRM data sync &amp; interoperability</span>
              </a>
              <a href="{root_prefix}technology/data-analytics.html" class="nav-simple-item" role="menuitem">
                <strong>Data Analytics &amp; Intelligence</strong>
                <span>Operational KPI dashboards, anomaly detection &amp; trend forecasting</span>
              </a>
            </div>
          </li>

          <!-- Item 4: Industries Dropdown -->
          <li class="nav-item-dropdown nav-item-industries">
            <a href="{root_prefix}industries.html" class="nav-dropdown-link{ind_active}" id="industriesDropdownToggle" aria-haspopup="true" aria-expanded="false">
              <span>Industries</span>
              <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <div class="nav-simple-dropdown" aria-labelledby="industriesDropdownToggle" role="menu">
              <a href="{root_prefix}industries.html" class="nav-simple-item" role="menuitem">
                <strong>All Industries Overview</strong>
                <span>Cross-sector digital transformation &amp; systems engineering</span>
              </a>
              <a href="{root_prefix}industries/foodtech.html" class="nav-simple-item" role="menuitem">
                <strong>FoodTech &amp; Food Distribution</strong>
                <span>Digital ordering, cold chain tracking &amp; batch traceability</span>
              </a>
              <a href="{root_prefix}industries/retail-ecommerce.html" class="nav-simple-item" role="menuitem">
                <strong>Retail &amp; Digital Commerce</strong>
                <span>B2B/B2C storefronts, inventory coordination &amp; catalog sync</span>
              </a>
              <a href="{root_prefix}industries/manufacturing.html" class="nav-simple-item" role="menuitem">
                <strong>Manufacturing &amp; Industrial Operations</strong>
                <span>Equipment monitoring, telemetry alerts &amp; process automation</span>
              </a>
              <a href="{root_prefix}industries/logistics.html" class="nav-simple-item" role="menuitem">
                <strong>Logistics &amp; Supply Chain</strong>
                <span>Shipment visibility, fleet tracking &amp; warehouse operations</span>
              </a>
              <a href="{root_prefix}industries/enterprise.html" class="nav-simple-item" role="menuitem">
                <strong>Enterprise &amp; Professional Services</strong>
                <span>CRM, HRMS, approval hierarchies &amp; business applications</span>
              </a>
              <a href="{root_prefix}industries/healthcare.html" class="nav-simple-item" role="menuitem">
                <strong>Healthcare &amp; Health Technology</strong>
                <span>Administrative automation, digital intake &amp; system connectivity</span>
              </a>
            </div>
          </li>
        </ul>
      </nav>

      <!-- Desktop Action Buttons -->
      <div class="nav-actions">
        <button class="nav-search-btn" id="siteSearchBtn" aria-label="Search Nova Arc services, technology, and industries" title="Search">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
        </button>
        <a href="{root_prefix}contact.html" class="btn btn-connect-nav">Connect with us</a>
      </div>

      <!-- Mobile Hamburger Toggle -->
      <button class="mobile-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="3" y1="12" x2="21" y2="12"></line>
          <line x1="3" y1="6" x2="21" y2="6"></line>
          <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
      </button>
    </div>

    <!-- Redesigned Full-Screen Mobile Navigation Drawer (White AGS-Style) -->
    <div class="mobile-nav-drawer" id="mobileDrawer" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Mobile Navigation">
      <!-- Top Bar: Logo on Left, Close (X) on Right -->
      <div class="mobile-drawer-topbar">
        <a href="{root_prefix}index.html" class="mobile-drawer-logo" aria-label="Nova Arc Home">
          <img src="{root_prefix}images/nova-arc-logo.png" alt="Nova Arc Logo" width="38" height="34" class="mobile-drawer-logo-img">
          <span class="mobile-drawer-logo-title">Nova<span class="mobile-drawer-logo-accent">Arc</span></span>
        </a>
        <button type="button" class="mobile-drawer-close-btn" id="mobileDrawerCloseBtn" aria-label="Close navigation menu">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      </div>

      <!-- Main Navigation Menu: EXACT 5 Options -->
      <nav class="mobile-drawer-nav" aria-label="Mobile Menu">
        <ul class="mobile-drawer-list">

          <!-- 1. Services (Accordion) -->
          <li class="mobile-nav-item">
            <button type="button" class="mobile-nav-btn mobile-accordion-toggle" id="mobileServicesToggle" aria-expanded="false" aria-controls="mobileServicesSubmenu">
              <span class="mobile-nav-label">Services</span>
              <svg class="mobile-nav-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </button>
            <div class="mobile-submenu-collapse" id="mobileServicesSubmenu" aria-hidden="true">
              <div class="mobile-submenu-inner">
                <div class="mobile-subcat-group">
                  <a href="{root_prefix}services.html" class="mobile-subcat-main-link">
                    <span>All Services Catalog</span>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                  </a>
                </div>

                <div class="mobile-subcat-group">
                  <a href="{root_prefix}services/digital-commerce.html" class="mobile-subcat-title">Digital Commerce &amp; Supply Chain</a>
                  <ul class="mobile-sublink-list">
                    <li><a href="{root_prefix}services/digital-commerce-platforms.html" class="mobile-sublink">Digital Commerce Platforms</a></li>
                    <li><a href="{root_prefix}services/foodtech.html" class="mobile-sublink">FoodTech Solutions</a></li>
                    <li><a href="{root_prefix}services/supply-chain-management.html" class="mobile-sublink">Supply Chain Management</a></li>
                    <li><a href="{root_prefix}services/procurement.html" class="mobile-sublink">Procurement &amp; Vendor Management</a></li>
                    <li><a href="{root_prefix}services/logistics.html" class="mobile-sublink">Logistics &amp; Distribution</a></li>
                  </ul>
                </div>

                <div class="mobile-subcat-group">
                  <a href="{root_prefix}services/enterprise-business.html" class="mobile-subcat-title">Enterprise Business Solutions</a>
                  <ul class="mobile-sublink-list">
                    <li><a href="{root_prefix}services/crm.html" class="mobile-sublink">Customer Relationship Management (CRM)</a></li>
                    <li><a href="{root_prefix}services/hrms.html" class="mobile-sublink">Human Resource Management (HRMS)</a></li>
                    <li><a href="{root_prefix}services/business-process-automation.html" class="mobile-sublink">Business Process Automation</a></li>
                    <li><a href="{root_prefix}services/enterprise-applications.html" class="mobile-sublink">Custom Enterprise Applications</a></li>
                    <li><a href="{root_prefix}services/enterprise-integration.html" class="mobile-sublink">Enterprise Integration &amp; Middleware</a></li>
                  </ul>
                </div>

                <div class="mobile-subcat-group">
                  <a href="{root_prefix}services/intelligent-monitoring.html" class="mobile-subcat-title">Intelligent Monitoring &amp; Automation</a>
                  <ul class="mobile-sublink-list">
                    <li><a href="{root_prefix}services/real-time-monitoring.html" class="mobile-sublink">Real-Time Monitoring &amp; Dashboards</a></li>
                    <li><a href="{root_prefix}services/iot-integration.html" class="mobile-sublink">IoT &amp; Device Integration</a></li>
                    <li><a href="{root_prefix}services/operational-analytics.html" class="mobile-sublink">Operational Analytics</a></li>
                    <li><a href="{root_prefix}services/workflow-automation.html" class="mobile-sublink">Workflow &amp; Process Automation</a></li>
                    <li><a href="{root_prefix}services/infrastructure-monitoring.html" class="mobile-sublink">System &amp; Infrastructure Monitoring</a></li>
                  </ul>
                </div>

                <div class="mobile-subcat-group">
                  <a href="{root_prefix}services/ai-healthcare.html" class="mobile-subcat-title">AI &amp; Healthcare Technology</a>
                  <ul class="mobile-sublink-list">
                    <li><a href="{root_prefix}services/agentic-ai.html" class="mobile-sublink">Agentic AI &amp; Intelligent Agents</a></li>
                    <li><a href="{root_prefix}services/generative-ai.html" class="mobile-sublink">Generative AI &amp; Enterprise Assistants</a></li>
                    <li><a href="{root_prefix}services/document-processing.html" class="mobile-sublink">Intelligent Document Processing</a></li>
                    <li><a href="{root_prefix}services/ai-workflow-automation.html" class="mobile-sublink">AI-Powered Workflow Automation</a></li>
                    <li><a href="{root_prefix}services/healthcare-automation.html" class="mobile-sublink">Healthcare Technology &amp; Automation</a></li>
                    <li><a href="{root_prefix}services/healthcare-data-analytics.html" class="mobile-sublink">Healthcare Data Integration &amp; Analytics</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <!-- 2. Technology (Accordion) -->
          <li class="mobile-nav-item">
            <button type="button" class="mobile-nav-btn mobile-accordion-toggle" id="mobileTechToggle" aria-expanded="false" aria-controls="mobileTechSubmenu">
              <span class="mobile-nav-label">Technology</span>
              <svg class="mobile-nav-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </button>
            <div class="mobile-submenu-collapse" id="mobileTechSubmenu" aria-hidden="true">
              <div class="mobile-submenu-inner">
                <div class="mobile-subcat-group">
                  <a href="{root_prefix}technology.html" class="mobile-subcat-main-link">
                    <span>Technology Platform Overview</span>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                  </a>
                </div>
                <div class="mobile-subcat-group">
                  <ul class="mobile-sublink-list">
                    <li><a href="{root_prefix}technology/agentic-ai.html" class="mobile-sublink">Agentic AI</a></li>
                    <li><a href="{root_prefix}technology/generative-ai.html" class="mobile-sublink">Generative AI</a></li>
                    <li><a href="{root_prefix}technology/intelligent-automation.html" class="mobile-sublink">Intelligent Automation</a></li>
                    <li><a href="{root_prefix}technology/iot.html" class="mobile-sublink">Internet of Things (IoT)</a></li>
                    <li><a href="{root_prefix}technology/enterprise-integration.html" class="mobile-sublink">Enterprise Integration</a></li>
                    <li><a href="{root_prefix}technology/data-analytics.html" class="mobile-sublink">Data Analytics &amp; Intelligence</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <!-- 3. Industries (Accordion) -->
          <li class="mobile-nav-item">
            <button type="button" class="mobile-nav-btn mobile-accordion-toggle" id="mobileIndustriesToggle" aria-expanded="false" aria-controls="mobileIndustriesSubmenu">
              <span class="mobile-nav-label">Industries</span>
              <svg class="mobile-nav-chevron" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </button>
            <div class="mobile-submenu-collapse" id="mobileIndustriesSubmenu" aria-hidden="true">
              <div class="mobile-submenu-inner">
                <div class="mobile-subcat-group">
                  <a href="{root_prefix}industries.html" class="mobile-subcat-main-link">
                    <span>All Industries Overview</span>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                  </a>
                </div>
                <div class="mobile-subcat-group">
                  <ul class="mobile-sublink-list">
                    <li><a href="{root_prefix}industries/foodtech.html" class="mobile-sublink">FoodTech &amp; Food Distribution</a></li>
                    <li><a href="{root_prefix}industries/retail-ecommerce.html" class="mobile-sublink">Retail &amp; Digital Commerce</a></li>
                    <li><a href="{root_prefix}industries/manufacturing.html" class="mobile-sublink">Manufacturing &amp; Industrial Operations</a></li>
                    <li><a href="{root_prefix}industries/logistics.html" class="mobile-sublink">Logistics &amp; Supply Chain</a></li>
                    <li><a href="{root_prefix}industries/enterprise.html" class="mobile-sublink">Enterprise &amp; Professional Services</a></li>
                    <li><a href="{root_prefix}industries/healthcare.html" class="mobile-sublink">Healthcare &amp; Health Technology</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <!-- 4. Search -->
          <li class="mobile-nav-item">
            <button type="button" class="mobile-nav-btn" id="mobileMenuSearchBtn">
              <span class="mobile-nav-label">Search</span>
              <svg class="mobile-nav-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <circle cx="11" cy="11" r="8"></circle>
                <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
              </svg>
            </button>
          </li>

          <!-- 5. Contact Us -->
          <li class="mobile-nav-item">
            <a href="{root_prefix}contact.html" class="mobile-nav-btn mobile-nav-link-direct">
              <span class="mobile-nav-label">Contact Us</span>
              <svg class="mobile-nav-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </a>
          </li>

        </ul>
      </nav>
    </div>
  </header>
"""

def get_shared_footer(root_prefix):
    return f"""  <footer class="site-footer">
    <div class="container footer-container">
      <div class="footer-grid">
        <!-- Col 1: Brand & Positioning -->
        <div class="footer-col-brand">
          <a href="{root_prefix}index.html" class="footer-logo">
            <img src="{root_prefix}images/nova-arc-logo.png" alt="Nova Arc Logo" width="36" height="32" class="footer-logo-img">
            <span class="footer-logo-text">Nova<span class="logo-highlight">Arc</span></span>
          </a>
          <p class="footer-desc">
            Nova Arc is an enterprise technology and intelligent solutions company helping organizations modernize business operations through digital platforms, enterprise applications, connected systems, intelligent automation, and applied AI.
          </p>
          <div class="footer-tagline">Engineering Intelligent Solutions for a Connected Business World.</div>
        </div>

        <!-- Col 2: Services -->
        <div>
          <h4 class="footer-col-title">Services</h4>
          <ul class="footer-links-list">
            <li><a href="{root_prefix}services/digital-commerce.html" class="footer-link">Digital Commerce &amp; Supply Chain</a></li>
            <li><a href="{root_prefix}services/enterprise-business.html" class="footer-link">Enterprise Business Solutions</a></li>
            <li><a href="{root_prefix}services/intelligent-monitoring.html" class="footer-link">Intelligent Monitoring &amp; Automation</a></li>
            <li><a href="{root_prefix}services/ai-healthcare.html" class="footer-link">AI &amp; Healthcare Technology</a></li>
            <li><a href="{root_prefix}services.html" class="footer-link">Full Services Catalog</a></li>
          </ul>
        </div>

        <!-- Col 3: Company & Technology -->
        <div>
          <h4 class="footer-col-title">Company</h4>
          <ul class="footer-links-list">
            <li><a href="{root_prefix}about.html" class="footer-link">About Nova Arc</a></li>
            <li><a href="{root_prefix}technology.html" class="footer-link">Technology Platform</a></li>
            <li><a href="{root_prefix}industries.html" class="footer-link">Industries We Serve</a></li>
            <li><a href="{root_prefix}contact.html" class="footer-link">Connect With Us</a></li>
            <li><a href="{root_prefix}connect/project-enquiry.html" class="footer-link">Discuss Your Project</a></li>
            <li><a href="{root_prefix}connect/technical-support.html" class="footer-link">Technical Support</a></li>
          </ul>
        </div>

        <!-- Col 4: Contact Info -->
        <div>
          <h4 class="footer-col-title">Headquarters</h4>
          <div class="footer-contact-info">
            <div class="footer-contact-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
              <span>BP Raju Marg, Laxmi Cyber City, Whitefields<br>Kondapur, Telangana &ndash; 500081</span>
            </div>
            <div class="footer-contact-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
              <span>040-46146093</span>
            </div>
            <div class="footer-contact-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <span>support@novaarctech.in</span>
            </div>
            <div class="footer-contact-item">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
              <a href="{root_prefix}contact.html" style="color: #38BDF8; font-weight: 600;">Direct Contact Directory &rarr;</a>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer Bottom Copyright -->
      <div class="footer-bottom">
        <p>&copy; 2026 Nova Arc Technologies, Inc. All rights reserved.</p>
      </div>
    </div>
  </footer>
"""

def get_hero_highlights_html(capabilities):
    """Generates 3 compact highlights pills from the page capabilities."""
    pills = []
    icons = [
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>',
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
        '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>'
    ]
    
    for idx, cap in enumerate(capabilities[:3]):
        icon = icons[idx % len(icons)]
        title = cap['title'].split('&')[0].strip()
        pills.append(f'<span class="hero-highlight-pill">{icon} {title}</span>')
    
    pills_html = "".join(pills)
    return f'<div class="hero-highlights-strip">{pills_html}</div>' if pills else ""


# Mapping of Core Service Domain Key Capabilities to their dedicated subpages
CAPABILITY_PAGE_MAP = {
    # Domain 1: Digital Commerce & Supply Chain
    'Digital Commerce Platforms': 'services/digital-commerce-platforms.html',
    'FoodTech Solutions': 'services/foodtech.html',
    'Supply Chain Management': 'services/supply-chain-management.html',
    'Procurement & Vendor Management': 'services/procurement.html',
    'Logistics & Distribution': 'services/logistics.html',
    
    # Domain 2: Enterprise Business Solutions
    'Customer Relationship Management (CRM)': 'services/crm.html',
    'Human Resource Management (HRMS)': 'services/hrms.html',
    'Business Process Automation (BPA)': 'services/business-process-automation.html',
    'Enterprise Application Development': 'services/enterprise-applications.html',
    'System Integration & Data Connectivity': 'services/enterprise-integration.html',
    
    # Domain 3: Intelligent Monitoring & Automation
    'Real-Time Monitoring & Dashboards': 'services/real-time-monitoring.html',
    'Internet of Things (IoT) Solutions': 'services/iot-integration.html',
    'Operational Analytics': 'services/operational-analytics.html',
    'Intelligent Workflow Automation': 'services/workflow-automation.html',
    'System & Infrastructure Monitoring': 'services/infrastructure-monitoring.html',
    
    # Domain 4: AI & Healthcare Technology
    'Agentic AI & Intelligent Agents': 'services/agentic-ai.html',
    'Generative AI Applications': 'services/generative-ai.html',
    'Intelligent Document Processing': 'services/document-processing.html',
    'AI-Powered Workflow Automation': 'services/ai-workflow-automation.html',
    'Healthcare Technology Solutions': 'services/healthcare-automation.html',
    'Healthcare Data Integration & Analytics': 'services/healthcare-data-analytics.html',
}

# New generate_subpage implementation for two-colour theme

def generate_subpage(rel_path, root_prefix, category_badge, page_title, page_subtitle,
                     breadcrumbs, overview_paragraphs, capabilities, challenges,
                     workflow_steps, outcomes, related_links, seo_desc,
                     use_cases=None, integrations=None, considerations=None, faqs=None,
                     what_we_deliver=None, industries_served=None, why_choose_us=None):
    """
    Generates a complete, informative enterprise subpage that follows Nova Arc's
    two-colour theme (Dark Navy Blue + White / Light Background) with strict alternation.
    """
    active_sec = "services"
    if "technology/" in rel_path:
        active_sec = "technology"
    elif "industries/" in rel_path:
        active_sec = "industries"
    elif "connect/" in rel_path:
        active_sec = "connect"

    is_domain_page = bool(what_we_deliver)

    # Breadcrumbs HTML (inside dark hero)
    bc_items = []
    for idx, (label, link) in enumerate(breadcrumbs):
        if link:
            bc_items.append(f'<li><a href="{root_prefix}{link}">{label}</a></li>')
        else:
            bc_items.append(f'<li aria-current="page">{label}</li>')
    breadcrumbs_html = '<span class="breadcrumb-separator">/</span>'.join(bc_items)

    # Ensure 5 or 6 detailed, page-specific capability cards
    capabilities = get_supplemental_capabilities(rel_path, capabilities)

    # Save original industries for domain deep-dive, and get curated industries for top strip
    original_industries_served = industries_served
    strip_industries = get_industries_for_page(rel_path)

    # 1. Four Business Value Propositions Strip HTML (ALWAYS in LIGHT SLATE section)
    bv_cards = []
    default_icons = [
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>',
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
        '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>'
    ]
    for idx, out in enumerate(outcomes[:4]):
        icon = default_icons[idx % len(default_icons)]
        bv_cards.append(f"""
        <div class="business-value-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px 22px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04); display: flex; flex-direction: column; transition: transform 0.25s ease, box-shadow 0.25s ease;">
          <div style="width: 38px; height: 38px; border-radius: 8px; background: rgba(2, 132, 199, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 12px; color: #0284C7;">
            {icon}
          </div>
          <h3 style="font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 6px; line-height: 1.35;">{out['title']}</h3>
          <p style="font-size: 0.88rem; color: #475569; line-height: 1.55; margin: 0;">{out['desc']}</p>
        </div>
        """)
    business_value_cards_html = "".join(bv_cards)

    business_value_section_html = f"""
  <!-- Section: Four Business Value Propositions (LIGHT SLATE) -->
  <section id="business-value" class="subpage-section-light-alt" style="padding: clamp(32px, 4vw, 48px) 0; background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: var(--space-xl); flex-wrap: wrap; gap: 12px;">
        <div>
          <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; font-size: 0.8rem; letter-spacing: 0.08em;">MEASURABLE IMPACT</span>
          <h2 style="font-size: clamp(1.4rem, 2.2vw, 1.85rem); font-weight: 800; color: #0F172A; margin: 4px 0 0; letter-spacing: -0.01em;">Four Core Business Value Propositions</h2>
        </div>
        <span style="font-size: 0.85rem; color: #64748B; font-weight: 500;">Direct Operational &amp; Financial Outcomes</span>
      </div>

      <div class="business-value-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px;">
        {business_value_cards_html}
      </div>
    </div>
  </section>
    """

    # 2. Key Capabilities HTML with Read More / Show Less Toggle (ALWAYS in dark section)
    cap_cards = []
    for idx, cap in enumerate(capabilities):
        all_points = cap.get('points', [])
        first_3 = all_points[:3]
        remaining = all_points[3:]

        first_3_html = "".join([f'<li style="color: #CBD5E1; font-size: 0.85rem; margin-bottom: 6px; display: flex; align-items: flex-start; gap: 8px;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg><span>{item}</span></li>' for item in first_3])

        more_html = ""
        btn_html = ""
        if remaining:
            clean_id = f"cap-more-{rel_path.replace('/', '-').replace('.', '-')}-{idx}"
            rem_items_html = "".join([f'<li style="color: #CBD5E1; font-size: 0.85rem; margin-bottom: 6px; display: flex; align-items: flex-start; gap: 8px;"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg><span>{item}</span></li>' for item in remaining])
            more_html = f'<div id="{clean_id}" class="capability-more-wrap" style="display: none;"><ul style="list-style: none; padding: 0; margin: 0; padding-top: 4px;">{rem_items_html}</ul></div>'
            btn_html = f'<button type="button" class="btn-read-more-caps" data-read-more-text="Read More (+{len(remaining)} more)" onclick="toggleCaps(this, \'{clean_id}\')" aria-expanded="false" style="margin-top: 6px;">Read More (+{len(remaining)} more) <svg class="chevron-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></button>'

        # Determine if this capability has a destination link (strictly for the 4 core service domain pages)
        domain_overview_pages = {
            'services/digital-commerce.html',
            'services/enterprise-business.html',
            'services/intelligent-monitoring.html',
            'services/ai-healthcare.html'
        }
        cap_link = None
        if (is_domain_page or rel_path in domain_overview_pages) and rel_path.startswith("services/"):
            cap_link = cap.get('link') or CAPABILITY_PAGE_MAP.get(cap.get('title'))
        if cap_link:
            card_class = "card subpage-card-padded capability-card capability-card-linked"
            title_html = f"""<h3 style="font-size: 1.15rem; font-weight: 700; margin-bottom: 8px;">
              <a href="{root_prefix}{cap_link}" class="capability-title-link" style="color: #FFFFFF; text-decoration: none; display: inline-flex; align-items: center; justify-content: space-between; width: 100%; gap: 8px;">
                <span>{cap['title']}</span>
                <svg class="cap-arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-left: auto;">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </a>
            </h3>"""
        else:
            card_class = "card subpage-card-padded capability-card"
            title_html = f'<h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">{cap["title"]}</h3>'

        cap_cards.append(f"""
        <div class="{card_class}" style="padding: var(--space-xl); display: flex; flex-direction: column; background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg); align-self: stretch; height: auto;">
          <div>
            <div style="width: 42px; height: 42px; border-radius: 10px; background: rgba(14, 165, 233, 0.12); display: flex; align-items: center; justify-content: center; margin-bottom: 12px; color: #38BDF8;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                <line x1="8" y1="21" x2="16" y2="21"></line>
                <line x1="12" y1="17" x2="12" y2="21"></line>
              </svg>
            </div>
            {title_html}
            <p style="color: #94A3B8; font-size: 0.90rem; line-height: 1.55; margin-bottom: 12px;">{cap['desc']}</p>
          </div>
          <div style="margin-top: auto;">
            <ul style="list-style: none; padding: 0; margin: 0; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 10px;">
              {first_3_html}
            </ul>
            {more_html}
            {btn_html}
          </div>
        </div>
        """)
    capabilities_html = "".join(cap_cards)

    # 3. Industries Served Strip HTML (ALWAYS in LIGHT section)
    ind_pills = []
    for ind in strip_industries:
        ind_name = ind.get('name') if isinstance(ind, dict) else str(ind)
        icon_key = ind.get('icon', 'layers') if isinstance(ind, dict) else 'layers'
        icon_svg = INDUSTRY_ICON_MAP.get(icon_key, INDUSTRY_ICON_MAP['layers'])
        ind_pills.append(f"""
        <span class="industry-badge-pill" style="display: inline-flex; align-items: center; gap: 7px; background: #F1F5F9; border: 1px solid #E2E8F0; padding: 7px 14px; border-radius: 999px; font-size: 0.85rem; font-weight: 600; color: #1E293B;">
          {icon_svg}
          <span>{ind_name}</span>
        </span>
        """)
    industries_badges_html = "".join(ind_pills)

    industries_served_section_html = f"""
  <!-- Section: Relevant Industries Served (LIGHT) -->
  <section id="industries-served" class="subpage-section-light" style="padding: clamp(24px, 3.2vw, 38px) 0; background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <span style="font-size: 0.8rem; font-weight: 800; color: #0284C7; letter-spacing: 0.08em; text-transform: uppercase;">INDUSTRIES SERVED:</span>
          <span style="font-size: 0.88rem; color: #64748B; font-weight: 500;">Tailored engineering implementations delivering proven ROI across:</span>
        </div>
        <div class="industry-pills-row" style="display: flex; flex-wrap: wrap; gap: 10px; align-items: center;">
          {industries_badges_html}
        </div>
      </div>
    </div>
  </section>
    """

    # 3. What We Deliver Section HTML (Present on domain pages -> LIGHT SLATE)
    what_we_deliver_html = ""
    if what_we_deliver:
        del_cards = []
        for d in what_we_deliver:
            items_html = "".join([f'<li style="color: #334155; font-size: 0.875rem; margin-bottom: 7px; display: flex; align-items: flex-start; gap: 8px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg><span>{it}</span></li>' for it in d.get('deliverables', [])])
            # Stack data removed per user request
            tech_tag = ""
            del_cards.append(f"""
            <div class="deliver-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); padding: var(--space-xl); display: flex; flex-direction: column; box-shadow: 0 4px 16px -2px rgba(11, 37, 69, 0.05);">
              <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #0284C7; background: #E0F2FE; padding: 4px 10px; border-radius: 999px; display: inline-block; margin-bottom: 12px; align-self: flex-start;">PRODUCTION DELIVERABLE</span>
              <h3 style="font-size: 1.25rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">{d['title']}</h3>
              <p style="color: #475569; font-size: 0.95rem; line-height: 1.6; margin-bottom: var(--space-md);">{d['desc']}</p>
              <ul style="list-style: none; padding: 0; margin: 0 0 var(--space-md) 0; border-top: 1px solid #E2E8F0; padding-top: var(--space-md);">
                {items_html}
              </ul>
              {tech_tag}
            </div>
            """)
        del_cards_str = "".join(del_cards)
        what_we_deliver_html = f"""
  <!-- What We Build / What We Deliver Section -->
  <section id="what-we-deliver" class="subpage-section-light-alt" style="padding: var(--space-4xl) 0; background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #0284C7;">WHAT WE BUILD &amp; DELIVER</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: #0F172A; margin: 8px 0 12px;">Production-Grade Platforms, Portals &amp; Engines</h2>
        <p class="subpage-section-desc" style="color: #475569; font-size: 1.05rem;">Concrete software architectures designed, built, integrated, and maintained for enterprise scale.</p>
      </div>
      <div class="subpage-grid-cards">
        {del_cards_str}
      </div>
    </div>
  </section>
        """

    # 4. Industries Served Deep-Dive Section HTML (Present on domain pages -> LIGHT SLATE)
    industries_served_html = ""
    if is_domain_page and original_industries_served:
        ind_cards = []
        for ind in original_industries_served:
            ind_title = ind.get('industry') or ind.get('name') or "Industry"
            ind_app = ind.get('application') or f"Tailored {ind_title} workflows engineered for maximum reliability."
            ind_out = ind.get('outcome') or f"Measurable operational efficiency and compliance for {ind_title}."
            ind_cards.append(f"""
            <div class="industry-served-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); padding: var(--space-xl); display: flex; flex-direction: column; box-shadow: 0 4px 16px -2px rgba(11, 37, 69, 0.05);">
              <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #0284C7; background: #E0F2FE; padding: 3px 10px; border-radius: 999px; display: inline-block; margin-bottom: 10px; align-self: flex-start;">INDUSTRY VERTICAL</span>
              <h3 style="font-size: 1.2rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">{ind_title}</h3>
              <div style="margin-bottom: var(--space-sm);">
                <strong style="color: #64748B; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 4px;">Vertical Implementation:</strong>
                <p style="color: #334155; font-size: 0.925rem; line-height: 1.55; margin: 0;">{ind_app}</p>
              </div>
              <div style="margin-top: auto; padding: 10px 14px; background: #F0F9FF; border-left: 3px solid #0284C7; border-radius: 6px; font-size: 0.85rem; color: #0C4A6E; line-height: 1.5;">
                <strong style="color: #0284C7; display: block; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Key Business Outcome:</strong>
                <span>{ind_out}</span>
              </div>
            </div>
            """)
        ind_cards_str = "".join(ind_cards)
        industries_served_html = f"""
  <!-- Industries Served Deep-Dive Section -->
  <section id="industries-deep-dive" class="subpage-section-light-alt" style="padding: var(--space-4xl) 0; background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #0284C7;">INDUSTRIES SERVED DEEP-DIVE</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: #0F172A; margin: 8px 0 12px;">Domain-Specific Vertical Applications</h2>
        <p class="subpage-section-desc" style="color: #475569; font-size: 1.05rem;">Proven engineering architectures tailored to the operational demands and regulatory standards of each sector.</p>
      </div>
      <div class="subpage-grid-cards">
        {ind_cards_str}
      </div>
    </div>
  </section>
        """

    # 5. Why Choose Us Section HTML (Present on domain pages -> LIGHT)
    why_choose_us_html = ""
    if why_choose_us:
        why_cards = []
        for w in why_choose_us:
            why_cards.append(f"""
            <div class="why-choose-card" style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); padding: var(--space-xl); position: relative; overflow: hidden; box-shadow: 0 4px 16px -2px rgba(11, 37, 69, 0.05);">
              <div style="width: 44px; height: 44px; border-radius: 10px; background: #E0F2FE; display: flex; align-items: center; justify-content: center; color: #0284C7; margin-bottom: 14px;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
              </div>
              <h3 style="font-size: 1.2rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">{w['title']}</h3>
              <p style="color: #475569; font-size: 0.925rem; line-height: 1.6; margin: 0;">{w['desc']}</p>
            </div>
            """)
        why_choose_us_str = "".join(why_cards)
        why_choose_us_html = f"""
  <!-- Why Choose Us Section -->
  <section id="why-choose-us" class="subpage-section-light" style="padding: var(--space-4xl) 0; background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #0284C7;">WHY CHOOSE NOVA ARC</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: #0F172A; margin: 8px 0 12px;">Architectural Rigor, Zero Lock-In &amp; Engineering Excellence</h2>
        <p class="subpage-section-desc" style="color: #475569; font-size: 1.05rem;">Built by senior architects and engineers committed to clean code, production reliability, and client code ownership.</p>
      </div>
      <div class="subpage-grid-2col">
        {why_choose_us_str}
      </div>
    </div>
  </section>
        """

    # Core Service Domains Switcher removed per user request
    services_domain_nav_html = ""

    # Problem & Resolution HTML:
    # If domain page: DARK (#0A1628)
    # If standard page: LIGHT SLATE (#F8FAFC)
    chal_cards = []
    for ch in challenges:
        if is_domain_page:
            chal_cards.append(f"""
            <div class="card subpage-card-padded" style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg); padding: var(--space-xl); display: flex; flex-direction: column;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: var(--space-sm);">
                <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 4px 10px; border-radius: 999px; background: rgba(239, 68, 68, 0.15); color: #F87171;">Business Challenge</span>
              </div>
              <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: var(--space-xs);">Business Problem</h3>
              <p style="color: #CBD5E1; font-size: 0.95rem; line-height: 1.55; margin-bottom: var(--space-md);">{ch['challenge']}</p>
              
              <div style="margin-bottom: var(--space-md); padding-top: var(--space-sm); border-top: 1px solid rgba(255,255,255,0.06);">
                <span style="font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: #F59E0B; display: block; margin-bottom: 4px;">Why It Matters:</span>
                <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.55; margin: 0;">{ch['impact']}</p>
              </div>

              <div style="margin-top: auto; padding: var(--space-md); background: rgba(14, 165, 233, 0.08); border-left: 3px solid #38BDF8; border-radius: 6px;">
                <strong style="color: #38BDF8; font-size: 0.85rem; display: block; margin-bottom: 4px;">Proposed Resolution:</strong>
                <span style="color: #E2E8F0; font-size: 0.9rem; line-height: 1.55;">{ch['solution']}</span>
              </div>
            </div>
            """)
        else:
            chal_cards.append(f"""
            <div class="card subpage-card-padded" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); padding: var(--space-xl); display: flex; flex-direction: column; box-shadow: 0 4px 16px -2px rgba(11, 37, 69, 0.05);">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: var(--space-sm);">
                <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 4px 10px; border-radius: 999px; background: #FEE2E2; color: #DC2626;">Business Challenge</span>
              </div>
              <h3 style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: var(--space-xs);">Business Problem</h3>
              <p style="color: #334155; font-size: 0.95rem; line-height: 1.55; margin-bottom: var(--space-md);">{ch['challenge']}</p>
              
              <div style="margin-bottom: var(--space-md); padding-top: var(--space-sm); border-top: 1px solid #E2E8F0;">
                <span style="font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: #D97706; display: block; margin-bottom: 4px;">Why It Matters:</span>
                <p style="color: #475569; font-size: 0.9rem; line-height: 1.55; margin: 0;">{ch['impact']}</p>
              </div>

              <div style="margin-top: auto; padding: var(--space-md); background: #F0F9FF; border-left: 3px solid #0284C7; border-radius: 6px;">
                <strong style="color: #0284C7; font-size: 0.85rem; display: block; margin-bottom: 4px;">Proposed Resolution:</strong>
                <span style="color: #0C4A6E; font-size: 0.9rem; line-height: 1.55;">{ch['solution']}</span>
              </div>
            </div>
            """)
    challenges_html = "".join(chal_cards)

    chal_sec_cls = "subpage-section-dark-alt" if is_domain_page else "subpage-section-light-alt"
    chal_sec_bg = "#0A1628" if is_domain_page else "#F8FAFC"
    chal_sec_border = "rgba(255,255,255,0.06)" if is_domain_page else "#E2E8F0"
    chal_eyebrow = "#38BDF8" if is_domain_page else "#0284C7"
    chal_heading = "#FFFFFF" if is_domain_page else "#0F172A"
    chal_desc = "#94A3B8" if is_domain_page else "#475569"

    section_problem_resolution_html = f"""
  <!-- Section 3: Problem & Resolution -->
  <section id="problem-resolution" class="{chal_sec_cls}" style="padding: var(--space-4xl) 0; background: {chal_sec_bg}; border-bottom: 1px solid {chal_sec_border};">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: {chal_eyebrow};">PROBLEM &amp; RESOLUTION</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: {chal_heading}; margin: 8px 0 12px;">Operational Challenges &amp; Technical Resolutions</h2>
        <p class="subpage-section-desc" style="color: {chal_desc}; font-size: 1.05rem;">How Nova Arc overcomes systemic process inefficiencies, operational friction, and technology bottlenecks.</p>
      </div>

      <div class="subpage-grid-cards">
        {challenges_html}
      </div>
    </div>
  </section>
    """

    # Practical Applications HTML:
    # If domain page: LIGHT (#FFFFFF)
    # If standard page: DARK (#08111F)
    use_cases_html = ""
    if use_cases:
        uc_cards = []
        for uc in use_cases:
            if is_domain_page:
                ex_box = f"<div style='margin-top: auto; padding: 12px 14px; background: #F0F9FF; border-radius: 6px; border-left: 3px solid #0284C7; font-size: 0.875rem; color: #0C4A6E; line-height: 1.55;'><strong style='color: #0284C7; display: block; margin-bottom: 3px; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em;'>Expected Operational Value:</strong>{uc['example']}</div>" if uc.get('example') else ""
                uc_cards.append(f"""
                <div class="card subpage-card-padded" style="padding: var(--space-xl); background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); display: flex; flex-direction: column; box-shadow: 0 4px 16px -2px rgba(11, 37, 69, 0.04);">
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                    <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #0284C7; background: #E0F2FE; padding: 4px 10px; border-radius: 999px;">PRACTICAL APPLICATION</span>
                  </div>
                  <h3 style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin-bottom: var(--space-xs);"><span style="display: block; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #64748B; font-weight: 600; margin-bottom: 2px;">Application Name</span>{uc['title']}</h3>
                  <div style="margin-bottom: var(--space-md);">
                    <strong style="display: block; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #64748B; font-weight: 600; margin-bottom: 2px;">Business Scenario &amp; How It Is Used:</strong>
                    <p style="color: #334155; font-size: 0.925rem; line-height: 1.6; margin: 0;">{uc['desc']}</p>
                  </div>
                  {ex_box}
                </div>
                """)
            else:
                ex_box = f"<div style='margin-top: auto; padding: 12px 14px; background: rgba(56, 189, 248, 0.08); border-radius: 6px; border-left: 3px solid #38BDF8; font-size: 0.875rem; color: #E2E8F0; line-height: 1.55;'><strong style='color: #38BDF8; display: block; margin-bottom: 3px; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em;'>Expected Operational Value:</strong>{uc['example']}</div>" if uc.get('example') else ""
                uc_cards.append(f"""
                <div class="card subpage-card-padded" style="padding: var(--space-xl); background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg); display: flex; flex-direction: column;">
                  <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;">
                    <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #38BDF8; background: rgba(56, 189, 248, 0.1); padding: 4px 10px; border-radius: 999px;">PRACTICAL APPLICATION</span>
                  </div>
                  <h3 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: var(--space-xs);"><span style="display: block; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #94A3B8; font-weight: 600; margin-bottom: 2px;">Application Name</span>{uc['title']}</h3>
                  <div style="margin-bottom: var(--space-md);">
                    <strong style="display: block; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #94A3B8; font-weight: 600; margin-bottom: 2px;">Business Scenario &amp; How It Is Used:</strong>
                    <p style="color: #94A3B8; font-size: 0.925rem; line-height: 1.6; margin: 0;">{uc['desc']}</p>
                  </div>
                  {ex_box}
                </div>
                """)

        uc_sec_cls = "subpage-section-light" if is_domain_page else "subpage-section-dark"
        uc_sec_bg = "#FFFFFF" if is_domain_page else "#08111F"
        uc_sec_border = "#E2E8F0" if is_domain_page else "rgba(255,255,255,0.06)"
        uc_eyebrow = "#0284C7" if is_domain_page else "#38BDF8"
        uc_heading = "#0F172A" if is_domain_page else "#FFFFFF"
        uc_desc = "#475569" if is_domain_page else "#94A3B8"

        use_cases_html = f"""
  <!-- Section: Practical Applications -->
  <section id="practical-applications" class="{uc_sec_cls}" style="padding: var(--space-4xl) 0; background: {uc_sec_bg}; border-bottom: 1px solid {uc_sec_border};">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: {uc_eyebrow};">PRACTICAL APPLICATIONS</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: {uc_heading}; margin: 8px 0 12px;">Real-World Enterprise Applications &amp; Workflows</h2>
        <p class="subpage-section-desc" style="color: {uc_desc}; font-size: 1.05rem;">Realistic ways organizations apply these capabilities to solve tangible operational challenges.</p>
      </div>
      <div class="subpage-grid-cards">
        {"".join(uc_cards)}
      </div>
    </div>
  </section>
        """

    # Engineering Methodology HTML (5-Stage Lifecycle):
    # If domain page: DARK (#0A1628)
    # If standard page: LIGHT (#FFFFFF)
    steps_html = []
    for st in workflow_steps:
        if is_domain_page:
            steps_html.append(f"""
            <div class="subpage-methodology-card" style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: var(--radius-lg); padding: 24px 18px; display: flex; flex-direction: column; position: relative;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <span class="subpage-methodology-badge" style="font-size: 0.95rem; font-weight: 800; color: #38BDF8; background: rgba(56, 189, 248, 0.12); padding: 4px 10px; border-radius: 6px; display: inline-block; width: fit-content;">{st['step']}</span>
                <div style="width: 28px; height: 28px; border-radius: 50%; background: rgba(255,255,255,0.06); display: flex; align-items: center; justify-content: center; color: #38BDF8;">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                </div>
              </div>
              <h4 class="subpage-methodology-title" style="font-size: 1.05rem; font-weight: 700; color: #FFFFFF; margin: 8px 0;">{st['title']}</h4>
              <p class="subpage-methodology-desc" style="color: #94A3B8; font-size: 0.9rem; line-height: 1.55; margin: 0;">{st['desc']}</p>
            </div>
            """)
        else:
            steps_html.append(f"""
            <div class="subpage-methodology-card" style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); padding: 24px 18px; display: flex; flex-direction: column; position: relative; box-shadow: 0 2px 8px -2px rgba(11, 37, 69, 0.05);">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <span class="subpage-methodology-badge" style="font-size: 0.95rem; font-weight: 800; color: #0284C7; background: #E0F2FE; padding: 4px 10px; border-radius: 6px; display: inline-block; width: fit-content;">{st['step']}</span>
                <div style="width: 28px; height: 28px; border-radius: 50%; background: #FFFFFF; border: 1px solid #E2E8F0; display: flex; align-items: center; justify-content: center; color: #0284C7;">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                </div>
              </div>
              <h4 class="subpage-methodology-title" style="font-size: 1.05rem; font-weight: 700; color: #0F172A; margin: 8px 0;">{st['title']}</h4>
              <p class="subpage-methodology-desc" style="color: #475569; font-size: 0.9rem; line-height: 1.55; margin: 0;">{st['desc']}</p>
            </div>
            """)
    workflow_html = "".join(steps_html)

    wf_sec_cls = "subpage-section-dark-alt" if is_domain_page else "subpage-section-light"
    wf_sec_bg = "#0A1628" if is_domain_page else "#FFFFFF"
    wf_sec_border = "rgba(255,255,255,0.06)" if is_domain_page else "#E2E8F0"
    wf_eyebrow = "#38BDF8" if is_domain_page else "#0284C7"
    wf_heading = "#FFFFFF" if is_domain_page else "#0F172A"
    wf_desc = "#94A3B8" if is_domain_page else "#475569"

    section_methodology_html = f"""
  <!-- Section 4: Engineering Methodology (5-Stage Lifecycle) -->
  <section id="engineering-methodology" class="{wf_sec_cls}" style="padding: var(--space-4xl) 0; background: {wf_sec_bg}; border-bottom: 1px solid {wf_sec_border};">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: {wf_eyebrow};">ENGINEERING METHODOLOGY</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: {wf_heading}; margin: 8px 0 12px;">Disciplined 5-Stage Engineering Lifecycle</h2>
        <p class="subpage-section-desc" style="color: {wf_desc}; font-size: 1.05rem;">A structured implementation approach tailored to your systems, workflows, and governance requirements.</p>
      </div>

      <div class="subpage-methodology-grid">
        {workflow_html}
      </div>
    </div>
  </section>
    """

    # System Connectivity HTML (ALWAYS DARK NAVY)
    integrations_html = ""
    if integrations:
        int_cards = []
        for item in integrations:
            int_cards.append(f"""
            <div style="background: rgba(11, 25, 44, 0.65); border: 1px solid rgba(56, 189, 248, 0.16); border-radius: var(--radius-md); padding: var(--space-lg);">
              <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: #38BDF8; background: rgba(56, 189, 248, 0.1); padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px;">Integration Boundary</span>
              <h4 style="font-size: 1.05rem; font-weight: 700; color: #FFFFFF; margin-bottom: 6px;">{item['category']}</h4>
              <p style="color: #CBD5E1; font-size: 0.9rem; line-height: 1.55; margin: 0;">{item['details']}</p>
            </div>
            """)
        int_sec_bg = "#08111F" if is_domain_page else "#0A1628"
        integrations_html = f"""
  <!-- Section: System Connectivity -->
  <section id="system-connectivity" class="subpage-section-dark" style="padding: var(--space-4xl) 0; background: {int_sec_bg}; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8;">SYSTEM CONNECTIVITY</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: #FFFFFF; margin: 8px 0 12px;">Enterprise System Connectivity &amp; Data Flow</h2>
        <p class="subpage-section-desc" style="color: #94A3B8; font-size: 1.05rem;">Configurable interfaces connecting with your existing enterprise infrastructure, databases, and APIs.</p>
      </div>
      <div class="subpage-grid-2col">
        {"".join(int_cards)}
      </div>
    </div>
  </section>
        """

    # Deployment & Oversight HTML:
    # If domain page: DARK (#0A1628)
    # If standard page: LIGHT SLATE (#F8FAFC)
    considerations_html = ""
    if considerations:
        cons_cards = []
        for c in considerations:
            if is_domain_page:
                cons_cards.append(f"""
                <div class="subpage-card-padded" style="padding: var(--space-lg); background: rgba(15, 23, 42, 0.6); border-radius: var(--radius-md); border-left: 3px solid #38BDF8; border-top: 1px solid rgba(255,255,255,0.06); border-right: 1px solid rgba(255,255,255,0.06); border-bottom: 1px solid rgba(255,255,255,0.06);">
                  <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: #94A3B8; display: inline-block; margin-bottom: 4px;">Governance &amp; Controls</span>
                  <h4 style="font-size: 1.05rem; font-weight: 700; color: #FFFFFF; margin-bottom: 6px;">{c['title']}</h4>
                  <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.55; margin: 0;">{c['desc']}</p>
                </div>
                """)
            else:
                cons_cards.append(f"""
                <div class="subpage-card-padded" style="padding: var(--space-lg); background: #FFFFFF; border-radius: var(--radius-md); border: 1px solid #E2E8F0; border-left: 3px solid #0284C7; box-shadow: 0 2px 8px -2px rgba(11, 37, 69, 0.04);">
                  <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; color: #64748B; display: inline-block; margin-bottom: 4px;">Governance &amp; Controls</span>
                  <h4 style="font-size: 1.05rem; font-weight: 700; color: #0F172A; margin-bottom: 6px;">{c['title']}</h4>
                  <p style="color: #475569; font-size: 0.9rem; line-height: 1.55; margin: 0;">{c['desc']}</p>
                </div>
                """)

        cons_sec_cls = "subpage-section-dark-alt" if is_domain_page else "subpage-section-light-alt"
        cons_sec_bg = "#0A1628" if is_domain_page else "#F8FAFC"
        cons_sec_border = "rgba(255,255,255,0.06)" if is_domain_page else "#E2E8F0"
        cons_eyebrow = "#38BDF8" if is_domain_page else "#0284C7"
        cons_heading = "#FFFFFF" if is_domain_page else "#0F172A"
        cons_desc = "#94A3B8" if is_domain_page else "#475569"

        considerations_html = f"""
  <!-- Section: Deployment & Oversight -->
  <section id="deployment-oversight" class="{cons_sec_cls}" style="padding: var(--space-4xl) 0; background: {cons_sec_bg}; border-bottom: 1px solid {cons_sec_border};">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: {cons_eyebrow};">DEPLOYMENT &amp; OVERSIGHT</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: {cons_heading}; margin: 8px 0 12px;">Implementation Lifecycle, Security &amp; Human Oversight</h2>
        <p class="subpage-section-desc" style="color: {cons_desc}; font-size: 1.05rem;">Prerequisites, security safeguards, and human review gates required for dependable execution.</p>
      </div>
      <div class="subpage-grid-2col">
        {"".join(cons_cards)}
      </div>
    </div>
  </section>
        """

    # Potential Business Benefits HTML:
    # If domain page: LIGHT (#FFFFFF)
    # If standard page: DARK (#08111F)
    outcomes_html_list = []
    for out in outcomes:
        if is_domain_page:
            outcomes_html_list.append(f"""
            <div class="subpage-card-padded" style="background: #F8FAFC; border: 1px solid #BAE6FD; border-radius: var(--radius-lg); padding: var(--space-xl); box-shadow: 0 4px 16px -2px rgba(11, 37, 69, 0.05);">
              <div style="width: 36px; height: 36px; border-radius: 8px; background: #E0F2FE; display: flex; align-items: center; justify-content: center; color: #0284C7; margin-bottom: var(--space-md);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              </div>
              <h4 style="font-size: 1.1rem; font-weight: 700; color: #0F172A; margin-bottom: 6px;">{out['title']}</h4>
              <p style="color: #475569; font-size: 0.9rem; line-height: 1.55; margin: 0;">{out['desc']}</p>
            </div>
            """)
        else:
            outcomes_html_list.append(f"""
            <div class="subpage-card-padded" style="background: rgba(15, 23, 42, 0.55); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: var(--radius-lg); padding: var(--space-xl);">
              <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(56, 189, 248, 0.15); display: flex; align-items: center; justify-content: center; color: #38BDF8; margin-bottom: var(--space-md);">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              </div>
              <h4 style="font-size: 1.1rem; font-weight: 700; color: #FFFFFF; margin-bottom: 6px;">{out['title']}</h4>
              <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.55; margin: 0;">{out['desc']}</p>
            </div>
            """)
    outcomes_grid_html = "".join(outcomes_html_list)

    out_sec_cls = "subpage-section-light" if is_domain_page else "subpage-section-dark"
    out_sec_bg = "#FFFFFF" if is_domain_page else "#08111F"
    out_sec_border = "#E2E8F0" if is_domain_page else "rgba(255,255,255,0.06)"
    out_eyebrow = "#0284C7" if is_domain_page else "#38BDF8"
    out_heading = "#0F172A" if is_domain_page else "#FFFFFF"
    out_desc = "#475569" if is_domain_page else "#94A3B8"

    section_benefits_html = f"""
  <!-- Section 7: Potential Business Benefits -->
  <section id="business-benefits" class="{out_sec_cls}" style="padding: var(--space-4xl) 0; background: {out_sec_bg}; border-bottom: 1px solid {out_sec_border};">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: {out_eyebrow};">POTENTIAL BUSINESS BENEFITS</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: {out_heading}; margin: 8px 0 12px;">Operational Advantages &amp; Measured Business Value</h2>
        <p class="subpage-section-desc" style="color: {out_desc}; font-size: 1.05rem;">Streamlining repetitive administrative overhead into sustained operational velocity.</p>
      </div>

      <div class="subpage-grid-outcomes">
        {outcomes_grid_html}
      </div>
    </div>
  </section>
    """

    # Frequently Asked Questions HTML:
    # If domain page: DARK (#0A1628)
    # If standard page: LIGHT (#FFFFFF)
    faqs_html = ""
    if faqs:
        faq_items = []
        for q in faqs:
            if is_domain_page:
                faq_items.append(f"""
                <details style="background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-md); padding: var(--space-md) var(--space-lg); margin-bottom: var(--space-sm);">
                  <summary style="font-weight: 700; color: #FFFFFF; font-size: 1.05rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                    <span>{q['q']}</span>
                    <span style="color: #38BDF8; font-size: 1.25rem; font-weight: 400; margin-left: 12px;">+</span>
                  </summary>
                  <div style="color: #94A3B8; font-size: 0.925rem; line-height: 1.6; margin-top: var(--space-sm); border-top: 1px solid rgba(255,255,255,0.06); padding-top: var(--space-sm);">
                    {q['a']}
                  </div>
                </details>
                """)
            else:
                faq_items.append(f"""
                <details style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: var(--radius-md); padding: var(--space-md) var(--space-lg); margin-bottom: var(--space-sm); box-shadow: 0 1px 4px rgba(11,37,69,0.03);">
                  <summary style="font-weight: 700; color: #0F172A; font-size: 1.05rem; cursor: pointer; display: flex; justify-content: space-between; align-items: center;">
                    <span>{q['q']}</span>
                    <span style="color: #0284C7; font-size: 1.25rem; font-weight: 400; margin-left: 12px;">+</span>
                  </summary>
                  <div style="color: #475569; font-size: 0.925rem; line-height: 1.6; margin-top: var(--space-sm); border-top: 1px solid #E2E8F0; padding-top: var(--space-sm);">
                    {q['a']}
                  </div>
                </details>
                """)

        faq_sec_cls = "subpage-section-dark-alt" if is_domain_page else "subpage-section-light"
        faq_sec_bg = "#0A1628" if is_domain_page else "#FFFFFF"
        faq_sec_border = "rgba(255,255,255,0.06)" if is_domain_page else "#E2E8F0"
        faq_eyebrow = "#38BDF8" if is_domain_page else "#0284C7"
        faq_heading = "#FFFFFF" if is_domain_page else "#0F172A"
        faq_desc = "#94A3B8" if is_domain_page else "#475569"

        faqs_html = f"""
  <!-- Section: Frequently Asked Questions -->
  <section id="frequently-asked-questions" class="{faq_sec_cls}" style="padding: var(--space-4xl) 0; background: {faq_sec_bg}; border-bottom: 1px solid {faq_sec_border};">
    <div class="container" style="max-width: 860px; margin: 0 auto;">
      <div style="text-align: center; margin-bottom: var(--space-3xl);">
        <span class="eyebrow-ags" style="color: {faq_eyebrow};">FREQUENTLY ASKED QUESTIONS</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: {faq_heading}; margin: 8px 0 12px;">Frequently Asked Questions</h2>
        <p class="subpage-section-desc" style="color: {faq_desc}; font-size: 1.05rem;">Practical guidance regarding project scope, integrations, and operational requirements.</p>
      </div>
      <div>
        {"".join(faq_items)}
      </div>
    </div>
  </section>
        """

    # Connected Ecosystem HTML:
    # If domain page: LIGHT SLATE (#F8FAFC)
    # If standard page: DARK (#08111F)
    related_html = []
    for rel in related_links:
        if is_domain_page:
            related_html.append(f"""
            <a href="{root_prefix}{rel['link']}" class="card" style="padding: var(--space-lg); text-decoration: none; display: block; transition: all 0.2s ease; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); box-shadow: 0 2px 8px -2px rgba(11, 37, 69, 0.05);">
              <span style="font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #0284C7; font-weight: 700; background: #E0F2FE; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 6px;">{rel.get('tag', 'Related Service')}</span>
              <h4 style="font-size: 1.1rem; color: #0F172A; margin: 6px 0 4px;">{rel['title']} &rarr;</h4>
              <p style="color: #475569; font-size: 0.85rem; margin: 0; line-height: 1.45;">{rel['desc']}</p>
            </a>
            """)
        else:
            related_html.append(f"""
            <a href="{root_prefix}{rel['link']}" class="card" style="padding: var(--space-lg); text-decoration: none; display: block; transition: all 0.2s ease; background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg);">
              <span style="font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #38BDF8; font-weight: 700; background: rgba(56, 189, 248, 0.1); padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 6px;">{rel.get('tag', 'Related Service')}</span>
              <h4 style="font-size: 1.1rem; color: #FFFFFF; margin: 6px 0 4px;">{rel['title']} &rarr;</h4>
              <p style="color: #94A3B8; font-size: 0.85rem; margin: 0; line-height: 1.45;">{rel['desc']}</p>
            </a>
            """)
    related_grid_html = "".join(related_html)

    rel_sec_cls = "subpage-section-light-alt" if is_domain_page else "subpage-section-dark"
    rel_sec_bg = "#F8FAFC" if is_domain_page else "#08111F"
    rel_sec_border = "#E2E8F0" if is_domain_page else "rgba(255,255,255,0.06)"
    rel_eyebrow = "#0284C7" if is_domain_page else "#38BDF8"
    rel_heading = "#0F172A" if is_domain_page else "#FFFFFF"
    rel_desc = "#475569" if is_domain_page else "#94A3B8"

    section_ecosystem_html = f"""
  <!-- Section 9: Connected Ecosystem -->
  <section id="connected-ecosystem" class="{rel_sec_cls}" style="padding: var(--space-4xl) 0; background: {rel_sec_bg}; border-bottom: 1px solid {rel_sec_border};">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: {rel_eyebrow};">CONNECTED ECOSYSTEM</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: {rel_heading}; margin: 8px 0 12px;">Cross-Domain Enterprise Ecosystem Integration</h2>
        <p class="subpage-section-desc" style="color: {rel_desc}; font-size: 1.05rem;">Integrate complementary enterprise modules across our four core service domains.</p>
      </div>

      <div class="subpage-grid-related">
        {related_grid_html}
      </div>
    </div>
  </section>
    """

    # Bottom CTA:
    # If domain page (connected ecosystem is light): DARK GRADIENT BANNER
    # If standard page (connected ecosystem is dark): LIGHT CONTAINER WITH FLOATING DARK GRADIENT CARD
    if is_domain_page:
        bottom_cta_html = f"""
  <!-- Bottom CTA Banner (Dark Gradient) -->
  <section class="cta-strip-ags subpage-section-dark" style="padding: var(--space-4xl) 0; background: linear-gradient(135deg, #07172B 0%, #0B2545 60%, #0E2E56 100%); text-align: center; border-top: 1px solid rgba(255,255,255,0.08);">
    <div class="container" style="max-width: 760px; margin: 0 auto;">
      <h2 style="font-size: clamp(2rem, 3.5vw, 2.8rem); font-weight: 800; color: #FFFFFF; margin-bottom: var(--space-md); letter-spacing: -0.02em;">
        Let’s Build Your Next Business Solution.
      </h2>
      <p style="font-size: 1.1rem; color: #CBD5E1; line-height: 1.65; margin-bottom: var(--space-2xl);">
        Discuss your business challenges, operational needs, and technology goals with our team. We evaluate your existing system architecture and help you plan the right solution.
      </p>
      <div style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap;">
        <a href="{root_prefix}contact.html" class="btn btn-consultation-ags" style="font-size: 1.05rem; padding: 14px 34px;">
          <span>Discuss Your Project</span>
          <svg class="btn-arrow-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </a>
        <a href="tel:04046146093" class="btn btn-outline-white" style="font-size: 1.05rem; padding: 14px 28px;">
          <span>Call 040-46146093</span>
        </a>
      </div>
    </div>
  </section>
        """
    else:
        bottom_cta_html = f"""
  <!-- Bottom CTA Container (Light Background with Floating Dark Gradient Card) -->
  <section class="subpage-cta-section subpage-section-light-alt" style="padding: var(--space-4xl) 0; background: #F8FAFC; border-top: 1px solid #E2E8F0; text-align: center;">
    <div class="container" style="max-width: 960px; margin: 0 auto;">
      <div style="background: linear-gradient(135deg, #07172B 0%, #0B2545 60%, #0E2E56 100%); border-radius: var(--radius-xl); padding: var(--space-3xl) var(--space-2xl); text-align: center; box-shadow: 0 20px 45px -10px rgba(11,37,69,0.22); border: 1px solid rgba(56, 189, 248, 0.25);">
        <h2 style="font-size: clamp(2rem, 3.5vw, 2.7rem); font-weight: 800; color: #FFFFFF; margin-bottom: var(--space-md); letter-spacing: -0.02em;">
          Let’s Build Your Next Business Solution.
        </h2>
        <p style="font-size: 1.05rem; color: #CBD5E1; line-height: 1.65; max-width: 680px; margin: 0 auto var(--space-2xl);">
          Discuss your business challenges, operational needs, and technology goals with our team. We evaluate your existing system architecture and help you plan the right solution.
        </p>
        <div style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap;">
          <a href="{root_prefix}contact.html" class="btn btn-consultation-ags" style="font-size: 1.05rem; padding: 14px 34px;">
            <span>Discuss Your Project</span>
            <svg class="btn-arrow-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </a>
          <a href="tel:04046146093" class="btn btn-outline-white" style="font-size: 1.05rem; padding: 14px 28px;">
            <span>Call 040-46146093</span>
          </a>
        </div>
      </div>
    </div>
  </section>
        """

    # Introductory description (approx 40-60 words) & Supporting explanation (approx 25-40 words)
    intro_desc = overview_paragraphs[0] if len(overview_paragraphs) > 0 else page_subtitle
    supp_expl = overview_paragraphs[1] if len(overview_paragraphs) > 1 else ""
    if len(overview_paragraphs) > 2 and len(intro_desc.split()) < 35:
        intro_desc = f"{overview_paragraphs[0]} {overview_paragraphs[1]}"
        supp_expl = overview_paragraphs[2]

    # Large domain-specific hero illustration
    hero_illustration_svg = get_hero_svg_for_page(rel_path, page_title, category_badge)

    canonical_url = f"https://novaarctech.in/{rel_path}"

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

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="{root_prefix}images/nova-arc-logo.png">

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

{get_shared_header(root_prefix, active_sec)}

  <!-- Hero Section (Information-Rich Two-Column Layout) -->
  <section class="services-hero-ags hero-two-col-section" style="min-height: calc(100vh - 75px); display: flex; flex-direction: column; justify-content: center; box-sizing: border-box; padding-top: calc(75px + clamp(16px, 2.2vw, 32px)); padding-bottom: clamp(24px, 3.2vw, 44px); position: relative; overflow: hidden;">
    <div class="hero-orchestrated-glow-cyan"></div>
    <div class="hero-orchestrated-glow-blue"></div>
    {get_ecg_waveform_html()}

    <div class="container hero-container-ags">
      <div class="hero-two-col-grid">
        
        <!-- Left Column: Content & Context -->
        <div class="hero-left-col">
          <nav class="breadcrumb-nav" aria-label="Breadcrumb" style="margin-bottom: 8px;">
            <ol class="breadcrumb-list" style="display: flex; gap: 8px; list-style: none; padding: 0; margin: 0; font-size: 0.82rem; color: #94A3B8;">
              {breadcrumbs_html}
            </ol>
          </nav>
          <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; font-size: 0.82rem; letter-spacing: 0.08em; display: inline-block; margin-bottom: 8px;">{category_badge}</span>
          <h1 class="hero-title-ags" style="font-size: clamp(2.1rem, 3.3vw, 3.2rem); line-height: 1.15; color: #FFFFFF; font-weight: 800; margin-bottom: 12px; letter-spacing: -0.02em;">{page_title}</h1>
          <p class="hero-tagline-ags" style="font-size: clamp(1.02rem, 1.25vw, 1.15rem); font-weight: 600; color: #38BDF8; line-height: 1.45; margin-bottom: 14px;">
            {page_subtitle}
          </p>
          <p class="hero-intro-text" style="font-size: 0.98rem; line-height: 1.65; color: #E2E8F0; margin-bottom: 12px;">
            {intro_desc}
          </p>
          {f'<p class="hero-supporting-text" style="font-size: 0.88rem; line-height: 1.6; color: #94A3B8; margin-bottom: 22px;">{supp_expl}</p>' if supp_expl else ''}
          <div class="hero-actions-ags" style="display: flex; gap: var(--space-md); flex-wrap: wrap; align-items: center;">
            <a href="{root_prefix}contact.html" class="btn btn-consultation-ags" style="padding: 12px 28px; font-size: 0.98rem;">
              <span>Discuss Your Project</span>
              <svg class="btn-arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </a>
            <a href="#key-capabilities" class="btn btn-outline-white" style="padding: 12px 24px; font-size: 0.98rem;">
              <span>Explore Capabilities</span>
            </a>
          </div>
        </div>

        <!-- Right Column: Domain Architectural Diagram -->
        <div class="hero-right-col">
          {hero_illustration_svg}
        </div>

      </div>
    </div>
  </section>

  {services_domain_nav_html}

  {business_value_section_html}

  <!-- Section 2: Key Capabilities (DARK NAVY) -->
  <section id="key-capabilities" class="subpage-section-dark" style="padding: clamp(48px, 6vw, 76px) 0; background: #08111F; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8;">KEY CAPABILITIES</span>
        <h2 class="subpage-section-heading" style="font-size: clamp(1.8rem, 2.8vw, 2.4rem); font-weight: 800; color: #FFFFFF; margin: 8px 0 12px;">Core Architecture &amp; Functional Capabilities</h2>
        <p class="subpage-section-desc" style="color: #94A3B8; font-size: 1.02rem; line-height: 1.6;">Purpose-built engineering modules designed to integrate cleanly into your existing enterprise stack.</p>
      </div>

      <div class="subpage-grid-cards capability-grid-compact">
        {capabilities_html}
      </div>
    </div>
  </section>

  {industries_served_section_html}

  {what_we_deliver_html}

  {section_problem_resolution_html}

  {use_cases_html}

  {section_methodology_html}

  {integrations_html}

  {why_choose_us_html}

  {considerations_html}

  {faqs_html}

  {section_ecosystem_html}

  {bottom_cta_html}

{get_shared_footer(root_prefix)}

  <!-- Scripts -->
  <script src="{root_prefix}js/main.js?v=4.0"></script>
</body>
</html>
"""
    return html
