#!/usr/bin/env python3
"""
Nova Arc - Domain-Specific Hero Architectural Visuals
Generates authentic, high-resolution SVG architectural topology diagrams
representing the actual enterprise solution workflow for each page.
"""

def get_hero_svg_for_page(rel_path, page_title, category_badge):
    """
    Returns an authentic, premium SVG illustration tailored to the specific
    solution, service, technology, or industry domain.
    """
    # 1. Digital Commerce & Storefronts
    if "digital-commerce" in rel_path or "foodtech" in rel_path or "retail" in rel_path:
        if "foodtech" in rel_path:
            return _svg_foodtech_architecture()
        return _svg_commerce_architecture()

    # 2. Supply Chain, Procurement & Logistics
    elif "supply-chain" in rel_path or "procurement" in rel_path or "logistics" in rel_path:
        if "procurement" in rel_path:
            return _svg_procurement_architecture()
        elif "logistics" in rel_path:
            return _svg_logistics_architecture()
        return _svg_supply_chain_architecture()

    # 3. Enterprise Business Solutions, CRM, HRMS, BPA
    elif "enterprise-business" in rel_path or "crm" in rel_path or "hrms" in rel_path or "enterprise-applications" in rel_path or "business-process" in rel_path:
        if "crm" in rel_path:
            return _svg_crm_architecture()
        elif "hrms" in rel_path:
            return _svg_hrms_architecture()
        elif "business-process" in rel_path:
            return _svg_bpa_architecture()
        return _svg_enterprise_core_architecture()

    # 4. Intelligent Monitoring, IoT & Operational Analytics
    elif "intelligent-monitoring" in rel_path or "iot" in rel_path or "operational-analytics" in rel_path or "real-time-monitoring" in rel_path or "infrastructure-monitoring" in rel_path or "monitoring" in rel_path:
        if "iot" in rel_path:
            return _svg_iot_architecture()
        elif "analytics" in rel_path:
            return _svg_analytics_architecture()
        elif "infrastructure" in rel_path:
            return _svg_infrastructure_architecture()
        return _svg_monitoring_architecture()

    # 5. AI, Agentic AI, GenAI, Document Processing
    elif "ai-" in rel_path or "agentic-ai" in rel_path or "generative-ai" in rel_path or "document-processing" in rel_path or "ai-workflow" in rel_path:
        if "agentic" in rel_path:
            return _svg_agentic_ai_architecture()
        elif "generative" in rel_path:
            return _svg_generative_rag_architecture()
        elif "document" in rel_path:
            return _svg_document_processing_architecture()
        return _svg_ai_orchestration_architecture()

    # 6. Healthcare Technology & Data Interoperability
    elif "healthcare" in rel_path:
        if "data" in rel_path or "analytics" in rel_path:
            return _svg_healthcare_interop_architecture()
        return _svg_healthcare_platform_architecture()

    # 7. Technology Subpages (Integration, etc.)
    elif "integration" in rel_path:
        return _svg_system_integration_architecture()
    elif "automation" in rel_path:
        return _svg_bpa_architecture()

    # 8. Industry Subpages (Manufacturing, etc.)
    elif "manufacturing" in rel_path:
        return _svg_manufacturing_architecture()

    # 9. Connect / General Fallback
    elif "connect" in rel_path:
        return _svg_connect_architecture()

    # Default Enterprise Topology
    return _svg_enterprise_core_architecture()


# ============================================================================
# SVG Architectural Diagram Generators
# ============================================================================

def _card_box(x, y, w, h, title, subtext, icon_type="box", status=None, active=False):
    border_color = "rgba(56, 189, 248, 0.45)" if active else "rgba(255, 255, 255, 0.12)"
    bg_color = "rgba(14, 34, 61, 0.85)" if active else "rgba(10, 22, 40, 0.75)"
    title_color = "#38BDF8" if active else "#FFFFFF"
    
    return f"""
    <g transform="translate({x}, {y})">
      <rect width="{w}" height="{h}" rx="8" fill="{bg_color}" stroke="{border_color}" stroke-width="1.2"/>
      <rect x="1" y="1" width="{w-2}" height="3" rx="1.5" fill="{title_color}" opacity="{0.9 if active else 0.4}"/>
      <text x="14" y="24" fill="{title_color}" font-family="Inter, sans-serif" font-size="12" font-weight="700">{title}</text>
      <text x="14" y="40" fill="#94A3B8" font-family="Inter, sans-serif" font-size="10" font-weight="400">{subtext}</text>
    </g>
    """

def _connector(x1, y1, x2, y2, label=None, animated=True):
    color = "#38BDF8"
    dash = 'stroke-dasharray="4 4"' if animated else ''
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    label_svg = f'<text x="{mid_x}" y="{mid_y - 4}" fill="#38BDF8" font-family="Inter, sans-serif" font-size="9" text-anchor="middle">{label}</text>' if label else ''
    return f"""
    <path d="M {x1} {y1} L {x2} {y2}" stroke="{color}" stroke-width="1.5" opacity="0.65" {dash}/>
    <circle cx="{x2}" cy="{y2}" r="3" fill="{color}"/>
    {label_svg}
    """

def _svg_wrapper(inner_svg, title_badge, subtitle_badge):
    return f"""
<div class="hero-diagram-container" style="position: relative; width: 100%; max-width: 540px; margin: 0 auto;">
  <div style="background: rgba(10, 22, 40, 0.65); border: 1px solid rgba(56, 189, 248, 0.22); border-radius: 16px; padding: 20px 22px 16px; backdrop-filter: blur(12px); box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.5), 0 0 30px rgba(56, 189, 248, 0.1);">
    
    <!-- Top Diagram Status Bar -->
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding-bottom: 12px; margin-bottom: 16px;">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: #38BDF8; box-shadow: 0 0 8px #38BDF8;"></span>
        <span style="font-family: 'Inter', sans-serif; font-size: 0.78rem; font-weight: 700; color: #E2E8F0; letter-spacing: 0.05em; text-transform: uppercase;">{title_badge}</span>
      </div>
      <span style="font-family: 'Inter', sans-serif; font-size: 0.72rem; color: #94A3B8; background: rgba(56, 189, 248, 0.1); padding: 3px 8px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.2);">{subtitle_badge}</span>
    </div>

    <!-- Scalable Vector Diagram -->
    <svg viewBox="0 0 500 310" width="100%" height="auto" style="display: block; overflow: visible;">
      <defs>
        <linearGradient id="grad-blue" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#0E2E56"/>
          <stop offset="100%" stop-color="#07172B"/>
        </linearGradient>
        <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
          <feGaussianBlur stdDeviation="3" result="blur" />
          <feComposite in="SourceGraphic" in2="blur" operator="over"/>
        </filter>
      </defs>
      {inner_svg}
    </svg>

    <!-- Bottom Architectural Flow Legend -->
    <div style="margin-top: 14px; padding-top: 10px; border-top: 1px solid rgba(255, 255, 255, 0.06); display: flex; justify-content: space-between; align-items: center; font-size: 0.72rem; color: #64748B;">
      <span>Architecture: High-Throughput Microservices</span>
      <span style="color: #38BDF8;">● Resilient Zero-Loss Pipeline</span>
    </div>
  </div>
</div>
"""

# ----------------------------------------------------------------------------
# 1. Digital Commerce Topology
# ----------------------------------------------------------------------------
def _svg_commerce_architecture():
    svg = f"""
    <!-- Layer 1: Ingestion Channels -->
    {_card_box(20, 20, 135, 54, "Omnichannel Storefront", "B2B / B2C Web & Mobile", active=True)}
    {_card_box(20, 95, 135, 54, "Procurement Portals", "PunchOut & Buyer Catalogs")}
    {_card_box(20, 170, 135, 54, "Marketplace Hubs", "Multi-Channel Order Feeds")}

    <!-- Connectors to API Gateway -->
    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    <!-- Layer 2: API Gateway Core -->
    {_card_box(195, 95, 120, 60, "API Gateway Bus", "GraphQL / REST Mesh", active=True)}

    <!-- Connectors to Processing Services -->
    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    <!-- Layer 3: Commerce Microservices -->
    {_card_box(345, 20, 135, 54, "Pricing & Stock Engine", "Real-Time Allocation")}
    {_card_box(345, 95, 135, 54, "Checkout & Payment", "PCI-DSS Level 1 Gateway", active=True)}
    {_card_box(345, 170, 135, 54, "Fulfillment Router", "Warehouse & ERP Sync")}

    <!-- Bottom Synchronization Layer -->
    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Enterprise Back-Office Data Bus</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Bidirectional Sync with SAP, NetSuite, Dynamics 365 &amp; Logistics WMS</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "COMMERCE PIPELINE ARCHITECTURE", "LIVE ENGINE")

# ----------------------------------------------------------------------------
# 2. FoodTech Architecture
# ----------------------------------------------------------------------------
def _svg_foodtech_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Multi-Channel Orders", "Aggregators & QR Dine-In", active=True)}
    {_card_box(20, 95, 135, 54, "Commissary & Sourcing", "Supplier PO Intake")}
    {_card_box(20, 170, 135, 54, "Cold-Chain Telemetry", "IoT Sensor Data Streams")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Central Kitchen KDS", "Ticket Routing & Timing", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Recipe Depletion", "Ingredient Inventory")}
    {_card_box(345, 95, 135, 54, "Dispatch Engine", "Hyperlocal Fleet Routing", active=True)}
    {_card_box(345, 170, 135, 54, "Safety Compliance", "HACCP & Expiry Logs")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Food Production &amp; Distribution Ledger</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">End-to-End Batch Traceability, Delivery SLA Governance &amp; Kitchen Analytics</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "FOODTECH OPERATIONAL TOPOLOGY", "REAL-TIME FLOW")

# ----------------------------------------------------------------------------
# 3. Supply Chain Architecture
# ----------------------------------------------------------------------------
def _svg_supply_chain_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Multi-Tier Suppliers", "PO Transmission & ASN", active=True)}
    {_card_box(20, 95, 135, 54, "Distribution Centers", "Inbound Pallet & Lot Intake")}
    {_card_box(20, 170, 135, 54, "Regional Warehouses", "Bin Allocation & Wave Pick")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Inventory Engine", "Multi-Node Allocation", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Demand Forecasting", "ML Stock Replenishment")}
    {_card_box(345, 95, 135, 54, "Fulfillment Routing", "Cross-Docking Dispatch", active=True)}
    {_card_box(345, 170, 135, 54, "Reverse Logistics", "RMA & Restocking")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Global Supply Chain Control Tower</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Continuous Inventory Reconciliation, Lead-Time Tracking &amp; OTIF Governance</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "SUPPLY CHAIN CONTROL TOWER", "END-TO-END VISIBILITY")

# ----------------------------------------------------------------------------
# 4. Procurement Architecture
# ----------------------------------------------------------------------------
def _svg_procurement_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Purchase Requisitions", "Department Catalog Orders", active=True)}
    {_card_box(20, 95, 135, 54, "Vendor Onboarding", "KYC & Compliance Docs")}
    {_card_box(20, 170, 135, 54, "E-Invoicing Gateway", "Automated PDF/EDI Intake")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Spend Governance", "Approval Hierarchy Engine", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "PO Auto-Generation", "Contract Pricing Locks")}
    {_card_box(345, 95, 135, 54, "3-Way Matching Engine", "PO vs GRN vs Invoice", active=True)}
    {_card_box(345, 170, 135, 54, "Vendor Scorecards", "SLA & Performance Metrics")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Accounts Payable &amp; Enterprise ERP Sync</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Automated Financial Ledger Postings, Audit Trails &amp; Early-Payment Discounts</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "PROCUREMENT & VENDOR GOVERNANCE", "AUTOMATED WORKFLOW")

# ----------------------------------------------------------------------------
# 5. Logistics Architecture
# ----------------------------------------------------------------------------
def _svg_logistics_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Order Dispatch Queue", "Consolidated Consignments", active=True)}
    {_card_box(20, 95, 135, 54, "Carrier Interfaces", "API / EDI Freight Booking")}
    {_card_box(20, 170, 135, 54, "Fleet Telemetry Hub", "Vehicle GPS & Sensor Feeds")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Dynamic Routing", "Multi-Drop Optimization", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Milestone Tracking", "Live ETA Recalculation")}
    {_card_box(345, 95, 135, 54, "Proof of Delivery", "Digital Signature / Geofence", active=True)}
    {_card_box(345, 170, 135, 54, "Carrier Analytics", "On-Time Delivery Metrics")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Connected Logistics Management System</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Unified Freight Tracking, Exception Management &amp; Demurrage Reduction</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "LOGISTICS & FLEET TOPOLOGY", "ACTIVE DISPATCH")

# ----------------------------------------------------------------------------
# 6. Enterprise Business Core Architecture (ERP / Apps)
# ----------------------------------------------------------------------------
def _svg_enterprise_core_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Finance & Ledgers", "General Ledger & Billing", active=True)}
    {_card_box(20, 95, 135, 54, "Operations & WMS", "Inventory & Production")}
    {_card_box(20, 170, 135, 54, "Sales & CRM", "Quotes, Orders & Accounts")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Enterprise Event Bus", "Kafka / Event Mesh", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Workflow Engine", "Policy & Approval Logic")}
    {_card_box(345, 95, 135, 54, "Custom Portals", "Role-Based Access Control", active=True)}
    {_card_box(345, 170, 135, 54, "Executive Intelligence", "Cross-Entity Data Lake")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Unified Enterprise Systems Architecture</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Seamless Workflows Across Departments, Single Source of Truth &amp; API Connectivity</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "ENTERPRISE SYSTEM ARCHITECTURE", "SYNCHRONIZED BUS")

# ----------------------------------------------------------------------------
# 7. CRM Architecture
# ----------------------------------------------------------------------------
def _svg_crm_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Multi-Channel Inbound", "Web, Email, Forms & Chat", active=True)}
    {_card_box(20, 95, 135, 54, "Account Telemetry", "Product Usage & History")}
    {_card_box(20, 170, 135, 54, "Support Tickets", "Customer Inquiries & SLAs")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "360° Customer Core", "Unified Customer Graph", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Pipeline Automation", "Stage Routing & Scoring")}
    {_card_box(345, 95, 135, 54, "Contract Management", "Digital Signatures & Quotes", active=True)}
    {_card_box(345, 170, 135, 54, "Retention Analytics", "Churn Risk & Churn Alerts")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Customer Relationship &amp; Revenue Engine</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Accelerated Sales Cycles, Proactive Account Health &amp; Enterprise Service Desks</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "CUSTOMER INTELLIGENCE PIPELINE", "UNIFIED GRAPH")

# ----------------------------------------------------------------------------
# 8. HRMS Architecture
# ----------------------------------------------------------------------------
def _svg_hrms_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Recruitment & ATS", "Applicant Tracking Feeds", active=True)}
    {_card_box(20, 95, 135, 54, "Biometric & Shifts", "Attendance & Clock Logs")}
    {_card_box(20, 170, 135, 54, "Leave & Expenses", "Self-Service Claims")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Workforce Core", "Employee Lifecycle Hub", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Automated Onboarding", "Document Verification")}
    {_card_box(345, 95, 135, 54, "Payroll Engine", "Tax, Deduction & Direct Pay", active=True)}
    {_card_box(345, 170, 135, 54, "Compliance Tracker", "Statutory Filings & Audits")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Human Capital Management Ecosystem</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Seamless Employee Lifecycle, Accurate Payroll Processing &amp; Regulatory Compliance</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "HUMAN RESOURCE MANAGEMENT SUITE", "LIFECYCLE ENGINE")

# ----------------------------------------------------------------------------
# 9. Business Process Automation (BPA) Architecture
# ----------------------------------------------------------------------------
def _svg_bpa_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Event Triggers", "System Webhooks & APIs", active=True)}
    {_card_box(20, 95, 135, 54, "Document Intake", "Forms, Scans & PDFs")}
    {_card_box(20, 170, 135, 54, "Scheduled Crons", "Periodic Batch Triggers")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Process Orchestrator", "Deterministic State Logic", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Approval Matrix", "Dynamic Escalation Chains")}
    {_card_box(345, 95, 135, 54, "Cross-System Tasks", "Automated API Mutations", active=True)}
    {_card_box(345, 170, 135, 54, "Audit & Logging", "Immutable History Records")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Intelligent Workflow Automation Framework</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Eliminating Operational Bottlenecks, Enforcing Compliance &amp; Slashing Latency</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "WORKFLOW ORCHESTRATION TOPOLOGY", "EVENT-DRIVEN MESH")

# ----------------------------------------------------------------------------
# 10. Intelligent Monitoring & Observability Architecture
# ----------------------------------------------------------------------------
def _svg_monitoring_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Device & Sensor Feeds", "Time-Series Telemetry", active=True)}
    {_card_box(20, 95, 135, 54, "Application Logs", "Syslog, JSON & Traces")}
    {_card_box(20, 170, 135, 54, "Infrastructure Health", "CPU, Memory, Network I/O")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Telemetry Ingestion", "Stream Processing Bus", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Anomaly Detection", "Dynamic Threshold Engine")}
    {_card_box(345, 95, 135, 54, "Alert Escalation", "Slack, PagerDuty, Webhooks", active=True)}
    {_card_box(345, 170, 135, 54, "Command Console", "Real-Time Telemetry Panels")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Real-Time Observability &amp; Incident Mesh</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Sub-Second Incident Detection, Automated Remediation &amp; Uptime Assurance</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "OBSERVABILITY & MONITORING SUITE", "24/7 TELEMETRY STREAM")

# ----------------------------------------------------------------------------
# 11. IoT & Device Connectivity Architecture
# ----------------------------------------------------------------------------
def _svg_iot_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Industrial Edge Sensors", "Temperature, Vibe, Power", active=True)}
    {_card_box(20, 95, 135, 54, "Smart Gateways", "Local Edge Pre-Processing")}
    {_card_box(20, 170, 135, 54, "Mobile & RFID Assets", "Real-Time Location Beacons")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "MQTT / TLS Broker", "High-Throughput Bus", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Telemetry Lake", "TimescaleDB / InfluxDB")}
    {_card_box(345, 95, 135, 54, "Predictive Diagnostics", "Failure Early-Warning", active=True)}
    {_card_box(345, 170, 135, 54, "Device Management", "OTA Firmware & Heartbeats")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Connected Device &amp; Asset Telemetry Fabric</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Secure Mutual TLS, Edge Computing Resilience &amp; Real-Time Operational Analytics</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "IOT & EDGE DEVICE TOPOLOGY", "CONNECTED SENSORS")

# ----------------------------------------------------------------------------
# 12. Operational Analytics Architecture
# ----------------------------------------------------------------------------
def _svg_analytics_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Transactional Data", "OLTP DBs & Event Feeds", active=True)}
    {_card_box(20, 95, 135, 54, "Operational Metrics", "Fleet, Warehouse & Systems")}
    {_card_box(20, 170, 135, 54, "External Market Data", "APIs & Vendor Data Feeds")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Streaming Pipeline", "Cleanse & Normalization", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Analytics Warehouse", "Aggregated OLAP Datamart")}
    {_card_box(345, 95, 135, 54, "Trend Modeling", "Statistical Projections", active=True)}
    {_card_box(345, 170, 135, 54, "Decision Dashboards", "Executive Actionable KPIs")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Enterprise Operational Analytics Engine</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Actionable Visibility, Historical Cohort Benchmarking &amp; Automated Alerts</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "OPERATIONAL ANALYTICS ENGINE", "DATA INSIGHTS")

# ----------------------------------------------------------------------------
# 13. System Infrastructure Monitoring Architecture
# ----------------------------------------------------------------------------
def _svg_infrastructure_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Container Clusters", "Kubernetes Pod Telemetry", active=True)}
    {_card_box(20, 95, 135, 54, "Database Nodes", "Query Latency & IOPS")}
    {_card_box(20, 170, 135, 54, "Edge Balancers", "SSL, Traffic & Status Codes")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Health Aggregator", "Distributed Tracing", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Auto-Scaling Logic", "Dynamic Resource Allocation")}
    {_card_box(345, 95, 135, 54, "Incident Routing", "On-Call Pager Automation", active=True)}
    {_card_box(345, 170, 135, 54, "Resilient Failover", "Multi-AZ High Availability")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Mission-Critical Cloud Infrastructure</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Zero-Downtime Deployments, Disaster Recovery Governance &amp; Latency Guards</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "INFRASTRUCTURE HEALTH TOPOLOGY", "RESILIENT MESH")

# ----------------------------------------------------------------------------
# 14. Agentic AI & Autonomous Multi-Agent Loop
# ----------------------------------------------------------------------------
def _svg_agentic_ai_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Enterprise Goal Intake", "Natural Language Prompts", active=True)}
    {_card_box(20, 95, 135, 54, "Task Decomposition", "Sub-Plan Graph Creation")}
    {_card_box(20, 170, 135, 54, "Context Memory", "Session State & Cache")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Agent Coordinator", "Multi-Agent Orchestrator", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "API Tool Calling", "Enterprise System Execution")}
    {_card_box(345, 95, 135, 54, "Safety Guardrails", "Output Verification & Ethics", active=True)}
    {_card_box(345, 170, 135, 54, "State Feedback Loop", "Self-Correction & Refinement")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Autonomous Agentic Architecture</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Reasoning Loops, Safe Tool Execution, Deterministic Policy Adherence</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "AGENTIC AI EXECUTION TOPOLOGY", "AUTONOMOUS REASONING")

# ----------------------------------------------------------------------------
# 15. Generative AI & Enterprise RAG Architecture
# ----------------------------------------------------------------------------
def _svg_generative_rag_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Internal Knowledge Base", "Manuals, SOPs & Docs", active=True)}
    {_card_box(20, 95, 135, 54, "Enterprise Vector Store", "Chroma / Pinecone / pgvector")}
    {_card_box(20, 170, 135, 54, "User Prompt Query", "Contextual Enterprise Inquiries")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "RAG Retrieval Hub", "Hybrid Semantic Search", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "LLM Inference Engine", "Private Enterprise Model")}
    {_card_box(345, 95, 135, 54, "Fact-Check Validator", "Hallucination Defense", active=True)}
    {_card_box(345, 170, 135, 54, "Grounded Output", "Role-Based Answer & Citations")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Enterprise Generative AI &amp; RAG Pipeline</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Private Cloud Deployment, Zero Data Leakage, Exact Citation Grounding</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "ENTERPRISE RAG ARCHITECTURE", "GROUNDED INFERENCE")

# ----------------------------------------------------------------------------
# 16. Intelligent Document Processing (IDP) Architecture
# ----------------------------------------------------------------------------
def _svg_document_processing_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Unstructured Ingestion", "PDFs, Scans, Invoices & Forms", active=True)}
    {_card_box(20, 95, 135, 54, "OCR & Pre-Processing", "Binarization & Dewarping")}
    {_card_box(20, 170, 135, 54, "Classification Engine", "Document Type Identification")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Extraction Core", "Key-Value / Table Parser", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Validation Rules", "Confidence Score Gates")}
    {_card_box(345, 95, 135, 54, "Human-in-the-Loop", "Low-Confidence Review Queue", active=True)}
    {_card_box(345, 170, 135, 54, "Structured Injection", "Direct ERP / CRM Posting")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Intelligent Document Extraction Pipeline</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">99%+ Extraction Accuracy, Automated Table Ingestion &amp; Complete Audit Trail</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "DOCUMENT UNDERSTANDING TOPOLOGY", "INTELLIGENT OCR")

# ----------------------------------------------------------------------------
# 17. AI Orchestration General Architecture
# ----------------------------------------------------------------------------
def _svg_ai_orchestration_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Enterprise Data Lakes", "Structured & Unstructured", active=True)}
    {_card_box(20, 95, 135, 54, "Real-Time Telemetry", "Event Feeds & Sensor Data")}
    {_card_box(20, 170, 135, 54, "Human Task Feeds", "Operational Requests")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "AI Orchestrator", "Task Classification & ML", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Predictive Models", "Machine Learning Scoring")}
    {_card_box(345, 95, 135, 54, "Autonomous Triggers", "System API Mutations", active=True)}
    {_card_box(345, 170, 135, 54, "Governance Audit", "Model Explainability")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Applied Enterprise AI Infrastructure</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Continuous Model Observability, Zero Operational Hallucinations &amp; Secure APIs</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "APPLIED AI SYSTEMS ARCHITECTURE", "PRODUCTION WORKFLOW")

# ----------------------------------------------------------------------------
# 18. Healthcare Platform Architecture
# ----------------------------------------------------------------------------
def _svg_healthcare_platform_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Patient Intake Portals", "Pre-Registration & Forms", active=True)}
    {_card_box(20, 95, 135, 54, "Scheduling Gateways", "Multi-Specialty Slots")}
    {_card_box(20, 170, 135, 54, "Insurance Eligibility", "Real-Time EDI 270/271")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Clinical Workflow Core", "HIPAA-Compliant Engine", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Prior Authorization", "Clinical Criteria Matching")}
    {_card_box(345, 95, 135, 54, "Claims Pre-Scrubbing", "Payer Rule Edits & Validation", active=True)}
    {_card_box(345, 170, 135, 54, "Provider Dashboards", "Care Team Collaboration")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Healthcare Operations &amp; Clinical Integration</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">EHR Interoperability (Epic/Cerner), Administrative Automation &amp; HIPAA Security</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "HEALTHCARE PLATFORM TOPOLOGY", "HIPAA COMPLIANT")

# ----------------------------------------------------------------------------
# 19. Healthcare Data Interoperability (HL7 / FHIR)
# ----------------------------------------------------------------------------
def _svg_healthcare_interop_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Hospital EHR Records", "Epic, Cerner & Allscripts", active=True)}
    {_card_box(20, 95, 135, 54, "Diagnostic Lab Feeds", "HL7 v2 / LIS Systems")}
    {_card_box(20, 170, 135, 54, "Imaging & PACS", "DICOM Metadata Sync")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "FHIR Interop Bus", "SMART on FHIR API", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Clinical Data Lake", "Longitudinal Patient Record")}
    {_card_box(345, 95, 135, 54, "Cohort Analytics", "Risk Stratification & Trends", active=True)}
    {_card_box(345, 170, 135, 54, "Care Quality KPIs", "HEDIS & Regulatory Reports")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Clinical Data Integration &amp; Interoperability Mesh</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Standardized FHIR Resources, Secure Data Translation &amp; Zero Clinical Data Loss</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "CLINICAL DATA INTEROPERABILITY", "FHIR / HL7 COMPLIANT")

# ----------------------------------------------------------------------------
# 20. System Integration & API Gateway
# ----------------------------------------------------------------------------
def _svg_system_integration_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Legacy Core Systems", "AS400, Mainframe, SQL", active=True)}
    {_card_box(20, 95, 135, 54, "Cloud SaaS Platforms", "Salesforce, Workday, Hubspot")}
    {_card_box(20, 170, 135, 54, "Third-Party Partners", "B2B EDI & Webhooks")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Enterprise API Bus", "Schema Mapping & Transform", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Message Queues", "Zero-Loss Kafka Buffer")}
    {_card_box(345, 95, 135, 54, "Target Synchronization", "Transactional Consistency", active=True)}
    {_card_box(345, 170, 135, 54, "Traffic Throttling", "Rate Limits & Health Mesh")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Enterprise High-Throughput Integration Mesh</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Bidirectional Connectivity, Protocol Normalization &amp; Resilient Circuit Breaking</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "ENTERPRISE INTEGRATION MESH", "BIDIRECTIONAL SYNC")

# ----------------------------------------------------------------------------
# 21. Manufacturing & Industry Topologies
# ----------------------------------------------------------------------------
def _svg_manufacturing_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Shop-Floor Machines", "PLC, SCADA & CNC Feeds", active=True)}
    {_card_box(20, 95, 135, 54, "Assembly Tracking", "RFID Part Milestone Scans")}
    {_card_box(20, 170, 135, 54, "Quality Cameras", "Computer Vision Inspection")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "MES Execution Core", "Production Line Balancing", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Maintenance Triggers", "Predictive Vibration Alerts")}
    {_card_box(345, 95, 135, 54, "Work-in-Progress Hub", "ERP Inventory Depletion", active=True)}
    {_card_box(345, 170, 135, 54, "OEE Analytics", "Availability & Quality Yield")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Industrial Manufacturing Execution System</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Real-Time Shop-Floor Visibility, Downtime Mitigation &amp; Defect Minimization</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "CONNECTED MANUFACTURING TOPOLOGY", "SMART FACTORY")

# ----------------------------------------------------------------------------
# 22. Connect / Engagement Architecture
# ----------------------------------------------------------------------------
def _svg_connect_architecture():
    svg = f"""
    {_card_box(20, 20, 135, 54, "Project Inquiries", "Business Objectives & Scope", active=True)}
    {_card_box(20, 95, 135, 54, "Technical Discovery", "Architecture Review")}
    {_card_box(20, 170, 135, 54, "Service Collaboration", "Solution Roadmapping")}

    {_connector(155, 47, 195, 107)}
    {_connector(155, 122, 195, 122)}
    {_connector(155, 197, 195, 137)}

    {_card_box(195, 95, 120, 60, "Solution Engineering", "Tailored Technical Roadmap", active=True)}

    {_connector(315, 107, 345, 47)}
    {_connector(315, 122, 345, 122)}
    {_connector(315, 137, 345, 197)}

    {_card_box(345, 20, 135, 54, "Rapid Prototype", "Proof-of-Concept Validation")}
    {_card_box(345, 95, 135, 54, "Enterprise Deployment", "Secure Phased Rollout", active=True)}
    {_card_box(345, 170, 135, 54, "Dedicated Support", "Ongoing 24/7 SLA Backing")}

    <rect x="20" y="245" width="460" height="48" rx="8" fill="rgba(14, 165, 233, 0.08)" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1.2"/>
    <text x="35" y="268" fill="#FFFFFF" font-family="Inter, sans-serif" font-size="11" font-weight="700">Nova Arc Engineering Engagement Model</text>
    <text x="35" y="283" fill="#94A3B8" font-family="Inter, sans-serif" font-size="9">Collaborative Scoping, Transparent Architecture Design &amp; Measurable Business Outcomes</text>
    <circle cx="455" cy="269" r="6" fill="#10B981" filter="url(#glow)"/>
    """
    return _svg_wrapper(svg, "ENTERPRISE ENGAGEMENT WORKFLOW", "CLIENT COLLABORATION")
