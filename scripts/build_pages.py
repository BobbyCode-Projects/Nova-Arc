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
      <a href="{root_prefix}index.html" class="logo" aria-label="NovaArc Homepage">
        <img src="{root_prefix}images/novaarc-icon.svg" alt="NovaArc Logo" class="logo-img" width="38" height="38">
        <span class="logo-text">NOVA<span class="logo-highlight">ARC</span></span>
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
        <a href="{root_prefix}index.html" class="mobile-drawer-logo" aria-label="NovaArc Home">
          <img src="{root_prefix}images/novaarc-icon-dark.svg" alt="NovaArc Logo" width="36" height="36" class="mobile-drawer-logo-img">
          <span class="mobile-drawer-logo-title">NOVA<span class="mobile-drawer-logo-accent">ARC</span></span>
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
                <div class="mobile-subcat-group mobile-catalog-link-group">
                  <a href="{root_prefix}services.html" class="mobile-subcat-main-link">
                    <span>All Services Catalog</span>
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                  </a>
                </div>

                <!-- 1. Digital Commerce & Supply Chain -->
                <div class="mobile-subcat-accordion">
                  <button type="button" class="mobile-subcat-toggle mobile-accordion-toggle" id="toggleSubcatDC" aria-expanded="false" aria-controls="collapseSubcatDC">
                    <span class="mobile-subcat-toggle-text">Digital Commerce &amp; Supply Chain</span>
                    <svg class="mobile-subcat-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                      <polyline points="6 9 12 15 18 9"></polyline>
                    </svg>
                  </button>
                  <div class="mobile-nested-collapse" id="collapseSubcatDC" aria-hidden="true">
                    <ul class="mobile-sublink-list">
                      <li>
                        <a href="{root_prefix}services/digital-commerce.html" class="mobile-sublink mobile-sublink-overview">
                          <span>Digital Commerce Overview</span>
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                      </li>
                      <li><a href="{root_prefix}services/digital-commerce-platforms.html" class="mobile-sublink">Digital Commerce Platforms</a></li>
                      <li><a href="{root_prefix}services/foodtech.html" class="mobile-sublink">FoodTech Solutions</a></li>
                      <li><a href="{root_prefix}services/supply-chain-management.html" class="mobile-sublink">Supply Chain Management</a></li>
                      <li><a href="{root_prefix}services/procurement.html" class="mobile-sublink">Procurement &amp; Vendor Management</a></li>
                      <li><a href="{root_prefix}services/logistics.html" class="mobile-sublink">Logistics &amp; Distribution</a></li>
                    </ul>
                  </div>
                </div>

                <!-- 2. Enterprise Business Solutions -->
                <div class="mobile-subcat-accordion">
                  <button type="button" class="mobile-subcat-toggle mobile-accordion-toggle" id="toggleSubcatEBS" aria-expanded="false" aria-controls="collapseSubcatEBS">
                    <span class="mobile-subcat-toggle-text">Enterprise Business Solutions</span>
                    <svg class="mobile-subcat-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                      <polyline points="6 9 12 15 18 9"></polyline>
                    </svg>
                  </button>
                  <div class="mobile-nested-collapse" id="collapseSubcatEBS" aria-hidden="true">
                    <ul class="mobile-sublink-list">
                      <li>
                        <a href="{root_prefix}services/enterprise-business.html" class="mobile-sublink mobile-sublink-overview">
                          <span>Enterprise Business Overview</span>
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                      </li>
                      <li><a href="{root_prefix}services/crm.html" class="mobile-sublink">Customer Relationship Management (CRM)</a></li>
                      <li><a href="{root_prefix}services/hrms.html" class="mobile-sublink">Human Resource Management (HRMS)</a></li>
                      <li><a href="{root_prefix}services/business-process-automation.html" class="mobile-sublink">Business Process Automation</a></li>
                      <li><a href="{root_prefix}services/enterprise-applications.html" class="mobile-sublink">Custom Enterprise Applications</a></li>
                      <li><a href="{root_prefix}services/enterprise-integration.html" class="mobile-sublink">Enterprise Integration &amp; Middleware</a></li>
                    </ul>
                  </div>
                </div>

                <!-- 3. Intelligent Monitoring & Automation -->
                <div class="mobile-subcat-accordion">
                  <button type="button" class="mobile-subcat-toggle mobile-accordion-toggle" id="toggleSubcatIMA" aria-expanded="false" aria-controls="collapseSubcatIMA">
                    <span class="mobile-subcat-toggle-text">Intelligent Monitoring &amp; Automation</span>
                    <svg class="mobile-subcat-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                      <polyline points="6 9 12 15 18 9"></polyline>
                    </svg>
                  </button>
                  <div class="mobile-nested-collapse" id="collapseSubcatIMA" aria-hidden="true">
                    <ul class="mobile-sublink-list">
                      <li>
                        <a href="{root_prefix}services/intelligent-monitoring.html" class="mobile-sublink mobile-sublink-overview">
                          <span>Intelligent Monitoring Overview</span>
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                      </li>
                      <li><a href="{root_prefix}services/real-time-monitoring.html" class="mobile-sublink">Real-Time Monitoring &amp; Dashboards</a></li>
                      <li><a href="{root_prefix}services/iot-integration.html" class="mobile-sublink">IoT &amp; Device Integration</a></li>
                      <li><a href="{root_prefix}services/operational-analytics.html" class="mobile-sublink">Operational Analytics</a></li>
                      <li><a href="{root_prefix}services/workflow-automation.html" class="mobile-sublink">Workflow &amp; Process Automation</a></li>
                      <li><a href="{root_prefix}services/infrastructure-monitoring.html" class="mobile-sublink">System &amp; Infrastructure Monitoring</a></li>
                    </ul>
                  </div>
                </div>

                <!-- 4. AI & Healthcare Technology -->
                <div class="mobile-subcat-accordion">
                  <button type="button" class="mobile-subcat-toggle mobile-accordion-toggle" id="toggleSubcatAIH" aria-expanded="false" aria-controls="collapseSubcatAIH">
                    <span class="mobile-subcat-toggle-text">AI &amp; Healthcare Technology</span>
                    <svg class="mobile-subcat-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                      <polyline points="6 9 12 15 18 9"></polyline>
                    </svg>
                  </button>
                  <div class="mobile-nested-collapse" id="collapseSubcatAIH" aria-hidden="true">
                    <ul class="mobile-sublink-list">
                      <li>
                        <a href="{root_prefix}services/ai-healthcare.html" class="mobile-sublink mobile-sublink-overview">
                          <span>AI &amp; Healthcare Overview</span>
                          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                        </a>
                      </li>
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
          <a href="{root_prefix}index.html" class="footer-logo" aria-label="NovaArc Technologies Services Home">
            <img src="{root_prefix}images/novaarc-logo-stacked.svg" alt="NovaArc Technologies Services Pvt Ltd" class="footer-logo-stacked" width="220" height="183">
          </a>
          <p class="footer-desc">
            NovaArc is an enterprise technology and intelligent solutions company helping organizations modernize business operations through digital platforms, enterprise applications, connected systems, intelligent automation, and applied AI.
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
    'Digital Commerce': 'services/digital-commerce-platforms.html',
    'FoodTech Solutions': 'services/foodtech.html',
    'Supply Chain Management': 'services/supply-chain-management.html',
    'Procurement & Vendor Management': 'services/procurement.html',
    'Logistics & Distribution': 'services/logistics.html',
    
    # Domain 2: Enterprise Business Solutions
    'Customer Relationship Management (CRM)': 'services/crm.html',
    'Customer Relationship Management': 'services/crm.html',
    'CRM Solutions': 'services/crm.html',
    'CRM': 'services/crm.html',
    'Human Resource Management (HRMS)': 'services/hrms.html',
    'Human Resource Management': 'services/hrms.html',
    'HRMS & Workforce Systems': 'services/hrms.html',
    'HRMS': 'services/hrms.html',
    'Business Process Automation (BPA)': 'services/business-process-automation.html',
    'Business Process Automation': 'services/business-process-automation.html',
    'Custom Enterprise Applications': 'services/enterprise-applications.html',
    'Enterprise Application Development': 'services/enterprise-applications.html',
    'Enterprise Applications': 'services/enterprise-applications.html',
    'Enterprise Systems Integration': 'services/enterprise-integration.html',
    'System Integration & Data Connectivity': 'services/enterprise-integration.html',
    'Enterprise Integration & Middleware': 'services/enterprise-integration.html',
    
    # Domain 3: Intelligent Monitoring & Automation
    'Real-Time Operational Monitoring': 'services/real-time-monitoring.html',
    'Real-Time Monitoring & Dashboards': 'services/real-time-monitoring.html',
    'IoT & Connected Systems': 'services/iot-integration.html',
    'Internet of Things (IoT) Solutions': 'services/iot-integration.html',
    'IoT & Device Integration': 'services/iot-integration.html',
    'Operational Analytics & Dashboards': 'services/operational-analytics.html',
    'Operational Analytics': 'services/operational-analytics.html',
    'Intelligent Workflow Automation': 'services/workflow-automation.html',
    'Workflow & Process Automation': 'services/workflow-automation.html',
    'System & Infrastructure Monitoring': 'services/infrastructure-monitoring.html',
    
    # Domain 4: AI & Healthcare Technology
    'Agentic AI Solutions': 'services/agentic-ai.html',
    'Agentic AI & Intelligent Agents': 'services/agentic-ai.html',
    'Generative AI & Knowledge Systems': 'services/generative-ai.html',
    'Generative AI Applications': 'services/generative-ai.html',
    'Generative AI & Enterprise Assistants': 'services/generative-ai.html',
    'Intelligent Document Processing': 'services/document-processing.html',
    'Healthcare Automation': 'services/healthcare-automation.html',
    'Healthcare Technology & Automation': 'services/healthcare-automation.html',
    'Healthcare Technology Solutions': 'services/healthcare-automation.html',
    'Healthcare AI & Decision Support': 'services/healthcare-data-analytics.html',
    'Healthcare Data Integration & Analytics': 'services/healthcare-data-analytics.html',
    'AI Systems Integration & Governance': 'services/ai-workflow-automation.html',
    'AI-Powered Workflow Automation': 'services/ai-workflow-automation.html',
}

def generate_subpage(rel_path, root_prefix, category_badge, page_title, page_subtitle,
                     breadcrumbs, overview_paragraphs, capabilities, challenges,
                     workflow_steps, outcomes, related_links, seo_desc,
                     use_cases=None, integrations=None, considerations=None, faqs=None,
                     what_we_deliver=None, industries_served=None, why_choose_us=None):
    """
    Generates a clean, concise, executive enterprise subpage that strictly follows Nova Arc's
    two-colour theme (Dark Navy Blue + Light Slate/White) with alternating sections.
    """
    active_sec = "services"
    if "technology/" in rel_path:
        active_sec = "technology"
    elif "industries/" in rel_path:
        active_sec = "industries"
    elif "connect/" in rel_path:
        active_sec = "connect"

    domain_overview_pages = {
        'services/digital-commerce.html',
        'services/enterprise-business.html',
        'services/intelligent-monitoring.html',
        'services/ai-healthcare.html'
    }
    is_domain_page = rel_path in domain_overview_pages

    # 1. Breadcrumbs HTML
    bc_items = []
    for idx, (label, link) in enumerate(breadcrumbs):
        if link:
            bc_items.append(f'<li><a href="{root_prefix}{link}">{label}</a></li>')
        else:
            bc_items.append(f'<li aria-current="page">{label}</li>')
    breadcrumbs_html = '<span class="breadcrumb-separator">/</span>'.join(bc_items)

    # 2. Editorial Problem & Resolution Section HTML (LIGHT SLATE #F8FAFC)
    # 8th Visual Reference: Consulting / Editorial Row Layout
    chal_rows = []
    for idx, ch in enumerate(challenges):
        formatted_idx = f"{idx+1:02d}"
        challenge_title = ch.get('title') or ch.get('challenge', 'Operational Challenge')

        if ch.get('title') and ch.get('challenge'):
            challenge_title = ch.get('title')
            problem_desc = ch.get('challenge')
            if ch.get('impact'):
                problem_desc = f"{problem_desc} {ch.get('impact')}"
        elif ch.get('challenge') and ch.get('impact'):
            challenge_title = ch.get('challenge')
            problem_desc = ch.get('impact')
        else:
            problem_desc = ch.get('impact') or ch.get('problem') or ch.get('challenge', '')

        resolution_desc = ch.get('solution') or ch.get('resolution', '')

        chal_rows.append(f"""
        <div class="editorial-resolution-row">
          <div class="editorial-row-meta">
            <span class="editorial-num">{formatted_idx}</span>
            <h3 class="editorial-challenge-title">{challenge_title}</h3>
          </div>
          <div class="editorial-problem-col">
            <div class="editorial-label problem-label">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#DC2626" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
              <span>The Challenge</span>
            </div>
            <p class="editorial-problem-desc">{problem_desc}</p>
          </div>
          <div class="editorial-resolution-col">
            <div class="editorial-label resolution-label">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
              <span>Engineered Resolution</span>
            </div>
            <p class="editorial-resolution-desc">{resolution_desc}</p>
          </div>
        </div>
        """)
    challenges_html = "".join(chal_rows)

    # Contextual editorial title and intro tailored to domain/page
    editorial_heading = "From Operational Complexity to Engineered Performance"
    editorial_intro = "Modern enterprise operations depend on synchronized architectures, transparent data flows, and automated execution. We eliminate system friction, manual bottlenecks, and operational blind spots through purpose-built technology solutions."

    if "digital-commerce" in rel_path or "foodtech" in rel_path or "procurement" in rel_path or "supply-chain" in rel_path or "logistics" in rel_path or "retail" in rel_path:
        editorial_heading = "From Operational Complexity to Connected Commerce"
        editorial_intro = "Modern commerce operations depend on coordinated systems, accurate information, and efficient workflows. We address the technology challenges that limit visibility, coordination, and operational performance."
    elif "enterprise" in rel_path or "crm" in rel_path or "hrms" in rel_path or "business-process" in rel_path or "integration" in rel_path or "applications" in rel_path:
        editorial_heading = "From Fragmented Workflows to Operational Velocity"
        editorial_intro = "Enterprise operations stall when critical customer records, workforce data, and administrative processes remain locked in siloed systems. We engineer unified platforms that automate business workflows and accelerate cross-departmental coordination."
    elif "monitoring" in rel_path or "iot" in rel_path or "operational-analytics" in rel_path or "infrastructure" in rel_path:
        editorial_heading = "From Silent Failures to Real-Time Operational Intelligence"
        editorial_intro = "Distributed infrastructure and device networks generate massive operational telemetry that often goes unmonitored until costly outages occur. We deploy real-time observation pipelines and automated alerting engines that diagnose friction proactively."
    elif "ai" in rel_path or "document" in rel_path or "healthcare" in rel_path:
        editorial_heading = "From Manual Overhead to Autonomous Intelligence"
        editorial_intro = "Enterprise productivity slows down when knowledge workers spend hours on repetitive data transcription, document triage, and disjointed coordination. We design governed agentic AI and intelligent automation pipelines that transform operations."

    section_problem_resolution_html = f"""
  <!-- Section 1: Problem & Resolution (LIGHT SLATE #F8FAFC) - Editorial Consulting Layout -->
  <section id="problem-resolution" class="editorial-resolution-section">
    <div class="container">
      <div class="editorial-header">
        <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; letter-spacing: 0.08em; display: inline-block; margin-bottom: 8px;">PROBLEM &amp; RESOLUTION</span>
        <h2 style="font-size: clamp(1.85rem, 2.8vw, 2.4rem); font-weight: 800; color: #0F172A; margin: 0 0 14px; letter-spacing: -0.02em;">{editorial_heading}</h2>
        <p style="color: #475569; font-size: 1.05rem; line-height: 1.65; max-width: 780px; margin: 0;">{editorial_intro}</p>
      </div>

      <div class="editorial-rows-container">
        {challenges_html}
      </div>
    </div>
  </section>
    """

    # 3. Key Capabilities HTML (DARK NAVY #08111F) with Independent Read More Toggle
    cap_cards = []
    for idx, cap in enumerate(capabilities):
        all_points = cap.get('points', [])
        first_4 = all_points[:4]
        remaining = all_points[4:]

        first_4_html = "".join([
            f'<li style="color: #CBD5E1; font-size: 0.88rem; margin-bottom: 8px; display: flex; align-items: flex-start; gap: 8px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg><span>{item}</span></li>'
            for item in first_4
        ])

        clean_id = f"cap-more-{rel_path.replace('/', '-').replace('.', '-')}-{idx}"
        more_html = ""
        btn_html = ""
        if remaining:
            rem_items_html = "".join([
                f'<li style="color: #CBD5E1; font-size: 0.88rem; margin-bottom: 8px; display: flex; align-items: flex-start; gap: 8px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg><span>{item}</span></li>'
                for item in remaining
            ])
            more_html = f'<div id="{clean_id}" class="capability-more-wrap" style="display: none;"><ul style="list-style: none; padding: 0; margin: 0;">{rem_items_html}</ul></div>'
            btn_html = f'<button type="button" class="btn-read-more-caps" data-read-more-text="Read More" onclick="toggleCaps(this, \'{clean_id}\')" aria-expanded="false">Read More <svg class="chevron-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></button>'

        cap_link = None
        if is_domain_page and rel_path.startswith("services/"):
            cap_link = cap.get('link') or CAPABILITY_PAGE_MAP.get(cap.get('title'))

        if cap_link:
            title_html = f"""<h3 style="font-size: 1.18rem; font-weight: 700; margin-bottom: 10px;">
              <a href="{root_prefix}{cap_link}" class="capability-title-link" style="color: #FFFFFF; text-decoration: none; display: inline-flex; align-items: center; justify-content: space-between; width: 100%; gap: 8px;">
                <span>{cap['title']}</span>
                <svg class="cap-arrow-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0; margin-left: auto;">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </a>
            </h3>"""
            explore_btn = f"""<div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.08);">
              <a href="{root_prefix}{cap_link}" style="color: #38BDF8; font-size: 0.88rem; font-weight: 600; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
                <span>Explore Dedicated Subpage</span>
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
              </a>
            </div>"""
        else:
            title_html = f'<h3 style="font-size: 1.18rem; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">{cap["title"]}</h3>'
            explore_btn = ""

        cap_cards.append(f"""
        <div class="card subpage-card-padded capability-card" style="padding: var(--space-xl); display: flex; flex-direction: column; background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg); align-self: start; height: auto;">
          <div>
            <div style="width: 42px; height: 42px; border-radius: 10px; background: rgba(14, 165, 233, 0.12); display: flex; align-items: center; justify-content: center; margin-bottom: 14px; color: #38BDF8;">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                <line x1="8" y1="21" x2="16" y2="21"></line>
                <line x1="12" y1="17" x2="12" y2="21"></line>
              </svg>
            </div>
            {title_html}
            <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.55; margin-bottom: 14px;">{cap.get('desc', '')}</p>
          </div>
          <div style="margin-top: auto; padding-top: 14px; border-top: 1px solid rgba(255,255,255,0.08);">
            <ul style="list-style: none; padding: 0; margin: 0;">
              {first_4_html}
            </ul>
            {more_html}
            {btn_html}
            {explore_btn}
          </div>
        </div>
        """)
    capabilities_html = "".join(cap_cards)

    section_capabilities_html = f"""
  <!-- Section 2: Key Capabilities (DARK NAVY) -->
  <section id="key-capabilities" class="subpage-section-dark" style="padding: clamp(48px, 6vw, 76px) 0; background: #08111F; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; letter-spacing: 0.08em;">KEY CAPABILITIES</span>
        <h2 class="subpage-section-heading" style="font-size: clamp(1.8rem, 2.8vw, 2.4rem); font-weight: 800; color: #FFFFFF; margin: 8px 0 12px; letter-spacing: -0.01em;">Core Architecture &amp; Functional Capabilities</h2>
        <p class="subpage-section-desc" style="color: #94A3B8; font-size: 1.02rem; line-height: 1.6;">Purpose-built engineering modules designed to integrate cleanly into your existing enterprise stack.</p>
      </div>

      <div class="subpage-grid-cards capability-grid-compact">
        {capabilities_html}
      </div>
    </div>
  </section>
    """

    # 4. Four Business Value Propositions HTML (LIGHT WHITE #FFFFFF)
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
        <div class="business-value-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 22px 24px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04); display: flex; flex-direction: column; transition: transform 0.25s ease, box-shadow 0.25s ease;">
          <div style="width: 40px; height: 40px; border-radius: 8px; background: rgba(2, 132, 199, 0.1); display: flex; align-items: center; justify-content: center; margin-bottom: 14px; color: #0284C7;">
            {icon}
          </div>
          <h3 style="font-size: 1.08rem; font-weight: 700; color: #0F172A; margin-bottom: 8px; line-height: 1.35;">{out.get('title', '')}</h3>
          <p style="font-size: 0.90rem; color: #475569; line-height: 1.55; margin: 0;">{out.get('desc', '')}</p>
        </div>
        """)
    business_value_cards_html = "".join(bv_cards)

    section_business_value_html = f"""
  <!-- Section 3: Four Business Value Propositions (LIGHT WHITE) -->
  <section id="business-value" class="subpage-section-light" style="padding: clamp(48px, 6vw, 76px) 0; background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; letter-spacing: 0.08em;">MEASURABLE IMPACT</span>
        <h2 class="subpage-section-heading" style="font-size: clamp(1.8rem, 2.8vw, 2.4rem); font-weight: 800; color: #0F172A; margin: 8px 0 12px; letter-spacing: -0.01em;">Four Core Business Value Propositions</h2>
        <p class="subpage-section-desc" style="color: #475569; font-size: 1.05rem; line-height: 1.6;">Direct operational velocity, architectural resilience, and measurable financial return.</p>
      </div>

      <div class="business-value-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
        {business_value_cards_html}
      </div>
    </div>
  </section>
    """

    # 5. Practical Applications HTML (DARK NAVY #0A1628)
    uc_cards = []
    if use_cases:
        for uc in use_cases[:4]:
            ex_box = f"""<div style='margin-top: auto; padding: 12px 14px; background: rgba(56, 189, 248, 0.08); border-radius: 6px; border-left: 3px solid #38BDF8; font-size: 0.88rem; color: #CBD5E1; line-height: 1.55;'>
              <strong style='color: #38BDF8; display: block; margin-bottom: 3px; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em;'>Expected Operational Value:</strong>
              {uc.get('example', '')}
            </div>""" if uc.get('example') else ""

            uc_cards.append(f"""
            <div class="card subpage-card-padded" style="padding: var(--space-xl); background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg); display: flex; flex-direction: column;">
              <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
                <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 4px 10px; border-radius: 999px; background: rgba(56, 189, 248, 0.12); color: #38BDF8;">{uc.get('tag', 'Enterprise Workflow')}</span>
              </div>
              <h3 style="font-size: 1.18rem; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">{uc.get('title', '')}</h3>
              <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6; margin-bottom: var(--space-md);">{uc.get('desc', '')}</p>
              {ex_box}
            </div>
            """)

    if uc_cards:
        uc_cards_str = "".join(uc_cards)
        section_practical_applications_html = f"""
  <!-- Section 4: Practical Applications (DARK NAVY) -->
  <section id="practical-applications" class="subpage-section-dark-alt" style="padding: clamp(48px, 6vw, 76px) 0; background: #0A1628; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; letter-spacing: 0.08em;">PRACTICAL APPLICATIONS</span>
        <h2 class="subpage-section-heading" style="font-size: clamp(1.8rem, 2.8vw, 2.4rem); font-weight: 800; color: #FFFFFF; margin: 8px 0 12px; letter-spacing: -0.01em;">Real-World Enterprise Applications &amp; Workflows</h2>
        <p class="subpage-section-desc" style="color: #94A3B8; font-size: 1.02rem; line-height: 1.6;">Realistic ways forward-thinking organizations apply these capabilities to solve tangible operational challenges.</p>
      </div>
      <div class="subpage-grid-cards">
        {uc_cards_str}
      </div>
    </div>
  </section>
    """
    else:
        section_practical_applications_html = ""

    # 6. Connected Ecosystem HTML (LIGHT SLATE #F8FAFC)
    related_html = []
    for rel in related_links[:4]:
        related_html.append(f"""
        <a href="{root_prefix}{rel['link']}" class="card" style="padding: var(--space-xl); text-decoration: none; display: flex; flex-direction: column; transition: all 0.25s ease; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);">
          <span style="font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #0284C7; font-weight: 700; background: #E0F2FE; padding: 4px 10px; border-radius: 999px; display: inline-block; margin-bottom: 10px; align-self: flex-start;">{rel.get('tag', 'Connected Module')}</span>
          <h3 style="font-size: 1.15rem; font-weight: 700; color: #0F172A; margin: 0 0 8px; display: flex; align-items: center; justify-content: space-between;">
            <span>{rel['title']}</span>
            <span style="color: #0284C7; font-size: 1.2rem;">&rarr;</span>
          </h3>
          <p style="color: #475569; font-size: 0.90rem; margin: 0; line-height: 1.55;">{rel.get('desc', '')}</p>
        </a>
        """)

    related_cards_str = "".join(related_html)
    section_ecosystem_html = f"""
  <!-- Section 5: Connected Ecosystem (LIGHT SLATE) -->
  <section id="connected-ecosystem" class="subpage-section-light-alt" style="padding: clamp(48px, 6vw, 76px) 0; background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #0284C7; font-weight: 700; letter-spacing: 0.08em;">CONNECTED ECOSYSTEM</span>
        <h2 class="subpage-section-heading" style="font-size: clamp(1.8rem, 2.8vw, 2.4rem); font-weight: 800; color: #0F172A; margin: 8px 0 12px; letter-spacing: -0.01em;">Cross-Domain Enterprise Ecosystem Integration</h2>
        <p class="subpage-section-desc" style="color: #475569; font-size: 1.05rem; line-height: 1.6;">Integrate complementary enterprise modules across our four core service domains.</p>
      </div>

      <div class="subpage-grid-related" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
        {related_cards_str}
      </div>
    </div>
  </section>
    """

    # 7. Bottom CTA Banner (Dark Gradient)
    bottom_cta_html = f"""
  <!-- Bottom CTA Banner (Dark Gradient) -->
  <section class="cta-strip-ags subpage-section-dark" style="padding: clamp(56px, 7vw, 84px) 0; background: linear-gradient(135deg, #07172B 0%, #0B2545 60%, #0E2E56 100%); text-align: center; border-top: 1px solid rgba(255,255,255,0.08);">
    <div class="container" style="max-width: 780px; margin: 0 auto;">
      <h2 style="font-size: clamp(2rem, 3.5vw, 2.8rem); font-weight: 800; color: #FFFFFF; margin-bottom: 16px; letter-spacing: -0.02em;">
        Let’s Build Your Next Business Solution.
      </h2>
      <p style="font-size: 1.1rem; color: #CBD5E1; line-height: 1.65; margin-bottom: 32px;">
        Discuss your business challenges, operational needs, and technology goals with our team. We evaluate your existing system architecture and help you plan the right solution.
      </p>
      <div style="display: flex; gap: var(--space-md); justify-content: center; flex-wrap: wrap;">
        <a href="{root_prefix}contact.html" class="btn btn-consultation-ags" style="font-size: 1.02rem; padding: 14px 32px;">
          <span>Discuss Your Project</span>
          <svg class="btn-arrow-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </a>
        <a href="tel:04046146093" class="btn btn-outline-white" style="font-size: 1.02rem; padding: 14px 28px;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="margin-right: 6px;"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>040-46146093</span>
        </a>
      </div>
    </div>
  </section>
    """

    # Introductory description (exactly 2 paragraphs: page_subtitle and intro_desc)
    intro_desc = overview_paragraphs[0] if len(overview_paragraphs) > 0 else page_subtitle

    # Category pills for domain pages or highlights for subpages (matching Screenshot 3 layout)
    pills_list = []
    if is_domain_page:
        domain_subpages = []
        if "digital-commerce" in rel_path:
            domain_subpages = [
                ("Digital Commerce Platforms", "services/digital-commerce-platforms.html"),
                ("FoodTech Solutions", "services/foodtech.html"),
                ("Supply Chain Management", "services/supply-chain-management.html"),
                ("Procurement & Vendor Management", "services/procurement.html"),
                ("Logistics & Distribution", "services/logistics.html")
            ]
        elif "enterprise-business" in rel_path:
            domain_subpages = [
                ("CRM Solutions", "services/crm.html"),
                ("HRMS & Workforce Systems", "services/hrms.html"),
                ("Business Process Automation", "services/business-process-automation.html"),
                ("Custom Enterprise Applications", "services/enterprise-applications.html"),
                ("Enterprise Systems Integration", "services/enterprise-integration.html")
            ]
        elif "intelligent-monitoring" in rel_path:
            domain_subpages = [
                ("Real-Time Operational Monitoring", "services/real-time-monitoring.html"),
                ("IoT & Connected Systems", "services/iot-integration.html"),
                ("Operational Analytics", "services/operational-analytics.html"),
                ("Intelligent Workflow Automation", "services/workflow-automation.html"),
                ("Infrastructure Monitoring", "services/infrastructure-monitoring.html")
            ]
        elif "ai-healthcare" in rel_path:
            domain_subpages = [
                ("Agentic AI Solutions", "services/agentic-ai.html"),
                ("Generative AI Assistants", "services/generative-ai.html"),
                ("Intelligent Document Processing", "services/document-processing.html"),
                ("Healthcare Automation", "services/healthcare-automation.html"),
                ("Healthcare Analytics", "services/healthcare-data-analytics.html"),
                ("AI Workflow Automation", "services/ai-workflow-automation.html")
            ]
        for p_title, p_link in domain_subpages:
            pills_list.append(
                f'<a href="{root_prefix}{p_link}" class="category-pill-link category-pill-cta" style="padding: 9px 18px; font-size: 0.88rem; display: inline-flex; align-items: center; gap: 8px;">'
                f'<span>{p_title}</span>'
                f'<svg class="pill-arrow-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#1F6FEB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                f'<line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline>'
                f'</svg>'
                f'</a>'
            )
    else:
        for cap in capabilities[:4]:
            c_title = cap['title'].split('&')[0].strip()
            pills_list.append(f'<span class="hero-highlight-pill" style="font-size: 0.85rem; padding: 7px 16px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> {c_title}</span>')

    hero_pills_html = f'<div class="hero-highlights-strip" style="display: flex; flex-wrap: wrap; gap: 10px; margin-top: 24px;">{"".join(pills_list)}</div>' if pills_list else ""

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

{get_shared_header(root_prefix, active_sec)}

  <!-- Hero Section (Clean Open Layout matching Screenshot 3) -->
  <section class="page-hero page-hero-dark" style="min-height: calc(100vh - 75px); min-height: calc(100dvh - 75px); display: flex; flex-direction: column; justify-content: center; box-sizing: border-box; padding-top: calc(75px + clamp(16px, 2.5vw, 36px)); padding-bottom: clamp(28px, 4vw, 52px); position: relative; overflow: hidden;">
    <div class="hero-orchestrated-glow-cyan"></div>
    <div class="hero-orchestrated-glow-blue"></div>
    {get_ecg_waveform_html()}

    <div class="container hero-container-ags" style="position: relative; z-index: 5;">
      <nav class="breadcrumb-nav" aria-label="Breadcrumb" style="margin-bottom: 14px;">
        <ol class="breadcrumb-list" style="display: flex; gap: 8px; list-style: none; padding: 0; margin: 0; font-size: 0.82rem; color: #94A3B8;">
          {breadcrumbs_html}
        </ol>
      </nav>

      <div class="page-hero-content" style="max-width: 900px;">
        <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; font-size: 0.82rem; letter-spacing: 0.08em; display: inline-block; margin-bottom: 12px;">{category_badge}</span>
        <h1 class="page-hero-title" style="font-size: clamp(1.75rem, 3.8vw, 3.2rem); line-height: 1.18; color: #FFFFFF; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.02em; overflow-wrap: break-word; word-break: normal;">{page_title}</h1>
        <p class="hero-tagline-ags" style="font-size: clamp(1.02rem, 1.3vw, 1.2rem); font-weight: 600; color: #38BDF8; line-height: 1.5; margin-bottom: 14px;">
          {page_subtitle}
        </p>
        <p class="hero-intro-text" style="font-size: 1.02rem; line-height: 1.65; color: #E2E8F0; margin-bottom: 24px;">
          {intro_desc}
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
        <a href="#key-capabilities" class="btn btn-outline-white" style="padding: 12px 24px; font-size: 0.98rem;">
          <span>Explore Capabilities</span>
        </a>
      </div>

      {hero_pills_html}
    </div>
  </section>

  {section_problem_resolution_html}

  {section_capabilities_html}

  {section_business_value_html}

  {section_practical_applications_html}

  {section_ecosystem_html}

  {bottom_cta_html}

{get_shared_footer(root_prefix)}

  <!-- Scripts -->
  <script src="{root_prefix}js/main.js?v=4.0"></script>
</body>
</html>
"""
    return html
