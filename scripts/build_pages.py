#!/usr/bin/env python3
"""
Nova Arc - Multi-Page Complete Website Builder
Builds all 54 pages across Home, Solutions, Services, Technology, Industries, and Connect.
Preserves existing visual design, CSS styling, components, responsive layouts, and branding.
"""

import os
import sys
from ecg_component import get_ecg_waveform_html

def get_shared_header(root_prefix, active_section=""):
    sol_active = ' active' if active_section == 'solutions' else ''
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
          <!-- Item 1: Solutions Dropdown -->
          <li class="nav-item-dropdown nav-item-solutions">
            <a href="{root_prefix}solutions.html" class="nav-dropdown-link{sol_active}" id="solutionsDropdownToggle" aria-haspopup="true" aria-expanded="false">
              <span>Solutions</span>
              <svg class="dropdown-chevron" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <polyline points="6 9 12 15 18 9"></polyline>
              </svg>
            </a>
            <div class="nav-simple-dropdown" aria-labelledby="solutionsDropdownToggle" role="menu">
              <a href="{root_prefix}solutions.html" class="nav-simple-item" role="menuitem">
                <strong>All Solutions Overview</strong>
                <span>Comprehensive enterprise digital and automation architecture</span>
              </a>
              <a href="{root_prefix}solutions/digital-commerce.html" class="nav-simple-item" role="menuitem">
                <strong>Digital Commerce Solutions</strong>
                <span>B2B/B2C storefronts, digital ordering &amp; catalog management</span>
              </a>
              <a href="{root_prefix}solutions/supply-chain.html" class="nav-simple-item" role="menuitem">
                <strong>Supply Chain &amp; Procurement</strong>
                <span>End-to-end inventory visibility, PO workflows &amp; vendor portals</span>
              </a>
              <a href="{root_prefix}solutions/enterprise-business.html" class="nav-simple-item" role="menuitem">
                <strong>Enterprise Business Solutions</strong>
                <span>Modern CRM, HRMS, and automated cross-departmental operations</span>
              </a>
              <a href="{root_prefix}solutions/intelligent-monitoring.html" class="nav-simple-item" role="menuitem">
                <strong>Intelligent Monitoring Solutions</strong>
                <span>Real-time telemetry, IoT ingestion &amp; automated incident response</span>
              </a>
              <a href="{root_prefix}solutions/ai-automation.html" class="nav-simple-item" role="menuitem">
                <strong>AI &amp; Agentic Automation</strong>
                <span>Task-specific intelligent agents &amp; governed document understanding</span>
              </a>
              <a href="{root_prefix}solutions/healthcare-technology.html" class="nav-simple-item" role="menuitem">
                <strong>Healthcare Technology Solutions</strong>
                <span>Administrative workflow automation &amp; secure healthcare integration</span>
              </a>
            </div>
          </li>

          <!-- Item 2: Services Mega-Menu -->
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
        <button class="nav-search-btn" id="siteSearchBtn" aria-label="Search Nova Arc services and solutions" title="Search">
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

    <!-- Mobile Drawer Menu -->
    <div class="mobile-nav-drawer" id="mobileDrawer">
      <ul class="mobile-nav-list">
        <!-- Mobile Solutions Accordion -->
        <li class="mobile-accordion-item">
          <button class="mobile-nav-link mobile-accordion-toggle" id="mobileSolutionsToggle" aria-expanded="false" aria-controls="mobileSolutionsSubmenu">
            <span>Solutions</span>
            <svg class="mobile-accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <div class="mobile-submenu-collapse" id="mobileSolutionsSubmenu" aria-hidden="true">
            <div class="mobile-submenu-section">
              <a href="{root_prefix}solutions.html" class="mobile-submenu-link" style="font-weight: 700; color: #38BDF8;">All Solutions Overview</a>
              <a href="{root_prefix}solutions/digital-commerce.html" class="mobile-submenu-link">Digital Commerce Solutions</a>
              <a href="{root_prefix}solutions/supply-chain.html" class="mobile-submenu-link">Supply Chain &amp; Procurement</a>
              <a href="{root_prefix}solutions/enterprise-business.html" class="mobile-submenu-link">Enterprise Business Solutions</a>
              <a href="{root_prefix}solutions/intelligent-monitoring.html" class="mobile-submenu-link">Intelligent Monitoring Solutions</a>
              <a href="{root_prefix}solutions/ai-automation.html" class="mobile-submenu-link">AI &amp; Agentic Automation</a>
              <a href="{root_prefix}solutions/healthcare-technology.html" class="mobile-submenu-link">Healthcare Technology Solutions</a>
            </div>
          </div>
        </li>

        <!-- Mobile Services Accordion -->
        <li class="mobile-accordion-item">
          <button class="mobile-nav-link mobile-accordion-toggle" id="mobileServicesToggle" aria-expanded="false" aria-controls="mobileServicesSubmenu">
            <span>Services</span>
            <svg class="mobile-accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <div class="mobile-submenu-collapse" id="mobileServicesSubmenu" aria-hidden="true">
            <div class="mobile-submenu-section">
              <a href="{root_prefix}services.html" class="mobile-submenu-link" style="font-weight: 700; color: #38BDF8;">All Services Catalog</a>
            </div>
            <div class="mobile-submenu-section">
              <h4 class="mobile-category-title"><a href="{root_prefix}services/digital-commerce.html">Digital Commerce &amp; Supply Chain</a></h4>
              <a href="{root_prefix}services/digital-commerce-platforms.html" class="mobile-submenu-link">Digital Commerce Platforms</a>
              <a href="{root_prefix}services/foodtech.html" class="mobile-submenu-link">FoodTech Solutions</a>
              <a href="{root_prefix}services/supply-chain-management.html" class="mobile-submenu-link">Supply Chain Management</a>
              <a href="{root_prefix}services/procurement.html" class="mobile-submenu-link">Procurement &amp; Vendor Management</a>
              <a href="{root_prefix}services/logistics.html" class="mobile-submenu-link">Logistics &amp; Distribution</a>
            </div>
            <div class="mobile-submenu-section">
              <h4 class="mobile-category-title"><a href="{root_prefix}services/enterprise-business.html">Enterprise Business Solutions</a></h4>
              <a href="{root_prefix}services/crm.html" class="mobile-submenu-link">CRM</a>
              <a href="{root_prefix}services/hrms.html" class="mobile-submenu-link">HRMS</a>
              <a href="{root_prefix}services/business-process-automation.html" class="mobile-submenu-link">Business Process Automation</a>
              <a href="{root_prefix}services/enterprise-applications.html" class="mobile-submenu-link">Custom Enterprise Applications</a>
              <a href="{root_prefix}services/enterprise-integration.html" class="mobile-submenu-link">Enterprise Integration &amp; BI</a>
            </div>
            <div class="mobile-submenu-section">
              <h4 class="mobile-category-title"><a href="{root_prefix}services/intelligent-monitoring.html">Intelligent Monitoring &amp; Automation</a></h4>
              <a href="{root_prefix}services/real-time-monitoring.html" class="mobile-submenu-link">Real-Time Monitoring &amp; Dashboards</a>
              <a href="{root_prefix}services/iot-integration.html" class="mobile-submenu-link">IoT &amp; Device Integration</a>
              <a href="{root_prefix}services/operational-analytics.html" class="mobile-submenu-link">Operational Analytics</a>
              <a href="{root_prefix}services/workflow-automation.html" class="mobile-submenu-link">Workflow &amp; Process Automation</a>
              <a href="{root_prefix}services/infrastructure-monitoring.html" class="mobile-submenu-link">System &amp; Infrastructure Monitoring</a>
            </div>
            <div class="mobile-submenu-section">
              <h4 class="mobile-category-title"><a href="{root_prefix}services/ai-healthcare.html">AI &amp; Healthcare Technology</a></h4>
              <a href="{root_prefix}services/agentic-ai.html" class="mobile-submenu-link">Agentic AI &amp; Intelligent Agents</a>
              <a href="{root_prefix}services/generative-ai.html" class="mobile-submenu-link">Generative AI &amp; Enterprise Assistants</a>
              <a href="{root_prefix}services/document-processing.html" class="mobile-submenu-link">Intelligent Document Processing</a>
              <a href="{root_prefix}services/ai-workflow-automation.html" class="mobile-submenu-link">AI-Powered Workflow Automation</a>
              <a href="{root_prefix}services/healthcare-automation.html" class="mobile-submenu-link">Healthcare Technology &amp; Automation</a>
              <a href="{root_prefix}services/healthcare-data-analytics.html" class="mobile-submenu-link">Healthcare Data Integration &amp; Analytics</a>
            </div>
          </div>
        </li>

        <!-- Mobile Technology Accordion -->
        <li class="mobile-accordion-item">
          <button class="mobile-nav-link mobile-accordion-toggle" id="mobileTechToggle" aria-expanded="false" aria-controls="mobileTechSubmenu">
            <span>Technology</span>
            <svg class="mobile-accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <div class="mobile-submenu-collapse" id="mobileTechSubmenu" aria-hidden="true">
            <div class="mobile-submenu-section">
              <a href="{root_prefix}technology.html" class="mobile-submenu-link" style="font-weight: 700; color: #38BDF8;">Technology Overview</a>
              <a href="{root_prefix}technology/agentic-ai.html" class="mobile-submenu-link">Agentic AI</a>
              <a href="{root_prefix}technology/generative-ai.html" class="mobile-submenu-link">Generative AI</a>
              <a href="{root_prefix}technology/intelligent-automation.html" class="mobile-submenu-link">Intelligent Automation</a>
              <a href="{root_prefix}technology/iot.html" class="mobile-submenu-link">Internet of Things (IoT)</a>
              <a href="{root_prefix}technology/enterprise-integration.html" class="mobile-submenu-link">Enterprise Integration</a>
              <a href="{root_prefix}technology/data-analytics.html" class="mobile-submenu-link">Data Analytics &amp; Intelligence</a>
            </div>
          </div>
        </li>

        <!-- Mobile Industries Accordion -->
        <li class="mobile-accordion-item">
          <button class="mobile-nav-link mobile-accordion-toggle" id="mobileIndustriesToggle" aria-expanded="false" aria-controls="mobileIndustriesSubmenu">
            <span>Industries</span>
            <svg class="mobile-accordion-chevron" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </button>
          <div class="mobile-submenu-collapse" id="mobileIndustriesSubmenu" aria-hidden="true">
            <div class="mobile-submenu-section">
              <a href="{root_prefix}industries.html" class="mobile-submenu-link" style="font-weight: 700; color: #38BDF8;">All Industries Overview</a>
              <a href="{root_prefix}industries/foodtech.html" class="mobile-submenu-link">FoodTech &amp; Food Distribution</a>
              <a href="{root_prefix}industries/retail-ecommerce.html" class="mobile-submenu-link">Retail &amp; Digital Commerce</a>
              <a href="{root_prefix}industries/manufacturing.html" class="mobile-submenu-link">Manufacturing &amp; Industrial Operations</a>
              <a href="{root_prefix}industries/logistics.html" class="mobile-submenu-link">Logistics &amp; Supply Chain</a>
              <a href="{root_prefix}industries/enterprise.html" class="mobile-submenu-link">Enterprise &amp; Professional Services</a>
              <a href="{root_prefix}industries/healthcare.html" class="mobile-submenu-link">Healthcare &amp; Health Technology</a>
            </div>
          </div>
        </li>
      </ul>
      <div class="mobile-nav-bottom">
        <button class="btn btn-secondary mobile-search-trigger" id="mobileSearchTrigger" style="width: 100%; display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 8px;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          Search Services
        </button>
        <a href="tel:04046146093" class="btn btn-secondary" style="width: 100%; margin-bottom: 8px;">Call 040-46146093</a>
        <a href="{root_prefix}contact.html" class="btn btn-primary" style="width: 100%;">Connect with us</a>
      </div>
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
            Nova Arc helps businesses modernize operations through digital commerce, enterprise business solutions, intelligent monitoring, automation, and AI-powered technology.
          </p>
          <div class="footer-tagline">Build Smarter. Operate Better. Scale Faster.</div>
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

        <!-- Col 3: Solutions -->
        <div>
          <h4 class="footer-col-title">Solutions</h4>
          <ul class="footer-links-list">
            <li><a href="{root_prefix}solutions/digital-commerce.html" class="footer-link">Digital Commerce Solutions</a></li>
            <li><a href="{root_prefix}solutions/supply-chain.html" class="footer-link">Supply Chain &amp; Procurement</a></li>
            <li><a href="{root_prefix}solutions/enterprise-business.html" class="footer-link">Enterprise Business Solutions</a></li>
            <li><a href="{root_prefix}solutions/intelligent-monitoring.html" class="footer-link">Intelligent Monitoring</a></li>
            <li><a href="{root_prefix}solutions/ai-automation.html" class="footer-link">AI &amp; Agentic Automation</a></li>
            <li><a href="{root_prefix}solutions/healthcare-technology.html" class="footer-link">Healthcare Technology</a></li>
          </ul>
        </div>

        <!-- Col 4: Company & Industries -->
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

        <!-- Col 5: Contact Info -->
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

      <!-- Footer Bottom Legal & Copyright -->
      <div class="footer-bottom">
        <p>&copy; 2026 Nova Arc Technologies, Inc. All rights reserved.</p>
        <div class="footer-legal-links">
          <a href="{root_prefix}contact.html#privacy">Privacy Policy</a>
          <a href="{root_prefix}contact.html#terms">Terms of Service</a>
          <a href="{root_prefix}contact.html#security">Security &amp; Trust</a>
          <a href="{root_prefix}contact.html#cookies">Cookie Preferences</a>
        </div>
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

def get_hero_visual_html(rel_path, page_title, category_badge, capabilities):
    """
    Generates a domain-specific, interactive glassmorphic system architecture preview window
    for the right-hand column of the subpage hero section.
    """
    # Determine window title and status based on path and subject
    if "solutions/" in rel_path:
        arch_title = "Enterprise Solution Flow"
        badge_text = "● CONNECTED SYSTEM"
    elif "technology/" in rel_path:
        arch_title = "Platform Engine Stack"
        badge_text = "● RUNTIME READY"
    elif "industries/" in rel_path:
        arch_title = "Industry Operations Flow"
        badge_text = "● DOMAIN VALIDATED"
    elif "connect/" in rel_path:
        arch_title = "Direct Concierge Intake"
        badge_text = "● DIRECT DISPATCH"
    else:
        arch_title = "Service Architecture"
        badge_text = "● ACTIVE WORKFLOW"

    tag_classes = ["synced", "active", "governed", "secure"]
    tag_labels = ["Synchronized", "Orchestrated", "Governed", "Automated"]

    stage_items = []
    # Build up to 4 pipeline stages from capabilities or fallbacks
    for idx, cap in enumerate(capabilities[:4]):
        num = idx + 1
        name = cap['title']
        sub = cap['desc'][:68] + "..." if len(cap['desc']) > 70 else cap['desc']
        tag_cls = tag_classes[idx % len(tag_classes)]
        tag_lbl = tag_labels[idx % len(tag_labels)]

        stage_items.append(f"""
          <div class="hero-stage-item">
            <div class="hero-stage-left">
              <span class="hero-stage-num">{num}</span>
              <div>
                <div class="hero-stage-name">{name}</div>
                <div class="hero-stage-sub">{sub}</div>
              </div>
            </div>
            <span class="hero-stage-tag {tag_cls}">{tag_lbl}</span>
          </div>
        """)

    stages_html = "".join(stage_items)

    return f"""
      <div class="hero-arch-window">
        <div class="hero-arch-topbar">
          <div class="hero-arch-dots">
            <span class="hero-arch-dot red"></span>
            <span class="hero-arch-dot amber"></span>
            <span class="hero-arch-dot green"></span>
          </div>
          <span class="hero-arch-title">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
            {arch_title}
          </span>
          <span class="hero-arch-badge">{badge_text}</span>
        </div>
        <div class="hero-arch-body">
          <div class="hero-pipeline-stages">
            {stages_html}
          </div>
          <div class="hero-arch-footer">
            <div class="hero-arch-footer-item">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
              <span>Latency: <strong>&lt; 250ms</strong></span>
            </div>
            <div class="hero-arch-footer-item">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#34D399" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
              <span>Security: <strong>Zero-Trust</strong></span>
            </div>
            <div class="hero-arch-footer-item">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
              <span>Uptime: <strong>99.99%</strong></span>
            </div>
          </div>
        </div>
      </div>
    """

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
    if "solutions/" in rel_path:
        active_sec = "solutions"
    elif "technology/" in rel_path:
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

    # 1. Overview HTML (in light section)
    overview_html = "".join([f'<p style="font-size: 1.05rem; line-height: 1.8; color: #334155; margin-bottom: 18px;">{p}</p>' for p in overview_paragraphs])

    # 2. Key Capabilities HTML with Read More / Show Less Toggle (ALWAYS in dark section)
    cap_cards = []
    for idx, cap in enumerate(capabilities):
        all_points = cap.get('points', [])
        first_4 = all_points[:4]
        remaining = all_points[4:]

        first_4_html = "".join([f'<li style="color: #CBD5E1; font-size: 0.875rem; margin-bottom: 7px; display: flex; align-items: flex-start; gap: 8px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg><span>{item}</span></li>' for item in first_4])

        more_html = ""
        btn_html = ""
        if remaining:
            clean_id = f"cap-more-{rel_path.replace('/', '-').replace('.', '-')}-{idx}"
            rem_items_html = "".join([f'<li style="color: #CBD5E1; font-size: 0.875rem; margin-bottom: 7px; display: flex; align-items: flex-start; gap: 8px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg><span>{item}</span></li>' for item in remaining])
            more_html = f'<div id="{clean_id}" class="capability-more-wrap" style="display: none;"><ul style="list-style: none; padding: 0; margin: 0; padding-top: 4px;">{rem_items_html}</ul></div>'
            btn_html = f'<button type="button" class="btn-read-more-caps" data-read-more-text="Read More (+{len(remaining)} more)" onclick="toggleCaps(this, \'{clean_id}\')" aria-expanded="false">Read More (+{len(remaining)} more) <svg class="chevron-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"/></svg></button>'

        cap_cards.append(f"""
        <div class="card subpage-card-padded capability-card" style="padding: var(--space-2xl); display: flex; flex-direction: column; background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg); align-self: start !important; height: auto !important;">
          <div>
            <div style="width: 48px; height: 48px; border-radius: 10px; background: rgba(14, 165, 233, 0.12); display: flex; align-items: center; justify-content: center; margin-bottom: var(--space-md); color: #38BDF8;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                <line x1="8" y1="21" x2="16" y2="21"></line>
                <line x1="12" y1="17" x2="12" y2="21"></line>
              </svg>
            </div>
            <h3 style="font-size: 1.25rem; font-weight: 700; color: #FFFFFF; margin-bottom: var(--space-sm);">{cap['title']}</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6; margin-bottom: var(--space-md);">{cap['desc']}</p>
          </div>
          <div>
            <ul style="list-style: none; padding: 0; margin: 0; border-top: 1px solid rgba(255,255,255,0.08); padding-top: var(--space-md);">
              {first_4_html}
            </ul>
            {more_html}
            {btn_html}
          </div>
        </div>
        """)
    capabilities_html = "".join(cap_cards)

    # 3. What We Deliver Section HTML (Present on domain pages -> LIGHT SLATE)
    what_we_deliver_html = ""
    if what_we_deliver:
        del_cards = []
        for d in what_we_deliver:
            items_html = "".join([f'<li style="color: #334155; font-size: 0.875rem; margin-bottom: 7px; display: flex; align-items: flex-start; gap: 8px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2.5" style="flex-shrink: 0; margin-top: 3px;"><polyline points="20 6 9 17 4 12"/></svg><span>{it}</span></li>' for it in d.get('deliverables', [])])
            tech_tag = f'<div class="deliver-card-tech" style="background: #F1F5F9; border: 1px solid #E2E8F0; color: #334155; border-radius: 6px; padding: 6px 12px; font-size: 0.8rem; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; margin-top: auto;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#0284C7" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg><span>Stack: {d["tech_stack"]}</span></div>' if d.get('tech_stack') else ""
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

    # 4. Industries Served Section HTML (Present on domain pages -> LIGHT SLATE)
    industries_served_html = ""
    if industries_served:
        ind_cards = []
        for ind in industries_served:
            ind_cards.append(f"""
            <div class="industry-served-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: var(--radius-lg); padding: var(--space-xl); display: flex; flex-direction: column; box-shadow: 0 4px 16px -2px rgba(11, 37, 69, 0.05);">
              <span style="font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #0284C7; background: #E0F2FE; padding: 3px 10px; border-radius: 999px; display: inline-block; margin-bottom: 10px; align-self: flex-start;">INDUSTRY VERTICAL</span>
              <h3 style="font-size: 1.2rem; font-weight: 700; color: #0F172A; margin-bottom: 8px;">{ind['industry']}</h3>
              <div style="margin-bottom: var(--space-sm);">
                <strong style="color: #64748B; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 4px;">Vertical Implementation:</strong>
                <p style="color: #334155; font-size: 0.925rem; line-height: 1.55; margin: 0;">{ind['application']}</p>
              </div>
              <div style="margin-top: auto; padding: 10px 14px; background: #F0F9FF; border-left: 3px solid #0284C7; border-radius: 6px; font-size: 0.85rem; color: #0C4A6E; line-height: 1.5;">
                <strong style="color: #0284C7; display: block; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 2px;">Key Business Outcome:</strong>
                <span>{ind['outcome']}</span>
              </div>
            </div>
            """)
        ind_cards_str = "".join(ind_cards)
        industries_served_html = f"""
  <!-- Industries Served Section -->
  <section id="industries-served" class="subpage-section-light-alt" style="padding: var(--space-4xl) 0; background: #F8FAFC; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="text-align: center; max-width: 760px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #0284C7;">INDUSTRIES SERVED</span>
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

    # Core Service Domains Switcher
    core_domains = [
        ("01", "Digital Commerce & Supply Chain", "services/digital-commerce.html"),
        ("02", "Enterprise Business Solutions", "services/enterprise-business.html"),
        ("03", "Intelligent Monitoring & Automation", "services/intelligent-monitoring.html"),
        ("04", "AI & Healthcare Technology", "services/ai-healthcare.html"),
    ]
    services_domain_nav_html = ""
    if rel_path in [d[2] for d in core_domains]:
        pills = []
        for num, d_title, d_path in core_domains:
            active_cls = " active" if rel_path == d_path else ""
            pills.append(f'<a href="{root_prefix}{d_path}" class="service-domain-pill{active_cls}"><span class="domain-num">{num}</span><span>{d_title}</span></a>')
        pills_str = "".join(pills)
        services_domain_nav_html = f"""
  <!-- Core Service Domains Switcher -->
  <nav class="services-domain-nav" aria-label="Core Service Domains Quick Switcher">
    <div class="container">
      <div class="services-domain-nav-inner">
        <span class="services-domain-label">Core Domains:</span>
        <div class="services-domain-pills">
          {pills_str}
        </div>
      </div>
    </div>
  </nav>
        """

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
              <span style="font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #0284C7; font-weight: 700; background: #E0F2FE; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 6px;">{rel.get('tag', 'Service Domain')}</span>
              <h4 style="font-size: 1.1rem; color: #0F172A; margin: 6px 0 4px;">{rel['title']} &rarr;</h4>
              <p style="color: #475569; font-size: 0.85rem; margin: 0; line-height: 1.45;">{rel['desc']}</p>
            </a>
            """)
        else:
            related_html.append(f"""
            <a href="{root_prefix}{rel['link']}" class="card" style="padding: var(--space-lg); text-decoration: none; display: block; transition: all 0.2s ease; background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg);">
              <span style="font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; color: #38BDF8; font-weight: 700; background: rgba(56, 189, 248, 0.1); padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 6px;">{rel.get('tag', 'Service Domain')}</span>
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

    # Compute Hero Visual & Highlights
    hero_highlights_html = get_hero_highlights_html(capabilities)
    hero_visual_html = get_hero_visual_html(rel_path, page_title, category_badge, capabilities)

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
  <link rel="stylesheet" href="{root_prefix}css/style.css?v=3.5">

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

  <!-- Hero Section -->
  <section class="services-hero-ags" style="padding-top: calc(75px + var(--space-3xl)); padding-bottom: var(--space-4xl);">
    <div class="hero-orchestrated-glow-cyan"></div>
    <div class="hero-orchestrated-glow-blue"></div>
    {get_ecg_waveform_html()}

    <div class="container hero-container-ags">
      <div class="hero-subpage-grid">
        <!-- Left Column: Context, Hierarchy & Actions -->
        <div class="hero-subpage-left">
          <nav class="breadcrumb-nav" aria-label="Breadcrumb" style="margin-bottom: var(--space-sm);">
            <ol class="breadcrumb-list" style="display: flex; gap: 8px; list-style: none; padding: 0; margin: 0; font-size: 0.85rem; color: #94A3B8;">
              {breadcrumbs_html}
            </ol>
          </nav>
          <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 700; letter-spacing: 0.08em; display: inline-block; margin-bottom: 6px;">{category_badge}</span>
          <h1 class="hero-title-ags" style="font-size: clamp(2.2rem, 3.8vw, 3.3rem); line-height: 1.15; margin-bottom: 16px;">{page_title}</h1>
          <p class="hero-subtitle-ags" style="font-size: 1.1rem; line-height: 1.65; color: #CBD5E1; margin-bottom: 24px; max-width: 620px;">
            {page_subtitle}
          </p>
          <div class="hero-actions-ags" style="display: flex; gap: var(--space-md); flex-wrap: wrap;">
            <a href="{root_prefix}contact.html" class="btn btn-consultation-ags">
              <span>Discuss Your Project</span>
              <svg class="btn-arrow-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <line x1="5" y1="12" x2="19" y2="12"></line>
                <polyline points="12 5 19 12 12 19"></polyline>
              </svg>
            </a>
            <a href="{root_prefix}services.html" class="btn btn-outline-white">
              <span>Explore Services</span>
            </a>
          </div>
          {hero_highlights_html}
        </div>

        <!-- Right Column: Visual System Architecture & Live Telemetry Card -->
        <div class="hero-subpage-right">
          {hero_visual_html}
        </div>
      </div>
    </div>
  </section>

  {services_domain_nav_html}

  <!-- Section 1: Strategic Overview (LIGHT) -->
  <section id="strategic-overview" class="subpage-section-light" style="padding: var(--space-4xl) 0; background: #FFFFFF; border-bottom: 1px solid #E2E8F0;">
    <div class="container">
      <div style="max-width: 860px; margin: 0 auto; text-align: center;">
        <span class="eyebrow-ags" style="color: #0284C7;">STRATEGIC OVERVIEW</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: #0F172A; margin: 8px 0 20px; line-height: 1.3;">Engineered for Seamless Operations &amp; Measurable Outcomes</h2>
        <div style="text-align: left;">
          {overview_html}
        </div>
      </div>
    </div>
  </section>

  <!-- Section 2: Key Capabilities (DARK NAVY) -->
  <section id="key-capabilities" class="subpage-section-dark" style="padding: var(--space-4xl) 0; background: #08111F; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8;">KEY CAPABILITIES</span>
        <h2 class="subpage-section-heading" style="font-size: 2.1rem; font-weight: 800; color: #FFFFFF; margin: 8px 0 12px;">Core Architecture &amp; Functional Capabilities</h2>
        <p class="subpage-section-desc" style="color: #94A3B8; font-size: 1.05rem;">Purpose-built engineering modules designed to integrate cleanly into your existing enterprise stack.</p>
      </div>

      <div class="subpage-grid-cards">
        {capabilities_html}
      </div>
    </div>
  </section>

  {what_we_deliver_html}

  {section_problem_resolution_html}

  {use_cases_html}

  {section_methodology_html}

  {industries_served_html}

  {integrations_html}

  {why_choose_us_html}

  {considerations_html}

  {section_benefits_html}

  {faqs_html}

  {section_ecosystem_html}

  {bottom_cta_html}

{get_shared_footer(root_prefix)}

  <!-- Scripts -->
  <script src="{root_prefix}js/main.js?v=3.5"></script>
</body>
</html>
"""
    return html
