#!/usr/bin/env python3
"""
Nova Arc - Multi-Page Complete Website Builder
Builds all 54 pages across Home, Solutions, Services, Technology, Industries, and Connect.
Preserves existing visual design, CSS styling, components, responsive layouts, and branding.
"""

import os
import sys

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
              <a href="{root_prefix}document-processing.html" class="mobile-submenu-link">Intelligent Document Processing</a>
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

      <!-- Trust & Standards Strip -->
      <div class="footer-compliance-bar">
        <div class="compliance-badge-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Enterprise Security &amp; Encryption</span>
        </div>
        <div class="compliance-badge-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <span>High-Availability Architecture</span>
        </div>
        <div class="compliance-badge-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Data Privacy &amp; Governance</span>
        </div>
        <div class="compliance-badge-item">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Dedicated Engineering Support</span>
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

def generate_subpage(rel_path, root_prefix, category_badge, page_title, page_subtitle,
                     breadcrumbs, overview_paragraphs, capabilities, challenges,
                     workflow_steps, outcomes, related_links, seo_desc):
    """
    Generates a complete, beautiful subpage that perfectly fits Nova Arc's design system.
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

    # Breadcrumbs HTML
    bc_items = []
    for idx, (label, link) in enumerate(breadcrumbs):
        if link:
            bc_items.append(f'<li><a href="{root_prefix}{link}">{label}</a></li>')
        else:
            bc_items.append(f'<li aria-current="page">{label}</li>')
    breadcrumbs_html = '<span class="breadcrumb-separator">/</span>'.join(bc_items)

    # Overview HTML
    overview_html = "".join([f'<p class="overview-body-text">{p}</p>' for p in overview_paragraphs])

    # Capabilities Cards HTML
    cap_cards = []
    for cap in capabilities:
        cap_cards.append(f"""
        <div class="card" style="padding: var(--space-2xl); display: flex; flex-direction: column; justify-content: space-between;">
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
          <ul style="list-style: none; padding: 0; margin: 0; border-top: 1px solid rgba(255,255,255,0.08); padding-top: var(--space-md);">
            {"".join([f'<li style="color: #CBD5E1; font-size: 0.875rem; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#38BDF8" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>{item}</li>' for item in cap.get('points', [])])}
          </ul>
        </div>
        """)
    capabilities_html = "".join(cap_cards)

    # Challenges HTML
    chal_cards = []
    for ch in challenges:
        chal_cards.append(f"""
        <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg); padding: var(--space-xl);">
          <div style="display: flex; align-items: center; gap: 10px; margin-bottom: var(--space-sm);">
            <span style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 3px 8px; border-radius: 4px; background: rgba(239, 68, 68, 0.15); color: #F87171;">Operational Challenge</span>
          </div>
          <h4 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: var(--space-sm);">{ch['challenge']}</h4>
          <p style="color: #94A3B8; font-size: 0.925rem; line-height: 1.6; margin-bottom: var(--space-md);">{ch['impact']}</p>
          <div style="padding: var(--space-md); background: rgba(14, 165, 233, 0.08); border-left: 3px solid #38BDF8; border-radius: 4px;">
            <strong style="color: #38BDF8; font-size: 0.85rem; display: block; margin-bottom: 4px;">Nova Arc Implementation Solution:</strong>
            <span style="color: #E2E8F0; font-size: 0.9rem; line-height: 1.5;">{ch['solution']}</span>
          </div>
        </div>
        """)
    challenges_html = "".join(chal_cards)

    # Workflow Steps HTML
    steps_html = []
    for st in workflow_steps:
        steps_html.append(f"""
        <div style="background: #111D33; border: 1px solid rgba(255,255,255,0.08); border-radius: var(--radius-lg); padding: var(--space-xl); position: relative;">
          <span style="font-size: 1.8rem; font-weight: 900; color: rgba(56, 189, 248, 0.3); position: absolute; top: var(--space-md); right: var(--space-md);">{st['step']}</span>
          <h4 style="font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: var(--space-sm);">{st['title']}</h4>
          <p style="color: #94A3B8; font-size: 0.925rem; line-height: 1.6;">{st['desc']}</p>
        </div>
        """)
    workflow_html = "".join(steps_html)

    # Outcomes HTML
    outcomes_html = []
    for out in outcomes:
        outcomes_html.append(f"""
        <div style="background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: var(--radius-lg); padding: var(--space-xl);">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: rgba(56, 189, 248, 0.15); display: flex; align-items: center; justify-content: center; color: #38BDF8; margin-bottom: var(--space-md);">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
          </div>
          <h4 style="font-size: 1.1rem; font-weight: 700; color: #FFFFFF; margin-bottom: 6px;">{out['title']}</h4>
          <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5;">{out['desc']}</p>
        </div>
        """)
    outcomes_grid_html = "".join(outcomes_html)

    # Related Links HTML
    related_html = []
    for rel in related_links:
        related_html.append(f"""
        <a href="{root_prefix}{rel['link']}" class="card" style="padding: var(--space-lg); text-decoration: none; display: block; transition: all 0.2s ease;">
          <span style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: #38BDF8; font-weight: 700;">{rel.get('tag', 'Service Domain')}</span>
          <h4 style="font-size: 1.1rem; color: #FFFFFF; margin: 6px 0 4px;">{rel['title']} &rarr;</h4>
          <p style="color: #94A3B8; font-size: 0.85rem; margin: 0; line-height: 1.4;">{rel['desc']}</p>
        </a>
        """)
    related_grid_html = "".join(related_html)

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
  <link rel="stylesheet" href="{root_prefix}css/style.css?v=3.1">

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
<body>

{get_shared_header(root_prefix, active_sec)}

  <!-- Hero Section -->
  <section class="services-hero-ags" style="padding-top: calc(70px + var(--space-4xl));">
    <div class="hero-orchestrated-glow-cyan"></div>
    <div class="hero-orchestrated-glow-blue"></div>

    <div class="container hero-container-ags">
      <div class="hero-content-ags" style="max-width: 860px;">
        <nav class="breadcrumb-nav" aria-label="Breadcrumb" style="margin-bottom: var(--space-md);">
          <ol class="breadcrumb-list" style="display: flex; gap: 8px; list-style: none; padding: 0; margin: 0; font-size: 0.85rem; color: #94A3B8;">
            {breadcrumbs_html}
          </ol>
        </nav>
        <span class="eyebrow-ags" style="color: #38BDF8; font-weight: 600; letter-spacing: 0.08em; display: inline-block; margin-bottom: var(--space-xs);">{category_badge}</span>
        <h1 class="hero-title-ags" style="font-size: clamp(2.2rem, 3.8vw, 3.4rem);">{page_title}</h1>
        <p class="hero-subtitle-ags" style="font-size: 1.15rem; max-width: 720px; line-height: 1.65; color: #E2E8F0;">
          {page_subtitle}
        </p>
        <div class="hero-actions-ags" style="margin-top: var(--space-xl); display: flex; gap: var(--space-md); flex-wrap: wrap;">
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
      </div>
    </div>
  </section>

  <!-- Section 1: Strategic Overview -->
  <section class="section-overview-ags" style="padding: var(--space-4xl) 0; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div class="overview-content-centered" style="max-width: 840px;">
        <span class="eyebrow-ags">STRATEGIC OVERVIEW</span>
        <h2 class="overview-heading-ags" style="font-size: 2rem; margin-bottom: var(--space-lg);">Engineered for Seamless Operations &amp; Measurable Business Outcomes</h2>
        <div class="overview-body-wrap">
          {overview_html}
        </div>
      </div>
    </div>
  </section>

  <!-- Section 2: Core Capabilities -->
  <section style="padding: var(--space-4xl) 0; background: rgba(11, 25, 44, 0.4); border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8;">KEY CAPABILITIES</span>
        <h2 style="font-size: 2.1rem; font-weight: 800; color: #FFFFFF; margin: 8px 0 12px;">Core Architecture &amp; Technical Capabilities</h2>
        <p style="color: #94A3B8; font-size: 1.05rem;">Purpose-built engineering modules designed to integrate cleanly into your existing enterprise stack.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: var(--space-xl);">
        {capabilities_html}
      </div>
    </div>
  </section>

  <!-- Section 3: Operational Challenges & Solutions -->
  <section style="padding: var(--space-4xl) 0; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8;">PROBLEM &amp; RESOLUTION</span>
        <h2 style="font-size: 2.1rem; font-weight: 800; color: #FFFFFF; margin: 8px 0 12px;">Addressing Critical Operational Friction</h2>
        <p style="color: #94A3B8; font-size: 1.05rem;">How Nova Arc overcomes systemic process inefficiencies and technology bottlenecks.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: var(--space-xl);">
        {challenges_html}
      </div>
    </div>
  </section>

  <!-- Section 4: Implementation Lifecycle -->
  <section style="padding: var(--space-4xl) 0; background: rgba(11, 25, 44, 0.4); border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8;">ENGINEERING METHODOLOGY</span>
        <h2 style="font-size: 2.1rem; font-weight: 800; color: #FFFFFF; margin: 8px 0 12px;">Implementation &amp; Delivery Lifecycle</h2>
        <p style="color: #94A3B8; font-size: 1.05rem;">A disciplined, agile deployment framework ensuring stability, security, and immediate operational value.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: var(--space-lg);">
        {workflow_html}
      </div>
    </div>
  </section>

  <!-- Section 5: Measured Value & Outcomes -->
  <section style="padding: var(--space-4xl) 0; border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8;">BUSINESS VALUE</span>
        <h2 style="font-size: 2.1rem; font-weight: 800; color: #FFFFFF; margin: 8px 0 12px;">Measurable Enterprise Outcomes</h2>
        <p style="color: #94A3B8; font-size: 1.05rem;">Transforming daily administrative overhead into sustained operational velocity.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: var(--space-lg);">
        {outcomes_grid_html}
      </div>
    </div>
  </section>

  <!-- Section 6: Related Technology & Ecosystem Links -->
  <section style="padding: var(--space-4xl) 0; background: rgba(11, 25, 44, 0.4); border-bottom: 1px solid rgba(255,255,255,0.06);">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto var(--space-3xl);">
        <span class="eyebrow-ags" style="color: #38BDF8;">CONNECTED ECOSYSTEM</span>
        <h2 style="font-size: 2.1rem; font-weight: 800; color: #FFFFFF; margin: 8px 0 12px;">Explore Related Solutions &amp; Capabilities</h2>
        <p style="color: #94A3B8; font-size: 1.05rem;">Integrate complementary enterprise modules across our four core service domains.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-md);">
        {related_grid_html}
      </div>
    </div>
  </section>

  <!-- Bottom CTA Strip -->
  <section class="cta-strip-ags" style="padding: var(--space-4xl) 0; background: linear-gradient(135deg, rgba(14, 165, 233, 0.12) 0%, rgba(31, 111, 235, 0.18) 100%); text-align: center;">
    <div class="container" style="max-width: 760px; margin: 0 auto;">
      <h2 style="font-size: clamp(2rem, 3.5vw, 2.8rem); font-weight: 800; color: #FFFFFF; margin-bottom: var(--space-md); letter-spacing: -0.02em;">
        Let’s Build Your Next Competitive Advantage.
      </h2>
      <p style="font-size: 1.1rem; color: #CBD5E1; line-height: 1.65; margin-bottom: var(--space-2xl);">
        Tell us about your business challenge, operational requirements, or technology goals. Our team can help you explore the right solution across digital commerce, enterprise systems, intelligent automation, and AI-powered technology.
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

{get_shared_footer(root_prefix)}

  <!-- Scripts -->
  <script src="{root_prefix}js/main.js?v=3.1"></script>
</body>
</html>
"""
    return html

print("Shared templates loaded successfully.")
